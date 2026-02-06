import sys
import requests
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                             QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QLabel, QHBoxLayout)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class EquipmentApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer - Desktop")
        self.setGeometry(100, 100, 1000, 600)

        layout = QVBoxLayout()
        
        self.btn_upload = QPushButton("Upload CSV to Backend")
        self.btn_upload.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-weight: bold;")
        self.btn_upload.clicked.connect(self.upload_file)
        layout.addWidget(self.btn_upload)

        self.summary_label = QLabel("Ready to process equipment data...")
        layout.addWidget(self.summary_label)

        content_layout = QHBoxLayout()
        self.table = QTableWidget()
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        
        content_layout.addWidget(self.table)
        content_layout.addWidget(self.canvas)
        layout.addLayout(content_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            # Open the file in a 'with' block to ensure it closes properly
            try:
                with open(file_path, 'rb') as f:
                    files = {'file': f}
                    # Talking to your Django Backend!
                    # Note: Using AllowAny on backend, so auth is optional for the demo
                    response = requests.post("http://127.0.0.1:8000/api/upload/", files=files)
                    
                    if response.status_code == 201:
                        self.display_data(response.json())
                        self.summary_label.setText("Upload Successful!")
                    else:
                        self.summary_label.setText(f"Error: Server returned {response.status_code}")
            except Exception as e:
                self.summary_label.setText(f"Error: {str(e)}")

    def display_data(self, result):
        summary = result['summary']
        dist = result['distribution']
        data_rows = result['data']

        self.summary_label.setText(f"Total: {summary['total_rows']} | Avg Flowrate: {summary['mean_flowrate']:.2f}")

        self.table.setRowCount(len(data_rows))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Name", "Type", "Flow", "Press", "Temp"])
        
        for i, row in enumerate(data_rows):
            self.table.setItem(i, 0, QTableWidgetItem(str(row.get('Equipment Name', 'N/A'))))
            self.table.setItem(i, 1, QTableWidgetItem(str(row.get('Type', 'N/A'))))
            self.table.setItem(i, 2, QTableWidgetItem(str(row.get('Flowrate', 'N/A'))))
            self.table.setItem(i, 3, QTableWidgetItem(str(row.get('Pressure', 'N/A'))))
            self.table.setItem(i, 4, QTableWidgetItem(str(row.get('Temperature', 'N/A'))))

        self.canvas.axes.cla()
        self.canvas.axes.bar(dist.keys(), dist.values(), color='skyblue')
        self.canvas.axes.set_title("Equipment Distribution")
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentApp()
    window.show()
    sys.exit(app.exec_())
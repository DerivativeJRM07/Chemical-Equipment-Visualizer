# 🧪 Chemical Equipment Parameter Visualizer
> A Professional Hybrid Full-Stack Application for Engineering Data Analytics.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-18.0-61DAFB?style=flat&logo=react&logoColor=black)](https://reactjs.org/)

---

## 📖 Project Overview
The **Chemical Equipment Parameter Visualizer** is a high-performance hybrid application designed for chemical engineers to analyze, visualize, and report equipment parameters efficiently.

The system uses a centralized **Django REST API** that serves:
- 🌐 A **React.js Web Dashboard**
- 🖥️ A **PyQt5 Desktop Application**

Both clients consume the same backend, ensuring consistency and scalability.

---

## ✨ Advanced Features
- **Hybrid Architecture:** One backend powering multiple frontends
- **Data Analytics:** Automated statistical processing using **Pandas**
- **Data Visualization:** Charts and plots for parameter insights
- **Automated Reporting:** Generate professional **PDF reports**
- **Security:** API protected using **Basic Authentication**
- **Resource Management:** Automatically retains only the **latest 5 uploads**

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| **Backend** | Python, Django, Django REST Framework, Pandas, ReportLab |
| **Web Frontend** | React.js, Axios, Chart.js |
| **Desktop App** | PyQt5, Matplotlib, Requests |
| **Security** | Basic Authentication, CORS |

---

## ⚙️ Installation & Setup

### 1️⃣ Prerequisites
- Python **3.10+**
- Node.js & npm
- Git

---

### 2️⃣ Backend Setup (Django)

```bash
cd chemical_project
python -m venv venv

##Activate Virtual Environment
#Windows
.\venv\Scripts\activate

#Install dependencies and run server:
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

#Backend will run at:
http://127.0.0.1:8000/

---

### 3 Web Frontend setup(React)
cd chemical-frontend
npm install
npm start

#Web app will run at:
http://localhost:3000/

---

### 4 Desktop Appkication Setup(Pyqt5)
pip install PyQt5 matplotlib requests
python main_desktop.py

### 5 Api Endpoints

| Method | Endpoint             | Description                           |
| ------ | -------------------- | ------------------------------------- |
| POST   | `/api/upload/`       | Upload CSV file and receive analytics |
| GET    | `/api/download-pdf/` | Download PDF report of latest data    |
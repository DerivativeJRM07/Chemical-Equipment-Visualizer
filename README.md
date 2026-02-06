# 🧪 Chemical Equipment Parameter Visualizer (Hybrid Web + Desktop App)
> A Professional Application for Engineering Data Analytics and Hybrid Frontend Delivery.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-18.0-61DAFB?style=flat&logo=react&logoColor=black)](https://reactjs.org/)

---

## 📖 Project Overview
The **Chemical Equipment Parameter Visualizer** is a high-performance hybrid system designed for chemical engineers to analyze, visualize, and report equipment parameters across different platforms.

The system utilizes a centralized **Django REST API** that serves:
- 🌐 A **React.js Web Dashboard** (Dynamic analytics and tables)
- 🖥️ A **PyQt5 Desktop Application** (Native visualization with Matplotlib)

---

## ✨ Advanced Features
- **Hybrid Architecture:** Single backend source of truth powering multiple frontend clients.
- **Data Analytics:** Automated statistical processing (Mean Flowrate, Pressure, Temperature) using **Pandas**.
- **Data Visualization:** Integrated **Chart.js** for web and **Matplotlib** for desktop.
- **Automated Reporting:** Instant generation of professional **PDF reports** via **ReportLab**.
- **Security & CORS:** Configured with `cors-headers` and `CSRF-exempt` endpoints for seamless cross-platform data transmission.

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| **Backend** | Python, Django, Django REST Framework, Pandas, ReportLab |
| **Web Frontend** | React.js, Axios, Chart.js |
| **Desktop App** | PyQt5, Matplotlib, Requests |
| **Security** | Session Authentication, CORS, CSRF Protection |

---

## ⚙️ Installation & Setup

### 1️⃣ Prerequisites
- Python **3.10+**
- Node.js & npm
- Git

---

### 2️⃣ Backend Setup (Django)
```bash
# Navigate to root
cd Chemical_project_jrm

# Create and activate Virtual Environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install django djangorestframework django-cors-headers pandas reportlab requests

# Run migrations and start server
python manage.py migrate
python manage.py runserver
```
Backend API running at: http://127.0.0.1:8000/

---

### 3️⃣ Web Frontend Setup (React)
```bash
# Navigate to frontend folder
cd chemical-frontend

# Install dependencies and start
npm install
npm start
```
Web Dashboard running at: http://localhost:3000/

---

### 4️⃣ Desktop Application Setup (PyQt5)
```bash
# Ensure venv is active in a new terminal
.\venv\Scripts\activate

# Run the native application
python main_desktop.py
```
---

### 5️⃣ API Endpoints

| Method | Endpoint             | Description                           |
| ------ | -------------------- | ------------------------------------- |
| POST   | `/api/upload/`       | Upload CSV file and receive analytics |
| GET    | `/api/download-pdf/` | Download PDF report of latest data    |

---

### 📂 Project Structure
- **api/** - Backend app: CSV processing, PDF generation logic.
- **chemical_project/** - Core settings: CORS and Security configurations.
- **chemical-frontend/** - React project: Chart.js dashboards.
- **main_desktop.py** - Standalone PyQt5 GUI script.

---

# END of The Task 
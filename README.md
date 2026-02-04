# 🧪 Chemical Equipment Parameter Visualizer
> A Hybrid Full-Stack Application for Engineering Data Analytics.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-18.0-61DAFB?style=flat&logo=react&logoColor=black)](https://reactjs.org/)

## 📖 Project Overview
This project is a high-performance, hybrid solution designed to process chemical equipment data. It allows engineers to upload CSV files containing parameters like **Flowrate, Pressure, and Temperature**, providing instant statistical analysis and visual distribution charts across both web and desktop platforms.

---

## 🚀 Key Features

### 🛠️ Backend (The Core)
- **Django REST Framework:** Secure and scalable API endpoints.
- **Pandas Integration:** Robust data processing and statistical computation.
- **Smart Storage:** Automatic logic to retain only the **last 5 uploads** to manage server resources.

### 🌐 Web Frontend
- **React.js Dashboard:** A modern, responsive interface for data interaction.
- **Dynamic Charts:** Real-time data visualization using **Chart.js**.
- **Data Grid:** Clean, sortable table views of all equipment parameters.

### 💻 Desktop Client (In Progress)
- **PyQt5 Integration:** A native Windows experience for high-speed data access.
- **Matplotlib Visualization:** Scientific-grade plotting for equipment distribution.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python, Django, DRF, Pandas |
| **Web UI** | React.js, Axios, Chart.js |
| **Desktop** | PyQt5, Matplotlib, Requests |
| **Database** | SQLite3 |

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- Python 3.10+
- Node.js & npm

### 2. Backend Installation
```bash
# Navigate to project root
cd chemical_project
python -m venv venv
source venv/bin/activate  # Or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### 3. Frontend Installation
cd chemical-frontend
npm install
npm start

### 4. Desktop app launch 
python main_desktop.py
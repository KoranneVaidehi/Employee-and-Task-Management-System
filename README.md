# Employee and Task Management System

## Overview
The **Employee and Task Management System** is a web-based application built using Django and MySQL. It allows administrators and managers to manage employees, assign tasks, track performance, approve leaves, and facilitate communication via real-time chat and video meetings.

## Features
### Admin/Manager:
- Add/Delete Employees
- Assign Tasks
- Attendance Management (Graph-Based Visualization)
- Salary Management
- Leave Approval System
- Employee Performance Tracking
- Real-time Chat (WebSockets)
- Video Meetings (Google Meet-like Features)
- CRUD Operations on Employees

### Employee:
- View Assigned Tasks
- Submit Completed Tasks
- Check Attendance
- Apply for Leave
- View Salary Details
- Self-Performance Tracking
- Join Chat & Meetings

## Installation

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Django 
- MySQL
- Git

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/KoranneVaidehi/Employee-and-Task-Management-System.git
   ```
2. Navigate into the project directory:
   ```sh
   cd Employee-and-Task-Management-System
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Configure the database in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
6. Apply migrations:
   ```sh
   python manage.py migrate
   ```
7. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
8. Run the server:
   ```sh
   python manage.py runserver
   ```
9. Access the system at: `http://127.0.0.1:8000/`

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Author
Developed by **Vaidehi Koranne**

## Contributions
Feel free to contribute by submitting a pull request!

---

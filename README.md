# CRM System

A simple Django-based Customer Relationship Management (CRM) application designed for managing customer records.

---
## Live Demo

[Visit Live Demo](https://amelmarghany.pythonanywhere.com/)

---

## Features

- Access Control: Login required for dashboard and record operations

- Create Records
- View Records
- Update Records
- Delete Records
- Search Functionality

- Custom 404 Page

---

## Tech Stack

- **Backend Framework**: Django 6.0.1
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3, Bootstrap 4
- **Form Framework**: Django Crispy Forms with Bootstrap 4 integration
- **Authentication**: Django Built-in Authentication System

### Dependencies

```
Django==6.0.1
django-crispy-forms==2.5
crispy-bootstrap4==2025.6
asgiref==3.11.0
sqlparse==0.5.5
tzdata==2025.3
```

---

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Virtual Environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/AhmedElmarghany/crm.git
cd crm
```

### Step 2: Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations

```bash
python manage.py migrate
```

### Step 5: Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

---

## Configuration

### Settings Overview

Key settings in `crm/settings.py`:

- **DEBUG**: Set to `False` for production
- **ALLOWED_HOSTS**: Configure for your domain
- **DATABASES**: SQLite by default, easily switchable to PostgreSQL, MySQL, etc.
- **INSTALLED_APPS**: Includes Django admin, auth, and the webapp
- **MIDDLEWARE**: Security and session management
- **STATIC_FILES_DIRS**: Configuration for static file serving
- **TEMPLATES**: Template engine configuration

### Database

The project uses SQLite by default.

---

### API Endpoint

Search Record

```http
GET /JsonSearch
Content-Type: application/json

{
    "query": "id | name | character in name"
}
```

---
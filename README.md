# 📊 Django Reporting Service

A microservice built with **Django REST Framework** that consumes the Node.js Video Backend API and exposes reporting endpoints for users and videos.

---

## 🚀 Features

- **Fetch data** from Node.js API (`/users`, `/videos`)
- **Summary report** endpoint:
  - `/report/summary` → total users, total videos, top categories
- **User report** endpoint:
  - `/report/user/<id>` → activity report for a specific user
- **DRF serializers & viewsets** for clean API responses
- **Requests** library for consuming external APIs
- **Unit tests** for reliability

---

## 📂 Project Structure

```
reporting_service/
├── manage.py
├── reporting_service/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── reports/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── services.py
    ├── serializers.py
    └── tests.py
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/django-reporting-service.git
cd django-reporting-service
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4.Environment variables

```bash
DEBUG=True
SECRET_KEY=supersecretkey
NODE_API_BASE_URL=http://localhost:3000/api
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Run the server

```bash
python manage.py runserver
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

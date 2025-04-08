# Project CaravanSite DevLog / README  

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)](https://djangoproject.com)
[![WordPress](https://img.shields.io/badge/WordPress-6.x-royalblue?logo=wordpress)](https://wordpress.org)

## 🌍 Live Version  
Production site: [https://partnerkampery.pl/](https://partnerkampery.pl/)  

---

## 📖 Development Story  
This project began as my first advanced Django application, which I successfully deployed on a production server. Due to Django's resource-intensive nature for this specific use case, I later migrated the solution to WordPress while preserving all core functionalities.

### Key Learnings  https://partnerkampery.pl/
- **Server Administration**:  
  - Managed Linux server configuration   
  - Configured SMTP email services  

- **Django Development**:  
  - MySQL database integration  
  - Custom model architecture  
  - Form handling and validation  

- **WordPress Migration**:  
  - Custom theme development  
  - Plugin integration  
  - Performance optimization  

---

## 🛠 Setup (Django Legacy Version)  

### Requirements  
- Python 3.8+  
- MySQL 5.7+ or SQLite3  

### Installation  
```bash
# Clone repository
git clone [repo_url]

# Install dependencies
pip install -r requirements.txt

# Configure database in settings.py
# For SQLite development:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver

```
## 🔍 Areas for Growth (Things I Could Improve)

### Django Optimization
🔹 **Query efficiency** - Learn better ways to optimize Django ORM queries  
🔹 **Search algorithms** - Implement more advanced search solutions  
🔹 **Testing coverage** - Add more comprehensive test cases  

### Code Quality
🔹 **JavaScript structure** - Refactor into modular components  
🔹 **Error handling** - Implement proper error boundaries  

# django-celery-telegram-bot
Django backend with Celery, Redis, and Telegram bot integration

# 🛰️ Django Backend with DRF, Celery, Redis, and Telegram Bot

This is a Django REST Framework-based backend that supports:
- Token and session-based authentication
- Asynchronous email sending via Celery + Redis
- Telegram bot integration to register users via `/start`

---

## 🛠️ Tech Stack

- Python 3.12
- Django 5.1
- Django REST Framework
- Celery
- Redis (as broker)
- httpie (for API testing)
- Telegram Bot API (polling)

---

## 📦 Installation & Setup The Project Locally

### 1. Clone the repository

git clone https://github.com/your-username/your-repo.git
cd your-repo
## Create Virtual Environment
python -m venv venv
venv\Scripts\activate       # On Windows
# or
source venv/bin/activate    # On Linux/macOS
 ##Install Dependencies
 pip install -r requirements.txt
 | Package               | Purpose                                            |
| --------------------- | -------------------------------------------------- |
| Django             | Main web framework                                 |
| djangorestframework | REST API support                                   |
| python-decouple     | Manage environment variables via .env            |
| celery            | Asynchronous task queue                            |
| redis (Python lib)  | Redis client for Python (used by Celery)           |
| httpie             | Command-line HTTP client (used for testing APIs)   |
| requests            | Used in telegram_bot.py to call Telegram Bot API |
| pytz / tzdata     | Timezone support (often pulled by Django)          |

##Configure environment variables
SECRET_KEY=your_django_secret_key
DEBUG=True
(Or hardcode SECRET_KEY in settings.py during dev.)

.

🚀 Running the Project Locally
1. Start Redis
redis-server

2. Run Django server
python manage.py migrate
python manage.py runserver

3. Run Celery worker
celery -A backend worker --pool=solo --loglevel=info

4. Run Telegram bot
python telegram_bot.py

🔑 API Authentication
#Obtain JWT Token
http POST http://127.0.0.1:8000/api/token/ username=your_user password=your_pass

Use Token for Protected Routes
http GET http://127.0.0.1:8000/api/protected/ "Authorization: Bearer <access_token>"

🤖 Telegram Bot Usage
1. Talk to your bot: @your_bot_username
2. Send /start
3. Your Telegram username will be stored in the backend DB.
4. Script: telegram_bot.py polls and handles new users

🛡️ Admin Access
1. Create Superuser -> python manage.py createsuperuser
2. Log in at: http://127.0.0.1:8000/admin/
You can manage TelegramUser entries via Django Admin.

If project runs fine, the web page should look like following ->
<img width="482" alt="image" src="https://github.com/user-attachments/assets/59161fbe-aae3-4868-953f-4bce03276898" />
Check Celery in your local environment, after clicking LogIn. It should show like the following. 
<img width="614" alt="image" src="https://github.com/user-attachments/assets/5738e118-4383-4cc3-b591-0837d540f28c" />
The Chatbot with your preferred name should look like this->
<img width="493" alt="image" src="https://github.com/user-attachments/assets/3b32754b-b86d-48f9-bb36-2263a2bfa5f3" />





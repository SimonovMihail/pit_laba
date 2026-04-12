import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Добавь приложение в список
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'workshop',
]

# 2. Укажи путь к HTML (папка front/templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR.parent, 'front', 'templates')], # ВАЖНО
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Должно быть выше AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 3. Укажи путь к статике (CSS/JS)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR.parent, 'front', 'static'), # ВАЖНО
]

# Включаем режим отладки для разработки
DEBUG = True

# Разрешаем доступ с любых адресов (для локальной разработки это ок)
ALLOWED_HOSTS = ['*']

# Указываем путь к главному файлу со ссылками (urls.py в папке core)
ROOT_URLCONF = 'core.urls'

# Указываем путь к WSGI приложению (нужно для запуска сервера)
WSGI_APPLICATION = 'core.wsgi.application'

# Секретный ключ (обязателен для безопасности).
# Если его нет, придумай любую длинную строку:
SECRET_KEY = 'django-insecure-any-random-string-here'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'car_workshop',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
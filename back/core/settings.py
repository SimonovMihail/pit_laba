import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'workshop',
    'corsheaders',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR.parent, 'frontend')], # ВАЖНО
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
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR.parent, 'frontend'), # ВАЖНО
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
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': '5432',
    }
}

CORS_ALLOW_ALL_ORIGINS = True
# Используем официальный образ Python
FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Сначала копируем только файл зависимостей (из папки back)
COPY back/requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Теперь копируем все остальные файлы проекта в контейнер
COPY . .

# Переходим в папку back, так как именно там лежит manage.py
WORKDIR /app/back

# Открываем порт 8000
EXPOSE 8000

# Команда, которая запустит наш сервер внутри контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
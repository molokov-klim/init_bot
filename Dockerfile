# Используем базовый образ с Python
FROM python:3.9

# Устанавливаем аргументы сборки по умолчанию
ARG BOT_TOKEN

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

RUN apt update
RUN apt install -y android-tools-adb

# Устанавливаем переменные среды
ENV BOT_TOKEN=$BOT_TOKEN

# Копируем все файлы в рабочую директорию контейнера
COPY . .

# Указываем команду для запуска приложения
CMD ["python", "bot_launcher.py"]

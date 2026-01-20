# Используем легковесный образ Python
FROM python:3.10-slim-buster

# Настройка рабочей директории
WORKDIR /app

# Копируем файл требований
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальное содержимое проекта
COPY . .

# Экспонируем порт, если приложение является веб-сервером
# EXPOSE 5000

# Определяем точку входа для запуска приложения
CMD ["python", "main.py"]

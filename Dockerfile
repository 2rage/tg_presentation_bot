# Используем образ Python 3.10
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY poetry.lock pyproject.toml /app/

# Устанавливаем Poetry и зависимости
RUN pip install poetry && poetry install --no-dev

# Копируем всё приложение в контейнер
COPY . /app/

# Запускаем приложение
CMD ["poetry", "run", "python", "bot/app.py"]
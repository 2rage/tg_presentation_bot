FROM python:3.12

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry && poetry install --no-dev

COPY . /app/

EXPOSE 5005

CMD ["poetry", "run", "python", "app/bot.py"]
FROM python:3.8-slim

RUN mkdir /src

COPY ./requirements.txt /src

RUN pip install -r /src/requirements.txt --no-cache-dir

COPY ./.env /src

COPY ./alembic /src/alembic
COPY ./alembic.ini /src

COPY ./app /src/app
COPY ./backend.py /src
COPY ./notification /src/notification
COPY ./telegram_bot /src/telegram_bot
COPY ./bot.py /src

WORKDIR /src

CMD ["python", "backend.py"]
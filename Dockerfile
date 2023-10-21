FROM python:3.8-slim

RUN mkdir /src

COPY ./requirements.txt /src

RUN pip install -r /src/requirements.txt --no-cache-dir

COPY ./alembic /src/alembic
COPY ./app /src/app
COPY ./main.py /src
COPY ./.env /src
WORKDIR /src

CMD ["python", "main.py"]

#CMD ["python", "main.py", "runserver"]
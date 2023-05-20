FROM python:3

WORKDIR /code

RUN pip install --no-cache-dir flask

RUN pip install sqlalchemy

COPY . .

CMD [ "flask","run"]


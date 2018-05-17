FROM python:2.7-slim

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD python app.py


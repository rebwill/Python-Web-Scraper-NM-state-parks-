FROM python:3

WORKDIR /usr/src/app

RUN pip install requests

RUN pip install beautifulsoup4

COPY . .

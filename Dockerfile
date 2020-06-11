FROM python:3.7-slim

RUN pip install --upgrade pip

COPY ./requirements.txt ./
RUN pip --no-cache-dir install -r requirements.txt && rm -f requirements.txt

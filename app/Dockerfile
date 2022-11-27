FROM python:3.11-alpine

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN python -m pip install --upgrade pip
RUN apk add --no-cache gcc musl-dev linux-headers python3-dev libffi-dev openssl-dev

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD flask run
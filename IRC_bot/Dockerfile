FROM python:3.7-slim-buster

COPY requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt

WORKDIR /chatbot

COPY . .

CMD ["python3", "./main.py"]

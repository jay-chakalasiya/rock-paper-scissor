FROM python:3.6.15-slim-buster

RUN pip install numpy

WORKDIR /rock-paper-scissor

COPY . /rock-paper-scissor/

CMD ["python", "/rock-paper-scissor/main.py"]
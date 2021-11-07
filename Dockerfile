FROM python:3.6

WORKDIR /rock-paper-scissor

COPY . /rock-paper-scissor/

RUN pip install numpy

CMD ["python", "/rock-paper-scissor/main.py"]
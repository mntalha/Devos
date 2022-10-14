FROM python:latest

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY server.py /app


EXPOSE 5000
CMD ["python", "server.py"]
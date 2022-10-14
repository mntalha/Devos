FROM python:3.7

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY main.py /app


EXPOSE 5000
CMD ["uvicorn", "main:app"]
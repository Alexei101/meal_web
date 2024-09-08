#FROM ubuntu:latest
#LABEL authors="Алексей"
#
#ENTRYPOINT ["top", "-b"]

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]

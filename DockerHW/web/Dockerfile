FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

RUN useradd app
USER app

CMD ["python", "main.py"]

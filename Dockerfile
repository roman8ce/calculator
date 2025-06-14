FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python /app/init_db.py && exec uvicorn main:app --host 0.0.0.0 --port 8000
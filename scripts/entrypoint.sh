#!/bin/bash
python /app/init_db.py
exec uvicorn main:app --host 0.0.0.0 --port 8000
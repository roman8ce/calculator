import sympy as sp
import asyncpg
from fastapi import FastAPI, Depends, HTTPException
from database import get_db_connection

app = FastAPI()

@app.post('/')
async def calculation(expression: str, db: asyncpg.Connection = Depends(get_db_connection)) -> dict[str, float]:
    try:
        result = float(sp.sympify(expression).evalf())
        await db.execute('INSERT INTO calculation_history(expression, result) VALUES($1, $2)', expression, result)
        return {expression: result}

    except Exception as e:
        error_message = f'Error evaluating {expression}: {str(e)}'
        await db.execute('INSERT INTO calculation_history(expression, error_message) VALUES($1, $2)', expression, error_message)
        raise HTTPException(status_code=400, detail=error_message)
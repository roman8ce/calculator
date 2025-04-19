import asyncpg

DATABASE_URL = "postgresql://postgres:harDpa55w0rD@db:5432/calculator_db"

async def get_db_connection():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()
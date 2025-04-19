import asyncpg
import asyncio

DATABASE_URL = 'postgresql://postgres:harDpa55w0rD@db:5432/calculator_db'

async def create_table():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.execute('''
            CREATE EXTENSION IF NOT EXISTS "uuid-ossp";               

            CREATE TABLE IF NOT EXISTS calculation_history (
                        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                        expression VARCHAR(100) NOT NULL, 
                        result NUMERIC, error_message TEXT, 
                        date_and_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );
                        ''')
        print('Table calculation_history created successfully')
    except Exception as e:
        print(f'Error creating table: {e}')
    finally:
        await conn.close()


if __name__ == '__main__':
    asyncio.run(create_table())
import asyncio
import os
import asyncpg
from dotenv import load_dotenv


load_dotenv()

async def main():

    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT', 5432) 
    )
    
    print("successful connection to the database")
    await conn.close()

if __name__ == '__main__':
    asyncio.run(main())

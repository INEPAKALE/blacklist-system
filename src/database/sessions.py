from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from dotenv import load_dotenv
import os
import core.config

load_dotenv()




database_url = os.getenv("DATABASE_URL")

pool_size = core.config.SQLALCHEMY_POOL_SIZE
max_overflow = core.config.SQLALCHEMY_MAX_OVERFLOW
pool_timeout = core.config.POOL_TIMEOUT
pool_pre_ping = core.config.POOL_PRE_PING 
echo = core.config.ECHO

engine = create_async_engine(
    database_url,
    echo=echo,
    pool_size=pool_size,
    max_overflow=max_overflow,
    pool_timeout=pool_timeout,
    pool_pre_ping=pool_pre_ping,
)

app = FastAPI()

async def get_db():
    async with async_sessionmaker() as session:
        yield session
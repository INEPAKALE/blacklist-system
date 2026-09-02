import asyncio
import os
from logging.config import fileConfig
from sqlalchemy import pool
from alembic import context
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_engine_from_config
import sys

sys.path.append(os.getcwd())
load_dotenv()


config = context.config

config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


from src.models.base import Base


target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Запуск миграций в 'offline' режиме."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection) -> None:
    """Вспомогательная функция для выполнения миграций внутри синхронного контекста."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Запуск миграций в 'online' режиме (асинхронно)."""

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool if "poolclass" not in config.get_section(config.config_ini_section, {}) else None,
    )


    async with connectable.connect() as connection:

        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:

    asyncio.run(run_migrations_online())

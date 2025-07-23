import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.memory import SimpleEventIsolation
from aiogram.fsm.storage.redis import RedisStorage

from config_reader import config
from func import msg_get


def dp_setup():
    storage = RedisStorage.from_url('redis://localhost:6379/0', key_builder=DefaultKeyBuilder(with_destiny=True))
    dp = Dispatcher(events_isolation=SimpleEventIsolation(), storage=storage)
    return dp


async def main():
    dp = dp_setup()
    bot = Bot(config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode='HTML'))
    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.create_task(msg_get(bot))
    # Запускаем бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

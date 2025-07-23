import asyncio

from aiogram import Bot

import config
from date_exchange import get_global_variable


async def msg_get(bot: Bot):
    while True:
        new_gift_info = await get_global_variable('dtm_res')
        if not new_gift_info:
            return
        time_id = new_gift_info[0]
        dtm_id = new_gift_info[1]
        status = new_gift_info[2]

        if time_id not in config.uniqueness:
            config.uniqueness.append(time_id)
            text = f"{dtm_id} - {status}"

            await bot.send_message(736978777, text)
        await asyncio.sleep(0)


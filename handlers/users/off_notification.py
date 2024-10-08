from aiogram import types
from loader import dp
from utils.log_app import logger
from database import off_notification_in_db
from utils import regenerate_scheduler
import emoji
from utils.misc import rate_limit
from data.config import MIDDLEWARE_BAN


# Cоздаем message handler, который ловит команду /off_notification
@rate_limit(limit=MIDDLEWARE_BAN)
@dp.message_handler(commands=["off_notification"])
async def off_notification(message: types.Message):
    """
    Асинхронная функция, которая предназначена для выключения рассылки меню по расписанию
    :parameter message: Сообщение от пользователя
    """
    logger.info(f"Выключение рассылки у пользователя с chat_id = {message.chat.id}")
    await off_notification_in_db(message.chat.id)
    await message.answer(f"Рассылка меню по расписанию выключена" + emoji.emojize(" 🤐"))
    await regenerate_scheduler()
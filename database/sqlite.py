import sqlite3
from utils.log_app import logger

# Путь до БД
LOCATION = "database/olivka_food_bot.sqlite"


# Инициализируем переменную базы данных и создаем ее файл
async def connect_db():
    global db, cur
    db = sqlite3.connect(LOCATION)
    cur = db.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS notification (
        chat_id INTEGER N   OT NULL PRIMARY KEY,
        time TEXT NOT NULL DEFAULT "10:00",
        status INTEGER NOT NULL DEFAULT 1)
        """
        )
    db.commit()


async def create_chat_id(chat_id: int):
    """
    Функция добавляет нового пользователя в базу данных при вводе команды start
    :param int chat_id: chat id пользователя
    :return:
    """
    user = cur.execute(f"SELECT * FROM notification WHERE chat_id == {chat_id}").fetchone()
    if not user:
        # Подготавливаем множественный запрос
        sql = "INSERT INTO notification (CHAT_ID) values(?)"
        # Загружаем данные в базу
        cur.execute(sql, [chat_id])
        logger.info(f"Пользователь с chat_id = {chat_id} добавлен в базу данных с дефолтными параметрами")
        # Сохраняем изменения с помощью функции commit для объекта соединения
        db.commit()
        # Просмотр данных
        # data = cur.execute("SELECT * FROM notification")
        # for row in data:
        #     print(row)
    else:
        logger.info(f"Пользователь с chat_id = {chat_id} отправил сообщение /start, но он уже был добавлен в базу данных")


async def get_chat_id(chat_id: int):
    """
    Функция проверяет наличие записи в таблице, если запись есть возвращает его настройки, если нет то отправляет None
    :param int chat_id: chat id пользователя
    :return: tuple result: кортеж с данными записи о пользователе
    """
    sql = f"SELECT * FROM notification WHERE chat_id = {chat_id}"
    if cur.execute(sql).fetchone() is None:
        return None
    else:
        return cur.execute(sql).fetchone()


async def on_notification_in_db(chat_id: int):
    """
    Функция для внесения в поле on_off значения 1(on)
    :param int chat_id: chat id пользователя
    :return:
    """
    sql = f"UPDATE notification SET status = 1 WHERE chat_id = {chat_id}"
    cur.execute(sql)
    db.commit()


async def off_notification_in_db(chat_id: int):
    """
    Функция для внесения в поле on_off значения 0(off)
    :param int chat_id: chat id пользователя
    :return:
    """
    sql = f"UPDATE notification SET status = 0 WHERE chat_id = {chat_id}"
    cur.execute(sql)
    db.commit()


async def set_custom_time_in_db(chat_id: int, time: str):
    """
    Функция для внесения в поле time пользовательского времени
    :param int chat_id: chat id пользователя
    :param str time: устанавливаемое время в формате HH:MM
    :return:
    """
    sql = "UPDATE notification SET time == '{}' WHERE chat_id == '{}'".format(time, chat_id)
    cur.execute(sql)
    db.commit()


# import asyncio
# asyncio.run(connect_db())
# asyncio.run(create_chat_id(123))
# print(asyncio.run(get_chat_id(123)))

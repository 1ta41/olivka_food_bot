from aiogram import types
from loader import dp
import utils
import datetime

number_today = datetime.datetime.today().weekday() + 1  # Переменная, хранящая номер сегодняшнего дня недели


@dp.message_handler(text='/today')  # Cоздаем message handler который ловит команду /today
async def button_today(message: types.Message):  # Создаем асинхронную функцию, которая отправляет меню на сегодня
    menu = ""
    for item in utils.get_menu_to_list(number_today):
        menu += item + '\n'
    await message.answer(f"Меню на сегодня: \n"
                         f"{menu}")


@dp.message_handler(text='/monday')  # Cоздаем message handler который ловит команду /monday
async def button_monday(message: types.Message):  # Создаем асинхронную функцию, которая отправляет меню на понедельник
    menu = ""
    for item in utils.get_menu_to_list(1):
        menu += item + '\n'
    await message.answer(f"Меню на понедельник: \n"
                         f"{menu}")


@dp.message_handler(text='/tuesday')  # Cоздаем message handler который ловит команду /tuesday
async def button_tuesday(message: types.Message):  # Создаем асинхронную функцию, которая отправляет меню на вторник
    menu = ""
    for item in utils.get_menu_to_list(2):
        menu += item + '\n'
    await message.answer(f"Меню на вторник: \n"
                         f"{menu}")


@dp.message_handler(text='/wednesday')  # Cоздаем message handler который ловит команду /wednesday
async def button_wednesday(message: types.Message):  # Создаем асинхронную функцию, которая отправляет меню на среду
    menu = ""
    for item in utils.get_menu_to_list(3):
        menu += item + '\n'
    await message.answer(f"Меню на среду: \n"
                         f"{menu}")


@dp.message_handler(text='/thursday')  # Cоздаем message handler который ловит команду /thursday
async def button_thursday(message: types.Message):  # Создаем асинхронную функцию, которая отправляет меню на четверг
    menu = ""
    for item in utils.get_menu_to_list(4):
        menu += item + '\n'
    await message.answer(f"Меню на четверг: \n"
                         f"{menu}")


@dp.message_handler(text='/friday')  # Cоздаем message handler который ловит команду /friday
async def button_friday(message: types.Message):  # Создаем асинхронную функцию, которая отправляет меню на пятницу
    menu = ""
    for item in utils.get_menu_to_list(5):
        menu += item + '\n'
    await message.answer(f"Меню на пятницу: \n"
                         f"{menu}")

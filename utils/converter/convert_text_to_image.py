from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from data.config import FONT_LINK


def convert_text_to_image(text: str) -> bytes:
    """
    Функция преобразует текст в изображение. Затем полученное изображение возвращает в виде
    потока байтов.
    :param str text: Преобразуемый текст
    :return bytes result_byte_image: Изображение в виде потока байтов
    """
    # Создаем пустое изображение размером 400х200, цвет фона: белый
    img = Image.new("RGB", (400, 300), color=(255, 255, 255))

    # Создаем объект ImageDraw для рисования на изображении
    draw = ImageDraw.Draw(img)

    # Загружаем шрифт и устанавливаем его размер
    font = ImageFont.truetype(FONT_LINK, 15)

    # Рисуем текст на изображении
    draw.text((10, 10), text, font=font, fill=(0, 0, 0))

    # Сохраняем и возвращаем изображение в виде потока байтов
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="JPEG")
    result_byte_image = img_byte_arr.getvalue()
    img_byte_arr.close()
    return result_byte_image

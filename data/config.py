import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMIN_ID = int(os.getenv("ADMIN_ID"))
FONT_LINK = os.getenv("FONT_LINK")

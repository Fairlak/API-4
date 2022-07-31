import os
import random
import time

import telegram
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_KEY = os.getenv("TELEGRAM_KEY")
TIME = os.getenv("TIME")
CHAT_ID = os.getenv("CHAT_ID")




def publish_image():
    bot = telegram.Bot(token=TELEGRAM_KEY)
    while True:
        dir_pict = ['EPIC_NASA_images', 'NASA_images', 'spacex_images']
        random_dir = random.choice(dir_pict)
        pictures = os.listdir(path=random_dir)
        for picture in pictures:
            path = f'{random_dir}/{picture}'
            bot.send_document(chat_id=CHAT_ID, document=open(path, 'rb'))
            time.sleep(int(TIME))



if __name__ == '__main__':
    publish_image()



import os
import random
import time


import telegram
from dotenv import load_dotenv



def publish_image(telegram_key, message_interval, chat_id):
    bot = telegram.Bot(token=telegram_key)
    while True:
        dir_pict = ['EPIC_NASA_images', 'NASA_images', 'spacex_images']
        random_dir = random.choice(dir_pict)
        pictures = os.listdir(path=random_dir)
        for picture in pictures:
            path = os.path.join(random_dir, picture)
            bot.send_document(chat_id=chat_id, document=open(path, 'rb'))
            time.sleep(int(message_interval))


def main():
    load_dotenv()
    telegram_key = os.getenv("TELEGRAM_KEY")
    message_interval = os.getenv("TIME")
    chat_id = os.getenv("CHAT_ID")
    publish_image(telegram_key, message_interval, chat_id)

if __name__ == '__main__':
    main()



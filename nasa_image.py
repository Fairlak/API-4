import requests
import pathlib
import os
from dotenv import load_dotenv
from dowload_pictures import download_pictures




def generating_download_nasa_links(key_nasa):
    nasa_info = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": key_nasa, "count": 50}
    response = requests.get(nasa_info, params=params)
    nasa_answer = response.json()
    for number, nasa_picture_url in enumerate(nasa_answer):
        if not nasa_picture_url["url"]:
            continue
        nasa_photo_link = nasa_picture_url["url"]
        filename = 'nasa{}.jpg'.format(number)
        file_path = f"NASA_images/{filename}"
        download_pictures(nasa_photo_link, file_path)

def main():
    load_dotenv()
    key_nasa = os.getenv("KEY_NASA")
    pathlib.Path("NASA_images").mkdir(parents=True, exist_ok=True)
    generating_download_nasa_links(key_nasa)

if __name__ == '__main__':
    main()




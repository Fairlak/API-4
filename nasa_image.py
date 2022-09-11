import requests
import pathlib
import os
from dotenv import load_dotenv
from dowload_pictures import download_picture




def get_nasa_images(nasa_key, folder_name):
    nasa_link = 'https://api.nasa.gov/planetary/apod'
    pictures_count = 50
    params = {'api_key': nasa_key, 'count': pictures_count}
    response = requests.get(nasa_link, params=params)
    nasa_answer = response.json()
    for number, nasa_picture_url in enumerate(nasa_answer):
        if not nasa_picture_url['url']:
            continue
        nasa_photo_link = nasa_picture_url['url']
        filename = 'nasa{}.jpg'.format(number)
        file_path = os.path.join(folder_name, filename)
        download_picture(nasa_photo_link, file_path)

def main():
    folder_name = 'NASA_images'
    load_dotenv()
    nasa_key = os.getenv('NASA_KEY')
    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)
    get_nasa_images(nasa_key, folder_name)

if __name__ == '__main__':
    main()




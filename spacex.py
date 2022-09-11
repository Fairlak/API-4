import os

import requests
import pathlib

from dowload_pictures import download_picture


def get_spacex_links():
    request = requests.get('https://api.spacexdata.com/v4/launches')
    spacex_images = request.json()
    for spacex_image in spacex_images:
        if not spacex_image['links']['flickr']['original']:
            continue
        return spacex_image['links']['flickr']['original']


def fetch_spacex_last_launch(folder_name):
    images_links = get_spacex_links()
    for image_num, image_url in enumerate(images_links):
        file_name = f'spacex{image_num}.jpg'
        file_path = os.path.join(folder_name, file_name)
        download_picture(image_url, file_path)


def main():
    folder_name = 'SPACEX_images'
    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch(folder_name)


if __name__ == '__main__':
    main()
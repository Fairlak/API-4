import requests
import pathlib
from dowload_pictures import download_pictures


def spacex():
    request = requests.get('https://api.spacexdata.com/v4/launches')
    links = request.json()
    while len(links):
        spacex_info = links.pop()
        if not len(spacex_info['links']['flickr']['original']):
            continue
        return spacex_info['links']['flickr']['original']


def fetch_spacex_last_launch():
    image_url = spacex()
    for image_num, image_url in enumerate(image_url):
        file_name = f'spacex{image_num}.jpg'
        file_path = f'spacex_images/{file_name}'
        download_pictures(image_url, file_path)


def main():
    pathlib.Path('spacex_images').mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
import requests
import os
import pathlib
from dotenv import load_dotenv
from dowload_pictures import download_pictures

load_dotenv()
KEY_NASA = os.getenv("KEY_NASA")


def epic_nasa_pictures():
    epic_nasa = []
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": KEY_NASA, "count": 50}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_nasa_info = response.json()
    for epic_nasa_links in epic_nasa_info:
        detailed_epic_date = epic_nasa_links['date']
        epic_date = detailed_epic_date.split()[0].replace('-', '/')
        epic_name_image = epic_nasa_links['image']
        epic_links = "https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png".format(epic_date, epic_name_image)
        epic_nasa.append(epic_links)
    for number, picture_url in enumerate(epic_nasa):
        file_name = f'epic_nasa{number}.png'
        file_path = f"EPIC_NASA_images/{file_name}"
        download_pictures(picture_url, file_path, payload)


def main():
    pathlib.Path("EPIC_NASA_images").mkdir(parents=True, exist_ok=True)
    epic_nasa_pictures()


if __name__ == '__main__':
    main()
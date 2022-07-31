import requests
import os
import pathlib
from dotenv import load_dotenv
from dowload_pictures import download_pictures


def generating_download_epic_nasa_links(key_nasa):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": key_nasa}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_nasa_answer = response.json()
    for number, epic_nasa_link in enumerate(epic_nasa_answer):
        detailed_epic_date = epic_nasa_link['date']
        epic_date = detailed_epic_date.split()[0].replace('-', '/')
        epic_image_name = epic_nasa_link['image']
        epic_link = "https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png".format(epic_date, epic_image_name)
        file_name = f'epic_nasa{number}.png'
        file_path = f"EPIC_NASA_images/{file_name}"
        download_pictures(epic_link, file_path, payload)


def main():
    load_dotenv()
    key_nasa = os.getenv("KEY_NASA")
    pathlib.Path("EPIC_NASA_images").mkdir(parents=True, exist_ok=True)
    generating_download_epic_nasa_links(key_nasa)


if __name__ == '__main__':
    main()
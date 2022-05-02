import os
import requests
import pathlib
import os.path
from urllib.parse import urlparse



pathlib.Path("images").mkdir(parents=True, exist_ok=True)
pathlib.Path("NASA_images").mkdir(parents=True, exist_ok=True)
pathlib.Path("EPIC_NASA_images").mkdir(parents=True, exist_ok=True)

KEY_NASA = 'YaiWpAamjnLELDo7k5Y71nbHvwoqoHZRpzeF1IIw'


def nasa_extension():
    link = "https://example.com/txt/hello%20world.jpeg?v=9#python"
    link_parse = urlparse(link)
    print(os.path.splitext(link_parse.path)[1])



def nasa_pictures():
    nasa_info = "https://api.nasa.gov/planetary/apod?api_key=YaiWpAamjnLELDo7k5Y71nbHvwoqoHZRpzeF1IIw&count=50"
    response = requests.get(nasa_info)
    nasa_inf_json = response.json()
    nasa_url = []
    for nasa_picture_url in nasa_inf_json:
        nasa_links = nasa_picture_url['url'].split('.')
        nasa_link_url = nasa_links[-1]
        if nasa_link_url == 'jpg':
            nasa_url.append(nasa_picture_url['url'])
    return nasa_url



def download_nasa_pictures():
    for number, picture in enumerate(nasa_url):
        filename = 'nasa{}.jpg'.format(number)
        response = requests.get(picture)
        response.raise_for_status()
        with open("NASA_images/"+filename, 'wb') as file:
            file.write(response.content)



def epic_nasa_pictures():
    epic_nasa = []
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": KEY_NASA}
    response = requests.get(url, params=payload)
    epic_nasa_info = response.json()
    for epic_nasa_links in epic_nasa_info:        
        detailed_epic_date = epic_nasa_links['date']
        epic_date = detailed_epic_date.split()[0].replace('-', '/')
        epic_name_image = epic_nasa_links['image']
        epic_links = "https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png".format(epic_date, epic_name_image)
        epic_nasa.append(epic_links)
    return epic_nasa


def dowload_epic_nasa_pictures(epic_nasa):
    payload = {"api_key": KEY_NASA}
    for number, picture in enumerate(epic_nasa):
        filename = 'epic_nasa{}.png'.format(number)
        response = requests.get(picture, params=payload)
        response.raise_for_status()
        with open("EPIC_NASA_images/" + filename, 'wb') as file:
            file.write(response.content)



def downloading_picture():
    filename = 'hubble.jpeg'
    url_one_picture = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    response = requests.get(url_one_picture)
    response.raise_for_status()
    with open("images/"+filename, 'wb') as file:
        file.write(response.content)



def spacex():
    request = requests.get('https://api.spacexdata.com/v4/launches')
    links = request.json()
    while len(links):
        spacex_info = links.pop()
        if not len(spacex_info["links"]["flickr"]["original"]):
            continue
        return spacex_info["links"]["flickr"]["original"]



def fetch_spacex_last_launch(spacex):
    for image_num, image_url in enumerate(spacex):
        filename = 'spacex{}.jpg'.format(image_num)
        response = requests.get(image_url)
        response.raise_for_status()
        with open("images/"+filename, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    nasa_url = nasa_pictures()
    download_nasa_pictures()
    epic_nasa = epic_nasa_pictures()
    dowload_epic_nasa_pictures(epic_nasa)
    downloading_picture()
    spacex = spacex()
    fetch_spacex_last_launch(spacex)
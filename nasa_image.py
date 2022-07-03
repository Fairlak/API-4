import requests
import pathlib

from dowload_pictures import download_pictures




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
    for number, picture_url in enumerate(nasa_url):
        filename = 'nasa{}.jpg'.format(number)
        file_path = f"NASA_images/{filename}"
        download_pictures(picture_url, file_path)

def main():
    pathlib.Path("NASA_images").mkdir(parents=True, exist_ok=True)
    nasa_pictures()

if __name__ == '__main__':
    main()




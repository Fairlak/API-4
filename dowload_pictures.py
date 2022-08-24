import requests


def download_picture(picture_url, file_path, payload=None):
    response = requests.get(picture_url, params=payload)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)








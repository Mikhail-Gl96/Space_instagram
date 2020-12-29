import requests
import os
from utils import load_img_with_pillow


def get_spacex_images_urls():
    url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(url=url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    return links


def fetch_spacex_last_launch(path):
    name = "spacex"
    links = get_spacex_images_urls()
    for num, link in enumerate(links):
        temp_path = os.path.join(path, f'{name}_{num}')
        load_img_with_pillow(url=link, path=temp_path)


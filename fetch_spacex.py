import requests
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from utils import load_img_pillow


def get_spacex_images_urls():
    url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(url=url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    return links


def fetch_spacex_last_launch(path):
    name = "spacex"
    links = get_spacex_images_urls()
    if isinstance(links, list):
        for num, link in enumerate(links):
            temp_path = os.path.join(path, f'{name}_{num}')
            load_img_pillow(url=link, path=temp_path)

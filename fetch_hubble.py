import requests
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from utils import load_img_pillow


def get_hubble_images_id():
    url = "http://hubblesite.org/api/v3/images/all"
    response = requests.get(url=url)
    response.raise_for_status()
    links = response.json()
    images_id = [link['id'] for link in links]
    return images_id


def get_hubble_image_by_id(id: int, path: str):
    url = f"http://hubblesite.org/api/v3/image/{id}"
    name = f'hubble_image_{id}'
    response = requests.get(url=url)
    response.raise_for_status()
    image_files = response.json()['image_files']
    links = [f"https:{image_file['file_url']}" for image_file in image_files]
    big_image_link = links[-1]
    load_img_pillow(url=big_image_link, path=os.path.join(path, f'{name}'))


def get_hubble_images_from_collection(collection_name, path):
    url = f"http://hubblesite.org/api/v3/images/{collection_name}"
    response = requests.get(url=url)
    response.raise_for_status()
    images_json = response.json()
    images_id = [image_json["id"] for image_json in images_json]
    for image_id in images_id:
        get_hubble_image_by_id(id=image_id, path=path)

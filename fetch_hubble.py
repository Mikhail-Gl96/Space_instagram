import requests
import os
from utils import load_img_with_pillow


def get_hubble_image_ids():
    url = "http://hubblesite.org/api/v3/images/all"
    response = requests.get(url=url)
    response.raise_for_status()
    links = response.json()
    image_ids = [link['id'] for link in links]
    return image_ids


def get_hubble_image_by_id(img_id: int, path: str):
    url = f"http://hubblesite.org/api/v3/image/{img_id}"
    name = f'hubble_image_{img_id}'
    response = requests.get(url=url)
    response.raise_for_status()
    image_files = response.json()['image_files']
    links = [f"https:{image_file['file_url']}" for image_file in image_files]
    big_image_link = links[-1]
    load_img_with_pillow(url=big_image_link, path=os.path.join(path, f'{name}'))


def get_hubble_images_from_collection(collection_name, path):
    url = f"http://hubblesite.org/api/v3/images/{collection_name}"
    response = requests.get(url=url)
    response.raise_for_status()
    images_dict = response.json()
    image_ids = [image_json["id"] for image_json in images_dict]
    for image_id in image_ids:
        get_hubble_image_by_id(img_id=image_id, path=path)

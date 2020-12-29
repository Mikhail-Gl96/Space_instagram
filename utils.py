import requests
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from PIL import Image


def load_img_pillow(url, path):
    response = requests.get(url=url, verify=False, stream=True)
    response.raise_for_status()
    try:
        image = Image.open(response.raw)
        image.thumbnail((1080, 1080))
        rgb_im = image.convert('RGB')
        rgb_im.save(f'{path}.jpg')
    except IOError:
        print(f"Unable to open image from {url}")


def create_dir(path, name):
    path_dir = os.path.join(path, name)
    os.makedirs(path_dir, exist_ok=True)
    return path_dir

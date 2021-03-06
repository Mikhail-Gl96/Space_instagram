import requests
from PIL import Image


def load_img_with_pillow(url, path):
    response = requests.get(url=url, verify=False, stream=True)
    response.raise_for_status()
    try:
        image = Image.open(response.raw)
        image.thumbnail((1080, 1080))
        rgb_im = image.convert('RGB')
        rgb_im.save(f'{path}.jpg')
    except IOError:
        print(f"Unable to open image from {url}")

import os
import dotenv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import get_hubble_images_from_collection

from instabot import Bot


def download_all_photos(image_paths):
    try:
        fetch_spacex_last_launch(path=image_paths)
    except Exception as e:
        print(f'Error: {e}')

    collection_names = ["holiday_cards", "wallpaper", "spacecraft", "news",
                        "printshop", "stsci_gallery"]
    for collection in collection_names:
        try:
            get_hubble_images_from_collection(collection_name=collection, path=image_paths)
        except Exception as e:
            print(f'Error: {e}')


def get_all_image_paths(image_paths):
    images = os.listdir(image_paths)
    paths = [os.path.join(image_paths, image) for image in images]
    return paths


if __name__ == "__main__":
    dotenv.load_dotenv()

    instagram_login = os.getenv('INSTAGRAM_LOGIN')
    instagram_password = os.getenv('INSTAGRAM_PASSWORD')

    bot = Bot()
    bot.login(username=instagram_login, password=instagram_password)

    dir_name = 'images'

    base_path = os.getcwd()

    image_paths = os.path.join(base_path, dir_name)
    os.makedirs(image_paths, exist_ok=True)

    download_all_photos(image_paths=image_paths)

    paths = get_all_image_paths(image_paths=image_paths)

    for path in paths:
        try:
            bot.upload_photo(path, caption="Nice pic!")
            os.remove(f'{path}.REMOVE_ME')
        except Exception as e:
            os.remove(path)
            print(f'Wrong aspect ratio. Delete image file in {path}')


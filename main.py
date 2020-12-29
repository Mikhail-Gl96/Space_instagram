import os
import dotenv

from utils import create_dir
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import get_hubble_images_from_collection

from instabot import Bot


def download_all_photos(images_path):
    try:
        fetch_spacex_last_launch(path=images_path)
    except Exception as e:
        print(f'Error: {e}')

    collection_names = ["holiday_cards", "wallpaper", "spacecraft", "news",
                        "printshop", "stsci_gallery"]
    for collection in collection_names:
        try:
            get_hubble_images_from_collection(collection_name=collection, path=images_path)
        except Exception as e:
            print(f'Error: {e}')


def get_all_image_paths(images_path):
    images = os.listdir(images_path)
    paths = [os.path.join(images_path, image) for image in images]
    return paths


if __name__ == "__main__":
    dotenv.load_dotenv()

    login_instagram = os.getenv('LOGIN_INSTAGRAM')
    password_instagram = os.getenv('PASSWORD_INSTAGRAM')

    bot = Bot()
    bot.login(username=login_instagram, password=password_instagram)

    dir_name = 'images'

    base_path = os.getcwd()
    images_path = create_dir(path=base_path, name=dir_name)

    download_all_photos(images_path=images_path)

    paths = get_all_image_paths(images_path=images_path)

    for path in paths:
        try:
            bot.upload_photo(path, caption="Nice pic!")
            os.remove(f'{path}.REMOVE_ME')
        except Exception as e:
            os.remove(path)

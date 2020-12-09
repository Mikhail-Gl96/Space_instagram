import os
import dotenv

from utils import create_dir
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import get_hubble_images_from_collection

from instabot import Bot


def upload_photo_to_instagram(bot_instagram, path_photo):
    bot_instagram.upload_photo(path_photo, caption="Nice pic!")


def download_all_photos(images_path):
    fetch_spacex_last_launch(path=images_path)

    collection_names = ["holiday_cards", "wallpaper", "spacecraft", "news",
                        "printshop", "stsci_gallery"]
    for collection in collection_names:
        get_hubble_images_from_collection(collection_name=collection, path=images_path)


def get_all_image_paths(images_path):
    all_pics = os.listdir(images_path)
    paths = [os.path.join(images_path, image) for image in all_pics]
    return paths


if __name__ == "__main__":
    dotenv.load_dotenv()

    LOGIN = os.getenv('LOGIN')
    PASSWORD_INSTAGRAM = os.getenv('PASSWORD_INSTAGRAM')

    # bot = Bot()
    # bot.login(username=LOGIN, password=PASSWORD_INSTAGRAM)

    dir_name = 'images'

    BASE_PATH = os.getcwd()
    images_path = create_dir(path=BASE_PATH, name=dir_name)

    download_all_photos(images_path=images_path)

    paths = get_all_image_paths(images_path=images_path)

    for path in paths:
        upload_photo_to_instagram(bot_instagram=bot, path_photo=path)

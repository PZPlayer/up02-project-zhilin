import os
from PIL import Image, ImageTk

from config import BASE_DIR

RES_DIR = os.path.join(BASE_DIR, "resources")
PATH_PICTURE = os.path.join(RES_DIR, "picture.png")
PATH_LOGO = os.path.join(RES_DIR, "logo.png")
PATH_ICON = os.path.join(RES_DIR, "icon.ico")


def load_image(path, size=(100, 100)):
    try:
        if not path or not os.path.exists(path):
            return None
        img = Image.open(path).resize(size)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка загрузки {path}: {e}")
        return None


def load_image_proportional(path, max_size=(100, 100)):
    try:
        if not path or not os.path.exists(path):
            return None
        img = Image.open(path)
        img.thumbnail(max_size)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка загрузки {path}: {e}")
        return None


def get_product_image(image_name, size=(100, 100)):
    """Фото врача из resources/. Нет файла или имя пустое — заглушка picture.png."""
    if image_name:
        photo = load_image(os.path.join(RES_DIR, image_name), size)
        if photo:
            return photo
    return load_image(PATH_PICTURE, size)

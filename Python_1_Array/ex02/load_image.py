from PIL import Image, UnidentifiedImageError
import numpy as nompy

# c1r6p3% chmod 000 salut.jpeg
# print(ft_load(""))
# print(ft_load("adieu.jpeg")) adieu est un dossier HAHAHAHAHAHA CHEEEEH


def ft_load(path: str) -> nompy.array:
    """Loads an image"""
    type = [".jpeg", ".jpg"]
    try:
        assert isinstance(path, str), "wrong typeee 🤣🤣🤣"
        assert Image.open(path).format not in type, "wrong format 🤣🤣🤣"
    except (UnidentifiedImageError, AssertionError) as bad_args:
        print(bad_args)
        return
    except FileNotFoundError:
        print("File not found:", path)
        return
    img = Image.open(path)
    img.show(img)
    print("The shape of image is:", nompy.array(img).shape)
    print(nompy.array(img))
    img.load()
    return nompy.array(img)

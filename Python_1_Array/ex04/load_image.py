from PIL import Image, UnidentifiedImageError
import numpy as nompy


def ft_load(path: str) -> nompy.array:
    """Loads an image, crop it, flip it, and
    rotate it"""
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
    img_cropped = img.crop((450, 100, 850, 500))
    img_cropped = img_cropped.convert('L')
    print("The shape of image is:", nompy.array(img_cropped).shape)

    img_cropped = img_cropped.rotate(90, Image.NEAREST, expand = 1)
    img_cropped = img_cropped.transpose(Image.FLIP_TOP_BOTTOM)
    img_cropped.show()
    print(nompy.array(img_cropped).reshape(400, 400, 1))
    print("New shape after transpose:", nompy.array(img_cropped).shape)
    print(nompy.array(img_cropped))
    return nompy.array(img)

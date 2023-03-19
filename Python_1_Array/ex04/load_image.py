from PIL import Image, UnidentifiedImageError
import numpy as nompy


def ft_load(path: str) -> nompy.array:
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
    print("The shape of image is:", nompy.array(img).shape)
    print(nompy.array(img))

    img_cropped = img.crop((450, 100, 850, 500))
    img_cropped = img_cropped.convert('L')
    img_cropped.show()
    print("New shape after slicing:", nompy.array(img_cropped).shape)
    print(nompy.array(img_cropped).reshape(400, 400, 1))
    return nompy.array(img)

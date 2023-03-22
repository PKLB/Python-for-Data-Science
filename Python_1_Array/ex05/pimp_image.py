import numpy as nompy
from PIL import Image, ImageOps


def ft_invert(array: nompy.array) -> nompy.array:
    """Invert the COLORS of the image"""
    newparam = nompy.copy(array)
    newimg = Image.fromarray(newparam)
    newimg = ImageOps.invert(newimg)
    newimg.show(newparam)
    return newparam


def ft_red(array: nompy.array) -> nompy.array:
    """Put a red filter to the image"""
    newparam = nompy.copy(array)
    newparam[:, :, 1] = 0
    newparam[:, :, 2] = 0
    newimg = Image.fromarray(newparam)
    newimg.show(newparam)
    return newparam


def ft_green(array: nompy.array) -> nompy.array:
    """Put a green filter to the image"""
    newparam = nompy.copy(array)
    newparam[:, :, 0] = 0
    newparam[:, :, 2] = 0
    newimg = Image.fromarray(newparam)
    newimg.show(newparam)
    return newparam


def ft_blue(array: nompy.array) -> nompy.array:
    """Put a blue filter to the image"""
    newparam = nompy.copy(array)
    newparam[:, :, 0] = 0
    newparam[:, :, 1] = 0
    newimg = Image.fromarray(newparam)
    newimg.show(newparam)
    return newparam


def ft_grey(array: nompy.array) -> nompy.array:
    """Put a grey filter to the image"""
    newparam = nompy.copy(array)
    newimg = Image.fromarray(newparam)
    newimg = newimg.convert('L')
    newimg.show(newparam)
    return newparam

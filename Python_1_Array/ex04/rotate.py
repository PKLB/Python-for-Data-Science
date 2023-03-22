from load_image import ft_load


def ft_rotate(path: str):
    """Calls another modified ft_load function"""
    ft_load(path)


if __name__ == "__main__":
    ft_rotate("animal.jpeg")

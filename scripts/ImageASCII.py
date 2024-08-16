from PIL import Image

# ASCII characters
ASCII_CHAR = ['@', '#', 'S', '%', '?', '*', '+', ':', ',', '.']

def resize(im, new_width=100):
    """
    Resize image to new_width while maintaining aspect ratio.
    """
    width, height = im.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_image = im.resize((new_width, new_height))
    return resized_image

def desaturate(im):
    """
    Convert image to grayscale.
    """
    grayscale_image = im.convert("L")
    return grayscale_image

def pixels_to_ASCII(im):
    """
    Convert grayscale image to ASCII characters.
    """
    pixels = im.getdata()
    characters = "".join([ASCII_CHAR[pixel // 25] for pixel in pixels])
    return characters
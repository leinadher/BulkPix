from PIL import Image
import os

# ASCII characters
ASCII_CHAR = ['@', '#', 'S', '%', '?', '*', '+', ':', ',', '.']


# Resize image to 100xH
def resize(im, new_width=100):
    width, height = im.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_image = im.resize((new_width, new_height))
    return resized_image


# Desaturate image
def desaturate(im):
    grayscale_image = im.convert("L")
    return grayscale_image


# Convert grays to ASCII characters
def pixels_to_ASCII(im):
    pixels = im.getdata()
    characters = "".join([ASCII_CHAR[pixel // 25] for pixel in pixels])
    return characters


# Main
def main(new_width=100):
    file = input("Enter full image name (with extension) from 'images': ")
    path = f"images/{file}"
    try:
        im = Image.open(path)
    except FileNotFoundError:
        print(f"{path} is not a valid file path!")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Apply transformations
    resized_image = resize(im, new_width)
    desaturated_image = desaturate(resized_image)
    new_image_data = pixels_to_ASCII(desaturated_image)

    # Format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    print(ascii_image)

    with open("../ASCII/ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()

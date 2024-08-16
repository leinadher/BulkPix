from PIL import Image
import os

def resize(im, new_width):
    width, height = im.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_image = im.resize((new_width, new_height))
    return resized_image

## RESIZE IN BULK
files = os.listdir("images")
extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
i = 0

# Ensure the target directory exists
os.makedirs("images_resized", exist_ok=True)

while True:
    try:
        new_width = int(input("New width in pixels: "))
        break
    except ValueError:
        print("Please enter a valid integer for the width.")

for file in files:
    ext = file.split(".")[-1]
    if ext in extensions:
        i += 1
        im = Image.open(f"images/{file}")
        im_resized = resize(im, new_width)
        filepath = f"images_resized/{file}.jpg"
        im_resized.save(filepath)
        print(f"Image {i}/{len(files)}")

print(f"All {len(files)} images resized")
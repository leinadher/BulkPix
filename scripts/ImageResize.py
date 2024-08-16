from PIL import Image
import os

def resize_image(image_path, new_width, output_folder):
    try:
        im = Image.open(image_path)
        width, height = im.size
        ratio = height / width
        new_height = int(ratio * new_width)
        resized_image = im.resize((new_width, new_height))

        base_name = ".".join(os.path.basename(image_path).split(".")[:-1])
        new_filename = f"{base_name}_resized.jpg"
        output_path = os.path.join(output_folder, new_filename)
        resized_image.save(output_path)

        return output_path
    except Exception as e:
        raise RuntimeError(f"Error resizing image: {e}")

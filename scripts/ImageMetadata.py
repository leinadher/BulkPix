from PIL import Image
from PIL.ExifTags import TAGS
import pandas as pd
import os

# Function to extract only specific EXIF data from an image
def extract_specific_exif(image_path):
    """Extract specific EXIF data from an image and return it as a dictionary."""
    image = Image.open(image_path)
    exif_data = image._getexif()
    exif = {}

    # Extract file information
    exif['FileName'] = os.path.splitext(os.path.basename(image_path))[0]
    exif['ItemType'] = image.format
    exif['FileSize(KB)'] = round(os.path.getsize(image_path) / 1024, 2)  # Convert to KB
    exif['Width'] = image.width
    exif['Height'] = image.height
    exif['Resolution'] = image.info.get('dpi', (None, None))[0]  # DPI (horizontal resolution)
    exif['BitDepth'] = image.mode
    exif['ColourRepresentation'] = image.info.get('icc_profile', None) is not None

    # Mapping for required EXIF tags
    tag_map = {
        'DateTime': 'DateTaken',
        'Make': 'CameraMaker',
        'Model': 'CameraModel',
        'FNumber': 'F-Stop',
        'ExposureTime': 'ExposureTime',
        'ISOSpeedRatings': 'ISO',
        'ExposureBiasValue': 'ExposureBias',
        'FocalLength': 'FocalLength',
        'MaxApertureValue': 'MaxAperture',
        'Flash': 'FlashMode'
    }

    if exif_data is not None:
        for tag, value in exif_data.items():
            decoded_tag = TAGS.get(tag, tag)
            if decoded_tag in tag_map:
                exif[tag_map[decoded_tag]] = value

    return exif

# Function to apply the above extraction to a directory of images
def metadata_to_dataframe(image_dir):
    """Extract specific metadata from all JPG images in a directory and store it in a DataFrame."""
    data = []

    for root, dirs, files in os.walk(image_dir):
        for file_name in files:
            if file_name.lower().endswith('.jpg'):
                file_path = os.path.join(root, file_name)
                exif_data = extract_specific_exif(file_path)
                data.append(exif_data)

    # Create DataFrame from the collected data
    df = pd.DataFrame(data)
    return df

def extract_metadata(input_dir, output_dir):
    """Extract metadata from all JPG images in the input directory and save it as a CSV in the output directory."""

    try:
        # Extract metadata into a DataFrame
        df = metadata_to_dataframe(input_dir)

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Save DataFrame to CSV
        output_path = os.path.join(output_dir, "image_metadata.csv")
        df.to_csv(output_path, index=False)
        print(f"Metadata saved to {output_path}")

    except Exception as e:
        raise RuntimeError("Error with metadata extraction: " + str(e))
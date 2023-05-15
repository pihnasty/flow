"""Change the DPI (dots per inch) metadata of the result image file"""
from PIL import Image


def change_dpi_tag(image_path, new_dpi):
    image = Image.open(image_path)
    image_info = image.info

    # Create a new dictionary with the updated DPI value
    updated_info = {**image_info, 'dpi': (new_dpi, new_dpi)}

    # Save the image with the updated DPI
    image.save(image_path, **updated_info)

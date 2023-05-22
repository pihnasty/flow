"""Unit with utils"""

from PIL import Image


def change_dpi_tag(image_path, dpi):
    """The function changes the DPI (dots per inch) metadata
    of the result image file
    :param image_path:
    :param dpi:
    :return:
    """
    image = Image.open(image_path)
    image_info = image.info

    # Create a new dictionary with the updated DPI value
    updated_info = {**image_info, 'dpi': (dpi, dpi)}

    # Save the image with the updated DPI
    image.save(image_path, **updated_info)


def mm_to_inch(mm_value):
    """
    The function converts mm to inches.
    :param mm_value: size in mm.
    :return: size in inches.
    """
    return mm_value / 25.4

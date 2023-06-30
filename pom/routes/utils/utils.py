"""Unit with utils"""

from PIL import Image


def change_canvas_size(image_path, new_width, new_height, dpi, background_color):
    """The function changes the canvas size of an image
    of the result image file
    :param dpi:
    :param new_height:in mm
    :param new_width:in mm
    :param image_path:
    :param background_color:color in RGB, for ex. (255, 255, 255) = white
    :return:
    """
    image = Image.open(image_path)
    current_width, current_height = image.size

    # Convert image size from mm into pixels
    new_width = int(new_width * dpi / 25.4)
    new_height = int(new_height * dpi / 25.4)

    # Create a new image with the desired canvas size and background color
    new_image = Image.new('RGB', (new_width, new_height), background_color)

    # Paste the original image onto the new image, centered
    paste_x = (new_width - current_width) // 2
    paste_y = (new_height - current_height) // 2
    new_image.paste(image, (paste_x, paste_y))

    # Save the new image
    new_image.save(image_path)

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


def size_mm_to_inch(x_size, y_size, decimal_places):
    """
    Creates size of plot as string 'X,Y' converted form mm to inches
    :param x_size:
    :param y_size:
    :param decimal_places:
    :return: string 'X,Y'
    """
    return (format(mm_to_inch(x_size), f'.{decimal_places}f') +
            format(mm_to_inch(y_size), f'.{decimal_places}f'))

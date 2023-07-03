"""Unit with utils"""

from PIL import Image, ImageDraw


def change_canvas_size(image_path, new_width, new_height, dpi):
    """The function changes the canvas size of an image
    of the result image file
    :param dpi:
    :param new_height:in mm
    :param new_width:in mm
    :param image_path:
    :return:
    """
    image = Image.open(image_path)
    current_width, current_height = image.size

    # Convert image size from mm into pixels
    new_width = int(new_width * dpi / 25.4)
    new_height = int(new_height * dpi / 25.4)

    # Create a new image with the desired canvas size and
    # background color -> color=(255, 255, 255) = white
    new_image = Image.new('RGB', size=(new_width, new_height), color=(255, 255, 255))

    # Paste the original image onto the new image, centered
    paste_x = (new_width - current_width) // 2
    paste_y = (new_height - current_height) // 2
    new_image.paste(image, (paste_x, paste_y))

    # Save the new image
    new_image.save(image_path)


def cut_C_k_canvas(image_path, new_width, new_height, paste_x, paste_y):
    """The function cuts the canvas size of an image
    of the result image file
    :param paste_x:the position where to paste in pixels
    :param paste_y:the position where to paste in pixels
    :param new_height:in pixels
    :param new_width:in pixels
    :param image_path:
    :return:
    """
    image = Image.open(image_path)

    # Convert image size from mm into pixels
    # new_width = int(new_width * dpi / 25.4)
    # new_height = int(new_height * dpi / 25.4)

    # Create a new image with the desired canvas size and background color (color)
    new_image = Image.new('RGB', size=(new_width, new_height), color=(255, 255, 255))

    # Paste the original image onto the new image
    new_image.paste(image, (paste_x, paste_y))

    # Save the new image
    new_image.save(image_path)


def draw_frame(image_path, frame_width, frame_color):
    """The function draws a frame around the canvas of an image
    :param image_path:
    :param frame_width:
    :param frame_color:
    :return:
    """
    image = Image.open(image_path)
    image_width, image_height = image.size

    # Create a new image with increased canvas size to accommodate the frame
    new_width = image_width + 2 * frame_width
    new_height = image_height + 2 * frame_width
    new_image = Image.new('RGB', (new_width, new_height), frame_color)

    # Paste the original image onto the new image, centered within the frame
    paste_x = frame_width
    paste_y = frame_width
    new_image.paste(image, (paste_x, paste_y))

    # Draw the frame borders
    draw = ImageDraw.Draw(new_image)
    draw.rectangle([(0, 0), (new_width - 1, new_height - 1)],
                   outline=frame_color, width=frame_width)

    # Save the new image
    new_image.save(image_path)


def paste_c_k_into_route(route_path, c_k_path):
    """The function pastes C_k image into the result route image
    :param route_path:
    :param c_k_path:
    :return:
    """
    route_image = Image.open(route_path)
    c_k_image = Image.open(c_k_path)
    route_image.paste(c_k_image, (0, 0))

    route_image.save(route_path)


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

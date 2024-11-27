import pyautogui
from PIL import Image, ImageDraw
import cv2
import numpy as np
import time
import math
import keyboard

order_of_execution = 1
router_color = []
current_charater_position = [650, 340]


def get_average_color(position, image):
    # Coordinates of the top-left pixel of the square
    square_x = position[0] - 3
    square_y = position[1] - 3

    # Size of the square (in pixels)
    square_size = 6

    # Create an empty list to store the RGB values
    rgb_values = []

    # Iterate over each pixel within the square
    for y in range(square_y, square_y + square_size):
        for x in range(square_x, square_x + square_size):
            # Capture the color of the pixel and append it to the list
            pixel_color = image.getpixel((x, y))
            #pixel_color = pyautogui.pixel(x, y)
            rgb_values.append(pixel_color)

    # Calculate the average color
    average_color = tuple(np.mean(rgb_values, axis=0, dtype=int))
    return average_color


def find_the_direction_to_move(order_of_execution_def):

    current_position = pyautogui.position()

    # Capture a screenshot
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a PIL Image object
    image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Define the circle parameters
    # Replace with the actual coordinates of the center
    center = (current_charater_position[0], current_charater_position[1])
    radius = 100  # Replace with the actual radius value
    color = (0, 0, 255)  # Set the color of the circle (RGB format)
    thickness = 2  # Set the thickness of the circle

    # Draw the circle on the image
    # draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius),
    # outline=color, width=thickness)

    # Get the color code of the pixels within the circle
    circle_pixels = []
    circle_index_met = []
    global order_of_execution
    global router_color
    order_of_execution += 1

    if order_of_execution_def == 1:
        pyautogui.click()
        pyautogui.press("numlock")
        router_color = get_average_color(current_position, image)

    color_current_position = (router_color)
    color_difference = 5
    color_current_position_plus = (
        color_current_position[0] + color_difference,
        color_current_position[1] + color_difference,
        color_current_position[2] + color_difference)
    color_current_position_min = (
        color_current_position[0] - color_difference,
        color_current_position[1] - color_difference,
        color_current_position[2] - color_difference)

    for angle in range(0, 360):
        x = int(center[0] + radius * math.cos(math.radians(angle)))
        y = int(center[1] + radius * math.sin(math.radians(angle)))
        #pixel_color = image.getpixel((x, y))

        position_pixel_color = (x, y)
        # print(position_pixel_color)
        pixel_color = get_average_color(position_pixel_color, image)
        # print(pixel_color)

        if color_current_position_min <= pixel_color <= color_current_position_plus:
            # Draw the pixel with a different color
            # Set the color of the drawn pixel (RGB format)
            draw.point((x, y), fill=(0, 255, 0))
            circle_index_met.append((x, y))

        #print('pixel_color', pixel_color)
        # circle_pixels.append(pixel_color)

    if len(circle_index_met) != 0:
        print("color_current_position_min", color_current_position_min)
        print("color_current_position_plus", color_current_position_plus)
        filter_array = []
        for i in circle_index_met:
            average_color = get_average_color(i,image)
            print("average_color",average_color)
            if color_current_position_min <= average_color <= color_current_position_plus:
                draw.point((x, y), fill=(255, 0, 0))
                filter_array.append(i)

        nearest_index = min(range(len(circle_index_met)),
                            key=lambda i: math.hypot(
                                circle_index_met[i][0] - current_position[0],
                                circle_index_met[i][1] - current_position[1]))
        nearest_position = circle_index_met[nearest_index][0], circle_index_met[nearest_index][1]

        distance_between_nearest_current_position = math.sqrt(
            (nearest_position[0] - current_position[0])**2 + (nearest_position[1] - current_position[1])**2)

        if distance_between_nearest_current_position <= (radius):
            pyautogui.moveTo(nearest_position)

    image.show()


def move():
    pyautogui.moveTo(
        current_charater_position[0] - 50, current_charater_position[1] - 50)
    time.sleep(5)
    global order_of_execution

    while True:
        find_the_direction_to_move(order_of_execution)
        pyautogui.sleep(0.1)

    pyautogui.press("numlock")


def on_key_press(event):
    if event.name == 'space':
        move()

    if event.name == 'esc':
        print("Escape key pressed. Exiting...")
        keyboard.unhook_all()  # Stop listening for key events
        return


check = True


def test():
    # keyboard.on_press(on_key_press)  # Register the callback function
    global check
    # keyboard.wait('esc')  # Wait for the Escape key to be pressed
    while check == True:
        if keyboard.is_pressed('space'):
            print("Space key is pressed")
            # Execute your code here
            check = False
        elif keyboard.is_pressed('q'):
            print('q')


move()

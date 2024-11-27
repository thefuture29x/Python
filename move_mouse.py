import pyautogui
from PIL import Image
import time
import cv2
import numpy as np

def test123():
    # Read the image
    image = cv2.imread('/Users/haiphong/Desktop/Ảnh chụp Màn hình 2023-05-08 lúc 19.18.09.png',-1)
    # Draw a circle on the image
    center = (1440, 900)  # Replace with the actual coordinates of the center
    radius = 250  # Replace with the actual radius value
    color = (0, 0, 255)  # Set the color of the circle (BGR format)
    thickness = 2  # Set the thickness of the circle
    cv2.circle(image, center, radius, color, thickness)

    # Create a mask image with zeros
    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    # Draw a filled circle on the mask
    cv2.circle(mask, center, radius, 255, -1)  

    # Apply the mask to the original image
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Get the color code of the pixels within the circle
    circle_pixels = masked_image[np.where(masked_image != 0)]

    print(image.shape)
    cv2.imshow('Image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #for i in circle_pixels:

        #print(circle_pixels[i])

def test():

    current_charater = [640, 350]
    #pyautogui.moveTo(current_charater)
    pyautogui.moveTo(current_charater[0] + 100, current_charater[1] + 100)
    pyautogui.click()
    #pyautogui.press("numlock")

    #for i in range(3):

    # Capture a screenshot
    screenshot = pyautogui.screenshot()

    current_position = pyautogui.position()
    current_index = (current_position.x, current_position.y)

    #mouse_index = [(current_charater[0] + 50) , (current_charater[1] + 50)]

    # Get the color at the mouse index
    pixel_color = screenshot.getpixel(current_index)

    way_color = [pixel_color[0],pixel_color[1],pixel_color[2]]

    # Print the color values



    image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())
    # Draw a circle on the image
    center = (640, 350)  # Replace with the actual coordinates of the center
    radius = 250  # Replace with the actual radius value
    color = (0, 0, 255)  # Set the color of the circle (BGR format)
    thickness = 2  # Set the thickness of the circle
    cv2.circle(image, center, radius, color, thickness)

    # Create a mask image with zeros
    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    # Draw a filled circle on the mask
    cv2.circle(mask, center, radius, 255, -1)  

    # Apply the mask to the original image
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Get the color code of the pixels within the circle
    circle_pixels = masked_image[np.where(masked_image != 0)]

    print(image.shape)
    cv2.imshow('Image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    time.sleep(3)
    print(way_color)
        

    #pyautogui.press("numlock")



    

def moveMouse():
    # Get the current mouse position
    current_position = pyautogui.position()
    #current_x, current_y = current_position.x, current_position.y
    current_x, current_y = 665,355
    # Define the target coordinates
    print(current_x,current_y)
    target_x, target_y = 200, 200

    # Calculate the distance to move in each step
    delta_x = (target_x - current_x) / 25
    delta_y = (target_y - current_y) / 25

    # Move the mouse in steps
    for i in range(25):
        new_x = current_x + delta_x * i
        new_y = current_y + delta_y * i
        pyautogui.moveTo(new_x, new_y)

    # Move the mouse to the final destination
    pyautogui.moveTo(target_x, target_y)
    

test()
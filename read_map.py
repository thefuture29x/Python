import cv2
import pyautogui
import time


def moveMouse(x,y):
    # Get the current mouse position
    current_position = pyautogui.position()
    current_x, current_y = current_position.x, current_position.y
    #current_x, current_y = 1000,1000
    # Define the target coordinates
    target_x, target_y = x, y

    # Calculate the distance to move in each step
    delta_x = (target_x - current_x) / 10
    delta_y = (target_y - current_y) / 10

    # Move the mouse in steps
    for i in range(10):
        new_x = current_x + delta_x * i
        new_y = current_y + delta_y * i
        pyautogui.moveTo(new_x, new_y)

    # Move the mouse to the final destination
    pyautogui.moveTo(target_x, target_y)

def convertImageToBinary(map_image):
    # Perform operations on the image
        # ...
        # Apply image segmentation to obtain a binary image
        # You'll need to adapt this step to your specific map image
        
        binary_image = ...  # Apply appropriate segmentation techniques

        # Convert the map image to grayscale
        gray_image = cv2.cvtColor(map_image, cv2.COLOR_BGR2GRAY)

        threshold1 = 50
        threshold2 = 150
        # Apply Canny edge detection to obtain a binary image
        binary_image = cv2.Canny(gray_image, threshold1, threshold2)


        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Select the largest contour as the river path
        river_contour = max(contours, key=cv2.contourArea)

        # Simplify the river contour using Douglas-Peucker algorithm
        epsilon = 0.01 * cv2.arcLength(river_contour, True)
        simplified_contour = cv2.approxPolyDP(river_contour, epsilon, True)

        # Extract the coordinates of the river path
        river_path = []
        for point in simplified_contour:
            x, y = point[0]
            river_path.append((x, y))


        print(river_path)
        moveMouseAlongRiver(river_path)


def moveMouseAlongRiver(river_path):
    # Iterate through the river path and move the mouse
    for x, y in river_path:
        moveMouse(x,y)
        #pyautogui.moveTo(x, y)
        #time.sleep(2)


def readImage():
    # Load the map image
    map_image = cv2.imread('P:\Images\map-river.jpg')

    # Check if the image was loaded successfully
    if map_image is not None:
        convertImageToBinary(map_image)    
    else:
        print("Failed to load the image.")


readImage()
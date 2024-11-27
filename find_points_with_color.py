from PIL import Image, ImageDraw
import cv2

def find_points_with_color(image, center, radius, target_color, tolerance=0):
    # Create a mask image with zeros
    mask = Image.new('L', image.size, 0)

    # Draw a filled circle on the mask
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=255)

    # Iterate over the pixels within the circle
    points_with_color = []
    for x in range(center[0] - radius, center[0] + radius):
        for y in range(center[1] - radius, center[1] + radius):
            # Check if the pixel is within the circle
            if (x - center[0]) ** 2 + (y - center[1]) ** 2 <= radius ** 2:
                # Get the color code of the pixel
                pixel_color = image.getpixel((x, y))
                # Check if the color is within the tolerance range
                if all(abs(pixel_color[i] - target_color[i]) <= tolerance for i in range(3)):
                    points_with_color.append((x, y))

    return points_with_color

# Example usage
image = Image.open('/Users/haiphong/Desktop/Ảnh chụp Màn hình 2023-05-08 lúc 19.18.09.png')
center = (100, 100)  # Center of the circle
radius = 50  # Radius of the circle
target_color = (255, 0, 0)  # Color code to compare with
tolerance = 10  # Tolerance for color comparison

#points = find_points_with_color(image, center, radius, target_color, tolerance)
#print(points)
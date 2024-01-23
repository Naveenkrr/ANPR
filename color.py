import cv2
import numpy as np

def classify_vehicle_color(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define color ranges for common vehicle colors
    color_ranges = {
        'white': [(200, 200, 200), (255, 255, 255)],
        'black': [(0, 0, 0), (50, 50, 50)],
        'red': [(150, 0, 0), (255, 50, 50)],
        'blue': [(0, 0, 150), (50, 50, 255)],
        'green': [(0, 150, 0), (50, 255, 50)],
        'yellow': [(150, 150, 0), (255, 255, 50)],
    }

    # Loop through color ranges and check if the image contains pixels in that range
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(image_rgb, lower, upper)

        if cv2.countNonZero(mask) > 0:
            return color

    return "unknown"

# Example usage
image_path = 'C:/Users/Naveen/Desktop/vehicle-color-detection-master/car color dataset 200/black/000980.jpg'
vehicle_color = classify_vehicle_color(image_path)
print(f"The color of the vehicle is: {vehicle_color}")

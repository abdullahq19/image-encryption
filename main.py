import cv2
import os

# Specify the path to the image
image_path = 'your_image.png'

# Check if the file exists
if not os.path.exists(image_path):
    print(f"Error: The file at {image_path} does not exist. Please check the file path.")
else:
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
    else:
        # Resize the image
        # Get the dimensions of the image
        (height, width) = image.shape[:2]

        # Set the new width and height
        new_width = 800  # or any width you prefer
        new_height = int((new_width / width) * height)  # maintaining aspect ratio

        # Resize the image
        resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

        # Display the resized image in a window
        cv2.imshow('Resized Image Window', resized_image)

        # Wait for a key press indefinitely or for a specified amount of time in milliseconds
        cv2.waitKey(0)  # 0 means wait indefinitely

        # Destroy all windows created by OpenCV
        cv2.destroyAllWindows()

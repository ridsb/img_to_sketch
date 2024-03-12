import cv2
import os

# Get the name of the image file (assuming it's in the same folder as the script)
image_name = input("Enter the name of the image file (with extension, e.g., image.jpg): ")

# Get the path of the script
script_path = os.path.dirname(os.path.realpath(__file__))

# Construct the full path to the image
image_path = os.path.join(script_path, image_name)

# Read the input image
image1 = cv2.imread(image_path)

# Check if the image is successfully loaded
if image1 is None:
    print(f"Error: Unable to load the image '{image_name}'. Make sure it's in the same folder as the script.")
    exit()

window_name = 'Actual image'

cv2.imshow(window_name, image1)

grey_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

# Save the sketch image in the same folder as the script
sketch_path = os.path.join(script_path, "sketch.jpeg")
cv2.imwrite(sketch_path, sketch)

# Read the saved sketch image
sketch_image = cv2.imread(sketch_path)
window_name = 'Sketch image'

cv2.imshow(window_name, sketch_image)
cv2.waitKey(0)
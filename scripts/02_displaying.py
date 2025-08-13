import cv2
import os

image_path = os.path.join("..", "assets", "python_img.png")
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Image not found at '{image_path}'")
else:
    cv2.imshow("Image Display", image)
    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyAllWindows()

import cv2
import os

image_path = os.path.join("..", "assets", "python_img.png")

if not os.path.exists(image_path):
    print(f"Error: File not found at '{image_path}'")
else:
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image found but could not be read!")
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Original Image", image)
        cv2.imshow("Grayscale Image", gray)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

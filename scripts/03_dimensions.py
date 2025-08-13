import cv2
import os

image_path = os.path.join("..", "assets", "python_img.png")

if os.path.exists(image_path):
    image = cv2.imread(image_path)
    if image is not None:
        h, w, c = image.shape
        print(f"Success: Image Loaded! Size = {w}x{h}, Channels = {c}")
    else:
        print("Error: Image found but could not be read!")
else:
    print("Error: File not found at", image_path)

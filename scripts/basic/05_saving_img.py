import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "..","..","assets", "python_img.png")
output_path = os.path.join(script_dir, "..","..","assets", "edit_able_img.png")

if not os.path.exists(input_path):
    print(f"Error: File not found at '{input_path}'")
else:
    image = cv2.imread(input_path)

    if image is None:
        print("Error: Image found but could not be read!")
    else:
        success = cv2.imwrite(output_path, image)
        if success:
            print(f"Success: Image saved at '{output_path}'")
        else:
            print("Error: Failed to save the image.")

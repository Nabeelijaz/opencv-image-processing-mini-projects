import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "..", "..", "assets", "python_img.png")
image_path = os.path.abspath(image_path)

if not os.path.exists(image_path):
    print(f"Error: File not found at '{image_path}'")
    exit()

image = cv2.imread(image_path)
if image is None:
    print("Error: Could not read the image!")
    exit()

print("Original size:", image.shape[:2])  # height, width

# Resize image
width = int(input("Enter new width: "))
height = int(input("Enter new height: "))
resized_image = cv2.resize(image, (width, height))

# Show resized image
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ask to save
save_choice = input("Save resized image? (y/n): ").strip().lower()
if save_choice == "y":
    save_name = input("Enter file name (with extension .png/.jpg): ").strip()
    save_path = os.path.join(script_dir, "..", "..", "assets", save_name)
    success = cv2.imwrite(save_path, resized_image)
    if success:
        print(f"Resized image saved successfully at '{save_path}'")
    else:
        print("Error: Could not save image!")
else:
    print("Skipped saving resized image.")

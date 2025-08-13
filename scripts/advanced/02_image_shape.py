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

height, width, channels = image.shape
print(f"Original Image shape: {width}x{height}, Channels: {channels}")

# --- Rotate image ---
angle = float(input("Enter rotation angle (in degrees, clockwise): "))
center = (width // 2, height // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (width, height))
print(f"Image rotated by {angle} degrees.")

cv2.imshow("Original Image", image)
cv2.imshow("Rotated + Circle", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

save_choice = input("Save the modified image? (y/n): ").strip().lower()
if save_choice == "y":
    save_name = input("Enter file name (with .png/.jpg): ").strip()
    save_path = os.path.join(script_dir, "..", "..", "assets", save_name)
    success = cv2.imwrite(save_path, rotated)
    if success:
        print(f"Modified image saved successfully at '{save_path}'")
    else:
        print("Error: Could not save image!")
else:
    print("Skipped saving modified image.")

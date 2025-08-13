import cv2
import os

# Step 1: User se image path lena
image_path = input("Enter image path: ").strip()

# Check file exists
if not os.path.exists(image_path):
    print(f"Error: File not found at '{image_path}'")
    exit()

# Image load karo
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not read the image!")
    exit()

print("Step 1: Image loaded successfully!")

# Step 2: Grayscale conversion
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Step 2: Image converted to grayscale!")

# Step 3: Ask user to show image
show_choice = input("Do you want to show the image? (y/n): ").strip().lower()
if show_choice == 'y':
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Step 3: Image displayed!")
else:
    print("Step 3: Skipped image display.")

# Step 4: Ask user to save image
save_choice = input("Do you want to save the grayscale image? (y/n): ").strip().lower()
if save_choice == 'y':
    save_name = input("Enter file name to save (with .png or .jpg): ").strip()
    save_path = os.path.join(os.path.dirname(image_path), save_name)
    
    success = cv2.imwrite(save_path, gray_image)
    if success:
        print(f"Step 4: Image saved successfully as '{save_path}'")
    else:
        print("Error: Image could not be saved!")
else:
    print("Step 4: Skipped saving image.")

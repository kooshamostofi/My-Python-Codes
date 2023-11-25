#!/usr/bin/env python3

from PIL import Image
import os

image_folder = "images/"
output_folder = "/opt/icons/"

files = os.listdir(image_folder)
for file in files:
    # Construct the full path to the image file
    file_path = os.path.join(image_folder, file)

    try:
        # Try to open the image
        im = Image.open(file_path)

        # Rotate the image 90° clockwise
        rotated_image = im.rotate(-90)

        # Resize the image from 192x192 to 128x128
        resized_image = rotated_image.resize((128, 128))

        # Convert the image to 'RGB' mode
        rgb_resized_image = resized_image.convert('RGB')

        # Print the size of the original image
        print(f"{file} (Original): {im.size}")

        # Save the rotated, resized, and converted image to /opt/icons/ in JPEG format
        output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".jpeg")
        rgb_resized_image.save(output_path, "JPEG")

        # Print the size of the new image
        print(f"{file} (New): {rgb_resized_image.size}")
        print(f"Rotated, resized, and saved as {output_path}")

    except (OSError, Image.UnidentifiedImageError):
        # Skip files that are not valid images
        print(f"Skipping non-image file: {file}")

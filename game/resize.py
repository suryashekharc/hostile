from PIL import Image
import os

# Set the input and output directories
input_dir = "/Applications/hostiledesign/game/images_pre"
output_dir = "/Applications/hostiledesign/game/images"

# Set the desired output dimensions
output_size = (1920, 1080)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a JPEG
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # Open the image and resize it
        with Image.open(os.path.join(input_dir, filename)) as img:
            img = img.resize(output_size)
            # Save the resized image with a suffix
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            img.save(os.path.join(output_dir, output_filename), "JPEG")

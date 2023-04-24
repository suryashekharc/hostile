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
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".webp"):
        # # Open the image and resize it
        # with Image.open(os.path.join(input_dir, filename)) as img:
        #     img = img.resize(output_size)
        #     # Save the resized image with a suffix
        #     output_filename = os.path.splitext(filename)[0] + ".jpg"
        #     img.save(os.path.join(output_dir, output_filename), "JPEG")
        with Image.open(os.path.join(input_dir, filename)) as img:
            # Get the current size of the image
            width, height = img.size
            print("old", img.size)
            new_width, new_height = output_size
            # Calculate the aspect ratio
            aspect_ratio = width / height

            # Calculate the new aspect ratio
            new_aspect_ratio = new_width / new_height

            if aspect_ratio > new_aspect_ratio:
                # The current aspect ratio is wider than the new one, so crop the sides
                new_height = int(new_width / aspect_ratio)
            # else:
            #     # The current aspect ratio is taller than the new one, so crop the top and bottom
            #     new_width = int(new_height * aspect_ratio)

            # Resize the image
            resized_img = img.resize((new_width, new_height))

            # Save the resized image
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            print("new", resized_img.size)
            resized_img.save(os.path.join(output_dir, output_filename), "JPEG")

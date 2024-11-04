#!/usr/bin/env python3

from PIL import Image

def extract_lsb(image_path, output_path):
    image = Image.open(image_path)
    image = image.convert("RGB") 
    pixels = image.load()

    width, height = image.size
    new_image = Image.new("RGB", (width, height))
    new_pixels = new_image.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            
            r_lsb = r & 0b00000001
            g_lsb = g & 0b00000001
            b_lsb = b & 0b00000001
            
            # Set new pixel values for the new image, only keeping the LSB
            new_pixels[x, y] = (r_lsb * 255, g_lsb * 255, b_lsb * 255)  # scale to 255 for visibility

    new_image.save(output_path)
    print(f"LSB image saved as {output_path}")

extract_lsb("secret_image.png", "extracted_lsb_image.png")

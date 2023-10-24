from PIL import Image

# Load the image
image = Image.open("shape.png")
threshold = 100  # Adjust this threshold value as needed

# Iterate through the pixels and apply the filter
for x in range(image.width):
    for y in range(image.height):
        r, g, b, a = image.getpixel((x, y))
        if (r,g,b,a) != (255,255,255,255):
            print((r,g,b,a))
        if r < threshold:
            image.putpixel((x, y), (0, g, b))

# Save the modified image
#image.save("output_image.jpg")

from PIL import Image

image = Image.open("monro.jpg")
print(image.mode)
red,green,blue = image.split()
print(red)
red.save("Red.jpg")
print(green)
green.save("Green.jpg")
print(blue)
blue.save("Blue.jpg")

merge_image = Image.merge("RGB",(red,green,blue))
merge_image.save("monro 2.jpg")

image = Image.open("Red.jpg")
image = image.crop((86, 0, image.width, image.height))
image.save("Red 1.jpg")
image = Image.open("Red.jpg")
image = image.crop((43, 0, image.width-43, image.height))
image.save("Red 1.jpg")

image1 = Image.open("Red 1.jpg")
image2 = Image.open("Red 2.jpg")
image3 = Image.blend(image1, image2,0.65)
image3.save("Red 3.jpg")

image = Image.open("Blue.jpg")
image = image.crop((0, 0, image.width-86, image.height))
image.save("Blue 2.jpg")

image1 = Image.open("Red 3.jpg")
image2 = Image.open("Blue 2.jpg")
image3 = Image.blend(image1, image2,0.65)
image3.save("Blue 3.jpg")

image = Image.open("Green.jpg")
image = image.crop((43, 0, image.width-43, image.height))
image.save("Green 2.jpg")

red = Image.open("Red 3.jpg")
green = Image.open("Green 2.jpg")
blue = Image.open("Blue 3.jpg")
merge_image = Image.merge("RGB",(red,green,blue))
merge_image.save("monro 3.jpg")

image = Image.open("monro 3.jpg")
image.thumbnail((80,80))
print(image.size)
image.save("monro_thumbnail.jpg")
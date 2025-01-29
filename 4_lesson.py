from PIL import Image

image = Image.open("monro.jpg")
red,green,blue = image.split()

red_1 = red.crop((86, 0, red.width, red.height))
red_2 = red.crop((43, 0, red.width - 43, red.height))
red_blended = Image.blend(red_1, red_2, 0.65)

blue_1 = blue.crop((0, 0, blue.width - 86, blue.height))
blue_2 = blue.crop((43, 0, blue.width - 43, blue.height))
blue_blended = Image.blend(blue_1, blue_2, 0.65)

green_cropped = green.crop((43, 0, green.width - 43, green.height))

merge_image = Image.merge("RGB", (red_blended, green_cropped, blue_blended))

merge_image.thumbnail((80, 80))
merge_image.save("monro_thumbnail.jpg")

from captcha.image import ImageCaptcha
from PIL import Image, ImageDraw,ImageChops
import os, sys
from random import SystemRandom
val1="uploads/"+sys.argv[1]
val2=sys.argv[2]+"_B.png"
background = Image.open(val1)
overlay = Image.open(val2)

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
combined_image="combined.png"


new_img.save(combined_image,"PNG")
im1 = Image.open("combined.png")
val3 =sys.argv[2]+"_combined.png"
im2 = Image.open(val3)

if not ImageChops.difference(im2, im1).getbbox():
	print "key is correct"
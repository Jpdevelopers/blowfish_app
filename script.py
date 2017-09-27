from captcha.image import ImageCaptcha
from PIL import Image, ImageDraw
import os, sys
from random import SystemRandom

image = ImageCaptcha(fonts=['abcd.ttf'])
data = image.generate(sys.argv[1])
image.write(sys.argv[1], 'out.png')
image_file = Image.open("out.png") # open colour image
image_file = image_file.convert('1') # convert image to black and white
save_path = sys.argv[2]+".png"
image_file.save(save_path)

random = SystemRandom()



infile=save_path

if not os.path.isfile(infile):
	print "That file does not exist."
	exit()

img = Image.open(infile)

f, e = os.path.splitext(infile)
out_filename_A=f+"_A.png"
out_filename_B=f+"_B.png"

img=img.convert('1')#convert image to 1 bit

#Prepare two empty slider images for drawing
width=img.size[0]*2
height=img.size[1]*2
out_image_A = Image.new('1', (width, height))
out_image_B = Image.new('1', (width, height))
draw_A = ImageDraw.Draw(out_image_A)
draw_B = ImageDraw.Draw(out_image_B)
#using blowfish ans vcs together
# any number of patterns can be taken since we are using the random module
patterns=((1,1,0,0), (1,0,1,0), (1,0,0,1), (0,1,1,0), (0,1,0,1), (0,0,1,1))
#Cycle through pixels
for x in xrange(0, width/2):
	for y in xrange(0, height/2):
		pixel=img.getpixel((x,y))
		pat=random.choice(patterns)
		#A will always get the pattern
		draw_A.point((x*2, y*2), pat[0])
		draw_A.point((x*2+1, y*2), pat[1])
		draw_A.point((x*2, y*2+1), pat[2])
		draw_A.point((x*2+1, y*2+1), pat[3])
		if pixel==0:#Dark pixel so B gets the anti pattern
			draw_B.point((x*2, y*2), 1-pat[0])
			draw_B.point((x*2+1, y*2), 1-pat[1])
			draw_B.point((x*2, y*2+1), 1-pat[2])
			draw_B.point((x*2+1, y*2+1), 1-pat[3])
		else:
			draw_B.point((x*2, y*2), pat[0])
			draw_B.point((x*2+1, y*2), pat[1])
			draw_B.point((x*2, y*2+1), pat[2])
			draw_B.point((x*2+1, y*2+1), pat[3])

out_image_A.save(out_filename_A, 'PNG')
out_image_B.save(out_filename_B, 'PNG')
background = Image.open(out_filename_A)
overlay = Image.open(out_filename_B)

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
combined_image=sys.argv[2]+"_combined.png"
new_img.save(combined_image,"PNG")
print "Done."



import os
from os.path import isfile, join
import random
from PIL import Image, ImageDraw, ImageFont
#Opening Image & Creating New Text Layer
base_path = '.'
folder_ls = [f for f in os.listdir(base_path) if isfile(join(base_path, f))]
for file in folder_ls:
    if not file.__contains__(".py"):
        print(file)
        img = Image.open(file).convert("RGBA")
        txt = Image.new('RGBA', img.size, (255,255,255,0))

        #Creating Text
        text = "Umair Mukhtar"
        font = ImageFont.truetype("arial.ttf", 102)

        #Creating Draw Object
        d = ImageDraw.Draw(txt)

        #Positioning Text
        width, height = img.size 
        textwidth, textheight = d.textsize(text, font)
        x=width/2-textwidth/2
        y=height/2

        #Applying Text
        if height<1500:
            d.text((x,0), text, fill=(255,255,255, 125), font=font)
            d.text((x,y), text, fill=(255,255,255, 125), font=font)
            d.text((x,height-150), text, fill=(255,255,255, 125), font=font)
        else:
            font = ImageFont.truetype("arial.ttf", 152)
            d.text((x,0), text, fill=(255,255,255, 125), font=font)
            d.text((x,500), text, fill=(255,255,255, 125), font=font)
            d.text((x,1000), text, fill=(255,255,255, 125), font=font)
            d.text((x,1500), text, fill=(255,255,255, 125), font=font)
            d.text((x,2500), text, fill=(255,255,255, 125), font=font)
            d.text((x,3000), text, fill=(255,255,255, 125), font=font)
        #Combining Original Image with Text and Saving
        watermarked = Image.alpha_composite(img, txt)
        watermarked.save(file+'watermarked.png')
    


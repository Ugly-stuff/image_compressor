from PIL import Image
import os
#You can compress multiple images at same time, To reduce more size change mywidth value to 2000 or 1500
source_dir = r""    #Give manually the source path of images you want to compress.
destination_dir = r""  #Give manually the destination path for compressed images.

def resize_pic(old_pic, new_pic, mywidth):
    img = Image.open(old_pic)
    wpercent = mywidth / float(img.size[0])
    hsize = int(float(img.size[1]) * wpercent)
    img = img.resize((mywidth, hsize), Image.LANCZOS)  
    img.save(new_pic)

# Creating another function
def entire_directory(source_dir, dest_dir, width):
    files = os.listdir(source_dir)
    for file in files:
        old_pic = source_dir + "/" + file
        new_pic = dest_dir + "/" + file

        resize_pic(old_pic, new_pic, width)

mywidth = 2500 
entire_directory(source_dir, destination_dir, mywidth)

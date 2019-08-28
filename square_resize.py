# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:58:45 2019

@author: Francois
"""

from PIL import Image
import glob
import os
from tqdm import tqdm

def square_resize(category_name):
    cwd = os.getcwd()
    cat_path = cwd +'\\'+ category_name
    images = [f for f in glob.glob(cat_path +  "**/**/**/*.jpg", recursive=True)]
    for im_path in tqdm(images):
        subcat_path, im_name = os.path.split(im_path)
        subcat_name = os.path.basename(subcat_path)
       
        if not '500_' in subcat_path:
            im = Image.open(im_path)
            width, height = im.size
            if width > height:
                im = im.crop(((width-height)/2,0,(width+height)/2,height))
            elif width < height:
                im = im.crop((0,(height-width)/2,width,(height+width)/2))
            imResized = im.resize((500,500), Image.ANTIALIAS)
            
            new_category_path = os.path.join(cwd, '500_' + category_name)
            os.system("mkdir {}".format(new_category_path))

            new_subcat_path = os.path.join(new_category_path, "500_"+subcat_name)
            os.system("mkdir {}".format(new_subcat_path))
            imResized.save(os.path.join(new_subcat_path, "500_"+im_name), 'JPEG', quality = 90)

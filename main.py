## image disparity script
## jryzkns

import matplotlib.pyplot as plt, random,time ## testing
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np, copy

def char_to_pixels(text, path='FreeMono.ttf', fontsize=24):
        ''' Based on https://stackoverflow.com/a/27753869/190597 (jsheperd) '''
        font = ImageFont.truetype(path, fontsize) 
        w, h = font.getsize(text)
        h *= 2
        image = Image.new('L', (w, h), 1)  
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, font=font) 
        arr = np.asarray(image)
        arr = np.where(arr, 0, 1)
        arr = arr[(arr != 0).any(axis=1)]
        return arr

def shift(mesh_in,stim,steps):
        '''meshl = shift(meshr,stim,steps)'''
        mesh = copy.deepcopy(mesh_in)
        meshw,meshh = mesh.shape
        stimw,stimh = len(stim),len(stim[0])

        stimx,stimy = int((meshw - stimw)/2),int((meshh - stimh)/2)

        for i in range(len(stim)):
                for j in range(len(stim[0])):
                        if stim[i][j]:
                                mesh[stimx+i][stimy+j] = mesh[stimx+i][stimy+j+steps]
        return mesh

## TOP ##

random.seed(time.time()) ## seed rng

textmat = char_to_pixels("DOES THIS WORK?")

print(textmat)

meshr = np.random.randint(256,size=256*256).reshape(256,256)
meshl = shift(meshr,textmat,1)

plt.figure(1) #meshr
plt.title("right")
plt.imshow(meshr)
plt.figure(2) #meshl
plt.title("left")
plt.imshow(meshl)
plt.figure(3) #extra test
plt.title("extra")
plt.imshow(shift(meshr,textmat,20))

plt.show()
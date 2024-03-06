# Class09A Demos - Fast Voronoi!

from PIL import Image
import numpy as np
from collections import deque
import voronoi_fast as vs

## Steps to produce Voronoi Art
# TODO: 1. load a base image
im = Image.open("parkPhoto.jpg")
im.show()

# TODO: 2. set a density and choose the centers
density = 0.001
ctrs = vs.centers(im,density)

# TODO: 3a. prepare the output image
imOut = Image.new('RGB', (im.width,im.height), (255,255,255))

# TODO: 3b. iterate over pixels, setting the color of the output image
pix = imOut.load()

## OLD (slow) way! 
# for x in range(imOut.width):
#     for y in range(imOut.height):
#         pix[x,y] = ctrs.nearest_center_colour((x,y))

## New (fast) way using queues!
## #TODO Step 1: Create a "processed" numpy array to keep track of which pixels have already been processed

## #TODO Step 2: Create a new deck

## #TODO Step 3: Enqueue the centers, mark all the centers as "processed"

## #TODO Step 4: Iterate through all the points in the deck, find neighbours, enqueue if needed
    
# TODO: 4. save the output image
imOut.save('outputs/voronoiPark_fast.png')
imOut.show()

# TODO: 5. Add red dots in the centers

# Question: Can we make this more efficient?

for c in ctrs.ctrs:
    x,y = c.pt
    for i in [x-2,x-1,x,x+1,x+2]:
        for j in [y-2,y-1,y,y+1,y+2]:
            if i >= 0 and j >= 0 and i < imOut.width and j < imOut.height:
                pix[i,j] = (255,0,0)

# TODO: 5b. Save the new output image
imOut.save('outputs/vorPark02.jpg')
imOut.show()
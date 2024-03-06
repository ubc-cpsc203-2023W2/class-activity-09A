# Class09A Demos - Fast Voronoi!

from PIL import Image
import numpy as np
from collections import deque
import voronoi_fast as vs

## Steps to produce Voronoi Art
# TODONE: 1. load a base image
im = Image.open("parkPhoto.jpg")
im.show()

# TODONE: 2. set a density and choose the centers
density = 0.001
ctrs = vs.centers(im,density)

# TODONE: 3a. prepare the output image
imOut = Image.new('RGB', (im.width,im.height), (255,255,255))

# TODONE: 3b. iterate over pixels, setting the color of the output image
pix = imOut.load()

## OLD (slow) way! 
# for x in range(imOut.width):
#     for y in range(imOut.height):
#         pix[x,y] = ctrs.nearest_center_colour((x,y))


## New (fast) way using queues!
## #TODONE Step 1: Create a "processed" numpy array to keep track of which pixels have already been processed
processed = np.full((imOut.width, imOut.height), False) # use numpy to make a boolean array

## #TODONE Step 2: Create a new deck
deck = deque() # in python 3.12, queues were added! should refactor to use those (eventually)

## #TODONE Step 3: Enqueue the centers, mark all the centers as "processed"
for c in ctrs.ctrs:
    cx,cy = c.pt # give better names to the point of c.
    processed[cx,cy] = True # mark as processed
    pix[cx,cy] = c.color # put color in right place on new image
    deck.append(c) # enqueue center

## #TODONE Step 4: Iterate through all the points in the deck, find neighbours, enqueue if needed
while deck:  # while queue is not empty
    v = deck.popleft()  # dequeue a point

    for n in v.neighbours():
        if n.checksout(im, processed):
            nx, ny = n.pt  # give better names to the point of n.
            processed[nx, ny] = True  # mark as processed
            pix[nx, ny] = v.color  # put color in right place on new image
            deck.append(n)  # enqueue neighbour

    
# TODONE: 4. save the output image
imOut.save('outputs/voronoiPark_fast.png')
imOut.show()

# TODONE: 5. Add red dots in the centers

# Question: Can we make this more efficient?

for c in ctrs.ctrs:
    x,y = c.pt
    for i in [x-2,x-1,x,x+1,x+2]:
        for j in [y-2,y-1,y,y+1,y+2]:
            if i >= 0 and j >= 0 and i < imOut.width and j < imOut.height:
                pix[i,j] = (255,0,0)

# TODONE: 5b. Save the new output image
imOut.save('outputs/vorPark02.jpg')
imOut.show()

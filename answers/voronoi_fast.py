from PIL import Image
from dataclasses import dataclass, field
import random

from collections import deque
import numpy as np #easy way to do 2d arrays

@dataclass
class center:  ## we will be putting these on our deque
    pt: tuple[int,int]
    color: tuple[int, int, int]

    def checksout(self, img: Image, proc: np.ndarray) -> bool:
        px, py = self.pt
        w, h = img.width, img.height

        # want px to be in range (0 to w), py in range 0 to h, not processed
        t1 = px in range(w)
        t2 = py in range(h)
        if t1 and t2:
            t3 = not proc[px,py]
        else:
            t3 = False

        return t1 and t2 and t3
    
    def neighbours(self) -> list:
        vx, vy = self.pt
        colour = self.color
        # define neighbours
        up = center((vx, vy-1), colour)
        left = center((vx-1, vy), colour)
        down = center((vx, vy + 1), colour)
        right = center((vx+1, vy), colour)

        return [up, left, down, right]

@dataclass
class centers:

    ctrs: list[center] = field(default_factory=list) # only data of centers class

    def __init__(self,img:Image, density: float):
        pixels = img.load() # pixels loaded from image into a variable (table of points)
        self.ctrs = []
        num_pixels = density * img.width * img.height
        for c in range(int(num_pixels)):
            x = random.randint(0, img.width-1)
            y = random.randint(0, img.height-1)
            self.ctrs.append(center((x,y),pixels[x,y]))

    def dist(self,p1:tuple[int,int],p2:tuple[int,int])-> int:
        return ((p1[0]-p2[0])**2) + ((p1[1] - p2[1])**2)
    
    #### OLD DEPRECATED member function (for reference)
        # def nearest_center_color(self, pt:tuple[int,int])-> tuple[int,int,int]:
        #     # THIS code is just "findMin" using dist to center as a metric
        #     best_dist = self.dist(self.ctrs[0].pt,pt)
        #     best_center = self.ctrs[0]
        #     for c in self.ctrs:
        #         if (self.dist(c.pt,pt) < best_dist):
        #             best_dist = self.dist(c.pt,pt)
        #             best_center = c
        #     return best_center.color

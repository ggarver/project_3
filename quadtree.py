
from typing import List, Tuple, Optional
import numpy as np

class Quadtree:
    def __init__(self, img: np.ndarray, x: int, y: int, w: int, h: int,
                 min_size: int = 8, var_threshold: float = 500.0):
        self.img = img
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.mid = (x + w // 2, y + h // 2)
        self.min_size = min_size
        self.var_threshold = var_threshold
        self.children: Optional[List['Quadtree']] = None
        self.is_leaf = False

    def search(self, children, point):
        if self.is_leaf:
            if self.contains(point):
                return True
            return False
        else:
            for child in self.children:
                if child.search(children, point):
                    return print(f"Point found {point} in {child}")
            return False
        
    def get_leaves(self):
        # traverse to collect all leaf nodes
        if self.is_leaf:
            return [(self.x, self.y, self.w, self.h, self.get_average_color())]
        else:
            leaves = []
            for child in self.children:
                leaves.extend(child.get_leaves())
            return leaves

    def contains(self, point: Tuple[int, int]) -> bool:
        px, py = point
        return (self.x <= px < self.x + self.w) and (self.y <= py < self.y + self.h)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    

class Node:
    def __init__(self, x, y, w, h, capacity):
        self.x = x            # top-left corner x
        self.y = y            # top-left corner y
        self.w = w            # width
        self.h = h            # height
        self.capacity = capacity  # max points before subdividing
        self.points = []      # points stored in this node
        self.is_leaf = True   # starts as leaf
        self.children = []    # list of 4 children after subdivision

    def contains(self, point):
        # check if a Point object is inside this node
        return self.x <= point.x < self.x + self.w and self.y <= point.y < self.y + self.h

    def subdivide(self):
        # Split into 4 quadrants
        half_w = self.w // 2
        half_h = self.h // 2

        self.children = [
            Node(self.x, self.y, half_w, half_h, self.capacity),              # top-left
            Node(self.x + half_w, self.y, half_w, half_h, self.capacity),    # top-right
            Node(self.x, self.y + half_h, half_w, half_h, self.capacity),    # bottom-left
            Node(self.x + half_w, self.y + half_h, half_w, half_h, self.capacity)  # bottom-right
        ]
        self.is_leaf = False

    def insert(self, point):
        if not self.contains(point):
            return False

        if self.is_leaf:
            if len(self.points) < self.capacity:
                self.points.append(point)
                return True
            else:
                self.subdivide()
                # Re-insert points into children
                for p in self.points:
                    for child in self.children:
                        if child.insert(p):
                            break
                self.points = []  # clear points from parent
                # Now insert the new point
                for child in self.children:
                    if child.insert(point):
                        return True
        else:
            for child in self.children:
                if child.insert(point):
                    return True
        return False


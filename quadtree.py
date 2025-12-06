
from typing import List, Tuple, Optional
import numpy as np
from tree import Quad, Point

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
    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        self.name = name

    def get_name(self):
        return self.name
    

class Node:
        # A node represents a rectangular region!
    def __init__(self, x, y, w, h, capacity):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.capacity = capacity
        # Nodes know their points - points dont know their nodes
        self.points = []
        self.is_leaf = True # Start with no children
        self.children = []
        self.capacity = capacity

    def contains(self, point: Point) -> bool:
        # check if point is in node region
        return (self.x <= point.x < self.x + self.w) and (self.y <= point.y < self.y + self.h)
    
    def subdivide(self):
        # calculate dimensions
        half_w = self.w // 2
        half_h = self.h // 2

        self.children = [Node(self.x, self.y, half_w, half_h),
                         Node(self.x + half_h, self.y, half_w, half_h),
                         Node(self.x, self.y + half_h, half_w, half_h),
                         Node(self.x + half_h, self.y + half_h, half_w, half_h)]
        
        self.is_leaf = False

    def insert(self, point):
        # first check if point is in node region
        if not self.contains(point):
            return False
        
        if self.is_leaf: 
            if len(self.points) < self.capacity:
                self.points.append(point)
            else:
                self.subdivide()
                for child in self.children:
                    # recursively put point in
                    if child.insert(point):
                        return True
                return False
            
    def delete(self, point):
        # check if point is in node
        if not self.contains(point):
            return False
        
        elif self.is_leaf:
            if point in self.points:
                self.points.remove(point)
                return True
            else:
                return False
        else:
            # self is not a leaf = has children
            for child in self.children:
                if child.delete(point):
                    return True
            return False

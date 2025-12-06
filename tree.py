

from matplotlib.patches import Rectangle


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


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

class Quad:
    def __init__(self, boundary, capacity):
        self.boundary = boundary  # boundary is a rectangle defined by (x, y, width, height)
        self.capacity = capacity  # maximum number of points per quadrant
        self.points = []          # points contained in this quadrant
        self.divided = False      # whether this quadrant has been divided into sub-quadrants

    # insert points
    def insert(self, node):
        if node is None:
            raise Exception("Node is does not exist")
        
        # check if node is in boundary of current quad
        if not self.boundary.contains(node.pos):
            raise Exception("Node is out of bounds")
        
        # check if there is space in the current quad
        if len(self.points) < self.capacity:
            self.points.append
        else:
            if not self.divided:
                self.subdivide()
            # try to insert into sub-quadrants
            for quadrant in [self.northeast, self.northwest, self.southeast, self.southwest]:
                try:
                    quadrant.insert(node)
                    return
                except Exception:
                    continue
            raise Exception("Failed to insert node into any quadrant")
        
    def subdivide(self):
        # Node gets subdivided into four quadrants
        x, y, w, h = self.boundary.x, self.boundary.y, self.boundary.width, self.boundary.height
        ne = Rectangle(x + w/2, y, w/2, h/2)
        nw = Rectangle(x, y, w/2, h/2) 
        se = Rectangle(x + w/2, y + h/2, w/2, h/2)
        sw = Rectangle(x, y + h/2, w/2, h/2)

        self.northeast = Quad(ne, self.capacity)
        self.northwest = Quad(nw, self.capacity)
        self.southeast = Quad(se, self.capacity)
        self.southwest = Quad(sw, self.capacity)

        self.divided = True

    def delete(self, node):
        if node in self.points:
            self.points.remove(node)
            return True
        if self.divided:
            for quadrant in [self.northeast, self.northwest, self.southeast, self.southwest]:
                if quadrant.delete(node):
                    return True
        return False

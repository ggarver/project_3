"""
QuadTree Art Generator (Regular Quadtree Version)

This application:
1. Loads an image
2. Inserts N random points into a spatial quadtree
3. Subdivides based on capacity until leaves form
4. Computes the average color of each leaf region
5. Draws the leaves as rectangles filled with their mean color
"""

import numpy as np
from PIL import Image, ImageDraw
import cv2
import argparse

from quadtree import Node, Point  # <-- quadtree structure


class QuadArt:
    def __init__(self, img_array, capacity, num_points):
        self.img = img_array
        self.H, self.W = img_array.shape[:2]
        self.root = Node(0, 0, self.W, self.H, capacity)
        self.num_points = num_points


    @staticmethod
    def load_image(path):
        img = cv2.imread(path)
        if img is None:
            raise FileNotFoundError(f"Image not found: {path}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

    def insert_random_points(self):
        """Populate the quadtree with random points."""
        for _ in range(self.num_points):
            x = np.random.randint(0, self.W)
            y = np.random.randint(0, self.H)
            self.root.insert(Point(x, y))

    def collect_leaves(self, node):
        """Return a list of leaf regions as rectangles."""
        if node.is_leaf:
            return [(node.x, node.y, node.w, node.h)]
        leaves = []
        for child in node.children:
            leaves.extend(self.collect_leaves(child))
        return leaves
    
    def average_color(self, x, y, w, h):
        """Compute the average color of the image region defined by (x, y, w, h)."""
        region = self.img[y:y+h, x:x+w]
        avg_color = tuple(np.mean(region.reshape(-1, 3), axis=0).astype(int))
        return avg_color


    def render(self):
        """Generate the quadtree art image."""
        leaves = self.collect_leaves(self.root)
        out = Image.new("RGB", (self.W, self.H))
        draw = ImageDraw.Draw(out)

        for (x, y, w, h) in leaves:
            color = self.average_color(x, y, w, h)
            draw.rectangle([x, y, x+w, y+h], fill=color)

        return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="apple.jpg")
    parser.add_argument("--output", default="quad_art.png")
    parser.add_argument("--capacity", type=int, default=4,
                        help="max points per node before subdividing")
    parser.add_argument("--points", type=int, default=800,
                        help="number of random points to insert")

    args = parser.parse_args()

    img = QuadArt.load_image(args.input)
    art = QuadArt(img, capacity=args.capacity, num_points=args.points)

    print("Inserting points...")
    art.insert_random_points()

    print("Rendering...")
    out = art.render()
    out.save(args.output)

    print(f"Saved quadtree art to {args.output}")


if __name__ == "__main__":
    main()
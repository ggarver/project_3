
"""
Quadtree Art Generator (OOP, beginner-friendly)

Usage:
    python quadtree_art.py --input apple.jpg --output art.png --min-size 8 --var 800

This script reads an image, builds a quadtree based on color variance,
then paints each leaf tile with its average color to produce a stylized image.
"""
from quadtree import Point, Quadtree
import cv2





def main():
    img = cv2.imread("apple.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=500, qualityLevel=0.01, minDistance=5)

    qt = Quadtree(img, 0, 0, img.shape[1], img.shape[0])
    for (x,y) in corners:
        qt.insert(Point(x, y))


if __name__ == "__main__":
    main()
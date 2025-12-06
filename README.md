Random Image Segmentation (Quadtree Art)
Overview

This project implements a quadtree to segment an image based on randomly sampled points. The program inserts a user-chosen number of random points into the image, divides the space into quadtree nodes, and colors each node using the average color of the pixels it contains.

This can be used as a visual demonstration of:

How quadtrees partition 2D space

How randomized subdivisions affect image structure

Differences between quadtrees and traditional binary trees

Team Members

Just me — Grace Garver

Installation & Setup
Dependencies

Install prerequisites (virtual environment recommended):

pip install numpy opencv-python pillow

How to Run

From the project folder:

python application.py --input apple.jpg --output quad_art.png --capacity 4


When prompted:

How many randomized points would you like to insert?:


Enter a number up to 60,000.
More points → more subdivisions → more detail (but slower).

The generated image will be saved as:

quad_art.png

Screenshots / Demos

(Add screenshots here)

How the Quadtree Works

The image is treated as a 2D array of pixels.

The user chooses how many random points to insert.

Each quadtree node can hold up to capacity points.

When a node exceeds capacity, it subdivides into four children.

Each final leaf node is rendered using the average color of its region.

Complexity

Insertion:

Best/average: O(log n)

Worst (highly unbalanced): O(n)

Space:

Up to O(n) nodes in the worst case

Typically closer to O(n log n) with random distribution

Evolution of the Interface

Originally, I planned to use Harris Corners to guide subdivision.
Due to scope and time constraints, I scaled back to a randomized approach so I could deeply understand quadtree behavior and ensure a working implementation. This taught me the value of simplifying ambitious ideas into something achievable and educational.

Challenges & Solutions

Integrating VS Code with my terminal took time, but once configured, it sped up development.
A major challenge was getting the output image to change with the number of points — it initially produced a static result. Careful debugging and tracing through the subdivision logic eventually resolved this issue.

Future Enhancements

Integrating Harris Corners or other feature detectors

Adaptive subdivision based on image variance

Interactive visualization tools

Performance optimizations
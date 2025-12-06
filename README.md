Here you go — the whole thing cleanly formatted in Markdown:

# Random Image Segmentation (Quadtree Art)

## Overview
This project implements a **quadtree** to segment an image based on randomly sampled points.  
The program inserts a user-chosen number of random points into the image, divides the space into quadtree nodes, and colors each node using the **average color of the pixels** it contains.

This project visually demonstrates:

- How quadtrees partition 2D space  
- How randomized subdivisions affect image structure  
- Differences between quadtrees and traditional binary trees  

---

## Team Members
**Just me — Grace Garver**

---

## Installation & Setup

### Dependencies
Install prerequisites (virtual environment recommended):

```bash
pip install numpy opencv-python pillow

How to Run

From the project folder:

python application.py --input apple.jpg --output quad_art.png --capacity 4


When prompted:

"How many randomized points would you like to insert?"

Enter a number up to 60,000.
More points → more subdivisions → more detail (but slower).

The generated image will be saved as:

quad_art.png
```

# Screenshots / Demos

## 60 random points
<img width="537" height="539" alt="Screenshot 2025-12-05 234230" src="https://github.com/user-attachments/assets/ead6bd3c-3a73-422c-97f7-537b0c09d260" />

# 1000 random points
<img width="539" height="535" alt="Screenshot 2025-12-05 234259" src="https://github.com/user-attachments/assets/0236eef8-6bfc-4835-9dd0-d69c298515c2" />

# 50000 random points
<img width="531" height="537" alt="image" src="https://github.com/user-attachments/assets/d5859fe5-c09a-403d-bd7d-213fcf73de41" />



# How the Quadtree Works

- The image is treated as a 2D array of pixels.
- The user chooses how many random points to insert.
- Each quadtree node can hold up to capacity points.
- When a node exceeds capacity, it subdivides into four children.
- Each final leaf node is rendered using the average color of its region.

# Evolution of the Interface

Originally, I planned to use Harris Corners to guide subdivision. Due to scope and time constraints, I scaled back to a randomized approach so I could deeply understand quadtree behavior and ensure a working implementation. I learned that sometimes it is helpful to simplify my grander ideas to more manageable ones when on a time crunch.

# Challenges & Solutions
Integrating VS Code with my terminal took time — once configured, it sped up development.
A major challenge was getting the output image to actually change with the number of points; early versions produced a static result. Careful debugging and stepping through the subdivision logic fixed this.

# Future Enhancements
- Integrating Harris Corners or other feature detectors
- Adaptive subdivision based on image variance
- Interactive visualization tools
- Performance optimizations


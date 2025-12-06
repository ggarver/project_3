"""
application.py
---------------
Command-line entry point for the QuadTree Art Generator.

This file simply:
1. Parses command-line arguments
2. Loads the image
3. Builds the quadtree using QuadArt
4. Saves the resulting output image
"""

import argparse
from quadtree_art import QuadArt


def main():
    parser = argparse.ArgumentParser(description="Quadtree Art Generator (Regular Quadtree)")
    parser.add_argument("--input", default="apple.jpg",
                        help="Input image file")
    parser.add_argument("--output", default="quad_art.png",
                        help="Output image file")
    parser.add_argument("--capacity", type=int, default=4,
                        help="Max points per node before subdividing")
    parser.add_argument("--points", type=int, default=800,
                        help="Number of random points to insert for subdivision")

    args = parser.parse_args()

    # Load image
    img_array = QuadArt.load_image(args.input)

    # Initialize art generator
    art = QuadArt(img_array,
                  capacity=args.capacity,
                  num_points=args.points)

    print(f"Inserting {args.points} points...")
    art.insert_random_points()

    print("Rendering quadtree art...")
    out_img = art.render()

    # Save image
    out_img.save(args.output)
    print(f"Saved quadtree art to {args.output}")


if __name__ == "__main__":
    main()

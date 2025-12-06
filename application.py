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
    # parser.add_argument("--points", type=int, default=800,
    #                     help="Number of random points to insert for subdivision")

    args = parser.parse_args()

    # cap this at 60,000
    choice_points = int(input("How many randomized points would you like to insert?: "))
    if choice_points > 60000:
        choice_points = 60000

    # Load image
    img_array = QuadArt.load_image(args.input)

    # Initialize art generator
    art = QuadArt(img_array,
              capacity=args.capacity,
              num_points=choice_points)
    
    print(f"Inserting {choice_points} points...")
    art.insert_random_points()

    print("Rendering quadtree art...")
    out_img = art.render()

    # Save image
    out_img.save(args.output)
    print(f"Saved quadtree art to {args.output}")


if __name__ == "__main__":
    main()
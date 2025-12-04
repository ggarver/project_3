try:
    import cv2
    HAS_CV2 = True
except Exception:
    HAS_CV2 = False
    # Pillow can be used as a lightweight fallback for image display/opening
    from PIL import Image

from tree import Quad, Point

class QuadArt:
    def __init__(self, img):
        self.img = img
        self.root = Quad()

    def populate_quadtree(self, img):
        # root is the entire spatial image
        self.root = Quad()
        self.subdivide(self.root, img)

    def subdivide(self, quad, img):
        # Calculate color variance for this quadrant
        # If variance exceeds threshold, subdivide into 4 quadrants
        # Otherwise, mark as leaf node
        pass


    def color_diff(self):
        pass

    def recursive_draw(self, draw_func):
        # Draw points in the current quadrant
        for point in self.points:
            draw_func(point)

        # Recursively draw sub-quadrants if divided
        if self.divided:
            for quadrant in [self.northeast, self.northwest, self.southeast, self.southwest]:
                quadrant.recursive_draw(draw_func)


def main():
    img_path = 'C:\\Users\\grace\\OneDrive\\Desktop\\CS351\\Projects\\project_3\\apple.jpg'
    img1 = None
    if HAS_CV2:
        img1 = cv2.imread(img_path)
        if img1 is None:
            print('cv2 failed to read image at', img_path)
        else:
            try:
                cv2.imshow('Image', img1)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            except Exception as e:
                print('cv2 cannot display image in this environment:', e)
    else:
        # Fallback: try to open with Pillow and show (may use default image viewer)
        try:
            img1 = Image.open(img_path)
            try:
                img1.show()
            except Exception:
                print('Opened image with Pillow but cannot display in this environment.')
        except Exception as e:
            print('Pillow failed to open image at', img_path, ':', e)

    images = [img1]
    # test print
    print(images)

    # Try to generate a quadtree art image using the new module (optional)
    try:
        # import locally from project_3
        import sys, os
        proj_dir = os.path.join(os.getcwd(), 'Projects', 'project_3')
        if proj_dir not in sys.path:
            sys.path.insert(0, proj_dir)
        from quadtree_art import generate_from_image

        inp = os.path.join(proj_dir, 'apple.jpg')
        out = os.path.join(proj_dir, 'art_from_application.png')
        print('Generating quadtree art ->', out)
        generate_from_image(inp, out, min_size=8, var_threshold=800.0, outline=False)
        print('Generated art at', out)
    except Exception as e:
        print('Could not generate quadtree art:', e)


if __name__ == "__main__":
    main()
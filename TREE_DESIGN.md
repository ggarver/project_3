# Grace Garver

## Tree Selection - Which tree did you choose and why?
I chose the Quadtree because I am interested in the applications of it being used in Image compression and other computer vision based projects. 

## Use Cases - What problems does this tree solve well?
Quadtrees are great for representing spatial information in images, and are used for efficiently organizing and searching 2D spatial data.

## Properties - What makes this tree unique? What are its performance characteristics?
This tree is unique because it uses points within nodes to decide when to create a new leaf. The performance characteristics of this include very efficient time complexity due to the amount of recursion used. 

## Interface Design: Method signatures with descriptions
#### What operations does your tree support?
My quadtree supports searching for a point, adding a point, deleting a point, getting leaves, contains, and subdivide. 
### What are the parameters and return types?
Parameters include amount of points, image, image size, and more.
### What is the Big-O time complexity of each operation? (Required for every method)
Quadtree Search: O(n)
Quadtree get_leaves: O(n)
Quadtree contains: O(1)
Node contains: O(1)
Node subdivide: O(1)
Node insert: O(n)

## Implementation Notes: Key algorithms or techniques you'll use
I decided to use object oriented programming for this project because I feel like it is something that I need a bit more practice on. This technique was very good for finding small errors that would have been harder to find otherwise. 

# Splay Tree

A splay tree is a binary search tree with the additional property that recently accessed elements are quick to access again.<br>
Like self-balancing binary search trees, a splay tree performs basic operations such as insertion, look-up and removal.
All normal operations on a binary search tree are combined with one basic operation, called splaying. Splaying the tree for a certain element rearranges the tree so that the element is placed at the root of the tree.<br>
One way to do this with the basic search operation is to first perform a standard binary tree search for the element in question, and then use tree rotations in a specific fashion to bring the element to the top.
                <p align="center">![image](https://d18l82el6cdm1i.cloudfront.net/uploads/1IXcakC4O9-splay.gif)

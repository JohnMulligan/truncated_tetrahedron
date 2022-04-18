Illustration: http://www.johncmulligan.net/blog/2021/11/27/folding/

-------

By doing the following:

* Drawing a dodecagon
* Then connecting every third vertex

We produce:

* A "ring" that is a hexagon cut out of a dodecagon
* With 18 vertices
* And 12 intermediary line segments that "connect" the dodecagon to the hexagon (breaking the ring down into triangles and trapezoids)

If we then

* "Snip" on one of those connecting lines
* We have a sort of broken ring
* With an extra 2 vertices (20)

If we then start to fold

* The ring's triangular and trapezoidal components around those intermediary/connecting line segments
* At an angle of approximately 1.415471989998

Then the ring folds together

* Apparently in a perfect fit between certain vertices (I need to diagram this)
* And the 3D shape created by the folding of the 2D shape produces a sort of butterfly approximation of half a truncated tetrahedron

-------

In this folder, expanded.txt seems to balance to 0 for

* A dodecagon drawn from a circle with radius of r
* Using THT=1.415471989998
* Because Rx=Ox (again, I need a labeled diagram)

It was produced by having Python write literals for the rotations it performed to make the half-truncated-tetrahedron shape, then reducing it with string substitutions, then attempting to expand the equation in matlab.

But I have not been able to solve, in Matlab, or Python, or by hand, for Theta.


Longer but non-expanded formal expressions--which I'm more confident in because I didn't run them through a Matlab algorithm) can be found in the /tmp folder or, for the original equations that those were produced from, look to four.py (highly confident in this) and import Rx and Ox.
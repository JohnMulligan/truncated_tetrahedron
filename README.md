## Intro

This was put together from 3 separate repo's:

PyEngine3D for rendering the model (can probably use something better now): https://medium.com/quick-code/3d-graphics-using-the-python-standard-library-99914447760c

Sympy for the geometry, obviously: https://docs.sympy.org

A script by Bruce Vaughn for rotation about an arbitrary axis: https://www.eng.uc.edu/~beaucag/Classes/Properties/OptionalProjects/CoordinateTransformationCode/Rotate%20about%20an%20arbitrary%20axis%20(3%20dimensions).html

It's purpose built to:

* draw a dodecagon
* cut a small hexagon out of the dodecagon
* fold the dodecagon by the square root of 2 radians

This appears to construct two "near-miss" three dimensional forms out of the two regular polygons.

1. Very near intersections of points by virtue of the folding
1. Not-as-near: two of these objects almost fit into each other to form a truncated tetrahedron

To run:
	
	python3 m -venv venv
	source venv bin activate
	pip3 install -r requirements.txt
	python tetrahedron.py

It should print out the vertices and then render the model.

## Sept 20

It was a little off with my sqrt(2) folding angle, so I ran a multithreaded optimizer to try different folding angles.

No guarantee that there is a correct angle -- but the first run suggests there might be, around 1.415-ish radians. Running a second time.

See results in the optimization folder.

It's a very ugly optimization script that I ran but it's yielding good results. 1.415471962374 is very close to the "correct" angle, I think.

It's close enough, at least, that the folding of the second shape now worked well enough for me to polish off. The script generates the full form now, with the small gaps. Running a third optimization now on a very tight band of values.
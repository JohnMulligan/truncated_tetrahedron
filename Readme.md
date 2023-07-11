# Dihedral angles experiment

This is an ongoing project in identifying and rendering interesting symmetries of regular 2-D shapes in three dimensions.

Legacy commits in the history here contain the early attempts to produce these outputs by hard-coding different forms I had produced using physical models.

The "optimization" folder is designed to run as a high-throughput computing job capable of identifying these symmetries more or less autonomously. The "animations" folder renders these visually.

more recently, I refactored this rendering to use HTC methods as well.

## Background 
This project started in 2020, as an origami experiment of sorts. Working with a truncated tetrahedron, I found that cross-sections taken in parallel with its hexagonal faces up to the peak of the adjoining triangular facets could be "unfolded" into flat strips of alternating triangles and trapezoids. I used this to build physical models, in the form of spheres, by taking advantage of the fact that truncated tetrahedra *almost* tesselate in three dimensions, and that sheet metal and paper are flexible :)

I then started experimenting in the other direction, trying to fold flat shapes into regular, three-dimensional forms. I had seen something like this when I was trawling through Renaissance geometry -- a pattern in a notebook of a sprawling set of pentagons that could be cut out and folded into a dodecahedron. What I found was a little weirder than that, and I haven't been able to find anything quite like it.

I found, first empirically with paper models, then through computational optimization, that a dodecagon

* with a hexagon cut out of the middle such that
* the remaining ring was again an alternating series of triangles and trapezoids
* and that this ring could be folded
	* into three-dimensional shapes
	* along the ring's inner edges that the triangles & trapezoids shared
	* always at the same angle but in different directions
* these shapes were odd-looking
* but precisely aligned various vertices & faces of the two-dimensional ring
* and the angle at which it was to be folded looked a lot like the dihedral angle of a tetrahedron (was based on the arccos of the square root of 3)
	
So, in other words, I sort of lucked out. My manipulations of a 12-sided polygon was acting a lot like truncated tetrahedron's strips. However, all of the above took me a bit over a year of pecking away in my spare time.

The regularity of the solution led me to try out the same method on a decagon: cut out a pentagon, and see if folding along the resulting ring's inner edges, might align the form's vertices, edges, and faces in three dimensions. It did with a paper model, my computational model identified the optimal folding angle out to several decimal places, and the exact angle was listed on [this nice menu of dihedral angles for regular polyhedra](https://en.wikipedia.org/wiki/Table_of_polyhedron_dihedral_angles).

In May 2023 I decided to dust this project off and start testing this "method" on even-sided polygons.

## Current state

As of July 10, 2023

### Method

There are 2**(N-1) ways of folding any of these given rings.

I am using Networkx in Python to hold the state of the different vertices, their connections to one another, and their relative positions in the ring, because the folds must be performed in order.

#### 1. Sweeping the shapes

First, we find the optimal folding angles for an N-gon.

currently, this is broken into 2 steps-- a sweep using HTC and a serialized drilldown.

Each task gets an even slice of the 2(**N-2) different ways of folding the shape, and begins walking through these, folding it from -pi/2 to pi/2 degrees, and logging when nodes appear to be approaching one another.

The test for that is:

* set a threshold for "closeness"
	* relative to the shape's size
	* which is given by the radius of the circle we used to draw the N-gon
* at each step
	* evaluate all nodes' euclidean distances
	* catch all pairs that fall below the closeness threshold
* use that subset of close neighborings
	* and calculate a "closeness of close neighborings" average
	* along with which nodes are close neighbors in this configuration
* Those are all saved to json files in optimizer/outputs/N.json

The system is currently identifying good hits, from what I can see -- both in terms of the folding angles, which show up consistently in different foldings of the shape, and in the folding patterns, which look good when rendered visually.

#### 2. Animating the matches/hits

Running plot_hits flags local maxima, which are visually more interesting than their neighbors for reasons specific to this workflow.

Naming a particular shapenin the animations slurm script runs through all the flagged hits.
#### 3. Exporting

This requires the dihedral_flask app to be installed in parallel.

Processing.js files are written out to a static folder in that repo.
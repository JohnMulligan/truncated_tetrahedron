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



### Nov 11, 2023:

I've pulled everything from optimize down into the base folder and pushed the shared functions out to a folder named "common". And everything is cleaned up quite a bit, after our nots workshop.

Previously, I assumed that all good folding angles would have hits at the zero index on the fold iterator, which is just an N-long array of 1's (always folding right). However, this didn't yield anything interesting beyond 16-sided shapes.

It's worth noting, though, that this is creating exactly the blowout problem I'd been worried about. It's looking like a 20-sided shape will require 1.5M CPU hours???

I'm therefore going to:

#### First: Find a good resolution that should yield good folding angles (HTC)

this is ```find_approximate_folding_angles.py {{N}}```

visual analysis of outputs with ```graph_approximate_angles.py {{N}}```. Renders:

* heatmap
* 3d scatter
* unbinned 2d scatter
* binned 2d scatter

Seems to be yielding good results!

#### Then drill down on each of those approximated folding angles (MPI, I think)

this is ```targeted_driller``` -- which could be parallelized but doesn't really need it

it does need to be refactored, though, to use the new file naming conventions


#### Then find all the very good foldings on those improved folding angles

I've borrowed this back from my slurm workshop as ```find_folds_on_given_angles.py``` but it's untested

#### Then animate these very good foldings

Haven't touched any of this yet.






-------------------------


### As of June 10, 2023

#### Method

There are 2**(N-1) ways of folding any of these given rings.

I am using Networkx in Python to hold the state of the different vertices, their connections to one another, and their relative positions in the ring, because the folds must be performed in order.

##### 1. Sweeping the shapes

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

Current issues:

* My computational method is suboptimal
	* I'm using networkx, but have a lot of annoying/lazy scaffolding around it
	* And networkx necessitates some truly annoying workarounds
	* Perhaps this should be done in numpy instead, or alongside, for accuracy
* Refactor needed
	* There's a lot of duplicative code and poorly-used packages
* Accuracy & automation
	* I'm not *fully* there on autonomously
		* determining the optimal folding angles & patterns
		* ranking these 

##### 2. Animating the matches/hits

Running plot_hits flags local maxima, which are visually more interesting than their neighbors for reasons specific to this workflow.

Naming a particular shapenin the animations slurm script runs through all the flagged hits.
#### 3. Exporting

This requires the dihedral_flask app to be installed in parallel.

Where the underscore-joined numbers represent, in order:

* N
* The number of the folding pattern, indexed in the 2**(N-2) binary linspace
* Folded from zero to -1.314... radians
* In 10 steps
* Finally, a hash of a concatenated string of the nearest neighbor vertex labels

I'm hoping to be able to integrate this fairly well, with all those indices, into a Flask app for exploratory visual analysis.

##### 3. Missing middle steps

What I need now is to have the system act a little more intelligently.

* When an angle keeps showing up as a good match on a given N-gon
	* The system should attempt to
		* Optimize on that angle
		* for a single given folding pattern with a lot of hits
	* Or I just need a good kickoff script to handle this semi-manually
	* I need some visualization of the optimal angles across n-gons
* Once those angles are locked in to 5-ish decimal places
	* I need another sweep workflow
	* Where I begin to walk across all folding patterns
	* And come up with a way of ranking "good" matches
	* So I can have a principle for deciding what to animate (because it's expensive)

But what does that last one look like? Some combination of the number of close neighbors and the closeness of those neighbors, I'd think. Except that I don't want to rule out, especially in larger shapes, the possibility of very long unspoolings that connect in only a few places but in interesting ways.

What, then, is interesting??
=======
Processing.js files are written out to a static folder in that repo.
>>>>>>> a7ec8a01c8ee721c8fb9237d7df662173ce29710

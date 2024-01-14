# Dihedral angles experiment

This is an ongoing project in identifying and rendering interesting symmetries of regular 2-D shapes in three dimensions.

Legacy commits in the history here contain the early attempts to produce these outputs by hard-coding different forms I had produced using physical models.

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

## Nov 2023 update

I've pulled everything from optimize down into the base folder and pushed the shared functions out to a folder named "common". And everything is cleaned up quite a bit, after our nots workshop.

The job was, at this point, refactored to run as an HTC job on a slurm job scheduler.

## CONDOR SUBMIT (Dec 2023 update)

This has now been refactored to run as an HTC job on a condor job scheduler.

* Linear scaling
* Checkpointing
* Hand-rolled job array workload balancing

### Submission

Submit like ```condor_submit N=12 Procs=800 find_approximate_folding_angles_condor.submit```

* The submit file is ```find_approximate_folding_angles_condor.submit```
* Executable file is ```find_approximate_folding_angles.sh```
	* Hard-coded 5-hour walltime
	* 85 exit code resubmit
* Script file is ```find_approximate_folding_angles.py```
	* checkpoint files per proc are all ```checkpoint_$(N)_$(Procs)_$(Process).txt```
	* output files per proc are ```approximate_angles_worker_$(N)_$(Procs)_$(Process).txt```
	* output files on complete remapped to ```outputs/$(N)/approximate_angles_worker_$(Process).txt```

### Post-processing

Post-process with a simple:

1. Concatenation: ```cat outputs/{N}/approximate_angles_worker_*.txt > outputs/{N}/approximate_angles.txt```
	1. This sets up the full list of approximate angles that feeds the next step
1. Reduction to local minima: ```python3 isolate_local_minima_from_approx_angles.py {N}```
	1. This sets up the consolidated list, ```approximate_angles_consolidated.txt```
1. Then optimize the consolidated angles: ```python3 targeted_driller.py {N}```
	1. This picks, for each good angle, one of the corresponding folding patterns
	1. It then sweeps an ever-tightening window of angles, increasing its accuracy by one decimal point at each step
	1. The output file is ```outputs/{N}/angles_improved.txt```, whose columns are:
		1. improved angle
		1. original angle
		1. the np_id of the folding pattern this was tested on
		1. the min distance of that optimized folding
	1. This should be parallelized to the number of angles that need optimization (TBD)

Then do some manual checks/cleanups. Your angles_improved file will have 2 kinds of outlier:

1. Angles that are extremely close to one another = duplicates
	1. As in, identical out to 8 places
	1. The angle with the best optimized distance should be taken as canonical
	1. I've decided to merge these in the visualizations
1. Improved angles whose distances are not close enough = near misses
	1. As in, several orders of magnitude larger than the other distances
	1. They should be removed from the file so they're not visualized

### Subsequent full sweep

I appear to be losing some hits -- For instance, N=12,np_id=1984 is dropped in most runs?

Two options here -- figure out why that data is being dropped, or do a subsequent re-run of every folding pattern on the optimized angles. I think the latter is preferable, because we are getting many good results already, and there's nothing unreasonable about focusing way in on the small set of angles, now optimized, which are likely then to produce better hits.











## Notes on the code

See longer, unrevised notes further down in this doc for a basic explanation on the method. Here, I'm describing some of the work that had to be done to properly parallelize the experiment.

* Had to write my own version of numpy's array_split
	* That was not acting like a true iterator but instead creating a huge matrix
	* The job now appears to stay under 200MB memory for even large N's.
* The number of possible states to test is: 
	* ```(2**(N-1))*(Number of angles sampled)```
	* For now, I'm sampling 1000 angles from 0 to pi.
* As N grows, each step also takes more time to test. Could be sped up by:
	* Using quaternions (and a GPU?)
	* Using matrices instead of NetworkX
* But, again, at least I've solved the memory blowout
* There are some visualization scripts that I no longer use, e.g. ```graph_approximate_angles.py```:
	* heatmap
	* 3d scatter
	* unbinned 2d scatter
	* binned 2d scatter

## Exploratory data visualization

I need to refactor my visualization code. This should all be done in a single visualization package, rather than the mixture of processing.js and plotly I tried before.

I'll need to:

* further reduce the hits that need to be rendered:
	* on each folding angle, find the local maxima of hit counts by folding id
* preprocess the final xyz coords of each these maxima (folding id/angle address) in HTC
* make a two-paned app that allows a user to call up those renderings by clicking on the graphed local maxima (see the old app at http://johnconnor.pythonanywhere.com/)

![Sample image](/common/old_app.png)


-------------------------


### Previously (As of June 10, 2023)

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
	* and calculate a "closeness of close neighborings" min
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

What, then, is interesting?
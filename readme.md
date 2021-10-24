# truncated tetrahedra

This repo contains two (perhaps novel) constructions for truncated tetrahedra.

* "cross_sections"
	* this app builds a cross-section of a truncated tetrahedron, from a band of trapezoids.
* "dodecagon"
	* this app builds half of a truncated tetrahedron, from a cut up dodecagon

Both have the same structure and use the same packages:

## Installation

Use python virtual environments. I'm running python 3.6.8
	
	python3 m -venv venv
	source venv/bin/activate
	pip3 install -r requirements.txt

## Latest developments:

### Animation!

This is a good introduction. To see the dodecagon fold and unfold itself, run graph_auto.py

It is using the precalculated values in the "formal_expressions" subfolder.

### Formal expressions

We do now have formal expressions for the first five folds of the dodecagon. The first point of self-contact happens in fold five. 

The expression for Gx given in dodecagon/formal_expressions/five.py should be equivalent to zero. My current estimate of 1.415471989998 radians gives a value of 1.2246467991473532e-13 for that point.

That means it should be possible to solve for theta, formally. If someone manages that before me, I will happily give you half the credit if I publish on this :)

Same could be done with the "cross sections" fold angle, but I haven't had time to generate the formal equations.

## Interactive

Both apps contain an interactive script, "tetrahedron_interactive.py", which:

1. builds the 2D figure out of triangles
1. folds the 2D figure at particular joints, using a particular angle
1. renders the folded 3D construction in plotly (should open in your browser)

## Multiproc

But of course the question is, "what angle to fold at"?

To solve that, I have written two methods that make use of Python's multiprocessing package.

Both record the distances between two points that are supposed to coincide as a result of the folding.

It's necessary parallelize because each attempt can take up to a minute to run (on my laptop)

1. tetrahedron_multiproc_narrow.py
	1. Given a starting value, it slowly increases the precision of the estimate by trying values around this.
	1. It then uses the folding angle that resulted in the closest distance match, and uses this as the next step's starting point
	1. It's clever in principle, but there are some errors that creep in quickly
	1. It's very good as a first, quick step before you hand off to the other script:
1. tetrahedron_multiproc_range.py
	1. This one is ugly and a memory hog, but
	1. It tries every value in a given range

Note: You'll need to set an output path for your logs, in the env.py file

## Optimization/Graphing

I've also included some graphing functionality.

1. optimization/parser.py
	1. rolls up the ouput text files
	1. usage: `python parser.py path_to_output_files`
	1. its output is 'output.csv'
1. optimization/graph.py
	1. opens 'output.csv'
	1. renders a graph showing the values


## NFS storage

Notes on using NFS storage on an orion vm to write my multiproc results out to.

mount the rdf:

	yum install cifs-utils
	chmod u+s /bin/mount /bin/umount /usr/sbin/mount.cifs
	mkdir /mnt/rdf

ADD the below line LINE TO /etc/fstab:

	//smb.rdf.rice.edu/research/ /mnt/rdf cifs mfsymlinks,rw,vers=3.0,sign,noperm,domain=ADRICE,user,noauto 0 0

as our own netid user (not root), run the following and enter your password when prompted
	
	mount /mnt/rdf

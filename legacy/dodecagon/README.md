## Intro

Its purpose built to:

* draw a dodecagon
* cut a small hexagon out of the dodecagon to make a ring
* fold the dodecagon by the square root of 2 radians
* repeat, to make a truncated tetrahedron

One of these rings appears to be a perfect fit or else very near miss.

Building the second is not a perfect fit but it is still kind of close. There's not quite enough room left over from the first. This is visualizable, but the easy way to see it is to measure the space left for one of the small triangles against the actual size of the small triangle.


## Dependencies/credit

This was put together from 3 separate repo's:

Plotly for rendering the model 

Sympy for the geometry, obviously: https://docs.sympy.org

A script by Bruce Vaughn for rotation about an arbitrary axis: https://www.eng.uc.edu/~beaucag/Classes/Properties/OptionalProjects/CoordinateTransformationCode/Rotate%20about%20an%20arbitrary%20axis%20(3%20dimensions).html


## Sept 20 -- "tetrahedron multiproc"

It was a little off with my sqrt(2) folding angle, so I ran a multithreaded optimizer to try different folding angles.

No guarantee that there is a correct angle -- but the first run suggests there might be, around 1.415-ish radians. Running a second time.

See results in the optimization folder.

It's a very ugly optimization script that I ran but it's yielding good results. 1.415471962374 is very close to the "correct" angle, I think.

It's close enough, at least, that the folding of the second shape now worked well enough for me to polish off. The script generates the full form now, with the small gaps. Running a third optimization now on a very tight band of values.

## Sept 22 -- "tetrahedron multiproc precision"

I believe I have improved the optimization script. Rather than test every angle in a domain, I find the best match at a certain level of precision, then zoom in on that "address" and try its "subdomain" of 10 integer values at the next level of precision. I also check the n-1 value in case of rounding. So that should save about 80% of the work the computer was doing before.

This works, up to around 6 decimal places. It looks like it might be a very near miss? I am going to use the full sweep (non-optimized) multiprocessing script again, between radians: (1.415472073,1.415472075)

## March 22 -- formal expressions

The best approach to solving for theta is to use the equivalence of R and O at step 4, given in formal_expressions/four.py

## April 25 -- solution

```acos(2*sqrt(3)/3-1)``` radians

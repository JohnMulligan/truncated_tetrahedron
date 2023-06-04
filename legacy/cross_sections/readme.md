# Cross section construction

This uses a strip of alternating trapezoids to construct a cross section of a truncated tetrahedron.

The trapezoids are of two different sizes.

The shorter side on the longer trapezoid has the same length as the longer side on the shorter trapezoid.

Both trapezoids have interior angles of 60 and 120 degrees.

Appears to be working now. Refactored my multiproc scripts while applying them here.

On Oct. 5, the narrow band search ran out to somewhere around 11 decimal places before a memory failure.

best angle is -->  1.231  // with distance --> 19.8747772178808 in 81 seconds
best angle is -->  1.23096  // with distance --> 0.285357173970233 in 79 seconds
best angle is -->  1.2309594  // with distance --> 0.00872082395326979 in 79 seconds
best angle is -->  1.230959417  // with distance --> 0.000173537027473239 in 71 seconds
best angle is -->  1.23095941734  // with distance --> 1.62551053258285e-06 in 50 seconds
best angle is -->  1.2309594173409  // with distance --> 3.59284860756354e-07 in 50 seconds

Running on 8 cpu's, this comes out to about 1 cpu hour (54.6 cpu minutes).

Approximation visualization is in ../optimization/cross_sections/narrow_oct_5_6pm
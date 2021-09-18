from sympy.geometry import Point,Point3D, Line3D
from math import cos, sin, sqrt  
    
def rotate(axis,p0,theta):
	## PointRotate.py Version 1.02
	## Copyright (c) 2006 Bruce Vaughan, BV Detailing & Design, Inc.
	## All rights reserved.
	## NOT FOR SALE. The software is provided "as is" without any warranty.
	#############################################################################
	"""
		Return a point rotated about an arbitrary axis in 3D.
		Positive angles are counter-clockwise looking down the axis toward the origin.
		The coordinate system is assumed to be right-hand.
		Arguments: 'axis point 1', 'axis point 2', 'point to be rotated', 'angle of rotation (in radians)' >> 'new point'
		Revision History:
			Version 1.01 (11/11/06) - Revised function code
			Version 1.02 (11/16/06) - Rewrote PointRotate3D function

		Reference 'Rotate A Point About An Arbitrary Axis (3D)' - Paul Bourke        
	"""
	
	p1,p2=axis.points

	# Translate so axis is at origin    
	p = p0 - p1
	N = (p2-p1)
	Nm = sqrt(N.x**2 + N.y**2 + N.z**2)

	# Rotation axis unit vector
	n = Point(N.x/Nm, N.y/Nm, N.z/Nm)

	# Matrix common factors     
	c = cos(theta)
	t = (1 - cos(theta))
	s = sin(theta)
	X = n.x
	Y = n.y
	Z = n.z

	# Matrix 'M'
	d11 = t*X**2 + c
	d12 = t*X*Y - s*Z
	d13 = t*X*Z + s*Y
	d21 = t*X*Y + s*Z
	d22 = t*Y**2 + c
	d23 = t*Y*Z - s*X
	d31 = t*X*Z - s*Y
	d32 = t*Y*Z + s*X
	d33 = t*Z**2 + c

	#            |p.x|
	# Matrix 'M'*|p.y|
	#            |p.z|
	qx = d11*p.x + d12*p.y + d13*p.z
	qy = d21*p.x + d22*p.y + d23*p.z
	qz = d31*p.x + d32*p.y + d33*p.z

	q=Point(qx,qy,qz)
	# Translate axis and rotated point back to original location    
	endpoint=q+p1
	return endpoint
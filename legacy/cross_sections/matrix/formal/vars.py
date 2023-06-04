magical_angle="(asin(sqrt(3)/3)*2)"
ll="10000000"
r="3000000"

y_offset="(sin(math.pi/3)*" + r + ")"
x_offsets="(cos(math.pi/3)*" + r + ")"

ls="(" + ll +  "-cos(math.pi/3)*" + r + "*2)"
#ss="ls-cos(math.pi/3)*r*2"

ss="(" + ll + "-cos(math.pi/3)*" + r + "*2-cos(math.pi/3)*" + r + "*2)"
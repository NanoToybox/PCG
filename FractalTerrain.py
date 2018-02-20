# http://gameprogrammer.com/fractal.html#selfsim

from pyx import *
from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve
import math
from random import random

_canvas = canvas.canvas()

# midPoint Displacement in One Dimension
def midPointDisplacement(startPoint, endPoint, heightRatio):
	length = math.sqrt(math.pow(startPoint[0]-endPoint[0],2) + math.pow(startPoint[1]-endPoint[1],2))

	if (length < 11):
		_canvas.stroke(path.line(startPoint[0], startPoint[1], endPoint[0], endPoint[1]), [deco.filled([color.rgb.black])])
		return

	#calculate perpendicular midPoint
	x0 = endPoint[0] - startPoint[0] 
	y0 = endPoint[1] - startPoint[1]
	x1,y1 = symbols('x1,y1', real = True)

	system = [x0*x1+y0*y1, x1**2+y1**2-(length*heightRatio*(random()*0.4+0.8)**2)]
	
	result_set = nonlinsolve(system, [x1, y1])
	count = 0
	for r in result_set:
		if random() > 0.5 or count == 1 :
			midPoint_add = r
			midPoint = ( (startPoint[0]+endPoint[0])/2 + midPoint_add[0], (startPoint[1]+endPoint[1])/2 + midPoint_add[1])
		count += 1

	midPointDisplacement(startPoint, midPoint, heightRatio)
	midPointDisplacement(midPoint, endPoint, heightRatio)


midPointDisplacement((0,0), (50,0), heightRatio = 0.4)
_canvas.writePDFfile()

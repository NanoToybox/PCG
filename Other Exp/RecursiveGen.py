# http://natureofcode.com/book/chapter-8-fractals/

from pyx import *

_canvas = canvas.canvas()
INNER_RECT_RATIO = 0.4/2

# left_bottom corner is (0,0)
def drawFractal(p0, p1, p2, p3, useX = 1):
	length = min(abs(p0[0]-p1[0]),abs(p2[0]-p3[0])) if useX == 1 else min(abs(p0[1]-p2[1]),abs(p1[1]-p3[1]))
	#print("border ",p0,p1,p2,p3)
	#print(length)
	if (length < 1):
		return

	inner_rect = ((p0[0]+p1[0]+p2[0]+p3[0])/4-length*INNER_RECT_RATIO, 
                      (p0[1]+p1[1]+p2[1]+p3[1])/4-length*INNER_RECT_RATIO,
                      (p0[0]+p1[0]+p2[0]+p3[0])/4+length*INNER_RECT_RATIO,
                      (p0[1]+p1[1]+p2[1]+p3[1])/4+length*INNER_RECT_RATIO)
	inner_length = inner_rect[2] - inner_rect[0]
	#print("inner ", inner_rect)

	_canvas.stroke(path.rect(#(x, y, w, h)
		inner_rect[0],inner_rect[1],abs(inner_rect[2]-inner_rect[0]),abs(inner_rect[3]-inner_rect[1])
		), [style.linewidth.Thick])

	inner_lines = [
		(inner_rect[0],inner_rect[1],p0[0],p0[1]),
		(inner_rect[2],inner_rect[1],p1[0],p1[1]),
		(inner_rect[2],inner_rect[3],p3[0],p3[1]),
		(inner_rect[0],inner_rect[3],p2[0],p2[1])
	]
	
	#print(inner_lines)
	for index in range(len(inner_lines)):
		_canvas.stroke(
			path.line(
				inner_lines[index][0],
				inner_lines[index][1],
				inner_lines[index][2],
				inner_lines[index][3]),
			[style.linewidth.Thick]
			)
		next_i = index + 1 if index < 3 else 0
	#Am i fucking stupid? why wouldn't I just go up down left right?
	drawFractal((inner_rect[0],inner_rect[3]), (inner_rect[2],inner_rect[3]), p2, p3) #up
	drawFractal(p0, p1, (inner_rect[0],inner_rect[1]), (inner_rect[2],inner_rect[1])) #down
	drawFractal(p0, (inner_rect[0],inner_rect[1]), p2, (inner_rect[0],inner_rect[3]), 0) #left
	drawFractal((inner_rect[2],inner_rect[1]), p1, (inner_rect[2],inner_rect[3]), p3, 0) #right

drawFractal((0,0),(100,0),(0,100),(100,100))

_canvas.writePDFfile()

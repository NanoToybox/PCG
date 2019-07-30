import sys
sys.path.insert(0, 'D:\PCG\Helper')

import WaveLengthToRGB
import Representation
import Evaluation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy

class TestGound:
	generator = 0
	palette = []
	colors = []
	C = 0
	def __init__(self):
		geno = Representation.PlatesGeno()
		map_generator = Representation.Map()

		geno.plate_number = 5
		geno.default_height = (numpy.random.rand(geno.plate_number)*map_generator.size_y/2).astype(int)	
		geno.defualt_origin_center = numpy.random.rand(geno.plate_number,2) * map_generator.size_x
		geno.plate_direction = ((numpy.random.rand(geno.plate_number,2)-0.5)*2).astype(int)
		geno.crash_count = 1
		
		map_generator.create_mountains(geno)
		self.generator = map_generator

		#prepare colors from 380THz to 780THz
		for p in range(geno.plate_number):
			c = WaveLengthToRGB.waveLengthToRGB((740-420)/geno.plate_number*p+400)
			self.palette.append(c)

		self.colors = []
		for x in range(self.generator.size_x):
			for z in range(self.generator.size_z):
				self.colors.append(self.palette[self.generator.gen_map_plate[x][z]])
		self.colors = numpy.array(self.colors)
		
#run a test
test=TestGound()
X,Y,Z = test.generator.getXYZ()
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(X, Y, Z, color = test.colors/255.0) #wait... how am I plot surface with each "point" colored?

plt.show()


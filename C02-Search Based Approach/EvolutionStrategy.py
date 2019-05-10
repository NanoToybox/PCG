import Representation
import Evaluation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy

class TestGound:
	generator = 0
	def __init__(self):
		geno = Representation.PlatesGeno()
		geno.plate_number = 15
		geno.default_height = (numpy.random.rand(geno.plate_number)*5).astype(int)
		geno.defualt_origin_center = numpy.random.rand(geno.plate_number,2)*18
		geno.plate_direction = ((numpy.random.rand(geno.plate_number,2)-0.5)*2).astype(int)
		geno.crash_count = 1

		map_generator = Representation.Map()
		map_generator.create_mountains(geno)
		self.generator = map_generator
		
#run a test
X,Y,Z = TestGound().generator.getXYZ()
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z)
plt.show()

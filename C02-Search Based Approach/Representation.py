import math
import sys
import numpy

class Map:
	#地图示意图 链接: https://pan.baidu.com/s/1oathCnW8WFkCZsmwczIzYw 提取码: fhr5 
	#plate冲击的问题是，地球的地貌是经过长期plate冲击得来的，还要模拟plate本身变化，才能得到现在的地貌。

	#general bounds
	size_x = 32 	#depth
	size_z = 32  	#horizontal
	size_y = 8  	#vertical
	gen_map = []	#pheno map [x][z]
	gen_map_plate = []	#mark tile's plate number

	def __init__(self):
		self.gen_map = [[0 for z in range(self.size_z)] for x in range(self.size_x)]			
		self.gen_map_plate = [[-1 for z in range(self.size_z)] for x in range(self.size_x)]		


	###############################
	# generate pheno type 
	###############################
	def create_mountains(self, geno):
		c_geno = self.get_legitimate_geno(geno)
		self.init_plate(c_geno)
		#self.print()

		#itor-plates move
		for itor in range(c_geno.crash_count):
			self.move_plates(c_geno)
		#self.print()

	# get legitimate geno
	def get_legitimate_geno(self, geno):
		#diretion should be clamp to 1
		new_direction=[]
		for d in geno.plate_direction:
			new_d = (numpy.clip(d[0],0,1), numpy.clip(d[1],0,1))
			new_direction.append(new_d)
		geno.plate_direction = new_direction

		return geno

	# mark all tile to each plate, set tile default height
	def init_plate(self, geno):
		for x in range(self.size_x):
			for z in range(self.size_z):
				plate_number = self._calculate_belonging(x,z,geno)
				self.gen_map_plate[x][z] = plate_number
				self.gen_map[x][z] = geno.default_height[plate_number]

	def _calculate_belonging(self, x, z, geno):
		plate_number = -1
		min_dist = sys.maxsize
		# calculate closest plate center for each tile.
		for p in range(geno.plate_number):
			new_dist = math.sqrt((x - geno.defualt_origin_center[p][0])**2 + (z - geno.defualt_origin_center[p][1])**2)
			if(new_dist < min_dist):
				plate_number = p
				min_dist = new_dist
		return plate_number

	def move_plates(self, geno):
		#move tiles by plate_direction
		new_map = [[0 for z in range(self.size_z)] for x in range(self.size_x)]
		new_gen_map_plate = [[-1 for z in range(self.size_z)] for x in range(self.size_x)]		
		for x in range(self.size_x):
			for z in range(self.size_z):
				p = self.gen_map_plate[x][z]	#move p of map to new_map
				new_x = x + geno.plate_direction[p][0]
				new_z = z + geno.plate_direction[p][1]
				if(new_x in range(self.size_x) and
					new_z in range(self.size_z) and self.gen_map[x][z]> new_map[new_x][new_z]): #if clashed, use the higher one
					new_map[new_x][new_z] = self.gen_map[x][z]
					new_gen_map_plate[new_x][new_z] = p
		#mark changes
		for x in range(self.size_x):
			for z in range(self.size_z):
				if new_gen_map_plate[x][z] == -1:
					#solve abyss : sink
					new_map[x][z] = new_map[x][z] - 1
					#print("sink")
				elif (new_gen_map_plate[x][z] != self.gen_map_plate[x][z] and 
					new_gen_map_plate[x][z] != -1 
					and self.gen_map_plate[x][z] != -1):
					#solve conflict : arise
					new_map[x][z] = new_map[x][z] + 1
					#print("rise")
		self.gen_map=new_map
		self.gen_map_plate=new_gen_map_plate

	###############################
	# helpers
	###############################
	def print(self, printall = True):
		print("________________________map________________________")
		for x in range(self.size_x):
			print(self.gen_map[x])
		if(printall):
			print("________________________plate________________________")
			for x in range(self.size_x):
				print(self.gen_map_plate[x])
		print()

	def change_height(self, x,z,y):
		if(x in range(self.size_x) and y in range(self.size_y) and z in range(self.size_z)):
			self.gen_map[x,z]=y
		else:
			print("error! x,z,y out of range. " + x + " "+ z +" "+ y)	

	#format XYZ for matplotlib
	def getXYZ(self):
		X = numpy.array(range(self.size_x))
		Y = numpy.array(range(self.size_z))
		Z = numpy.array(self.gen_map)
		X, Y = numpy.meshgrid(X, Y)
		return X,Y,Z

class PlatesGeno:
	plate_number = 0 			#板块的数量
	default_height = []			#板块的高度
	plate_direction = []		#板块运动方向(x,z)
	defualt_origin_center = [] 	#(x,z) - 板块的重心，可能在x,z最大范围以外，不超过2x,2z范围
	crash_count = 0				#板块冲击的循环次数
	sea_level = 0				#≤海平面高度的位置是海洋

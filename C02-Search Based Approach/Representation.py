import math
import sys

class Map:
	#地图示意图 链接: https://pan.baidu.com/s/1oathCnW8WFkCZsmwczIzYw 提取码: fhr5 

	#general bounds
	size_x = 9 		#depth
	size_z = 9  	#horizontal
	size_y = 16  	#vertical
	gen_map = []
	gen_map_plate = []

	def __init__(self):
		self.gen_map = [[0 for z in range(self.size_z)] for x in range(self.size_x)]			#pheno map [x][z]
		self.gen_map_plate = [[0 for z in range(self.size_z)] for x in range(self.size_x)]		#mark tile's plate number


	###############################
	# generate pheno type 
	###############################
	def create_mountains(self, geno):
		self.init_plate(geno)
		#TODO : itor-plates crash
		#TODO : 

	# mark all tile to each plate
	# calculate closest plate center for each tile.
	def init_plate(self, geno):
		for x in range(self.size_x):
			for z in range(self.size_z):
				plate_number = -1
				min_dist = sys.maxsize
				for p in range(geno.plate_number):
					new_dist = math.sqrt((x - geno.defualt_origin_center[p][0])**2 + (z - geno.defualt_origin_center[p][1])**2)
					if(new_dist < min_dist):
						plate_number = p
						min_dist = new_dist
				self.gen_map_plate[x][z] = plate_number

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

	def change_height(self, x,z,y):
		if(x in range(self.size_x) and y in range(self.size_y) and z in range(self.size_z)):
			self.gen_map[x,z]=y
		else:
			print("error! x,z,y out of range. " + x + " "+ z +" "+ y)	

class PlatesGeno:
	plate_number = 0 			#板块的数量
	default_height = []			#板块的高度
	joint_point = (0,0)			#板块聚合的点
	defualt_origin_center = [] 	#(x,z) - 板块的重心，可能在x,z最大范围以外，不超过2x,2z范围
	crash_count = 0
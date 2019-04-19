class Map:
	#general bounds
	size_x = 9 		#depth
	size_z = 16  	#horizontal
	size_y = 9  	#vertical
	#链接: https://pan.baidu.com/s/1oathCnW8WFkCZsmwczIzYw 提取码: fhr5 
	gen_map = [[0 for z in range(size_z)] for x in range(size_x)]
	gen_map_plate = [[0 for z in range(size_z)] for x in range(size_x)]

	def create_mountains(geno):
		for z in range(size_z):
			for x in range(size_x):
				gen_map_plate[x][z] = decide_belonging(x,z,geno)


	def change_height(x,z,y):
		if(x in range(size_x) and y in range(size_y) and z in range(size_z))
			block[x,z]=y
		else
			print("error! x,z,y out of range. " + x + " "+ z +" "+ y)

	def decide_belonging(x,z,geno):
		for p in range(geno.plate_number):
			#TODO：计算x,z与p的重心的距离



class PlatesGeno:
	plate_number = 0 			#板块的数量
	default_height = []			#板块的高度
	joint_point = (0,0)			#板块聚合的点
	defualt_origin_center = [] 	#板块的重心，可能在9x9以外，不超过18x18;

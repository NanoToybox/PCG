import Representation
import Evaluation

class TestGound:

	def __init__(self):
		geno = Representation.PlatesGeno()
		geno.plate_number = 3
		geno.default_height = [1,5,10]
		geno.joint_point = (4,4)
		geno.defualt_origin_center = [(1,1),(8,3),(4,12)]
		
		gen_map = Representation.Map()
		gen_map.create_mountains(geno)
		gen_map.print()


#run a test
TestGound()
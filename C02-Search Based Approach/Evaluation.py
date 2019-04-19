class Mountain_Evaluation:
	prefered_max_tops = 4
	prefered_avg_heights_diff = 3
	traversalable = True

	#横看成岭侧成峰，远近高低各不同

	#跑题：如果有个爬虫一直在爬关于city的season，然后实时构建城市来map新闻，就算是文字版的，也算是很有趣的alpha city了吧？
	#当然如果是图像的就更好了，不行做成报纸，来截取照片，也不错啊

	def eval(mountain):
		s_tops = score_tops(mountain)
		s_heights_diff = score_heights_diff(mountain)
		s_traversalable = score_traversalable(mountain)
		return s_tops+s_heights_diff+s_traversalable

	def score_tops(mountain):
		for y in range(mountain.size_y):
			for x in range(mountain.size_x):
				for z in range(mountain.size_z)
					

	def score_heights_diff(mountain):

	def score_traversalable(mountain):

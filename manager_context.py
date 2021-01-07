class Files:
	def __init__(self,name_file):
		self.name_file = name_file

	def __enter__(self):
		self.f = open(self.name_file)
		return self.f

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.f:
			self.f.close()



files = Files('test.txt')

with files as f:
	print(f.read())


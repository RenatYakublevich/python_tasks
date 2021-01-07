import time


class RocketStart:
	def __init__(self):
		self.limit = 4

	def __iter__(self):
		return self

	def __next__(self):
		if self.limit > 1:		
			self.limit -= 1
			time.sleep(1)
			return self.limit
		else:
			raise StopIteration

rocket = RocketStart()

for tick in rocket:
	print(f'До взлёта - {tick}')

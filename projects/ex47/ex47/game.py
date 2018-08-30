class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		#paths is dict with key, value pair as {string : room obj}

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths) #update function includes key, value pair in parameter dict to calling object dict


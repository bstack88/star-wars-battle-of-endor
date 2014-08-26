""" 
Each GridSpace object represents a cube of the simulation space.
"""
class GridSpace():
	def __init__(self):
		self.flag = False
		self.actors = []

	# Add an actor to the grid
	def addActor(self,star_wars_actor):
		self.actors.append(star_wars_actor)
		self.flag = True

	# Remove an actor from the grid if it exists in the grid
	def removeActor(self,star_wars_actor):
		for actor in self.actors:
			if(actor == star_wars_actor):
				self.actors.remove(star_wars_actor)
				self.flag = True
				break

	# def getCoordinates(self):
	# 	coor = []
	# 	coor.append(self.x,self.x1,self.y,self.y1,self.z,self.z1);
	# 	return coor

	def getShips(self):
		neighbors=[]
		for star_wars_actor in self.actors:
			if(star_wars_actor.type == 'ship'):
				neighbors.append(star_wars_actor)
		return neighbors

	def getFlag(self):
		return self.flag
	def clearFlag(self):
		self.flag = False
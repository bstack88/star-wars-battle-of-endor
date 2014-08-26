from panda3d.core import TextNode
from panda3d.core import Point2,Point3,Vec3,Vec4
from direct.gui.OnscreenText import OnscreenText
from direct.task.Task import Task
from math import sin, cos, pi
from random import randint, choice, random
from direct.interval.MetaInterval import Sequence
from direct.interval.FunctionInterval import Wait,Func
from math import pi, sin, cos
from panda3d.core import Camera
from panda3d.core import Spotlight

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor, VBase4, DirectionalLight, PerspectiveLens


import cPickle, sys


from ship import *
from space import space

from filter import LpfVec3

class Environment(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)

		self.gameTask = taskMgr.add(self.gameLoop, "gameLoop")

		base.disableMouse()
		
		base.camera.setPos(500, 500, 2000)
		base.camera.lookAt(500,500,0)

		slight = Spotlight('slight')
		slight.setColor(VBase4(1, 1, 1, 1))
		lens = PerspectiveLens()
		slight.setLens(lens)

		# create rebel ships
		self.rebels = [Xwing('xwing' + str(x)) for x in xrange(20)]
		self.rebels += [Ywing('ywing' + str(x)) for x in xrange(20)]
		self.rebels += [Awing('awing' + str(x)) for x in xrange(20)]
		self.rebels += [Bwing('bwing' + str(x)) for x in xrange(20)]

		# create imperial ships
		self.imperials = [TieFighter('tiefighter' + str(x)) for x in xrange(80)]
		self.imperials += [TieInterceptor('tieinterceptor' + str(x)) for x in xrange(80)]

		self.shipList = []
		self.shipList += self.rebels + self.imperials

		for i, ship in enumerate(self.shipList):
			ship.reparentTo(render)
			ship.setScale(2)
			ship.setPos(Point3(random()*1000,
							   random()*1000,
							   random()*1000))

			directionalLight = DirectionalLight('directionalLight')
			directionalLightNP = render.attachNewNode(directionalLight)

			directionalLightNP.setHpr(180, -20, 0)
			ship.setLight(directionalLightNP)

		self.outFile = open('rebels_20_each_imperial_80_each_ship2ship','w')

		self.camFilter = LpfVec3(Vec3(0,0,0),20)


	def gameLoop(self, task):
		
		rebelAlive = 0

		for ship in self.rebels:
			if(ship.isDetached() == False): 
				rebelAlive += 1

		empireAlive = 0
		for ship in self.imperials:
			if(ship.isDetached() == False): empireAlive += 1
	
		return Task.cont

t = Environment()
t.run()
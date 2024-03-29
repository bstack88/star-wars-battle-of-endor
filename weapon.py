from panda3d.core import Point2,Point3,Vec3,Vec4
from direct.task.Task import Task
from panda3d.core import Camera
from panda3d.core import Spotlight
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor, VBase4, DirectionalLight, PerspectiveLens

from math import sqrt
from star_wars_actor import StarWarsActor


# Weapon - the base weapon class for all weapons in the simulation
class Weapon(object):
	def __init__(self, ship, name, weaponType, range, cooldown = 5):
		self.parent = ship
		self.name = name
		self.weaponType = weaponType
		self.range = range
		self.cooldown = cooldown

		# this is a list of references to all laser objects that have been fired
		self.shotList = []

	# Construct a message that this weapon was fired. Likely called from the
	# weapon system, with the message passed on somehow.
	def fire(self, parent, target):
		pass

	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name

	def getDamage(self):
		return self.damage
	def setDamage(self, damage):
		self.damage = damage

	def getRange(self):
		return self.range
	def setRange(self, range):
		self.range = range

	def getCooldown(self):
		return self.cooldown
	def setCooldown(self, cooldown):
		self.cooldown = cooldown

	def removeShot(self, shot):
		try:
			self.shotList.remove(shot)
		except (ValueError, AttributeError):
			pass

class XwingWeapon(Weapon):
	def __init__(self, ship, name, weaponType, wrange, cooldown = 0):
		super(XwingWeapon, self).__init__(ship, name, weaponType, cooldown)
		self.range = wrange

		self.gunSelection = 3

		gunPos = [
			Vec3(-2.5, 2, 1),
			Vec3(2.5, 2, -1),
			Vec3(-2.5, 2, -1),
			Vec3(2.5, 2, 1)]

		self.gunList = []
		for pos in gunPos:
			gun = self.parent.attachNewNode("dummyNode")
			gun.setScale(0.1)
			gun.setPos(pos)
			gun.hide()
			self.gunList.append(gun)

	def fire(self, parent, target):
		self.gunSelection = (self.gunSelection + 1) % 4
		laser = self.weaponType(parent, target, self.gunList[self.gunSelection], self.name + str(len(self.shotList)), self.range, self.removeShot)
		self.shotList.append(laser)

class YwingWeapon(Weapon):
	def __init__(self, ship, name, weaponType, wrange, cooldown = 5):
		super(YwingWeapon, self).__init__(ship, name, weaponType, cooldown)
		self.range = wrange

		gunPos = [
			Vec3(0.5, 3, 0),
			Vec3(-0.5, 3, 0)]

		self.gunList = []
		for pos in gunPos:
			gun = self.parent.attachNewNode("dummyNode")
			gun.setScale(0.1)
			gun.setPos(pos)
			gun.hide()
			self.gunList.append(gun)

	def fire(self, parent, target):
		laser0 = self.weaponType(parent, target, self.gunList[0], self.name + str(len(self.shotList)), self.range, self.removeShot)
		laser1 = self.weaponType(parent, target, self.gunList[1], self.name + str(len(self.shotList)), self.range, self.removeShot)
		self.shotList.append(laser0)
		self.shotList.append(laser1)


class AwingWeapon(Weapon):
	def __init__(self, ship, name, weaponType, wrange, cooldown = 5):
		super(AwingWeapon, self).__init__(ship, name, weaponType, cooldown)
		self.range = wrange

		self.gunSelection = 0

		gunPos = [
			Vec3(2, 3, 0.5),
			Vec3(-2, 3, 0.5)]

		self.gunList = []
		for pos in gunPos:
			gun = self.parent.attachNewNode("dummyNode")
			gun.setScale(0.1)
			gun.setPos(pos)
			gun.hide()
			self.gunList.append(gun)

	def fire(self, parent, target):
		self.gunSelection = (self.gunSelection + 1) % 2
		laser = self.weaponType(parent, target, self.gunList[self.gunSelection], self.name + str(len(self.shotList)), self.range, self.removeShot)
		self.shotList.append(laser)


class BwingWeapon(Weapon):
	def __init__(self, ship, name, weaponType, wrange, cooldown = 5):
		super(BwingWeapon, self).__init__(ship, name, weaponType, cooldown)
		self.range = wrange

		self.gunSelection = 0

		gunPos = [
			Vec3(3, 3, 0),
			Vec3(-3, 3, 0),
			Vec3(0, 3, -5.5)]

		self.gunList = []
		for pos in gunPos:
			gun = self.parent.attachNewNode("dummyNode")
			gun.setScale(0.1)
			gun.setPos(pos)
			gun.hide()
			self.gunList.append(gun)

	def fire(self, parent, target):
		self.gunSelection = (self.gunSelection + 1) % 3
		laser = self.weaponType(parent, target, self.gunList[self.gunSelection], self.name + str(len(self.shotList)), self.range, self.removeShot)
		self.shotList.append(laser)

class TieFighterWeapon(Weapon):
	def __init__(self, ship, name, weaponType, wrange, cooldown = 5):
		super(TieFighterWeapon, self).__init__(ship, name, weaponType, cooldown)
		self.range = wrange
				
		gunPos = [
			Vec3(0.5, 4, 0),
			Vec3(-0.5, 4, 0)]

		self.gunList = []
		for pos in gunPos:
			gun = self.parent.attachNewNode("dummyNode")
			gun.setScale(0.1)
			gun.setPos(pos)
			gun.hide()
			self.gunList.append(gun)

	def fire(self, parent, target):
		laser0 = self.weaponType(parent, target, self.gunList[0], self.name + str(len(self.shotList)), self.range, self.removeShot)
		laser1 = self.weaponType(parent, target, self.gunList[1], self.name + str(len(self.shotList)), self.range, self.removeShot)
		self.shotList.append(laser0)
		self.shotList.append(laser1)


class TieInterceptorWeapon(Weapon):
	def __init__(self, ship, name, weaponType, wrange, cooldown = 5):
		super(TieInterceptorWeapon, self).__init__(ship, name, weaponType, cooldown)
		self.range = wrange

		self.gunSelection = 3

		gunPos = [
			Vec3(-2.0, 2, 1),
			Vec3(2.0, 2, -1),
			Vec3(-2.0, 2, -1),
			Vec3(2.0, 2, 1)]

		self.gunList = []
		for pos in gunPos:
			gun = self.parent.attachNewNode("dummyNode")
			gun.setScale(0.1)
			gun.setPos(pos)
			gun.hide()
			self.gunList.append(gun)

	def fire(self, parent, target):
		self.gunSelection = (self.gunSelection + 1) % 4
		laser = self.weaponType(parent, target, self.gunList[self.gunSelection], self.name + str(len(self.shotList)), self.range, self.removeShot)
		self.shotList.append(laser)


class Laser(StarWarsActor):
	def __init__(self, model, timestep, parent, target, gun, name, damage, range, speed, callback):
		super(Laser, self).__init__(model, timestep, name)
		self.parent = parent
		self.target = target
		self.name = name
		self.damage = damage
		self.range = range
		self.speed = speed
		self.callback = callback
		
		self.type = 'weapon'
		self.startPos = gun.getPos(render)

		self.reparentTo(render)
		self.setScale(0.5)
		self.setPos(self.startPos)

		initialVelocity_n = Vec3(self.parent.getVelocity() + self.target.getVelocity()*3)
		initialVelocity_n.normalize()
		self.setVelocity((initialVelocity_n * self.speed) + self.parent.getVelocity())

		self.setHpr(self.navSystem.getDirection(self.parent.getVelocity()+self.target.getVelocity()*3))

	def remove(self):
		taskMgr.remove(self.task)
		self.callback(self)
		self.destroy()		

	def onCollision(self, swActor):
		# only look for ships, ignore other lasers
		if (swActor.type == 'ship' and swActor != self.parent):
			swActor.onCollision(self)
			self.remove()

	def getDistance(self, x0, x1):
		return Vec3(x1 - x0).length()

	def update(self, task):
		super(Laser,self).update(task)
		dt = task.time  #this is the elapsed time since the first call of this function

		pos = self.startPos + self.getVelocity()*dt
		self.setPos(pos)

		distance = self.getDistance(self.startPos, pos)
		if distance >= self.range:
			self.remove()

		return task.cont


class RedLaserLong(Laser):
	def __init__(self, parent, target, gun, name, wrange, callback):
		model = "models/beam"
		timestep = 0.3
		damage = 5
		speed = 400
		super(RedLaserLong, self).__init__(model, timestep, parent, target, gun, name, damage, wrange, speed, callback)

		directionalLight = DirectionalLight('directionalLight')
		directionalLight.setColor(Vec4(1, 0, 0, 1))
		directionalLightNP = render.attachNewNode(directionalLight)

		directionalLightNP.setHpr(180, -20, 0)
		self.setLight(directionalLightNP)


class RedLaserShort(Laser):
	def __init__(self, parent, target, gun, name, wrange, callback):
		model = "models/beam"
		timestep = 0.3
		damage = 10
		speed = 400
		super(RedLaserShort, self).__init__(model, timestep, parent, target, gun, name, damage, wrange, speed, callback)

		directionalLight = DirectionalLight('directionalLight')
		directionalLight.setColor(Vec4(1, 0, 0, 1))
		directionalLightNP = render.attachNewNode(directionalLight)

		directionalLightNP.setHpr(180, -20, 0)
		self.setLight(directionalLightNP)


class GreenLaserLong(Laser):
	def __init__(self, parent, target, gun, name, wrange, callback):
		model = "models/beam"
		timestep = 0.3
		damage = 5
		speed = 400
		super(GreenLaserLong, self).__init__(model, timestep, parent, target, gun, name, damage, wrange, speed, callback)

		directionalLight = DirectionalLight('directionalLight')
		directionalLight.setColor(Vec4(0, 1, 0, 1))
		directionalLightNP = render.attachNewNode(directionalLight)

		directionalLightNP.setHpr(180, -20, 0)
		self.setLight(directionalLightNP)


class GreenLaserShort(Laser):
	def __init__(self, parent, target, gun, name, wrange, callback):
		model = "models/beam"
		timestep = 0.3
		damage = 10
		speed = 400
		super(GreenLaserShort, self).__init__(model, timestep, parent, target, gun, name, damage, wrange, speed, callback)

		directionalLight = DirectionalLight('directionalLight')
		directionalLight.setColor(Vec4(0, 1, 0, 1))
		directionalLightNP = render.attachNewNode(directionalLight)

		directionalLightNP.setHpr(180, -20, 0)
		self.setLight(directionalLightNP)
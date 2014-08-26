from panda3d.core import Point2,Point3,Vec3,Vec4
from direct.task.Task import Task
from panda3d.core import Camera
from panda3d.core import AmbientLight, PointLight

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor, VBase4, DirectionalLight, PerspectiveLens

from ship import *
from weapon import *
from space import space

class test(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)

		base.disableMouse()
		
		dl = DirectionalLight('dLight')
		dl.setColor(Vec4(0.1,0.1,0.1,1))
		dlNP = render.attachNewNode(dl)
		dlNP.setPos(1000,1000,0)

		al = AmbientLight('alight')
		al.setColor(Vec4(0.3, 0.3, 0.3, 1))
		alNP = render.attachNewNode(al)

		pl = PointLight('plight')
		pl.setColor(VBase4(0.2,0.2,0.2,1))
		plNP = render.attachNewNode(pl)
		plNP.setPos(100,100,100)
		render.setLight(plNP)



		self.shipList = [
			Xwing('xwing1'),
			TieInterceptor("interceptor1")
		]

		for i, ship in enumerate(self.shipList):
			ship.reparentTo(render)
			ship.setScale(2)
			ship.setPos(Point3(i*0,i*50,i*0))
			# ship.setLight(dlNP)
			ship.setLight(alNP)


		base.camera.setPos(-200,300,0)
		base.camera.lookAt(0, 0, 0)
		taskMgr.add(self.clearSpaceFlag, 'clearFlags')

	def clearSpaceFlag(self, task):
		pass


t = test()
t.run()

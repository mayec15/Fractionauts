from IcnBasic import IcnBasic 
import HelperTexture
import HelperVec2

class IcnTextBox(IcnBasic):
	@staticmethod 
	def setFont(font):
		IcnTextBox.FONT = font

	def __init__(self, x, y, w, h, content, color=(255, 255, 255)):
		IcnBasic.__init__(self, x, y, w, h)
		self.posInit = (x, y)
		self.setContent(content, color)

	def helperDraw(self, screen):
		rect = screen.blit(self.mySurface, self.pos)
		return self.posInit[0], self.posInit[1], self.size[0], self.size[1]

	def setContent(self, c, color=(255, 255, 255)):
		self.content = str(c)
		self.mySurface = IcnTextBox.FONT.render(self.content, 1, color)
		size = (self.mySurface.get_width(), self.mySurface.get_height())
		ratio_1 = 1
		ratio_2 = 1
		if(self.mySurface.get_width() != 0 and self.mySurface.get_height() != 0):
			ratio_1 = self.size[0] / self.mySurface.get_width()
			ratio_2 = self.size[1] / self.mySurface.get_height()
		ratio = ratio_1 if ratio_1 < ratio_2 else ratio_2

		self.mySurface = HelperTexture.scale(self.mySurface, HelperVec2.mult(size, (ratio, ratio)))
		size = (self.mySurface.get_width(), self.mySurface.get_height())
		
		extra_space = HelperVec2.mult(HelperVec2.sub(self.size, size), (.5, .5))
		self.pos = HelperVec2.add(self.posInit, extra_space)
	



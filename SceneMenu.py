from SceneBasic import *
import DrawHelper
import HelperVec2
import random
from IcnBasic import IcnBasic
from IcnParticleShootingStar import IcnParticleShootingStar
from IcnParticleDistortCustomRange import IcnParticleDistortCustomRange

import SoundManager


class SceneMenu(SceneBasic):
    def __init__(self, resolution):
        SceneBasic.__init__(self, resolution)

    def registerEvent_play(self, e):
        self.EVENT_PLAY.append(e)

    def registerEvent_help(self, e):
        self.EVENT_HELP.append(e)

    def registerEvent_quit(self, e):
        self.EVENT_QUIT.append(e)

    def initEvents(self):
        self.EVENT_PLAY = []
        self.EVENT_HELP = []
        self.EVENT_QUIT = []

    def initImages(self, resolution):
        # self.textureIdTitle =	TextureLoader.load(os.path.join('assets', 'screenStart', 'title.png'), HelperVec2.mult(resolution, (.7,.13)))
        self.textureIdTitle = TextureLoader.load(os.path.join('assets', 'screenStart', 'title.png'))
        self.textureIdBG = TextureLoader.load(os.path.join('assets', 'screenStart', 'background.png'), resolution)

        self.textureIdBttnStart = TextureLoader.load(os.path.join('assets', 'screenStart', 'bttnStart.png'))
        self.textureIdBttnHelp = TextureLoader.load(os.path.join('assets', 'screenStart', 'bttnHelp.png'))
        self.textureIdBttnExit = TextureLoader.load(os.path.join('assets', 'screenStart', 'bttnExit.png'))

        self.textureIdShootingStar_00 = TextureLoader.load(os.path.join('assets', 'screenCommon', 'shootingStar00.png'))
        self.textureIdShootingStar_01 = TextureLoader.load(os.path.join('assets', 'screenCommon', 'shootingStar01.png'))

    def initOthers(self, resolution):
        self.initParticles(resolution)
        self.renderScreenObjects.extend(self.arrShootingStars)

        self.icnMouse = IcnBasic.FROM_PATH(os.path.join('assets', 'screenCommon', 'cursor.png'))
        self.renderScreenObjects.append(self.icnMouse)

    def helperInitKButton(self, center, textureID):
        texture = TextureLoader.get(textureID)
        size = (texture.get_width(), texture.get_height())
        return KButton(center[0] - size[0] * .5, center[1] - size[1] * .5, size[0], size[1], textureID)

    def initButtons(self, resolution):
        center = HelperVec2.mult(resolution, (.5, .5))
        # Main menu buttons
        self.bttnPlay = self.helperInitKButton((center[0], center[1] - 60), self.textureIdBttnStart)  # KButton(center[0]-100, center[1] - 100, 200, 75,s.textureIdBttnStart)
        self.bttnHow = self.helperInitKButton((center[0], center[1]), self.textureIdBttnHelp)
        self.bttnQuit = self.helperInitKButton((center[0], center[1] + 60), self.textureIdBttnExit)  # KButton(center[0]  -100,center[1] + 100, 200, 75,s.textureIdBttnExit)

        self.buttons = [self.bttnPlay, self.bttnHow, self.bttnQuit]

    def initParticles(self, resolution):
        self.arrShootingStars = []
        self.distortH = IcnParticleDistortCustomRange(0, 80, resolution[0], 5 / 600.0 * resolution[1], self.myBackground, 1, 0)
        self.distortV = IcnParticleDistortCustomRange(100, 0, resolution[0], 2 / 600.0 * resolution[1], self.myBackground, -1, 0)
        self.distortSpacing = 5 / 600.0 * resolution[1] * .5
        self.arrShootingStars.append(self.distortH)
        self.arrShootingStars.append(self.distortV)

        for i in range(0, 3):
            textureId = self.textureIdShootingStar_00 if random.random() < .5 \
                else self.textureIdShootingStar_01
            texture = TextureLoader.get(textureId)
            size = (texture.get_width(), texture.get_height())
            p = IcnParticleShootingStar(random.random() * resolution[0], random.random() * -resolution[1], size[0], size[1], textureId, resolution)
            self.arrShootingStars.append(p)
        # self.distortH = IcnParticleDistortCustomRange(0,80,resolution[0],15, self.myBackground,1,0 )
        # self.distortV = IcnParticleDistortCustomRange(100, 0,15,resolution[1], self.myBackground,1,0 )

        pass

    def EVENT_SCENE_START(self):
        print("SCENE_BASIC_ENTER")
        IcnParticleShootingStar.textureBG = self.myBackground

    def EVENT_CLICK(self):
        mouseAt = pygame.mouse.get_pos()
        print(mouseAt)
        buttons_event = [
            [self.bttnQuit, self.EVENT_QUIT],
            [self.bttnPlay, self.EVENT_PLAY],
            [self.bttnHow, self.EVENT_HELP],
        ]

        for bttn, event in buttons_event:
            if bttn.isUnder(mouseAt):
                self.helperRaiseEvent(event)
                break

    def initBackground(self, screen, size):
        screen.fill((255, 255, 255))
        DrawHelper.drawAspect(screen, self.textureIdBG, 0, 0)
        DrawHelper.drawAspect(screen, self.textureIdTitle, .12, .1)
        for button in self.buttons: button.draw(screen)

    ratio = 0

    def renderUpdate(self, timeElapsed):
        self.icnMouse.pos = pygame.mouse.get_pos()

        self.ratio = (self.ratio + 800.15 * timeElapsed) % 3.5
        self.distortH.range = (self.ratio, self.ratio)
        self.distortV.range = (-self.ratio, -self.ratio)
        # self.distortH.pos = (0,pygame.mouse.get_pos()[1])
        # self.distortV.pos = (pygame.mouse.get_pos()[0],0)
        self.distortH.pos = (0, pygame.mouse.get_pos()[1])
        self.distortV.pos = (0, pygame.mouse.get_pos()[1] + self.distortSpacing)
        for icn in self.arrShootingStars:
            icn.drawUpdate(timeElapsed)



# def initButtons(s,resolution):
# remove all the shit below fuck
# Load in Title Image and background images
#
#	s.logo = self.helperLoadImage(os.path.join('assets', 'startscreen', 'Title.png'))
#	s.startbg = self.helperLoadImage(os.path.join('assets', 'startscreen', 'night_sunset_gradient.png'))
#	s.startbg = self.helperRescaleImage(s.startbg ,(800,600) )
#
#	#idiotic scrollingImage take care of it please
#	s.stars_tiny =  ScrollingImage( \
#					   pygame.image.load(os.path.join('assets', 'startscreen', \
#									   'stars_tiny.png')), (-50,-50), float(.004))
#	s.stars_small = ScrollingImage( \
#					   pygame.image.load(os.path.join('assets', 'startscreen', \
#									   'stars_small.png')), (-50,-50), float(.008))
#	s.stars_medium = ScrollingImage( \
#						pygame.image.load(os.path.join('assets', 'startscreen', \
#									   'stars_medium.png')), (-50,-50), float(.012))
#	s.stars_big = ScrollingImage(
#		s.helperLoadImage(os.path.join('assets', 'startscreen', 'stars_big.png')) \
#		, (-50,-50), float(.36))
# idiot idiot stupid
#	s.sunsetoverlay = pygame.image.load(os.path.join('assets', 'startscreen', 'sunset_overlay.png'))


# def renderScreen(s, screen):
# self.main.screen.blit(s.startbg, (0, 0))
# self.stars_tiny.draw(self.main.screen,tick)
# self.stars_small.draw(self.main.screen, tick)
# self.stars_medium.draw(self.main.screen,tick)
# self.stars_big.draw(self.main.screen, tick)

# self.main.screen.blit(self.sunsetoverlay, (0, 0)) # this might make it too dim
# self.main.screen.blit(self.logo, (self.main.hcenter - 300, 150))


# woooha no please

#	def helperLoadImage(self, osPath):
#		img = pygame.image.load(osPath).convert_alpha()
#		return img
#	def helperRescaleImage(self, img, scale):
#		return pygame.transform.scale(img, scale)
#	def helperLoadImageAsScrolling(self, osPath, A, B):
#		return pygame.image.load(osPath)

# Module Name	Functionality
# pygame.cdrom	Access CD-ROMs
# pygame.cursors	Load cursors
# pygame.display	Control the display window and screen
# pygame.draw	Draw shapes, lines, and points
# pygame.event	Manage events
# pygame.font	Use fonts
# pygame.image	Load and save images
# pygame.joystick	Use gamepads or similar devices
# pygame.key	Read keyboard buttons
# pygame.mixer	Control sound
# pygame.mouse	Control the mouse
# pygame.movie	Play videos
# pygame.music	Play audio
# pygame.overlay	Access advanced video overlays
# pygame.rect	Manage rectangular areas
# pygame.sndarray	Manipulate sound data
# pygame.sprite	Manipulate animated images (sprites)
# pygame.surface	Manage images and the screen
# pygame.surfarray	Manage surface pixel data
# pygame.time	Manage time and sync information
# pygame.transform	Scale and move images
# pygame.locals
import pygame,sys,time,random
from pygame.locals import *



pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

aa=pygame.mixer.Sound("english.mp3")
aa.play()
screen.fill((0,0,0))


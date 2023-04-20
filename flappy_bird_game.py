import pygame
import random
import sys


# initialize pygame
pygame.init()

# FPS settings
FPS = 30
fpsClock = pygame.time.Clock()

# window settings
SCREENWIDTH = 288
SCREENHEIGHT = 512
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Flappy Bird')

# game assets
IMAGES = {}
IMAGES['background'] = pygame.image.load('background.png').convert()
IMAGES['player'] = (
    pygame.image.load('player.png').convert_alpha(),
    pygame.image.load('player2.png').convert_alpha(),
    pygame.image.load('player3.png').convert_alpha()
)
IMAGES['pipe'] = (
    pygame.transform.rotate(pygame.image.load('pipe.png').convert_alpha(), 180),
    pygame.image.load('pipe.png').convert_alpha()
)
IMAGES['base'] = pygame.image.load('base.png').convert_alpha()
IMAGES['numbers'] = (
    pygame.image.load('0.png').convert_alpha(),
    pygame.image.load('1.png').convert_alpha(),
    pygame.image.load('2.png').convert_alpha(),
    pygame.image.load('3.png').convert_alpha(),
    pygame.image.load('4.png').convert_alpha(),
    pygame.image.load('5.png').convert_alpha(),
    pygame.image.load('6.png').convert_alpha(),
    pygame.image.load('7.png').convert_alpha(),
    pygame.image.load('8.png').convert_alpha(),
    pygame.image.load('9.png').convert_alpha()
)
IMAGES['message'] = pygame.image.load('message.png').convert_alpha()
IMAGES['gameover'] = pygame.image.load('gameover.png').convert_alpha()

# game sounds
SOUNDS = {}
SOUNDS['die'] = pygame.mixer.Sound('die.wav')
SOUNDS['hit'] = pygame.mixer.Sound('hit.wav')
SOUNDS['point'] = pygame.mixer.Sound('point.wav')
SOUNDS['swoosh'] = pygame.mixer.Sound('swoosh.wav')
SOUNDS['wing'] = pygame.mixer.Sound('wing.wav')

# game variables
PLAYER_INDEX_GEN = cycle([0, 1, 2, 1])
FPS = 30
ANIMATION_TIME = 5
PIPE_GAP_SIZE = 100
BASEY = SCREENHEIGHT * 0.79
SCORE = 0


def main():
    global SCREEN, SOUNDS, IMAGES, SCORE
    pygame.init()

    # display variables
    DISPLAY = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bird')
    pygame.display.set_icon(IMAGES['player'][0])

    # game variables
    player = getPlayer()
    upperPipes = []
    lowerPipes = []
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
    upperPipes.append(newPipe1[0])
    lowerPipes.append(newPipe1[1])
    upperPipes.append(newPipe2[0])
    lowerPipes.append(newPipe2[1])
    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1
    playerFlapAccv = -8
    playerFlapped = False

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and
                event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
               

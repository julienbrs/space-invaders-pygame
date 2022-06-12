# pylint: disable=no-member
"""
File for class
"""

import pygame
import os

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 45, 78      #already in other file


IMG_PLAYER_CENTER1 = pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'player', 'center1.png')),(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))       #already in other file
IMG_PLAYER_CENTER2 = pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'player', 'center2.png')),(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)) 

IMG_PLAYER_LEFT1 = pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'player', 'left1.png')),(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
IMG_PLAYER_LEFT2 = pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'player', 'left2.png')),(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

IMG_PLAYER_RIGHT1 = pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'player', 'right1.png')),(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
IMG_PLAYER_RIGHT2 = pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'player', 'right2.png')),(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))




IMG_ENN_LITTLE_GREEN = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'little_green.png')), (60, 51)), 270)

IMG_ENN_LITTLE_RED = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'little_red.png')), (60, 51)), 270)

IMG_ENN_LITTLE_BLUE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'little_blue.png')), (60, 51)), 270)


IMG_ENN_LIT_MED_GREEN = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'lit_med_green.png')), (60, 51)), 270)

IMG_ENN_LIT_MED_RED = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'lit_med_red.png')), (60, 51)), 270)

IMG_ENN_LIT_MED_BLUE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'lit_med_blue.png')), (60, 51)), 270)



IMG_ENN_MEDIUM_GREEN = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'medium_green.png')), (60, 51)), 270)

IMG_ENN_MEDIUM_RED = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'medium_red.png')), (60, 51)), 270)

IMG_ENN_MEDIUM_BLUE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'medium_blue.png')), (60, 51)), 270)





GREEN_MISSILE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "green_missile.png")), (27.5, 12.5)), 270)
RED_MISSILE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "red_missile.png")), (27.5, 12.5)), 270)
BLUE_MISSILE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "blue_missile.png")), (27.5, 12.5)), 270)



RED   = (255, 0, 0)


def collide(item1, item2):
    "check if there is a collision"
    offset_x = item2.x - item1.x
    offset_y = item2.y - item1.y
    return item1.mask.overlap(item2.mask, (offset_x, offset_y)) is not None



class Laser():
    "Class of lasers, x and y: where it starts"
    def __init__(self, x, y, direction, img):
        self.x          = x
        self.y          = y
        self.direction  = direction
        self.img        = img
        self.mask       = pygame.mask.from_surface(self.img)

    def draw(self, surface):
        "draw item"
        surface.blit(self.img, (self.x, self.y))

    def move(self, velocity):
        "move the item, velocity can also change the direction + or -"
        self.y += velocity

    def off_screen(self, height):
        "check if item isn't off the screen"
        return self.y >= -15 and self.y <= height

    def collision(self, obj):
        "check a collision"
        return collide(self, obj)


class Shooter():
    "def class of shooter"

    def __init__(self, x, y, maxlife):
        self.x = x
        self.y = y
        self.lasers = []
        self.lifebar = maxlife
        self.maxlife = maxlife


    def draw(self, surface):
        "draw item"
        surface.blit(self.img, (self. x, self.y))
        percentage_life = self.lifebar / self.maxlife
        pygame.draw.line(surface, RED, (self.x*1.01, self.y + self.get_height() + 5),
         (self.x + 0.95*self.get_width()*percentage_life,self.y + self.get_height() + 5), width=2)
        for laser in self.lasers:
            laser.draw(surface)

    def shoot(self):
        "shoot"
        laser = Laser(self.x, self.y, None, self.img_laser)
        self.lasers.append(laser)

    def destroyed(self, damage):
        "is touched, return True if destroyed "
        self.lifebar -= damage
        if self.lifebar <= 0:
            return True
        return False

    def collision(self, other):
        "collision"
        return collide(self, other)

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()


class Player(Shooter):
    "class of the player"

    def __init__(self, x, y, width, height, img, img_laser):
        super().__init__(x, y, 100)
        self.width      = width #todo
        self.img = img
        self.img_laser = img_laser
        self.height     = height
        self.mask       = pygame.mask.from_surface(self.img)


    def shoot(self):
        "shoot"
        laser = Laser(self.x - self.width/2, self.y - self.height, None, self.img_laser)
        self.lasers.append(laser)

    def collision(self, other):
        "collision"
        return collide(self, other)

    def move(self, keys, vel, size, blink):
        "move the player"
        blink = (blink + 1) % 20
        CHANGED = False     #faire autrement ?
        if keys[pygame.K_LEFT] and self.x > 0:    #Left
            self.x -= vel
            if blink >= 10:
                self.img = IMG_PLAYER_LEFT1
            else:
                self.img = IMG_PLAYER_LEFT2
            CHANGED = True
        if keys[pygame.K_RIGHT] and self.x + self.width < size[0]:    #Right
            self.x += vel
            self.img = IMG_PLAYER_RIGHT1
            if blink >= 10:
                self.img = IMG_PLAYER_RIGHT1
            else:
                self.img = IMG_PLAYER_RIGHT2
            CHANGED = True
        if keys[pygame.K_UP] and self.y > 0:    #Top
            self.y -= vel
            CHANGED = True
        if keys[pygame.K_DOWN] and self.y + self.height < size[1]:    #Left
            self.y += vel
            CHANGED = True
        if not CHANGED:
            if blink >= 10:
                self.img = IMG_PLAYER_CENTER1
            else:
                self.img = IMG_PLAYER_CENTER2
        return blink
        


    def move_lasers(self, velocity, others, height):
        """move lasers of the shooter, check if collision with others, can
        change the direction with sign of velocity"""
        for laser in self.lasers:
            laser.move(velocity)
            on_screen = True #trouver meilleur moyen ?
            for other in others:
                if laser.collision(other):
                    if other.destroyed(5):        #todo mettre les degats dans le jeu
                        others.remove(other)
                    self.lasers.remove(laser)
                    on_screen = False
            if not laser.off_screen(height) and on_screen:
                self.lasers.remove(laser)


class Ennemy(Shooter):
    "class of the ennemy"


    def __init__(self, x, y, width, height, maxlife):
        super().__init__(x, y, maxlife)
        self.width      = width
        self.height     = height


    def move(self, velocity):
        "move the item, velocity can also change the direction + or -"
        self.y += velocity

    def move_lasers(self,player, vel, height):
        "move lasers and check if collision with player"
        for laser in self.lasers:
            laser.move(vel + 2)
            if not laser.off_screen(height): #fixer le nom aussi ici
                self.lasers.remove(laser)
            if laser.collision(player):
                player.destroyed(20)
                self.lasers.remove(laser)

    def not_off_screen(self, height):
        "check if item isn't off the screen"
        return self.y <= height

    def shoot(self):
        "shoot"
        laser = Laser(self.x - self.width/2, self.y - self.height, None, self.img_laser)
        self.lasers.append(laser)

    def collision(self, other):
        "collision"
        return collide(self, other)
    
    def destroy(self):
        self.lasers = []

class Little_Ennemy(Ennemy):
    COLOR_MAP = {
                "red": (IMG_ENN_LITTLE_RED, RED_MISSILE),
                "green": (IMG_ENN_LITTLE_GREEN, GREEN_MISSILE),
                "blue": (IMG_ENN_LITTLE_BLUE, BLUE_MISSILE)
                }
    def __init__(self, x, y, width, height, maxlife, color):
        img, img_laser = self.COLOR_MAP[color]
        super().__init__(x, y, width, height, maxlife)
        self.img = img
        self.img_laser = img_laser
        self.mask       = pygame.mask.from_surface(self.img)

class Lit_Med(Ennemy):
    COLOR_MAP = {
                "red": (IMG_ENN_LIT_MED_RED, RED_MISSILE),
                "green": (IMG_ENN_LIT_MED_GREEN, GREEN_MISSILE),
                "blue": (IMG_ENN_LIT_MED_BLUE, BLUE_MISSILE)
                }
    def __init__(self, x, y, width, height, maxlife, color):
        img, img_laser = self.COLOR_MAP[color]
        super().__init__(x, y, width, height, maxlife)
        self.img = img
        self.img_laser = img_laser
        self.mask       = pygame.mask.from_surface(self.img)

class Medium(Ennemy):
    COLOR_MAP = {
                "red": (IMG_ENN_MEDIUM_RED, RED_MISSILE),
                "green": (IMG_ENN_MEDIUM_GREEN, GREEN_MISSILE),
                "blue": (IMG_ENN_MEDIUM_BLUE, BLUE_MISSILE)
                }
    def __init__(self, x, y, width, height, maxlife, color):
        img, img_laser = self.COLOR_MAP[color]
        super().__init__(x, y, width, height, maxlife)
        self.img = img
        self.img_laser = img_laser
        self.mask       = pygame.mask.from_surface(self.img)
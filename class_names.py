# pylint: disable=no-member
"""
File for class
"""

from time import time
from tkinter import N
import pygame
import random
import os

VELOCITY_BOT  = 0.03
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 45, 78      #already in other file


IMG_EXPLOSION1 = pygame.image.load(os.path.join('Assets', 'effects', 'explosion1.png'))
IMG_EXPLOSION2 = pygame.image.load(os.path.join('Assets', 'effects', 'explosion2.png'))
IMG_EXPLOSION3 = pygame.image.load(os.path.join('Assets', 'effects', 'explosion3.png'))
IMG_EXPLOSION4 = pygame.image.load(os.path.join('Assets', 'effects', 'explosion4.png'))
IMG_EXPLOSION5 = pygame.image.load(os.path.join('Assets', 'effects', 'explosion5.png'))


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
    ('Assets', 'ennemies', 'little_green.png')), (38, 32)), 270)

IMG_ENN_LITTLE_RED = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'little_red.png')), (38, 32)), 270)

IMG_ENN_LITTLE_BLUE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'little_blue.png')), (38, 32)), 270)


IMG_ENN_LIT_MED_GREEN = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'lit_med_green.png')), (70, 63)), 270)

IMG_ENN_LIT_MED_RED = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'lit_med_red.png')), (70, 63)), 270)

IMG_ENN_LIT_MED_BLUE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'lit_med_blue.png')), (70, 63)), 270)



IMG_ENN_MEDIUM_GREEN = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'medium_green.png')), (75, 75)), 270)

IMG_ENN_MEDIUM_RED = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'medium_red.png')), (75, 75)), 270)

IMG_ENN_MEDIUM_BLUE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'medium_blue.png')), (75, 75)), 270)



IMG_ENN_BIG_GREEN = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'big_green.png')), (110, 110)), 270)

IMG_ENN_BIG_RED = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'big_red.png')), (110,110)), 270)

IMG_ENN_BIG_BLUE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'big_blue.png')), (110,110)), 270)




IMG_ENN_HUGE_GREEN = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'huge_green.png')), (152, 188)), 270)

IMG_ENN_HUGE_RED = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'huge_red.png')), (152, 188)), 270)

IMG_ENN_HUGE_BLUE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'ennemies', 'huge_blue.png')), (152, 188)), 270)



GREEN_LASER = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "basic_green_orb.png")), (27.5, 12.5)), 270)
RED_LASER = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "basic_red_orb.png")), (27.5, 12.5)), 270)
BLUE_LASER = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "basic_blue_orb.png")), (27.5, 12.5)), 270)



GREEN_LITTLE_BEAM_LASER = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "little_beams_green.png")), (25, 87))
RED_LITTLE_BEAM_LASER = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "little_beams_red.png")), (25, 87))
BLUE_LITTLE_BEAM_LASER = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "little_beams_blue.png")), (25, 87))


BIG_ORB_GREEN = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "big_orb_green.png")), (68, 128)), 180)
BIG_ORB_RED = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "big_orb_red.png")), (68, 128)), 180)
BIG_ORB_BLUE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "big_orb_blue.png")), (68, 128)), 180)

BASIC_LASER_PLAYER = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "laser", "basic_laser_player.png")), (65, 45)), 90)


GREEN_SPEAR_LASER = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "spear_laser_green.png")), (85, 150))
RED_SPEAR_LASER = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "spear_laser_red.png")), (85, 150))
BLUE_SPEAR_LASER = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "spear_laser_blue.png")), (85, 150))

BASIC_LASER_PLAYER = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "laser", "basic_laser_player.png")), (65, 45)), 90)


HUGE_LASER = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "laser", "huge_missile.png")), (232, 132)), 270)



#items
ITEM_HEALTH = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "items", "health.png")), (50, 50))

ITEM_SHIELD = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "items", "shield.png")), (50, 50))

SHIELD_EFFECT = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "items", "shield_effect.png")), (80, 80))


RED   = (255, 0, 0)

LIST_EXPLOSION = []

class Explosion():

    def __init__(self, x, y, support):
        self.x = x
        self.y = y
        self.timer_explosion = 0
        self.img = None
        self.support = support

    def handle(self, TIME_EXPLOSION):
        "TIME_EXPLOSION depends on FPS"
        TIME = TIME_EXPLOSION/5
        self.timer_explosion += 1
        if self.timer_explosion < TIME:
            self.img = IMG_EXPLOSION1
        elif self.timer_explosion < 2*TIME:
            self.img = IMG_EXPLOSION2
        elif self.timer_explosion < 3*TIME:
            self.img = IMG_EXPLOSION3
        elif self.timer_explosion < 4*TIME:
            self.img = IMG_EXPLOSION4
        elif self.timer_explosion < 5*TIME:
            self.img = IMG_EXPLOSION5
        else:
            self.timer_explosion = -1

    def draw(self, surface):
        if self.img is not None:
            surface.blit(pygame.transform.scale(self.img,
                (self.support.get_width() * 0.8, self.support.get_height() * 0.8) ), (self.x, self.y))

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()

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
        return self.y + self.img.get_height() >= 0  and self.y <= height

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
        self.shield_img = None
        self.timer_explosion = 0


    def draw(self, surface):
        "draw item"
        surface.blit(self.img, (self. x, self.y))
        if self.shield_img is not None:
            surface.blit(self.shield_img, (self.x - self.get_width() / 2, self.y - 15))

        percentage_life = self.lifebar / self.maxlife
        pygame.draw.line(surface, RED, (self.x*1.01, self.y + self.get_height() + 5),
         (self.x + 0.95*self.get_width()*percentage_life,self.y + self.get_height() + 5), width=2)
        for laser in self.lasers:
            laser.draw(surface)

    def touched(self, damage):
        "is touched, return True if destroyed "
        self.lifebar -= damage
        explosion = Explosion(self.x, self.y, self)
        LIST_EXPLOSION.append(explosion)
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

    def __init__(self, x, y, img):
        super().__init__(x, y, 100)
        self.img = img
        self.width = self.get_width()
        self.height = self.get_height()
        self.img_laser = BASIC_LASER_PLAYER
        self.mask       = pygame.mask.from_surface(self.img)
        self.damage     = 7
        self.shield_cooldown = None
        self.shield_cooldown_text = None


    def shoot(self):
        "shoot"
        laser = Laser(self.x + self.width/2 - self.img_laser.get_width()/2, self.y - self.height/2, None, self.img_laser)
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
                    if other.touched(self.damage):     #todo mettre les degats dans le jeu et factoriser
                        other.destroy()
                        others.remove(other)
                    try:
                        self.lasers.remove(laser)
                    except:
                        print("laser not in list anymore but still removing")
                    on_screen = False
            if on_screen and not laser.off_screen(height):
                self.lasers.remove(laser)

    def handle_shield(self):
        "when shield cooldown != None"
        now = pygame.time.get_ticks()
        time_elapsed = now - self.shield_cooldown
        if time_elapsed > 985:
            self.shield_cooldown_text = (self.shield_cooldown_text - time_elapsed)
            self.shield_cooldown = pygame.time.get_ticks()

        if  self.shield_cooldown_text < 100:
            self.shield_cooldown = None
            self.shield_img = None
            self.shield_cooldown_text = None




class Ennemy(Shooter):
    "class of the ennemy"


    def __init__(self, x, y, width, height, maxlife, cooldown, vel, vel_laser, damage):
        super().__init__(x, y, maxlife)
        self.width      = width
        self.height     = height
        self.vel = vel
        self.damage = damage
        self.vel_laser = vel_laser
        self.last = pygame.time.get_ticks()
        self.cooldown = cooldown

    def move(self):
        "move the item, velocity can also change the direction + or -"
        self.y += self.vel
    
    def move_lasers(self,player, height):
        "move lasers and check if collision with player"
        for laser in self.lasers:
            laser.move(self.vel_laser)
            if not laser.off_screen(height): #fixer le nom aussi ici
                self.lasers.remove(laser)
            if laser.collision(player):
                if player.shield_cooldown != None:
                    player.shield_cooldown -= 300 * self.damage
                else:
                    player.touched(self.damage)
                self.lasers.remove(laser)

    def came_on_screen(self):
        "return true if already on scren"
        return self.y + self.img.get_height() > 0

    def not_off_screen(self, height):
        "check if item isn't off the screen"
        return self.y <= height

    def shoot(self):
        "shoot"
        if random.randrange(1, self.cooldown) == 20:
            laser = Laser(self.x + self.width/2- self.img_laser.get_width()/2,
             self.y + self.height*0.8, None, self.img_laser)
            self.lasers.append(laser)

    def collision(self, other):
        "collision"
        return collide(self, other)
    
    def destroy(self):
        self.lasers = []

class Little_Ennemy(Ennemy):
    COLOR_MAP = {
                "red": (IMG_ENN_LITTLE_RED, RED_LASER),
                "green": (IMG_ENN_LITTLE_GREEN, GREEN_LASER),
                "blue": (IMG_ENN_LITTLE_BLUE, BLUE_LASER)
                }
    def __init__(self, x, y, color):
        img, img_laser = self.COLOR_MAP[color]
        height = img.get_height()
        width = img.get_width()
        super().__init__(x, y, width, height, 15, 500, VELOCITY_BOT * 10, VELOCITY_BOT * 25, 10)
        self.img = img
        self.img_laser = img_laser
        self.mask       = pygame.mask.from_surface(self.img)

class Lit_Med(Ennemy):
    COLOR_MAP = {
                "red": (IMG_ENN_LIT_MED_RED, RED_LITTLE_BEAM_LASER),
                "green": (IMG_ENN_LIT_MED_GREEN, GREEN_LITTLE_BEAM_LASER),
                "blue": (IMG_ENN_LIT_MED_BLUE, BLUE_LITTLE_BEAM_LASER)
                }
    def __init__(self, x, y, color):
        img, img_laser = self.COLOR_MAP[color]
        height = img.get_height()
        width = img.get_width()
        super().__init__(x, y, width, height, 40, 400, VELOCITY_BOT * 5, VELOCITY_BOT * 45, 15)     #mettre en lien avec FPS
        self.img = img
        self.img_laser = img_laser
        self.mask       = pygame.mask.from_surface(self.img)

class Medium(Ennemy):
    COLOR_MAP = {
                "red": (IMG_ENN_MEDIUM_RED, BIG_ORB_RED),
                "green": (IMG_ENN_MEDIUM_GREEN, BIG_ORB_GREEN),
                "blue": (IMG_ENN_MEDIUM_BLUE, BIG_ORB_BLUE)
                }
    def __init__(self, x, y, color):
        img, img_laser = self.COLOR_MAP[color]
        height = img.get_height()
        width = img.get_width()
        super().__init__(x, y, width, height, 100, 400, VELOCITY_BOT * 3, VELOCITY_BOT * 80, 25)
        self.img = img
        self.img_laser = img_laser
        self.mask       = pygame.mask.from_surface(self.img)

class Big(Ennemy):
    COLOR_MAP = {
                "red": (IMG_ENN_BIG_RED, RED_SPEAR_LASER),
                "green": (IMG_ENN_BIG_GREEN, GREEN_SPEAR_LASER),
                "blue": (IMG_ENN_BIG_BLUE, BLUE_SPEAR_LASER)
                }
    def __init__(self, x, y, color):
        img, img_laser = self.COLOR_MAP[color]
        height = img.get_height()
        width = img.get_width()
        super().__init__(x, y, width, height, 150, 400, VELOCITY_BOT * 2, VELOCITY_BOT * 240, 30)
        self.img = img
        self.img_laser = img_laser
        self.mask       = pygame.mask.from_surface(self.img)

class Huge(Ennemy):
    COLOR_MAP = {
                "red": (IMG_ENN_HUGE_RED, HUGE_LASER),
                "green": (IMG_ENN_HUGE_GREEN, HUGE_LASER),
                "blue": (IMG_ENN_HUGE_BLUE, HUGE_LASER)
                }
    def __init__(self, x, y, color):
        img, img_laser = self.COLOR_MAP[color]
        height = img.get_height()
        width = img.get_width()
        super().__init__(x, y, width, height, 500, 350, VELOCITY_BOT / 2, VELOCITY_BOT * 90, 60)    #400
        self.img = img
        self.img_laser = img_laser
        self.mask       = pygame.mask.from_surface(self.img)
    

    def shoot(self):
        "shoot"
        if random.randrange(1, self.cooldown) == 20:
            laser1 = Laser(self.x + self.width/2 - self.img_laser.get_width(),
             self.y + self.height*0.8, None, self.img_laser)

            laser2 = Laser(self.x + self.width/2,
             self.y + self.height*0.8, None, self.img_laser)

            self.lasers.append(laser1)
            self.lasers.append(laser2)
    


class Item():
    "def class of items"

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.last = pygame.time.get_ticks()
        


    def draw(self, surface):
        "draw item"
        now = pygame.time.get_ticks()
        if now - self.last >= 1000:
            surface.blit(self.img, (self. x, self.y))
            if now - self.last >= 2000:
                self.last = now

    def collision(self, other):
        "collision"
        return collide(self, other)

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()

class Item_Health(Item):
    def __init__(self, x, y):
        super().__init__(x, y, ITEM_HEALTH)

    def effect(self, player):
        player.lifebar = player.maxlife

class Item_Shield(Item):
    def __init__(self, x, y):
        super().__init__(x, y, ITEM_SHIELD)

    def effect(self, player):
        player.shield_img = pygame.transform.scale(SHIELD_EFFECT, (player.height* 1.2, player.height * 1.3))
        player.shield_cooldown = pygame.time.get_ticks()
        player.shield_cooldown_text = 30000
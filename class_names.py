# pylint: disable=no-member
"""
File for class
"""

import pygame

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

    def __init__(self, x, y,img, img_laser, maxlife):
        self.x = x
        self.y = y
        self.img = img
        self.lasers = []
        self.img_laser = img_laser
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
        super().__init__(x, y, img, img_laser, 100)
        self.width      = width #todo
        self.height     = height
        self.mask       = pygame.mask.from_surface(self.img)


    def shoot(self):
        "shoot"
        laser = Laser(self.x - self.width/2, self.y - self.height, None, self.img_laser)
        self.lasers.append(laser)

    def collision(self, other):
        "collision"
        return collide(self, other)

    def move(self, keys, vel, size):
        "move the player"
        if keys[pygame.K_LEFT] and self.x > 0:    #Left
            self.x -= vel
        if keys[pygame.K_RIGHT] and self.x + self.width < size[0]:    #Right
            self.x += vel
        if keys[pygame.K_UP] and self.y > 0:    #Top
            self.y -= vel
        if keys[pygame.K_DOWN] and self.y + self.height < size[1]:    #Left
            self.y += vel


    def move_lasers(self, velocity, others, height):
        """move lasers of the shooter, check if collision with others, can
        change the direction with sign of velocity"""
        for laser in self.lasers:
            laser.move(velocity)
            on_screen = True #trouver meilleur moyen ?
            for other in others:
                if laser.collision(other):
                    if other.destroyed(3):        #todo mettre les degats dans le jeu
                        others.remove(other)
                    self.lasers.remove(laser)
                    on_screen = False
            if not laser.off_screen(height) and on_screen:
                self.lasers.remove(laser)


class Ennemy(Shooter):
    "class of the ennemy"

    def __init__(self, x, y, width, height, img, img_laser, maxlife):
        super().__init__(x, y, img, img_laser, maxlife)
        self.width      = width
        self.height     = height
        self.mask       = pygame.mask.from_surface(self.img)


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

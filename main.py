# pylint: disable=no-member
""""
Space invaders
"""""
import os
import random
import pygame
import class_names as fclass
pygame.font.init()

#TOdo: transparent color for the menu

# Variables globales
FPS = 120

VELOCITY_PLAYER             = 20
VELOCITY_BOT                = 1
MAX_LASER_PLAYER            = 15
VELOCITY_LASER_PLAYER       = 9
LASER_SIZE = LASER_WIDTH, LASER_HEIGHT = 18,6


pygame.display.set_caption("Space Invaders")

WHITE   = (255, 255, 255)
GREY    = (125, 125, 125)
LIGHT_GREY = (175, 175, 175)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

FONT_MENU_WELCOME = pygame.font.SysFont("comicsans", 120)
FONT_MENU_START = pygame.font.SysFont("comicsans", 55)

MAIN_WIN_SIZE = WIDTH, HEIGHT = 1200, 800
MAIN_WIN = pygame.display.set_mode(MAIN_WIN_SIZE)

LIST_DIFFICULTY = ["Easy", "Medium", "Hard"]
DIFFICULTY_NUMBER = 0
text_menu_welcome       = FONT_MENU_WELCOME.render("Space Invaders Retro", 1, LIGHT_GREY)
text_menu_start_game    = FONT_MENU_START.render("Start the game", 1, GREY)
text_menu_difficulty    = FONT_MENU_START.render(
                            f"Difficulty: {LIST_DIFFICULTY[DIFFICULTY_NUMBER]}", 1, GREY)
text_menu_leaderboard   = FONT_MENU_START.render("Leaderboard", 1, GREY)


IMG_MENU_BACKGROUND = pygame.image.load(
    os.path.join('Assets', 'parallax-space-backgound.png'))
IMG_GAME_BACKGROUND = pygame.image.load(
    os.path.join('Assets', 'background-black.png'))
IMG_SPACESHIP_DEFAULT = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))

IMG_ENNEMY_SPACESHIP_YELLOW = pygame.image.load(
    os.path.join('Assets', 'pixel_ship_yellow.png')) #pygame.transform.scale()


RED_LASER = pygame.image.load(os.path.join("Assets", "pixel_laser_red.png"))

IMG_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    IMG_SPACESHIP_DEFAULT, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)

LVL_INIT = True

class LinkedText():
    "Class to link text for a menu"

    def __init__(self, x, y, next_text, prev_text):
        self.x = x
        self.y = y
        self.next_text = next_text
        self.prev_text = prev_text


    def draw(self, surface, text):
        "draw the text with line or not if selected"
        if self == MENU_SELECTED:
            new_size = (text.get_width() *1.8, text.get_height()*1.8)
            new_text = pygame.transform.scale(text, new_size)
            surface.blit(new_text, (self.x - new_text.get_width()/2,
                     self.y - new_text.get_height()/2))

            start_pos   = (self.x - new_text.get_width()/2, self.y + new_text.get_height() /2 )
            end_pos     = (self.x + new_text.get_width()/2, self.y + new_text.get_height() /2 )
            pygame.draw.line(surface, GREY,
                             start_pos, end_pos, width = int(text.get_height() * 0.08))

        else:
            surface.blit(text, (self.x - text.get_width()/2,
                     self.y - text.get_height()/2))

    def useless(self):
        "nothing"
        pass




start_game  = LinkedText(WIDTH /2, HEIGHT /2, None, None)
difficulty  = LinkedText(WIDTH /2, HEIGHT /1.5, None, start_game)
leaderboard = LinkedText(WIDTH /2, HEIGHT / 1.3, start_game, difficulty)
difficulty.next_text = leaderboard
start_game.next_text, start_game.prev_text = difficulty, leaderboard
MENU_SELECTED = start_game


player = fclass.Player((WIDTH- SPACESHIP_WIDTH)/2, HEIGHT * 0.75,
                 SPACESHIP_WIDTH, SPACESHIP_HEIGHT, IMG_SPACESHIP, RED_LASER)

def draw_menu(text_blink, text_scroll, surface):
    "draw the start menu, text_scroll can be up, down or none"

    surface.blit(pygame.transform.scale(IMG_MENU_BACKGROUND, MAIN_WIN_SIZE), (0,0))

    text_blink = (text_blink + 1) % 100
    if text_blink <= 50 :
        surface.blit(text_menu_welcome,((WIDTH - text_menu_welcome.get_width())/2,
                    (HEIGHT/3 - text_menu_welcome.get_height())/2))

    start_game.draw(surface, text_menu_start_game)
    difficulty.draw(surface, text_menu_difficulty)
    leaderboard.draw(surface, text_menu_leaderboard)
    global MENU_SELECTED
    if text_scroll == "DOWN":
        MENU_SELECTED = MENU_SELECTED.next_text
        text_scroll = None

    elif text_scroll == "UP":
        MENU_SELECTED = MENU_SELECTED.prev_text
        text_scroll = None

    pygame.display.update()
    return text_blink, text_scroll

def draw_game(ennemies, surface):
    "Draw the game"
    surface.blit(pygame.transform.scale(IMG_GAME_BACKGROUND, MAIN_WIN_SIZE), (0,0))
    for ennemy in ennemies:
        ennemy.draw(MAIN_WIN)
    player.draw(MAIN_WIN)
    pygame.display.update()

def wave_ennemies(level):
    "Spawn a wave of ennemies depending of the level"
    nb_ennemies = 4
    list_ennemies = []
    abscisse = 50
    for _ in range(nb_ennemies):

        ennemy = fclass.Ennemy(abscisse , 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, IMG_ENNEMY_SPACESHIP_YELLOW, RED_LASER)
        print(f"x = {ennemy.x}, y= {ennemy.y}")
        list_ennemies.append(ennemy)
        abscisse += 250
    return list_ennemies

def init_lvl():
    "Init a lvl: spawn ennemies, return the wave and update HUD"
    ennemies = wave_ennemies(1)
    print("les ennemies dans init:",len(ennemies))
    return ennemies, False

def move_ennemies(ennemies):
    "move all ennemies and their lasers"
    for ennemy in ennemies:
        ennemy.move(VELOCITY_BOT)
        ennemy.move_lasers(player, VELOCITY_BOT, HEIGHT)
        if ennemy.collision(player):
            ennemies.remove(ennemy)
        elif not ennemy.not_off_screen(HEIGHT): #todo enlever ces doubles negations
            ennemies.remove(ennemy)

def main():
    "main loop"
    clock = pygame.time.Clock()
    text_blink = 0
    text_scroll = None
    global DIFFICULTY_NUMBER
    global text_menu_difficulty
    app_run  = True
    run_menu = True
    run_game = False

    while app_run:

        while run_menu:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_menu, app_run = False, False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        text_scroll = "UP"
                        text_blink, text_scroll = draw_menu(text_blink - 1, text_scroll, MAIN_WIN)

                    if event.key == pygame.K_DOWN:
                        text_scroll = "DOWN"
                        text_blink, text_scroll = draw_menu(text_blink - 1, text_scroll, MAIN_WIN)

                    if event.key == pygame.K_RIGHT and MENU_SELECTED == difficulty:
                        DIFFICULTY_NUMBER = (DIFFICULTY_NUMBER + 1 ) %3
                        text_menu_difficulty = FONT_MENU_START.render(
                                    f"Difficulty: {LIST_DIFFICULTY[DIFFICULTY_NUMBER]}", 1, GREY)

                    if event.key == pygame.K_LEFT and MENU_SELECTED == difficulty:
                        DIFFICULTY_NUMBER = (DIFFICULTY_NUMBER - 1 ) %3
                        text_menu_difficulty = FONT_MENU_START.render(
                                    f"Difficulty: {LIST_DIFFICULTY[DIFFICULTY_NUMBER]}", 1, GREY)



                    if event.key == pygame.K_RETURN and MENU_SELECTED == start_game:
                        run_menu = False
                        run_game = True
            text_blink, text_scroll = draw_menu(text_blink, text_scroll, MAIN_WIN)

        while run_game:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game, app_run = False, False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(player.lasers) < MAX_LASER_PLAYER:
                        player.shoot()

            global LVL_INIT
            if LVL_INIT:
                ennemies, LVL_INIT = init_lvl()
            keys = pygame.key.get_pressed()
            player.move(keys, VELOCITY_PLAYER, MAIN_WIN_SIZE)
            move_ennemies(ennemies)
            for ennemy in ennemies:
                if random.randrange(0, 2*60) == 1:
                    ennemy.shoot()
            player.move_lasers(-VELOCITY_LASER_PLAYER, ennemies, HEIGHT)


            draw_game(ennemies, MAIN_WIN)

    pygame.quit()



if __name__ == "__main__":
    main()

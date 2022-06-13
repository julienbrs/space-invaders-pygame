# pylint: disable=no-member
""""
Space invaders
"""""
import os
import random
import pygame
import math
import class_names as fclass
pygame.font.init()
import flevel
#TOdo: transparent color for the menu

# Variables globales
FPS = 90

VELOCITY_PLAYER             = 10
VELOCITY_BOT                = 0.03
MAX_LASER_PLAYER            = 15
VELOCITY_LASER_PLAYER       = 9
LASER_SIZE = LASER_WIDTH, LASER_HEIGHT = 18,6

CURRENT_LEVEL   = 1
LIFE_LEFT       = 3
MAX_LEVEL       = 25
LIST_LEVEL      = flevel.create_list_level(MAX_LEVEL)
pygame.display.set_caption("Space Invaders")

WHITE   = (255, 255, 255)
GREY    = (125, 125, 125)
LIGHT_GREY = (175, 175, 175)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 45, 78

FONT_MENU_WELCOME = pygame.font.SysFont("comicsans", 120)
FONT_MENU_START = pygame.font.SysFont("comicsans", 55)
FONT_HUD        = pygame.font.SysFont("comicsans", 55)

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
    os.path.join('Assets', 'background','space_background.png'))

IMG_ENNEMY_SPACESHIP_YELLOW = pygame.image.load(
    os.path.join('Assets', 'pixel_ship_yellow.png')) #pygame.transform.scale()


RED_LASER = pygame.image.load(os.path.join("Assets", "pixel_laser_red.png"))

IMG_PLAYER = IMG_PLAYER_CENTER1 = pygame.transform.scale(pygame.image.load(os.path.join
    ('Assets', 'player', 'center1.png')),(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

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
                 SPACESHIP_WIDTH, SPACESHIP_HEIGHT, IMG_PLAYER, RED_LASER)

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

    #Draw HUD
    text_hud_life       = FONT_HUD.render(f"Life = {LIFE_LEFT}", 1, LIGHT_GREY)
    text_hud_lvl        = FONT_HUD.render(f"Level = {CURRENT_LEVEL}", 1, LIGHT_GREY)

    surface.blit(text_hud_life, (WIDTH * 0.85, 50))
    surface.blit(text_hud_lvl, (WIDTH * 0.85, 110))

    for ennemy in ennemies:
        ennemy.draw(MAIN_WIN)
    player.draw(MAIN_WIN)
    pygame.display.update()

def draw_lose(surface, text_blink):
    "Draw the losing screen"
    surface.blit(pygame.transform.scale(IMG_GAME_BACKGROUND, MAIN_WIN_SIZE), (0,0))

    text_lose       = FONT_MENU_WELCOME.render("U LOST", 1, LIGHT_GREY)
    text_press      = FONT_MENU_WELCOME.render("Press Enter", 1, LIGHT_GREY)

    text_blink = (text_blink + 1) % 100
    if text_blink <= 50 :
        surface.blit(text_press, (WIDTH/2 - text_press.get_width()/2,
                HEIGHT/2 - text_press.get_height()/2 + 1.35*text_lose.get_height()))

    surface.blit(text_lose, (WIDTH/2 - text_lose.get_width()/2,
                HEIGHT/2 - text_lose.get_height()/2))
    pygame.display.update()
    return text_blink

def wave_ennemies(nb_level):
    "Spawn a wave of ennemies depending of the level"
    global LIST_LEVEL
    stage_level = nb_level // 5 + 1
    list_ennemies = LIST_LEVEL[nb_level]
    random.shuffle(list_ennemies)
    ennemies = []
    number = len(list_ennemies)
    abscisse = random.randrange(WIDTH*0.1, WIDTH*0.3)       #trouver moyen de fix ça
    ordonnee = -50
    ennemies_on_line = 0
    for i in range(number):
        if WIDTH - abscisse < 40 or ennemies_on_line > 4 + math.floor(nb_level*1.5):
            ennemies_on_line = 0
            abscisse = random.randrange(WIDTH*0.05, WIDTH*0.15)
            ordonnee -= random.randrange(50, 350 - stage_level * 50)
        ord_rel = random.randrange(0, 80)
        current = list_ennemies[i]
        if current == "little":
            ennemy = fclass.Little_Ennemy(abscisse , ordonnee + ord_rel, 10,
            VELOCITY_BOT * 10, random.choice(["red", "blue", "green"]))
        elif current == "lit_med":
            ennemy = fclass.Lit_Med(abscisse , ordonnee + ord_rel, SPACESHIP_WIDTH,
            SPACESHIP_HEIGHT, 15, VELOCITY_BOT * 5, random.choice(["red", "blue", "green"]))
        elif current == "medium":
            ennemy = fclass.Medium(abscisse , ordonnee + ord_rel, SPACESHIP_WIDTH,
            SPACESHIP_HEIGHT, 30, VELOCITY_BOT * 3, random.choice(["red", "blue", "green"]))
        elif current == "big":
            ennemy = fclass.Big(abscisse , ordonnee + ord_rel, SPACESHIP_WIDTH,
            SPACESHIP_HEIGHT, 40,VELOCITY_BOT * 2, random.choice(["red", "blue", "green"]))
        elif current == "huge":
            ennemy = fclass.Huge(abscisse , ordonnee + ord_rel, SPACESHIP_WIDTH,
            SPACESHIP_HEIGHT, 100, VELOCITY_BOT / 2, random.choice(["red", "blue", "green"]))
        ennemies.append(ennemy)
        ennemies_on_line += 1
        abscisse += ennemy.get_width() + random.randrange(0, math.floor((WIDTH - abscisse) / 3))

    return ennemies

def init_lvl():
    "Init a lvl: spawn ennemies, return the wave and update HUD"
    ennemies = wave_ennemies(CURRENT_LEVEL - 1)
    return ennemies, False


def move_ennemies(ennemies):
    "move all ennemies and their lasers"
    for ennemy in ennemies:
        ennemy.move()
        ennemy.move_lasers(player, VELOCITY_BOT, HEIGHT)
        if ennemy.collision(player):
            player.lifebar -= 50
            ennemies.remove(ennemy)
        elif not ennemy.not_off_screen(HEIGHT): #todo enlever ces doubles negations
            ennemies.remove(ennemy)
            global LIFE_LEFT
            LIFE_LEFT -= 1


def main():
    "main loop"
    clock = pygame.time.Clock()
    text_blink = 0
    blink_player = 0
    text_scroll = None
    LEVEL_FINISHED = False
    global DIFFICULTY_NUMBER
    global LIFE_LEFT

    global CURRENT_LEVEL
    global player

    global text_menu_difficulty
    app_run  = True
    run_menu = True
    run_game = False
    run_transi = False

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
                LEVEL_FINISHED = False
                ennemies, LVL_INIT = init_lvl()
            keys = pygame.key.get_pressed()

            if len(ennemies) == 0:          #Mettre dans fonction
                if not LEVEL_FINISHED:
                    last = pygame.time.get_ticks()
                LEVEL_FINISHED = True
                now = pygame.time.get_ticks()
                if now - last >= 4000:
                    LEVEL_FINISHED  = True
                    LVL_INIT        = True
                    CURRENT_LEVEL   += 1

            blink_player = player.move(keys, VELOCITY_PLAYER, MAIN_WIN_SIZE, blink_player)
            move_ennemies(ennemies)
            for ennemy in ennemies:
                ennemy.shoot()
            player.move_lasers(-VELOCITY_LASER_PLAYER, ennemies, HEIGHT)

            if player.lifebar <= 0:
                player.lifebar = player.maxlife
                LIFE_LEFT -= 1
            draw_game(ennemies, MAIN_WIN)
            if LIFE_LEFT <= 0:
                CURRENT_LEVEL   = 1
                LIFE_LEFT       = 3
                player = fclass.Player((WIDTH- SPACESHIP_WIDTH)/2, HEIGHT * 0.75,
                 SPACESHIP_WIDTH, SPACESHIP_HEIGHT, IMG_PLAYER, RED_LASER)
                for ennemy in ennemies:
                    ennemy.destroy()
                ennemies = None
                LVL_INIT = True
                run_game = False
                run_transi = True

        while run_transi:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_menu, app_run, run_transi = False, False, False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        run_menu = True
                        run_transi = False
            text_blink = draw_lose(MAIN_WIN, text_blink)

    pygame.quit()



if __name__ == "__main__":
    main()

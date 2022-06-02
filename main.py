# pylint: disable=no-member
""""
Space invaders
"""""
import os
import pygame
pygame.font.init()

#TOdo: transparent color for the menu


FPS = 80

VELOCITY_PLAYER = 7

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
text_menu_difficulty    = FONT_MENU_START.render(f"Difficulty: {LIST_DIFFICULTY[DIFFICULTY_NUMBER]}", 1, GREY)
text_menu_leaderboard   = FONT_MENU_START.render("Leaderboard", 1, GREY)


IMG_MENU_BACKGROUND = pygame.image.load(
    os.path.join('Assets', 'parallax-space-backgound.png'))
IMG_GAME_BACKGROUND = pygame.image.load(
    os.path.join('Assets', 'background-black.png'))
IMG_SPACESHIP_DEFAULT = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))

IMG_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    IMG_SPACESHIP_DEFAULT, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)



class LinkedText():
    "Class to link text for a menu"

    def __init__(self, x, y, selected, next_text, prev_text):
        self.x = x
        self.y = y
        self.selected = selected
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
            pygame.draw.line(MAIN_WIN, GREY, start_pos, end_pos, width = int(text.get_height() * 0.08))

        else:
            surface.blit(text, (self.x - text.get_width()/2,
                     self.y - text.get_height()/2))

class Player():

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
    
    def draw(self):
        MAIN_WIN.blit(self.img, (self.x, self.y))

start_game  = LinkedText(WIDTH /2, HEIGHT /2, True, None, None)
difficulty  = LinkedText(WIDTH /2, HEIGHT /1.5, False, None, start_game)
leaderboard = LinkedText(WIDTH /2, HEIGHT / 1.3, False, start_game, difficulty)
difficulty.next_text = leaderboard
start_game.next_text, start_game.prev_text = difficulty, leaderboard
MENU_SELECTED = start_game


player = Player((WIDTH- SPACESHIP_WIDTH)/2, HEIGHT * 0.75, IMG_SPACESHIP)

def draw_menu(text_blink, text_scroll):
    "draw the start menu, text_scroll can be up, down or none"

    MAIN_WIN.blit(pygame.transform.scale(IMG_MENU_BACKGROUND, MAIN_WIN_SIZE), (0,0))

    text_blink = (text_blink + 1) % 100
    if text_blink <= 50 :
        MAIN_WIN.blit(text_menu_welcome,((WIDTH - text_menu_welcome.get_width())/2,
                    (HEIGHT/3 - text_menu_welcome.get_height())/2))

    start_game.draw(MAIN_WIN, text_menu_start_game)
    difficulty.draw(MAIN_WIN, text_menu_difficulty)
    leaderboard.draw(MAIN_WIN, text_menu_leaderboard)
    global MENU_SELECTED
    if text_scroll == "DOWN":
        MENU_SELECTED = MENU_SELECTED.next_text
        text_scroll = None

    elif text_scroll == "UP":
        MENU_SELECTED = MENU_SELECTED.prev_text
        text_scroll = None

    pygame.display.update()
    return text_blink, text_scroll

def draw_game():
    "Draw the game"
    MAIN_WIN.blit(pygame.transform.scale(IMG_GAME_BACKGROUND, MAIN_WIN_SIZE), (0,0))

    player.draw()
    pygame.display.update()

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
                        text_blink, text_scroll = draw_menu(text_blink - 1, text_scroll)

                    if event.key == pygame.K_DOWN:
                        text_scroll = "DOWN"
                        text_blink, text_scroll = draw_menu(text_blink - 1, text_scroll)

                    if event.key == pygame.K_RIGHT and MENU_SELECTED == difficulty:
                        DIFFICULTY_NUMBER = (DIFFICULTY_NUMBER + 1 ) %3
                        text_menu_difficulty = FONT_MENU_START.render(f"Difficulty: {LIST_DIFFICULTY[DIFFICULTY_NUMBER]}", 1, GREY)

                    if event.key == pygame.K_LEFT and MENU_SELECTED == difficulty:
                        DIFFICULTY_NUMBER = (DIFFICULTY_NUMBER - 1 ) %3
                        text_menu_difficulty = FONT_MENU_START.render(f"Difficulty: {LIST_DIFFICULTY[DIFFICULTY_NUMBER]}", 1, GREY)



                    if event.key == pygame.K_RETURN and MENU_SELECTED == start_game:
                        run_menu = False
                        run_game = True
            text_blink, text_scroll = draw_menu(text_blink, text_scroll)

        while run_game:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game, app_run = False, False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x > 0:    #Left
                player.x -= VELOCITY_PLAYER
            if keys[pygame.K_RIGHT] and player.x < WIDTH:    #Right
                player.x += VELOCITY_PLAYER
            if keys[pygame.K_UP] and player.y > 0:    #Top
                player.y -= VELOCITY_PLAYER
            if keys[pygame.K_DOWN] and player.y < HEIGHT:    #Left
                player.y += VELOCITY_PLAYER



            draw_game()

    pygame.quit()



if __name__ == "__main__":
    main()

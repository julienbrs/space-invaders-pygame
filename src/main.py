#!/usr/bin/env python3

"""
Space invaders
"""
import os
import random
import math
import pygame
import class_names as fclass
import flevel


pygame.font.init()
pygame.mixer.init()

# TOdo: transparent color for the menu

# CONSTANTS
FPS = 90

VELOCITY_PLAYER = 8
VELOCITY_BOT = 0.05
MAX_LASER_PLAYER = 8
VELOCITY_LASER_PLAYER = 9
LASER_SIZE = LASER_WIDTH, LASER_HEIGHT = 18, 6

CURRENT_LEVEL = 1
LIFE_LEFT = 3
MAX_LEVEL = 25
LIST_LEVEL = flevel.create_list_level(MAX_LEVEL)
pygame.display.set_caption("Space Invaders")

WHITE = (255, 255, 255)
GREY = (125, 125, 125)
LIGHT_GREY = (175, 175, 175)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 45, 78

FONT_MENU_WELCOME = pygame.font.SysFont("comicsans", 120)
FONT_MENU_START = pygame.font.SysFont("comicsans", 55)
FONT_HUD = pygame.font.SysFont("comicsans", 40)

MAIN_WIN_SIZE = WIDTH, HEIGHT = 1400, 800
MAIN_WIN = pygame.display.set_mode(MAIN_WIN_SIZE)

LIST_DIFFICULTY = ["Easy", "Medium", "Hard"]
DIFFICULTY_NUMBER = 0

text_menu_welcome = FONT_MENU_WELCOME.render(
    "Space Invaders Retro", 1, LIGHT_GREY)
text_menu_start_game = FONT_MENU_START.render("Start the game", 1, GREY)
TEXT_MENU_DIFFICULTY = FONT_MENU_START.render(
    f"Difficulty: {LIST_DIFFICULTY[DIFFICULTY_NUMBER]}", 1, GREY
)
text_menu_leaderboard = FONT_MENU_START.render("Leaderboard", 1, GREY)


SOUND_SELECT_MENU = pygame.mixer.Sound(
    os.path.join("Assets", "sound_effects", "menu.wav")
)
pygame.mixer.Sound.set_volume(SOUND_SELECT_MENU, 0.3)

# Assets
IMG_MENU_BACKGROUND = pygame.image.load(
    os.path.join("Assets", "parallax-space-backgound.png")
)

IMG_GAME_STAGE1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "background", "stage1.png")),
    (WIDTH, HEIGHT),
)
IMG_GAME_STAGE2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "background", "stage2.png")),
    (WIDTH, HEIGHT),
)
IMG_GAME_STAGE3 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "background", "stage3.png")),
    (WIDTH, HEIGHT),
)
IMG_GAME_STAGE4 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "background", "stage4.png")),
    (WIDTH, HEIGHT),
)
IMG_GAME_STAGE5 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "background", "stage5.png")),
    (WIDTH, HEIGHT),
)
IMG_ENNEMY_SPACESHIP_YELLOW = pygame.image.load(
    os.path.join("Assets", "pixel_ship_yellow.png")
)

IMG_PLAYER = IMG_PLAYER_CENTER1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "player", "center1.png")),
    (SPACESHIP_WIDTH, SPACESHIP_HEIGHT),
)
IMG_GAME_BACKGROUND = IMG_GAME_STAGE1


LVL_INIT = True


class LinkedText:
    "Class to link text for a menu"

    def __init__(self, x, y, next_text, prev_text):
        self.x = x
        self.y = y
        self.next_text = next_text
        self.prev_text = prev_text

    def draw(self, surface, text):
        "draw the text with line or not if selected"
        if self == MENU_SELECTED:
            new_size = (text.get_width() * 1.8, text.get_height() * 1.8)
            new_text = pygame.transform.scale(text, new_size)
            surface.blit(
                new_text,
                (self.x - new_text.get_width() / 2,
                 self.y - new_text.get_height() / 2),
            )

            start_pos = (
                self.x - new_text.get_width() / 2,
                self.y + new_text.get_height() / 2,
            )
            end_pos = (
                self.x + new_text.get_width() / 2,
                self.y + new_text.get_height() / 2,
            )
            pygame.draw.line(
                surface, GREY, start_pos, end_pos, width=int(
                    text.get_height() * 0.08)
            )

        else:
            surface.blit(
                text, (self.x - text.get_width() / 2,
                       self.y - text.get_height() / 2)
            )


start_game = LinkedText(WIDTH / 2, HEIGHT / 2, None, None)
difficulty = LinkedText(WIDTH / 2, HEIGHT / 1.5, None, start_game)
leaderboard = LinkedText(WIDTH / 2, HEIGHT / 1.3, start_game, difficulty)
difficulty.next_text = leaderboard
start_game.next_text, start_game.prev_text = difficulty, leaderboard
MENU_SELECTED = start_game


def draw_menu(text_blink, text_scroll, surface):
    "draw the start menu, text_scroll can be up, down or none"

    surface.blit(pygame.transform.scale(
        IMG_MENU_BACKGROUND, MAIN_WIN_SIZE), (0, 0))

    text_blink = (text_blink + 1) % 100
    if text_blink <= 50:
        surface.blit(
            text_menu_welcome,
            (
                (WIDTH - text_menu_welcome.get_width()) / 2,
                (HEIGHT / 3 - text_menu_welcome.get_height()) / 2,
            ),
        )

    start_game.draw(surface, text_menu_start_game)
    difficulty.draw(surface, TEXT_MENU_DIFFICULTY)
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


def draw_background(surface, img_background, i):
    "Draw the background which is moving vertically in an infinite loop"
    surface.fill((0, 0, 0))
    surface.blit(img_background, (0, i))
    surface.blit(img_background, (0, -HEIGHT + i))
    if i == HEIGHT:
        surface.blit(img_background, (0, HEIGHT - i))
        i = 0
    i += 0.5
    return i


def draw_game(player, ennemies, list_item, surface, img_background, i):
    "Draw the game"
    i = draw_background(surface, img_background, i)

    # Draw HUD
    text_hud_life = FONT_HUD.render(f"Life = {LIFE_LEFT}", 1, WHITE)
    text_hud_lvl = FONT_HUD.render(f"Level = {CURRENT_LEVEL}", 1, WHITE)

    surface.blit(text_hud_life, (WIDTH * 0.98 - text_hud_life.get_width(), 50))
    surface.blit(text_hud_lvl, (WIDTH * 0.98 - text_hud_lvl.get_width(), 100))
    if player.shield_cooldown_text is not None:
        text_hud_shield = FONT_HUD.render(
            f"Shield : {player.shield_cooldown_text // 1000}s", 1, WHITE
        )
        surface.blit(text_hud_shield, (WIDTH * 0.98 - text_hud_shield.get_width(), 200))

    if player.multiple_shoot_cooldown_text is not None:
        text_hud_multiple_shoot = FONT_HUD.render(
            f"Super Shoot : {player.multiple_shoot_cooldown_text // 1000}s",
            1,
            WHITE,
        )
        surface.blit(text_hud_multiple_shoot, (WIDTH * 0.98 - text_hud_multiple_shoot.get_width(), 250))

    for ennemy in ennemies:
        ennemy.draw(MAIN_WIN)

    for item in list_item:
        item.draw(MAIN_WIN)
    player.draw(MAIN_WIN)

    for explosion in fclass.LIST_EXPLOSION:
        explosion.handle(20)
        explosion.draw(MAIN_WIN)
        if explosion.timer_explosion == -1:
            fclass.LIST_EXPLOSION.remove(explosion)

    pygame.display.update()
    return i


def draw_lose(surface, text_blink):
    "Draw the losing screen"
    surface.blit(pygame.transform.scale(
        IMG_GAME_BACKGROUND, MAIN_WIN_SIZE), (0, 0))

    text_lose = FONT_MENU_WELCOME.render("YOU LOST", 1, LIGHT_GREY)
    text_press = FONT_MENU_WELCOME.render("Press Enter", 1, LIGHT_GREY)

    surface.blit(
        text_lose,
        (
            WIDTH / 2 - text_lose.get_width() / 2,
            HEIGHT / 3 - text_lose.get_height() / 2,
        ),
    )

    text_blink = (text_blink + 1) % 100
    if text_blink <= 50:
        surface.blit(
            text_press,
            (
                WIDTH / 2 - text_press.get_width() / 2,
                HEIGHT / 3
                - text_press.get_height() / 2
                + 1.35 * text_lose.get_height(),
            ),
        )
    pygame.display.update()
    return text_blink


def wave_ennemies(nb_level):
    "Spawn a wave of ennemies depending of the level"
    # stage_level = nb_level // 5 + 1
    list_ennemies = LIST_LEVEL[nb_level]
    random.shuffle(list_ennemies)
    ennemies = []
    number = len(list_ennemies)
    # trouver moyen de fix ça
    abscisse = random.randrange(int(WIDTH * 0.1), int(WIDTH * 0.3))
    ordonnee = -50
    ennemies_on_line = 0
    for i in range(number):
        if WIDTH - abscisse < 100 or ennemies_on_line > 7 + math.floor(nb_level * 1.5):
            ennemies_on_line = 0
            abscisse = random.randrange(int(WIDTH * 0.05), int(WIDTH * 0.15))
            ordonnee -= random.randrange(30, 80)
        ord_rel = random.randrange(0, 40)
        current = list_ennemies[i]
        if current == "little":
            ennemy = fclass.Little_Ennemy(
                abscisse, ordonnee +
                ord_rel, random.choice(["red", "blue", "green"])
            )
        elif current == "lit_med":
            ennemy = fclass.Lit_Med(
                abscisse, ordonnee +
                ord_rel, random.choice(["red", "blue", "green"])
            )
        elif current == "medium":
            ennemy = fclass.Medium(
                abscisse, ordonnee +
                ord_rel, random.choice(["red", "blue", "green"])
            )
        elif current == "big":
            ennemy = fclass.Big(
                abscisse, ordonnee +
                ord_rel, random.choice(["red", "blue", "green"])
            )
        elif current == "huge":
            ennemy = fclass.Huge(
                abscisse, ordonnee +
                ord_rel, random.choice(["red", "blue", "green"])
            )
        ennemies.append(ennemy)
        ennemies_on_line += 1
        abscisse += ennemy.get_width() + random.randrange(
            0, math.floor((WIDTH - abscisse) / 3)
        )
    return ennemies


def init_lvl():
    "Init a lvl: spawn ennemies, return the wave and update HUD"
    ennemies = wave_ennemies(CURRENT_LEVEL - 1)
    return ennemies, False


def move_ennemies(player, ennemies):
    "move all ennemies and their lasers"
    for ennemy in ennemies:
        ennemy.move()
        ennemy.move_lasers(player, HEIGHT, WIDTH)
        if ennemy.collision(player):
            if player.shield_cooldown is not None:
                player.shield_cooldown = None  # grouper dans fonction
                player.shield_img = None
                player.shield_cooldown_text = None
            else:
                pygame.mixer.Sound.play(fclass.SOUND_LASER_PLAYER)
                explosion = fclass.Explosion(player.x, player.y, player)
                fclass.LIST_EXPLOSION.append(explosion)
                player.lifebar -= 100
            pygame.mixer.Sound.play(fclass.SOUND_ENNEMY_EXPLOSION)
            explosion2 = fclass.Explosion(ennemy.x, ennemy.y, ennemy)
            fclass.LIST_EXPLOSION.append(explosion2)
            ennemies.remove(ennemy)
        # todo enlever ces doubles negations
        elif not ennemy.not_off_screen(HEIGHT):
            ennemies.remove(ennemy)
            global LIFE_LEFT
            LIFE_LEFT -= 1


def spawn_item(level):
    "Spawn a bonus item"
    list_item_spawned = []
    list_item_possible = [
        spawn_item_health,
        spawn_item_shield,
        spawn_item_multiple_shoot,
    ]
    nb_item_max = random.randrange((level // 5) + 1, 2 * (level // 5) + 6)

    for _ in range(nb_item_max):
        x = random.randrange(int(WIDTH * 0.1), int(WIDTH * 0.9))
        y = random.randrange(int(HEIGHT * 0.2), int(HEIGHT * 0.9))
        item = random.choice(list_item_possible)(x, y)
        list_item_spawned.append(item)
    return list_item_spawned


def spawn_item_health(x, y):
    "Spawn health bonus at coordinates (x,y)"
    item = fclass.Item_Health(x, y)
    return item


def spawn_item_shield(x, y):
    "Spawn shield bonus at coordinates (x,y)"
    item = fclass.Item_Shield(x, y)
    return item


def spawn_item_multiple_shoot(x, y):
    "Spawn multiple shoot bonus at coordinates (x,y)"
    item = fclass.Item_Multiple_Shoot(x, y)
    return item


def init_game_stage(level, old_background):
    "Update stage design and music"

    if level == 1:
        pygame.mixer.music.unload()
        pygame.mixer.music.load(
            os.path.join("Assets", "sound_effects", "music", "stage1.ogg")
        )
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        img_background = IMG_GAME_STAGE1
    elif level == 6:
        pygame.mixer.music.unload()
        pygame.mixer.music.load(
            os.path.join("Assets", "sound_effects", "music", "stage2.ogg")
        )
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        img_background = IMG_GAME_STAGE2
    elif level == 11:
        pygame.mixer.music.unload()
        pygame.mixer.music.load(
            os.path.join("Assets", "sound_effects", "music", "stage3.ogg")
        )
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        img_background = IMG_GAME_STAGE3
    elif level == 16:
        pygame.mixer.music.unload()
        pygame.mixer.music.load(
            os.path.join("Assets", "sound_effects", "music", "stage4.ogg")
        )
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        img_background = IMG_GAME_STAGE4
    elif level == 21:
        pygame.mixer.music.unload()
        pygame.mixer.music.load(
            os.path.join("Assets", "sound_effects", "music", "stage5.ogg")
        )
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        img_background = IMG_GAME_STAGE5
    else:
        img_background = old_background
    return img_background


def draw_inter_stage(level, surface):
    "Draw the transition between two stages"
    surface.fill((0, 0, 0))
    text_inter_stage = FONT_HUD.render(
        f"Stage {level // 5 + 1}", 1, LIGHT_GREY)

    surface.blit(
        text_inter_stage,
        (
            WIDTH / 2 - text_inter_stage.get_width() / 2,
            HEIGHT / 2 - text_inter_stage.get_height() / 2,
        ),
    )
    pygame.display.update()


def main():
    "main loop"
    clock = pygame.time.Clock()
    text_blink = 0
    blink_player = 0

    text_scroll = None
    level_finished = False

    player = fclass.Player(WIDTH / 2, HEIGHT * 0.9, IMG_PLAYER)
    global DIFFICULTY_NUMBER
    global LIFE_LEFT

    global CURRENT_LEVEL

    global TEXT_MENU_DIFFICULTY
    app_run = True
    run_menu = True
    run_game = False
    run_transi = False
    i = 0
    img_background = IMG_GAME_STAGE1

    init_menu_needed = True
    while app_run:
        while run_menu:
            clock.tick(FPS)

            if init_menu_needed:
                init_menu_needed = False
                pygame.mixer.music.load(
                    os.path.join("Assets", "sound_effects",
                                 "music", "Menu_Screen.ogg")
                )
                pygame.mixer.music.play(-1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_menu, app_run = False, False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        text_scroll = "UP"
                        pygame.mixer.Sound.play(SOUND_SELECT_MENU)
                        text_blink, text_scroll = draw_menu(
                            text_blink - 1, text_scroll, MAIN_WIN
                        )

                    if event.key == pygame.K_DOWN:
                        text_scroll = "DOWN"
                        pygame.mixer.Sound.play(SOUND_SELECT_MENU)
                        text_blink, text_scroll = draw_menu(
                            text_blink - 1, text_scroll, MAIN_WIN
                        )

                    if event.key == pygame.K_RIGHT and MENU_SELECTED == difficulty:
                        pygame.mixer.Sound.play(SOUND_SELECT_MENU)
                        DIFFICULTY_NUMBER = (DIFFICULTY_NUMBER + 1) % 3
                        TEXT_MENU_DIFFICULTY = FONT_MENU_START.render(
                            f"Difficulty: {LIST_DIFFICULTY[DIFFICULTY_NUMBER]}", 1, GREY
                        )

                    if event.key == pygame.K_LEFT and MENU_SELECTED == difficulty:
                        pygame.mixer.Sound.play(SOUND_SELECT_MENU)
                        DIFFICULTY_NUMBER = (DIFFICULTY_NUMBER - 1) % 3
                        TEXT_MENU_DIFFICULTY = FONT_MENU_START.render(
                            f"Difficulty: {LIST_DIFFICULTY[DIFFICULTY_NUMBER]}", 1, GREY
                        )

                    if event.key == pygame.K_RETURN and MENU_SELECTED == start_game:
                        pygame.mixer.Sound.play(SOUND_SELECT_MENU)
                        run_menu = False
                        run_game = True
                        init_menu_needed = True

            text_blink, text_scroll = draw_menu(
                text_blink, text_scroll, MAIN_WIN)

        while run_game:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game, app_run = False, False
                    init_menu_needed = True

                if event.type == pygame.KEYDOWN:
                    if (
                        event.key == pygame.K_SPACE
                        and len(player.lasers) < MAX_LASER_PLAYER
                    ):
                        player.shoot()

            if init_menu_needed:  # todo fusionner avec LVL_INIT ?
                init_menu_needed = False

            global LVL_INIT
            if LVL_INIT:
                img_background = init_game_stage(CURRENT_LEVEL, img_background)
                level_finished = False
                if CURRENT_LEVEL % 5 == 1:
                    draw_inter_stage(CURRENT_LEVEL, MAIN_WIN)
                    pygame.time.delay(4000)
                list_item = spawn_item(CURRENT_LEVEL)
                ennemies, LVL_INIT = init_lvl()
            keys = pygame.key.get_pressed()

            if len(ennemies) == 0:  # Mettre dans fonction
                if not level_finished:
                    last = pygame.time.get_ticks()
                level_finished = True
                now = pygame.time.get_ticks()
                if now - last >= 4000:
                    level_finished = True
                    LVL_INIT = True
                    CURRENT_LEVEL += 1

            blink_player = player.move(
                keys, VELOCITY_PLAYER, MAIN_WIN_SIZE, blink_player
            )  # utiliser classe
            for item in list_item:
                if item.collision(player):  # mettre dans fonction
                    pygame.mixer.Sound.play(fclass.SOUND_POWER_UP)
                    item.effect(player)
                    list_item.remove(item)

            if player.shield_cooldown is not None:
                player.handle_shield()

            if player.multiple_shoot_cooldown is not None:
                player.handle_multiple_shoot()

            move_ennemies(player, ennemies)
            for ennemy in ennemies:
                if ennemy.came_on_screen():
                    ennemy.shoot()

            player.move_lasers(-VELOCITY_LASER_PLAYER, ennemies, HEIGHT, WIDTH)

            if player.lifebar <= 0:
                player.lifebar = player.maxlife
                LIFE_LEFT -= 1
            i = draw_game(player, ennemies, list_item,
                          MAIN_WIN, img_background, i)
            if LIFE_LEFT <= 0:
                CURRENT_LEVEL = 1
                LIFE_LEFT = 3
                player = fclass.Player(WIDTH / 2, HEIGHT * 0.9, IMG_PLAYER)
                for ennemy in ennemies:
                    ennemy.destroy()

                ennemies = None
                LVL_INIT = True
                run_game = False
                run_transi = True
                init_menu_needed = True

        while run_transi:
            if init_menu_needed:
                pygame.mixer.music.unload()
                pygame.mixer.music.load(
                    os.path.join("Assets", "sound_effects",
                                 "music", "defeat.ogg")
                )
                pygame.mixer.music.play(-1)
                init_menu_needed = False

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

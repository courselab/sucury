#!/usr/bin/python3
#
#   Copyright (c) 2023 by Monaco F. J. <monaco@usp.br>
#   Copyright (c) 2023 by Sucury Authors
#
#   This file is part of Sucury.
#
#   Sucury is a derivative work of the code from KhobraPy by Monaco F. J.,
#   distributed under GNU GPL vr3. KnobraPy source code can be found at
#   https://github.com/monacofj/khobrapy. The main changes applied to the
#   original code are listed in the file Changelog.
#
#   Sucury is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
from button import Button
import random
import sys

##
## Game customization.
##

WIDTH, HEIGHT = 800, 800     # Game screen dimensions.

GRID_SIZE = 50               # Square grid size.

HEAD_COLOR      = "#00aa00"  # Color of the snake's head.
DEAD_HEAD_COLOR = "#4b0082"  # Color of the dead snake's head.
TAIL_COLOR      = "#00ff00"  # Color of the snake's tail.
APPLE_COLOR     = "#aa0000"  # Color of the apple.
SCREEN_COLOR    = "#202020"  # Color of the ground.
GRID_COLOR      = "#3c3c3b"  # Color of the grid lines.
SCORE_COLOR     = "#ffffff"  # Color of the scoreboard.
MESSAGE_COLOR   = "#808080"  # Color of the game-over message.

WINDOW_TITLE    = ["KhobraPy - Game", "KhobraPy - Menu"] # Window title.

CLOCK_TICKS     = 7         # How fast the snake moves.

START_POS_PADDING = 3       # Size of padding so that the snake does not start to close to the border.

##
## Game implementation.
##

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BIG_FONT   = pygame.font.Font("assets/font/Ramasuri.ttf", int(WIDTH/8))
SMALL_FONT = pygame.font.Font("assets/font/Ramasuri.ttf", int(WIDTH/20))
COLOR_MENU_FONT = pygame.font.Font("assets/font/GochiHand.ttf", int(WIDTH/20))

pygame.display.set_caption(WINDOW_TITLE[0])
BG = pygame.image.load("assets/Background.jpg")

def main_menu(): #Main Menu Screen
    pygame.display.set_caption(WINDOW_TITLE[1])

    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        MENU_TEXT = BIG_FONT.render("MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, HEIGHT/5))

        
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(WIDTH/2, HEIGHT/2.5), 
                            text_input="PLAY", font=SMALL_FONT, base_color="#d7fcd4", hovering_color="White")
        
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(WIDTH/2, HEIGHT/1.8), 
                            text_input="OPTIONS", font=SMALL_FONT, base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(WIDTH/2, HEIGHT/1.4), 
                            text_input="QUIT", font=SMALL_FONT, base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def options():
    return

## This function is called when the snake dies.

def center_prompt(title, subtitle):

    # Show title and subtitle.

    center_title = BIG_FONT.render(title, True, MESSAGE_COLOR)
    center_title_rect = center_title.get_rect(center=(WIDTH/2, HEIGHT/2))
    SCREEN.blit(center_title, center_title_rect)

    center_subtitle = SMALL_FONT.render(subtitle, True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*2/3))
    SCREEN.blit(center_subtitle, center_subtitle_rect)

    pygame.display.update()

   # Wait for a keypres or a game quit event.

    while ( event := pygame.event.wait() ):
        if event.type == pygame.KEYDOWN:
            break
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.key == pygame.K_q:          # 'Q' quits game
        main_menu()

class Snake:
    def __init__(self):

        # Calculating range of possible start positions for the snake.

        max_x, max_y = (WIDTH/GRID_SIZE)-START_POS_PADDING, (HEIGHT/GRID_SIZE)-START_POS_PADDING
        min_x, min_y = START_POS_PADDING, START_POS_PADDING

        # Dimension of each snake segment times a random position in range.

        self.x, self.y = random.randint(min_x, max_x)*GRID_SIZE, random.randint(min_y, max_y)*GRID_SIZE

        # Initial direction
        # xmov :  -1 left,    0 still,   1 right
        # ymov :  -1 up       0 still,   1 dows

        if self.x > WIDTH/2:    # If the snake starts at the right side of the screen, it goes left.
            self.xmov = -1
            self.ymov = 0
        else:                   # Otherwise, it goes right
            self.xmov = 1
            self.ymov = 0

        # The snake has a head segement,
        self.head = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

        # and a tail (array of segments).
        self.tail = []

        # The snake is born.
        self.alive = True

        # Default snake colors
        self.head_color = HEAD_COLOR
        self.tail_color = TAIL_COLOR

    # This function is called at each loop interation.

    def update(self):
        global apple

        # Check for border crash.
        if self.head.x not in range(0, WIDTH) or self.head.y not in range(0, HEIGHT):
            self.alive = False

        # Check for self-bite.
        for square in self.tail:
            if self.head.x == square.x and self.head.y == square.y:
                self.alive = False

        # In the event of death, reset the game SCREEN.
        if not self.alive:

            # Tell the bad news
            pygame.draw.rect(SCREEN, DEAD_HEAD_COLOR, self.head)
            center_prompt("Game Over", "Press to restart")

            # Respan the head
            max_x, max_y = (WIDTH/GRID_SIZE)-START_POS_PADDING, (HEIGHT/GRID_SIZE)-START_POS_PADDING
            min_x, min_y = START_POS_PADDING, START_POS_PADDING
            self.x, self.y = random.randint(min_x, max_x)*GRID_SIZE, random.randint(min_y, max_y)*GRID_SIZE

            self.head = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

            # Respan the initial tail
            self.tail = []

            if self.x > WIDTH/2:    # If the snake starts at the right side of the screen, it goes left.
                self.xmov = -1
                self.ymov = 0
            else:                   # Otherwise, it goes right
                self.xmov = 1
                self.ymov = 0

            # Resurrection
            self.alive = True

            # Drop and apple
            apple = Apple()


        # Move the snake.

        # If head hasn't moved, tail shouldn't either (otherwise, self-byte).
        if (self.xmov or self.ymov):

            # Prepend a new segment to tail and then remove the trailing segment.
            self.tail.insert(0,pygame.Rect(self.head.x, self.head.y, GRID_SIZE, GRID_SIZE))
            self.tail.pop()

            # Move the head along current direction.
            self.head.x += self.xmov * GRID_SIZE
            self.head.y += self.ymov * GRID_SIZE

class Apple:
    def __init__(self):

        # Pick a random position within the game SCREEN
        self.x = int(random.randint(0, WIDTH)/GRID_SIZE) * GRID_SIZE
        self.y = int(random.randint(0, HEIGHT)/GRID_SIZE) * GRID_SIZE

        # Create an apple at that location
        self.rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

    # This function is called each interation of the game loop

    def update(self):

        # Drop the apple
        pygame.draw.rect(SCREEN, APPLE_COLOR, self.rect)

##
## The color picker class.
##

class ColorPicker:
    def __init__(self, center, width, height):
        x, y = center 
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill(SCREEN_COLOR)
        self.rad = height // 2
        self.pwidth = width - self.rad*2
        for i in range(self.pwidth):    # Filling gradient
            color = pygame.Color(0)
            color.hsla = (int(360*i/self.pwidth), 100, 50, 100)
            pygame.draw.rect(self.image, color, (i + self.rad, height // 3, 1, height - 2*height//3))
        self.pos = 0

    def get_color(self):
        color = pygame.Color(0)
        color.hsla = (int(self.pos * self.pwidth), 100, 50, 100)
        return color

    def update(self):
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if mouse_buttons[0] and self.rect.collidepoint(mouse_pos):
            self.pos = (mouse_pos[0] - self.rect.left - self.rad) / self.pwidth
            self.pos = max(0, min(self.pos, 1))
    
    def draw(self, surf):
        surf.blit(self.image, self.rect)
        center = self.rect.left + self.rad + self.pos * self.pwidth, self.rect.centery
        pygame.draw.circle(surf, self.get_color(), center, self.rect.height // 4)


##
## Draw the SCREEN
##

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        for y in range(0, HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(SCREEN, GRID_COLOR, rect, 1)


def grid_resize():
    global grid_size
    # Show title and subtitle.
    center_title = BIG_FONT.render("Welcome", True, MESSAGE_COLOR)
    center_title_rect = center_title.get_rect(center=(WIDTH/2, HEIGHT/2))

    center_subtitle = SMALL_FONT.render("Press to Start.", True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*2/3))
    
    grid_size_text = SMALL_FONT.render(f"Grid Size Up Down: {grid_size}", True, MESSAGE_COLOR)
    grid_size_text_rect = grid_size_text.get_rect(center=(WIDTH/2, HEIGHT*3/4 + 20))

    while ( event := pygame.event.wait() ):
        if event.type == pygame.KEYDOWN:
            # Change grid size.
            if event.key == pygame.K_UP:
                grid_size += 1
                if grid_size >= 100: grid_size = 100  # Limit grid size up to 100px.
            elif event.key == pygame.K_DOWN:
                grid_size -= 1
                if grid_size <= 10: grid_size = 10 # Limit grid size down to 10px.
            else:   # Exit if other keys are pressed. 
                break
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        grid_size_text = SMALL_FONT.render(f"Grid Size Up Down: {grid_size}", True, MESSAGE_COLOR)
        SCREEN.fill(SCREEN_COLOR)

        draw_grid()


        SCREEN.blit(center_title, center_title_rect)
        SCREEN.blit(center_subtitle, center_subtitle_rect)
        SCREEN.blit(grid_size_text, grid_size_text_rect)

        pygame.display.update()

##
## Draw the color menu
##

def draw_color_menu(menu_text, color_picker, center):
    global SCREEN

    # Rendering text
    menu = COLOR_MENU_FONT.render(menu_text, True, SCORE_COLOR)
    menu_rect = menu.get_rect(center=center)
    pygame.draw.rect(SCREEN, SCREEN_COLOR, menu_rect)
    SCREEN.blit(menu, menu_rect)

    # Rendering color picker
    color_picker.update()
    color_picker.draw(SCREEN)

##
## Main loop
##
def play():
    game_on = 1
    show_color_menu = False

    SCREEN.fill("black")
    
    draw_grid()
    
    score = BIG_FONT.render("1", True, MESSAGE_COLOR)
    score_rect = score.get_rect(center=(WIDTH/2, HEIGHT/20+HEIGHT/30))

    snake = Snake()    # The snake

    apple = Apple()    # An apple

    best_score_num = 0 # Best score in the run

    best_score = SMALL_FONT.render("1", True, MESSAGE_COLOR)
    best_score_rect = best_score.get_rect(center=(WIDTH/2, HEIGHT/2+HEIGHT/3))

    head_color_picker = ColorPicker((WIDTH/4, HEIGHT/3), 400, 60)
    tail_color_picker = ColorPicker((WIDTH/4, HEIGHT/1.7), 400, 60)

    #center_prompt("Welcome", "Press to start")

    while True:

        for event in pygame.event.get():           # Wait for events

        # App terminated
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:    # Down arrow:  move down
                    snake.ymov = 1
                    snake.xmov = 0
                elif event.key == pygame.K_UP:    # Up arrow:    move up
                    snake.ymov = -1
                    snake.xmov = 0
                elif event.key == pygame.K_RIGHT: # Right arrow: move right
                    snake.ymov = 0
                    snake.xmov = 1
                elif event.key == pygame.K_LEFT:  # Left arrow:  move left
                    snake.ymov = 0
                    snake.xmov = -1
                elif event.key == pygame.K_q:     # Q         : quit game
                    main_menu()
                elif event.key == pygame.K_p:     # S         : pause game
                    game_on = not game_on
                    if show_color_menu: show_color_menu = False
                elif event.key == pygame.K_c:     # C:           show color menu
                    show_color_menu = not show_color_menu
                    game_on = False if show_color_menu else True

        ## Update the game

        if game_on:
          
            # If the player gets a new record
            if(len(snake.tail) > best_score_num):
                best_score_num = len(snake.tail)

            snake.update()

            SCREEN.fill(SCREEN_COLOR)
            draw_grid()

            apple.update()

        # Draw the tail
        for square in snake.tail:
            pygame.draw.rect(SCREEN, snake.tail_color, square)

        # Draw head
        pygame.draw.rect(SCREEN, snake.head_color, snake.head)

        score = BIG_FONT.render(f"{len(snake.tail)}", True, SCORE_COLOR)
        SCREEN.blit(score, score_rect)
        
        # Show the best score in the run until the end of the current game
        best_score = SMALL_FONT.render(f"Best score: {best_score_num}", True, SCORE_COLOR)
        SCREEN.blit(best_score, best_score_rect)


        # If the head pass over an apple, lengthen the snake and drop another apple
        if snake.head.x == apple.x and snake.head.y == apple.y:
            snake.tail.append(pygame.Rect(snake.head.x, snake.head.x, GRID_SIZE, GRID_SIZE))
            apple = Apple()


        if show_color_menu:
            draw_color_menu("HEAD COLOR", head_color_picker, (WIDTH/2, HEIGHT/3 - 60))
            snake.head_color = head_color_picker.get_color()

            draw_color_menu("TAIL COLOR", tail_color_picker, (WIDTH/2, HEIGHT/1.7 - 60))
            snake.tail_color = tail_color_picker.get_color()


        # Update display and move clock.
        pygame.display.update()
        clock.tick(CLOCK_TICKS)

main_menu()
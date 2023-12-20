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

WIDTH, HEIGHT = 650, 650     # Game screen dimensions.

GRID_SIZE = 50               # Square grid size.

APPLE     = 0  # Apple is the default fruit (type 0)
PEAR      = 1  # Pear is fruit type 1
BLUEBERRY = 2  # Blueberry is fruit type 2
ORANGE    = 3  # Orange is fruit type 3

HEAD_COLOR      = "#00aa00"  # Color of the snake's head.
DEAD_HEAD_COLOR = "#4b0082"  # Color of the dead snake's head.
TAIL_COLOR      = "#00ff00"  # Color of the snake's tail.
APPLE_COLOR     = "#aa0000"  # Color of the apple.
PEAR_COLOR      = "#91aa00"  # Color of the pear.
BLUEBERRY_COLOR = "#000eaa"  # Color of the blueberry.
ORANGE_COLOR    = "#cc6f04"  # Color of the orange.
SCREEN_COLOR    = "#202020"  # Color of the ground.
GRID_COLOR      = "#3c3c3b"  # Color of the grid lines.
SCORE_COLOR     = "#ffffff"  # Color of the scoreboard.
MESSAGE_COLOR   = "#808080"  # Color of the game-over message.

WINDOW_TITLE    = ["Sucury","Sucury"] # Window title.

CLOCK_TICKS     = 7         # How fast the snake moves.

START_POS_PADDING = 3       # Size of padding so that the snake does not start to close to the border.

##
## Game implementation.
##

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BIG_FONT   = pygame.font.Font("assets/font/prstart.ttf", int(WIDTH/10))
SMALL_FONT = pygame.font.Font("assets/font/prstart.ttf", int(WIDTH/20))
COLOR_MENU_FONT = pygame.font.Font("assets/font/GochiHand.ttf", int(WIDTH/20))

pygame.display.set_caption(WINDOW_TITLE[0])
BG = pygame.image.load("assets/Background.jpg")

def main_menu():  # Main Menu Screen
    pygame.display.set_caption(WINDOW_TITLE[1])
    menu_option = 0  # 0: Play, 1: Quit

    PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(WIDTH/2, HEIGHT/2.5),
                         text_input="PLAY", font=SMALL_FONT, base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(WIDTH/2, HEIGHT/1.8),
                         text_input="QUIT", font=SMALL_FONT, base_color="#d7fcd4", hovering_color="White")

    buttons = [PLAY_BUTTON, QUIT_BUTTON]

    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = BIG_FONT.render("MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, HEIGHT/5))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for i, button in enumerate(buttons):
            if i == menu_option:
                button.text = button.font.render(button.text_input, True, button.hovering_color)
            else:
                button.text = button.font.render(button.text_input, True, button.base_color)

            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[menu_option].checkForInput(MENU_MOUSE_POS):
                    if menu_option == 0:
                        play()
                    elif menu_option == 1:
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    menu_option = 1 - menu_option  # Toggle between 0 and 1
                elif event.key == pygame.K_RETURN:  # Enter key
                    if menu_option == 0:
                        play()
                    elif menu_option == 1:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()

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

   # Wait for a keypress or a game quit event.

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

        # The should grow or not on the next update
        self.should_grow = False

        # The snake is born.
        self.alive = True

        # Default snake colors
        self.head_color = HEAD_COLOR
        self.tail_color = TAIL_COLOR

        # initialize the movement queue
        self.movement_queue = []
        
    # This function is called at each loop interation.

    def update(self):
        global fruit

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
            self.should_grow = False

            # Drop a fruit
            fruit = Fruit()



        # Move the snake.
        
        # Check if the movement queue is not empty
        if self.movement_queue:
            # Update direction based on the queue
            self.xmov, self.ymov = self.movement_queue.pop(0)

        # If head hasn't moved, tail shouldn't either (otherwise, self-byte).
        if (self.xmov or self.ymov):

            # Prepend a new segment to tail.
            self.tail.insert(0,pygame.Rect(self.head.x, self.head.y, GRID_SIZE, GRID_SIZE))

            # If the snake should grow, keeps the last segment, else removes it.
            if self.should_grow:
                self.should_grow = False
            else:
                self.tail.pop()

            # Move the head along current direction.
            self.head.x += self.xmov * GRID_SIZE
            self.head.y += self.ymov * GRID_SIZE

            
  # Sets that the snake should grow on the next update.
    def update_direction(self, new_direction):
        # Add new direction to the queue
        self.movement_queue.append(new_direction)
        # Limit the size of the queue to prevent too much lag
        if len(self.movement_queue) > 2:
            self.movement_queue = self.movement_queue[-2:]

    def grow(self):
        self.should_grow = True

##
## The fruit class.
##

class Fruit:

    def __init__(self, snake):
        # Pick a random position within the game SCREEN
        self.x = int(random.randint(0, WIDTH)/GRID_SIZE) * GRID_SIZE
        self.y = int(random.randint(0, HEIGHT)/GRID_SIZE) * GRID_SIZE
        self.type = random.randint(0, 3)

        while True: # Keep generating until it's a valid position

            if (self.x,self.y) == (snake.head.x,snake.head.y): # If it's on top of snake head
                self.x = int(random.randint(0, WIDTH)/GRID_SIZE) * GRID_SIZE
                self.y = int(random.randint(0, HEIGHT)/GRID_SIZE) * GRID_SIZE
                continue
            for segment in snake.tail: # check if it's on top of snake body
                if (self.x,self.y) == (segment.x,segment.y): 
                    self.x = int(random.randint(0, WIDTH)/GRID_SIZE) * GRID_SIZE
                    self.y = int(random.randint(0, HEIGHT)/GRID_SIZE) * GRID_SIZE
                    break
            else:
                break

        # Create a fruit at that location
        self.rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

    def update(self, CLOCK_TICKS=6):

        # Drop the fruit
        if self.type == APPLE:
            pygame.draw.rect(arena, APPLE_COLOR, self.rect)

        elif self.type == PEAR:
            pygame.draw.rect(arena, PEAR_COLOR, self.rect)
          
        elif self.type == BLUEBERRY:
            pygame.draw.rect(arena, BLUEBERRY_COLOR, self.rect)

        elif self.type == ORANGE:
            pygame.draw.rect(arena, ORANGE_COLOR, self.rect)

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

    fruit = Fruit(snake)    # A fruit

    best_score_num = 0 # Best score in the run

    best_score = SMALL_FONT.render("1", True, MESSAGE_COLOR)
    best_score_rect = best_score.get_rect(center=(WIDTH/3, HEIGHT/2+HEIGHT/3))

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
                if game_on:
                    new_direction = None
                    # If player presses S o DOWN_ARROW, moves down
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s and snake.ymov == 0:  # Down arrow: move down
                        new_direction = (0, 1)
                    # If player presses W o UP_ARROW, moves up
                    elif event.key == pygame.K_UP or event.key == pygame.K_w and snake.ymov == 0:  # Up arrow: move up
                        new_direction = (0, -1)
                    # If player presses D o RIGHT_ARROW, moves right
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and snake.xmov == 0: # Right arrow: move right
                        new_direction = (1, 0)
                    # If player presses A o LEFT_ARROW, moves left
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a and snake.xmov == 0:  # Left arrow: move left
                        new_direction = (-1, 0)

                    if new_direction:
                        # Update the queue with new direction
                        snake.update_direction(new_direction)  
                    
                if event.key == pygame.K_q:     # Q         : quit game
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

            fruit.update()

        # Draw the tail
        for square in snake.tail:
            pygame.draw.rect(SCREEN, snake.tail_color, square)

        # Draw head
        pygame.draw.rect(SCREEN, snake.head_color, snake.head)

        # Show score (snake length = head + tail)
        score = BIG_FONT.render(f"{len(snake.tail)}", True, SCORE_COLOR)
        SCREEN.blit(score, score_rect)
        
        # Show the best score in the run until the end of the current game
        best_score = SMALL_FONT.render(f"Best score: {best_score_num}", True, SCORE_COLOR)
        SCREEN.blit(best_score, best_score_rect)


        # If the head pass over a fruit, lengthen the snake and drop another fruit
        if snake.head.x == fruit.x and snake.head.y == fruit.y:
            snake.grow()
            
            # Pear makes snake faster
            if fruit.type == PEAR:
                CLOCK_TICKS += 1 if CLOCK_TICKS < 12 else 0
            # Blueberry makes snake slower
            elif fruit.type == BLUEBERRY:
                CLOCK_TICKS -= 1 if CLOCK_TICKS > 2 else 0
            # Orange increases snake length by 2 instead of 1
            elif fruit.type == ORANGE:
                snake.grow()
                
            fruit = Fruit(snake)


        if show_color_menu:
            draw_color_menu("HEAD COLOR", head_color_picker, (WIDTH/2, HEIGHT/3 - 60))
            snake.head_color = head_color_picker.get_color()

            draw_color_menu("TAIL COLOR", tail_color_picker, (WIDTH/2, HEIGHT/1.7 - 60))
            snake.tail_color = tail_color_picker.get_color()


        # Update display and move clock.
        pygame.display.update()
        clock.tick(CLOCK_TICKS)

main_menu()

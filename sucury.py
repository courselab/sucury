#!/usr/bin/env python3
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

grid_size = 50               # Square grid size.

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

BLOCK_180_TURNS = True      # Disable 180° turns

# Directions
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

##
## Game implementation.
##

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BIG_FONT   = pygame.font.Font("assets/font/Ramasuri.ttf", int(WIDTH/8))
SMALL_FONT = pygame.font.Font("assets/font/Ramasuri.ttf", int(WIDTH/20))

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

###
### Display the main menu.
###
def main_menu():
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
        arena.fill(ARENA_COLOR)
        draw_grid()


        arena.blit(center_title, center_title_rect)
        arena.blit(center_subtitle, center_subtitle_rect)
        arena.blit(grid_size_text, grid_size_text_rect)

        pygame.display.update()
 
##
## Snake class
##


class Snake:
    def __init__(self):

        # Dimension of each snake segment.

        self.x, self.y = grid_size, grid_size

        # Initial direction
        # xmov :  -1 left,    0 still,   1 right
        # ymov :  -1 up       0 still,   1 dows
        self.xmov = 1
        self.ymov = 0

        # previous movement velocity
        self.last_velocity = (self.xmov, self.ymov)

        # The snake has a head segement,
        self.head = pygame.Rect(self.x, self.y, grid_size, grid_size)

        # and a tail (array of segments).
        self.tail = []

        # The snake is born.
        self.alive = True

        # The snake should grow in the next update.
        self.should_grow = False

    def change_direction(self, direction: tuple[int, int]):
        # Remove 1-frame 180 turns that lead to death
        if BLOCK_180_TURNS and (-self.last_velocity[0], -self.last_velocity[1]) == direction:
            return

        (self.xmov, self.ymov) = direction

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


        # Set the last_velocity, to remove 180° turns.
        # By assigning it at the end of the frame, removes the possibility
        # of a multi-input 180° turn
        self.last_velocity = (self.xmov, self.ymov)

        # In the event of death, reset the game arena.
        if not self.alive:

            # Tell the bad news
            pygame.draw.rect(SCREEN, DEAD_HEAD_COLOR, self.head)
            center_prompt("Game Over", "Press to restart")

            # Respan the head
            self.x, self.y = grid_size, grid_size
            self.head = pygame.Rect(self.x, self.y, grid_size, grid_size)

            # Respan the initial tail
            self.tail = []

            # Initial direction
            self.xmov = 1 # Right
            self.ymov = 0 # Still

            # Resurrection
            self.alive = True
            self.should_grow = False

            # Drop and apple
            apple = Apple()


        # Move the snake.

        # If head hasn't moved, tail shouldn't either (otherwise, self-byte).
        if (self.xmov or self.ymov):

            # Prepend a new segment to tail.
            self.tail.insert(0,pygame.Rect(self.head.x, self.head.y, grid_size, grid_size))
            
            # If the snake should grow, keeps the last segment, else removes it.
            if self.should_grow:
                self.should_grow = False
            else:
                self.tail.pop()

            # Move the head along current direction.
            self.head.x += self.xmov * grid_size
            self.head.y += self.ymov * grid_size

    # Sets that the snake should grow on the next update.

    def grow(self):
        self.should_grow = True

class Apple:
    def __init__(self):

<<<<<<< HEAD
        global snake
        # Pick a random position within the game arena
        self.x = int(random.randint(0, WIDTH)/grid_size) * grid_size
        self.y = int(random.randint(0, HEIGHT)/grid_size) * grid_size

        while True: # Keep generating until it's a  valid position

            if (self.x,self.y) == (snake.head.x,snake.head.y): # If it's on top of snake head
                self.x = int(random.randint(0, WIDTH)/grid_size) * grid_size
                self.y = int(random.randint(0, HEIGHT)/grid_size) * grid_size
                continue
            for segment in snake.tail: # check if it's on top of snake body
                if (self.x,self.y) == (segment.x,segment.y): 
                    self.x = int(random.randint(0, WIDTH)/grid_size) * grid_size
                    self.y = int(random.randint(0, HEIGHT)/grid_size) * grid_size
                    break
            else:
                break
=======
        # Pick a random position within the game SCREEN
        self.x = int(random.randint(0, WIDTH)/GRID_SIZE) * GRID_SIZE
        self.y = int(random.randint(0, HEIGHT)/GRID_SIZE) * GRID_SIZE
>>>>>>> c9fe9cdaf0f162429a4f1b02b5f9b4a61e4b984d

        # Create an apple at that location
        self.rect = pygame.Rect(self.x, self.y, grid_size, grid_size)

    # This function is called each interation of the game loop

    def update(self):

        # Drop the apple
        pygame.draw.rect(SCREEN, APPLE_COLOR, self.rect)

##
## Draw the SCREEN
##

def draw_grid():
<<<<<<< HEAD
    for x in range(0, WIDTH, grid_size):
        for y in range(0, HEIGHT, grid_size):
            rect = pygame.Rect(x, y, grid_size, grid_size)
            pygame.draw.rect(arena, GRID_COLOR, rect, 1)

score = BIG_FONT.render("1", True, MESSAGE_COLOR)
score_rect = score.get_rect(center=(WIDTH/2, HEIGHT/20+HEIGHT/30))

main_menu()

snake = Snake()    # The snake
apple = Apple()    # An apple
=======
    for x in range(0, WIDTH, GRID_SIZE):
        for y in range(0, HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(SCREEN, GRID_COLOR, rect, 1)
>>>>>>> c9fe9cdaf0f162429a4f1b02b5f9b4a61e4b984d

##
## Main loop
##
def play():
    game_on = 1
    SCREEN.fill("black")
    
    draw_grid()
    
    score = BIG_FONT.render("1", True, MESSAGE_COLOR)
    score_rect = score.get_rect(center=(WIDTH/2, HEIGHT/20+HEIGHT/30))

    snake = Snake()    # The snake

    apple = Apple()    # An apple
    #center_prompt("Welcome", "Press to start")

    while True:

<<<<<<< HEAD
        # Key pressed
        if event.type == pygame.KEYDOWN:
            if game_on:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:    # Down arrow or S:  move down
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:    # Up arrow or W:    move up
                    snake.change_direction(UP)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d: # Right arrow or D: move right
                    snake.change_direction(RIGHT)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:  # Left arrow or A:  move left
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_q:     # Q         : quit game
                    pygame.quit()
                    sys.exit()

            if event.key == pygame.K_p:     # S         : pause game
                game_on = not game_on

    ## Update the game

    if game_on:

        snake.update()
=======
        for event in pygame.event.get():           # Wait for events

        # App terminated
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
>>>>>>> c9fe9cdaf0f162429a4f1b02b5f9b4a61e4b984d

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

        ## Update the game

        if game_on:

            snake.update()

            SCREEN.fill(SCREEN_COLOR)
            draw_grid()

            apple.update()

        # Draw the tail
        for square in snake.tail:
            pygame.draw.rect(SCREEN, TAIL_COLOR, square)

        # Draw head
        pygame.draw.rect(SCREEN, HEAD_COLOR, snake.head)

        # Show score (snake length = head + tail)
        score = BIG_FONT.render(f"{len(snake.tail)}", True, SCORE_COLOR)
        SCREEN.blit(score, score_rect)

        # If the head pass over an apple, lengthen the snake and drop another apple
        if snake.head.x == apple.x and snake.head.y == apple.y:
            snake.tail.append(pygame.Rect(snake.head.x, snake.head.x, GRID_SIZE, GRID_SIZE))
            apple = Apple()

<<<<<<< HEAD
    # If the head pass over an apple, lengthen the snake and drop another apple
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.grow()
        apple = Apple()
=======
>>>>>>> c9fe9cdaf0f162429a4f1b02b5f9b4a61e4b984d

        # Update display and move clock.
        pygame.display.update()
        clock.tick(CLOCK_TICKS)

<<<<<<< HEAD
    # Update display and move clock.
    pygame.display.update()
    clock.tick(CLOCK_TICKS)
=======
main_menu()
>>>>>>> c9fe9cdaf0f162429a4f1b02b5f9b4a61e4b984d

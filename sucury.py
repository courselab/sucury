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
PEAR_COLOR      = "#91aa00"  # Color of the pear.
BLUEBERRY_COLOR = "#000eaa"  # Color of the blueberry.
ORANGE_COLOR    = "#cc6f04"  # Color of the orange.
ARENA_COLOR     = "#202020"  # Color of the ground.
GRID_COLOR      = "#3c3c3b"  # Color of the grid lines.
SCORE_COLOR     = "#ffffff"  # Color of the scoreboard.
MESSAGE_COLOR   = "#808080"  # Color of the game-over message.

WINDOW_TITLE    = "Sucury"   # Window title.

##
## Game implementation.
##

pygame.init()

clock = pygame.time.Clock()

arena = pygame.display.set_mode((WIDTH, HEIGHT))

BIG_FONT   = pygame.font.Font("assets/font/Ramasuri.ttf", int(WIDTH/8))
SMALL_FONT = pygame.font.Font("assets/font/Ramasuri.ttf", int(WIDTH/20))

pygame.display.set_caption(WINDOW_TITLE)

## This function is called when the snake dies.

def center_prompt(title, subtitle):

    # Show title and subtitle.

    center_title = BIG_FONT.render(title, True, MESSAGE_COLOR)
    center_title_rect = center_title.get_rect(center=(WIDTH/2, HEIGHT/2))
    arena.blit(center_title, center_title_rect)

    center_subtitle = SMALL_FONT.render(subtitle, True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*2/3))
    arena.blit(center_subtitle, center_subtitle_rect)

    pygame.display.update()

   # Wait for a keypress or a game quit event.

    while ( event := pygame.event.wait() ):
        if event.type == pygame.KEYDOWN:
            break
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.key == pygame.K_q:          # 'Q' quits game
        pygame.quit()
        sys.exit()


##
## Snake class
##

class Snake:
    def __init__(self):

        # Dimension of each snake segment.

        self.x, self.y = GRID_SIZE, GRID_SIZE

        # Initial direction
        # xmov :  -1 left,    0 still,   1 right
        # ymov :  -1 up       0 still,   1 dows
        self.xmov = 1
        self.ymov = 0

        # The snake has a head segement,
        self.head = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

        # and a tail (array of segments).
        self.tail = []

        # The snake is born.
        self.alive = True

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

        # In the event of death, reset the game arena.
        if not self.alive:

            # Tell the bad news
            pygame.draw.rect(arena, DEAD_HEAD_COLOR, self.head)
            center_prompt("Game Over", "Press to restart")

            # Respan the head
            self.x, self.y = GRID_SIZE, GRID_SIZE
            self.head = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

            # Respan the initial tail
            self.tail = []

            # Initial direction
            self.xmov = 1 # Right
            self.ymov = 0 # Still

            # Resurrection
            self.alive = True

            # Drop a fruit
            fruit = Fruit()
            fruit.update()


        # Move the snake.

        # If head hasn't moved, tail shouldn't either (otherwise, self-byte).
        if (self.xmov or self.ymov):

            # Prepend a new segment to tail and then remove the trailing segment.
            self.tail.insert(0,pygame.Rect(self.head.x, self.head.y, GRID_SIZE, GRID_SIZE))
            self.tail.pop()

            # Move the head along current direction.
            self.head.x += self.xmov * GRID_SIZE
            self.head.y += self.ymov * GRID_SIZE

##
## The fruit class.
##

class Fruit:
    def __init__(self):

        # Pick a random position within the game arena
        self.x = int(random.randint(0, WIDTH)/GRID_SIZE) * GRID_SIZE
        self.y = int(random.randint(0, HEIGHT)/GRID_SIZE) * GRID_SIZE

        # Create an fruit at that location
        self.rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

        self.type = random.randint(0, 3)

    # This function is called each interation of the game loop

    def update(self, CLOCK_TICKS=6):

        # Drop the fruit
        # Apple maintains snake's speed
        if self.type == 0:
            pygame.draw.rect(arena, APPLE_COLOR, self.rect)

        # Pear increases snake's speed
        elif self.type == 1:
            pygame.draw.rect(arena, PEAR_COLOR, self.rect)

        # Blueberry decreases snake's speed
        elif self.type == 2:
            pygame.draw.rect(arena, BLUEBERRY_COLOR, self.rect)

        # Orange makes snake grow 2 segments
        elif self.type == 3:
            pygame.draw.rect(arena, ORANGE_COLOR, self.rect)

        print(self.type, CLOCK_TICKS)
##
## Draw the arena
##

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        for y in range(0, HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(arena, GRID_COLOR, rect, 1)

def main():
    game_on = True
    CLOCK_TICKS = 6           # How fast the snake moves.
    score = BIG_FONT.render("1", True, MESSAGE_COLOR)
    score_rect = score.get_rect(center=(WIDTH/2, HEIGHT/20+HEIGHT/30))

    draw_grid()

    snake = Snake()    # The snake

    fruit = Fruit()    # A fruit

    center_prompt("Welcome", "Press to start")

    ##
    ## Main loop
    ##

    while True:

        for event in pygame.event.get():         # Wait for events

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
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_p:     # S         : pause game
                    game_on = not game_on

        ## Update the game

        if game_on:

            snake.update()

            arena.fill(ARENA_COLOR)
            draw_grid()

            fruit.update(CLOCK_TICKS)

        # Draw the tail
        for square in snake.tail:
            pygame.draw.rect(arena, TAIL_COLOR, square)

        # Draw head
        pygame.draw.rect(arena, HEAD_COLOR, snake.head)

        # Show score (snake length = head + tail)
        score = BIG_FONT.render(f"{len(snake.tail)}", True, SCORE_COLOR)
        arena.blit(score, score_rect)

        # If the head pass over an fruit, lengthen the snake and drop another fruit
        if snake.head.x == fruit.x and snake.head.y == fruit.y:
            snake.tail.append(pygame.Rect(snake.head.x, snake.head.x, GRID_SIZE, GRID_SIZE))
            if fruit.type == 1:
                CLOCK_TICKS += 1 if CLOCK_TICKS < 12 else 0
            elif fruit.type == 2:
                CLOCK_TICKS -= 1 if CLOCK_TICKS > 2 else 0
            elif fruit.type == 3:
                snake.tail.append(pygame.Rect(snake.head.x, snake.head.x, GRID_SIZE, GRID_SIZE))
            fruit = Fruit()


        # Update display and move clock.
        pygame.display.update()
        clock.tick(CLOCK_TICKS)

if __name__ == "__main__":
    main()
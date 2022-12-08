import curses
import time
import random

# Initialize the screen
screen = curses.initscr()
curses.curs_set(0)  # Hide the cursor
sh, sw = screen.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initialize the snake's position and direction
snake_x = sw//4
snake_y = sh//2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

food = [sh//2, sw//2]  # Initialize the food's position
w.addch(food[0], food[1], curses.ACS_PI)  # Add the food to the screen

key = curses.KEY_RIGHT  # Initialize the direction

while True:
    next_key = w.getch()  # Get the next key the user presses
    key = key if next_key == -1 else next_key  # Update the direction

    # Calculate the new position of the snake
    new_snake_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_snake_head[0] += 1
    if key == curses.KEY_UP:
        new_snake_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_snake_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_snake_head[1] += 1

    snake.insert(0, new_snake_head)

    # Check if the snake has eaten the food
    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = new_food if new_food not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Check if the snake has collided with the wall or itself
    if (
        snake[0][0] in [0, sh] or
        snake[0][1] in [0, sw] or
        snake[0] in snake[1:]
    ):
        curses.endwin()
        quit()

    # Move the snake's body
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

import curses
import random
import time

# Initialize the screen
screen = curses.initscr()
curses.curs_set(0)  # Hide the cursor
sh, sw = screen.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initialize the snake's position and direction
snake1_x = sw//4
snake1_y = sh//2
snake1 = [
    [snake1_y, snake1_x],
    [snake1_y, snake1_x-1],
    [snake1_y, snake1_x-2]
]

snake2_x = 3 * sw//4
snake2_y = sh//2
snake2 = [
    [snake2_y, snake2_x],
    [snake2_y, snake2_x+1],
    [snake2_y, snake2_x+2]
]

food = [sh//2, sw//2]  # Initialize the food's position
w.addch(food[0], food[1], curses.ACS_PI)  # Add the food to the screen

key1 = curses.KEY_RIGHT  # Initialize the direction for snake 1
key2 = curses.KEY_LEFT  # Initialize the direction for snake 2


while True:
    # Get the next key the user presses
    next_key1 = w.getch()
    next_key2 = w.getch()

    # Update the direction of the snakes
    key1 = key1 if next_key1 == -1 else next_key1
    key2 = key2 if next_key2 == -1 else next_key2

    # Calculate the new position of snake 1
    new_snake1_head = [snake1[0][0], snake1[0][1]]

    if key1 == curses.KEY_DOWN:
        new_snake1_head[0] += 1
    if key1 == curses.KEY_UP:
        new_snake1_head[0] -= 1
    if key1 == curses.KEY_LEFT:
        new_snake1_head[1] -= 1
    if key1 == curses.KEY_RIGHT:
        new_snake1_head[1] += 1

    snake1.insert(0, new_snake1_head)

    # Calculate the new position of snake 2
    new_snake2_head = [snake2[0][0], snake2[0][1]]

    # check if key2 is W, A, S, or D
    if key1 == curses.KEY_DOWN:
        new_snake1_head[0] += 1
    if key1 == curses.KEY_UP:
        new_snake1_head[0] -= 1
    if key1 == curses.KEY_LEFT:
        new_snake1_head[1] -= 1
    if key1 == curses.KEY_RIGHT:
        new_snake1_head[1] += 1

    snake2.insert(0, new_snake2_head)

    # Check if the snakes have eaten the food
    if snake1[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = new_food if new_food not in snake1 and new_food not in snake2 else None
        w.addch(food[0], food[1], curses.ACS_PI)

    # Move the snake's body
    tail1 = snake1.pop()
    w.addch(tail1[0], tail1[1], ' ')
    w.addch(snake1[0][0], snake1[0][1], curses.ACS_CKBOARD)

    # Check if snake 1 has collided with the wall or itself
    if (
        snake1[0][0] in [0, sh] or
        snake1[0][1] in [0, sw] or
        snake1[0] in snake1[1:] or
        snake1[0] in snake2
    ):
        curses.endwin()
        quit()

    # Move the snake's body
    tail2 = snake2.pop()
    w.addch(tail2[0], tail2[1], ' ')
    w.addch(snake2[0][0], snake2[0][1], curses.ACS_CKBOARD)
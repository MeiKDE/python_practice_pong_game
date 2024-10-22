# Pong Game

This project is a classic **Pong Game** implemented in Python using the `turtle` graphics library. The game involves two players controlling paddles and trying to hit the ball back and forth. The game tracks the score and ends when either player misses the ball.

## Features

- **Two Player Paddle Controls**: One player uses the arrow keys, and the other uses `W` and `S` to control the paddles.
- **Ball Movement**: The ball bounces off the walls and paddles, increasing speed after every bounce.
- **Scoreboard**: Displays the score for each player, and it updates as points are scored.
  
## Prerequisites

Before running the game, make sure you have Python installed along with the `turtle` module (which is included with Python by default).

## How to Run

1. Clone the repository or download the code files.
2. Make sure you have the following Python files in the same directory:
    - `main.py`: Contains the main game loop and logic.
    - `paddle.py`: Contains the `Paddle` class for creating and controlling paddles.
    - `ball.py`: Contains the `Ball` class that handles the ball's movement.
    - `scoreboard.py`: Contains the `Scoreboard` class to manage and display the score.
3. Run the main game file:

    ```bash
    python main.py
    ```

## Gameplay Instructions

- **Player 1 Controls**: Use the `Up` and `Down` arrow keys to control the right paddle.
- **Player 2 Controls**: Use the `W` (up) and `S` (down) keys to control the left paddle.
- **Objective**: Hit the ball back and forth using the paddles. If the ball passes a paddle, the opposing player scores a point.

## Code Overview

### `main.py`

- Sets up the game window using `turtle.Screen()`.
- Creates the paddles for both players, the ball, and the scoreboard.
- Contains the main game loop which updates the ball's movement, checks for collisions with the paddles or walls, and tracks the score.

### `Paddle` Class (`paddle.py`)

- Inherits from `Turtle` and is used to create and control the paddles.
- Includes methods for moving the paddle up and down the screen.

### `Ball` Class (`ball.py`)

- Inherits from `Turtle` and defines the ball's shape and movement.
- Handles ball collision with the walls and paddles.
- Includes methods to reverse the ball's direction (`bounce_x` and `bounce_y`), and reset the ball to the center after a point is scored.

### `Scoreboard` Class (`scoreboard.py`)

- Inherits from `Turtle` and manages the game's score.
- Displays the score for both players on the screen and updates it as players score points.

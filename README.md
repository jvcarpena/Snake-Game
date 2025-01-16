# Snake Game

A simple Snake game built using Python's Turtle graphics library. This classic game allows you to control a snake to eat food, grow longer, and avoid hitting walls or the snake's own tail.

## Features

- **Snake Movement**: Use the arrow keys to control the snake's movement.
- **Food**: The snake grows longer each time it eats food, and the score increases.
- **Collision Detection**: The game ends if the snake collides with the wall or itself.
- **Scoreboard**: The score increases each time the snake eats food, and resets when the game restarts.

## Requirements

- Python 3.x
- `turtle` module (comes with standard Python installation)

## Installation

1. Clone or download the repository:

    ```bash
    git clone https://github.com/jvcarpena/snake-game.git
    ```

2. Navigate to the project folder:

    ```bash
    cd snake-game
    ```

3. Run the game:

    ```bash
    python main.py
    ```

## How to Play

- Use the arrow keys (`Up`, `Down`, `Left`, `Right`) to move the snake.
- The snake will grow and the score will increase every time it eats food.
- Avoid hitting the walls or the snake's own tail.

## Project Structure

- `main.py`: The main game logic, including the screen setup and game loop.
- `snake.py`: Contains the `Snake` class, responsible for the snake's behavior.
- `food.py`: Contains the `Food` class, responsible for generating food and refreshing its position.
- `scoreboard.py`: Contains the `ScoreBoard` class, responsible for managing and displaying the player's score.

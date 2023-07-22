# Snake Game

#### Video Demo: https://youtu.be/9LcKFbr0_Uc

#### Description:

- This is a Python project, developed using the library [Pygame](https://www.pygame.org/docs/), that aims to recreate the well-known game Snake game
- The source code of `project.py` was developed with OOP (Objected oriented programming) in mind, aiming for a better organization, responsability separation, and code reutilization.
- The code was built in a single class, called Snake, which contains all the properties and methods necessary for the game to run properly.
- When we instanciate the class, the **init** function is called, settin up all important variables, such as `display size` and `snake_block_size`, and then, calls the function `start_game()`, to start the process.
- The functions `update_display()`, `generate_caption()` and `show_message()` are just abstractions for pygame's builtin functions. Its worth mentioning that the last function already handles correctly two pre-configured kind of fonts, and displays then dinamically
- The `start_game` function calls `pygame.init()`, which starts the internal processes of the library to correctly display and run the game.
- After that, we call the function `run()`, which is in fact the function that will handle all game variables
- Inside the function `run()`, we mainly have other methods, which do the following:
  - Generate a food in a random position of the screen, but ensuring that a food will never be generated in a spot already occupied by the snake body at that moment;
  - Handle the snake movement, by detecting the user's input in the keyboard, and then rendering the snake one step further in the direction prompted.
  - Its worth mentioning that this movement is made by constantly painting the screen with blue and black blocks. So the process occurs in the following order: first, we append one more block (by passing its coordinates to the `snake_body_sections` property) to the snake body. Then, we remove the snake's tail representation (which is the first element of the same array mentioned earlier). Finally, we re-render the entire snake block in the screen.
  - we also ensure that, if the snake collides with its own body, or with some screen border, the game will be lost, and the user will be prompted to insert a command telling if they want to have a rematch, or quit the game.
  - if at any given time the snake's head occupy the same spot than the food , another food block is generated, and the snake body grows one step (this is controlled by the property `snake_length`)

#### Challenges:

- It was necessary to ensure that the snake could not make any impossible movement, such as changing its direction to the opposite side. This was accomplished by creating boolean properties to store if a direction was able to be taken.
- When the user prompts the snake to go in a certain direction, two processes occurs: first, we reset all these boolean properties, switching them to `True`, and them we switch back only the property that represents the opposite direction back to `False`. So, for instance, if the snake is going to the left, the right direction will be disabled, and vice versa.
- If the user tries to make the snake move to a disabled direction, nothing occurs, and the snake keeps moving forward.

- It was necessary to ensure that a food would never be generated in a spot already occupied by the snake.
- This was accomplished by, at the start of the game, an array of coordinates was generated, containing all possible locations for a food to be generated.
- To reduze the size of this array, instead of storing all possible pixel coordinates (in a 600 x 600 screen there would be 360000 options), things were kept simpler, by dividing the screen size by the property `snake_block_size`, so we had (600 / 30) X (600 / 30) = 400 options for the food to be generated
- This array has been stored in memory, so there is no need to re-generate it more than once
- every time a food need to be generated, we remove from this array of options, all the blocks currently occupied by the snake (which we already have stored in the property `snake_body_elements`), and then choose a random coordinate from the resulting array.

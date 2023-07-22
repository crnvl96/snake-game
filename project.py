import random
import time

import pygame

from constants import colors


def disable_movements(self, direction):
    def reset_disabled_movements():
        self.can_snake_go_up = True
        self.can_snake_go_down = True
        self.can_snake_go_left = True
        self.can_snake_go_right = True

    reset_disabled_movements()

    if direction == "up":
        self.can_snake_go_up = False
    elif direction == "down":
        self.can_snake_go_down = False
    elif direction == "left":
        self.can_snake_go_left = False
    elif direction == "right":
        self.can_snake_go_right = False


def generate_coordinates(self):
    for abs_block in range(0, self.display_size, self.snake_block_size):
        for ord_block in range(0, self.display_size, self.snake_block_size):
            coordinates = [abs_block, ord_block]
            self.available_food_positions.append(coordinates)


def draw(self, color, absissa, ordinate):
    return pygame.draw.rect(
        self.display,
        color,
        [
            absissa,
            ordinate,
            self.snake_block_size,
            self.snake_block_size,
        ],
    )


def show_message(self, font, message, color):
    font_options = {
        "alert": self.alert_font,
        "score": self.score_font,
    }

    return self.display.blit(
        font_options[font].render(message, True, color),
        [
            self.initial_snake_absissa_position,
            self.initial_snake_ordinate_position,
        ],
    )


def seed_food(self):
    def get_available_positions():
        options = self.available_food_positions
        disabled_options = self.snake_body_sections
        available_options = [
            option for option in options if option not in disabled_options
        ]
        return random.choice(available_options)

    return get_available_positions()


class Snake:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.display_size = 600
        self.display = pygame.display.set_mode((self.display_size, self.display_size))

        self.snake_block_size = 30
        self.snake_speed = 7
        self.initial_snake_absissa_position = self.display_size / 2
        self.initial_snake_ordinate_position = self.display_size / 2
        self.snake_absissa = self.initial_snake_absissa_position
        self.snake_ordinate = self.initial_snake_ordinate_position
        self.snake_absissa_increment = 0
        self.snake_ordinate_increment = 0
        self.snake_body_sections = [
            [
                self.initial_snake_absissa_position,
                self.initial_snake_ordinate_position,
            ]
        ]
        self.snake_length = 1

        self.game_over = False
        self.game_close = False

        self.can_snake_go_up = True
        self.can_snake_go_down = True
        self.can_snake_go_left = True
        self.can_snake_go_right = True

        self.food_absissa = 0
        self.food_ordinate = 0
        self.available_food_positions = []

        self.font_size = 35
        self.alert_font_style = "hack"
        self.score_font_style = "comicsansms"

        self.caption_text = "Snake game by @crnvl96"

        self.start_game()

    @property
    def alert_font(self):
        return pygame.font.SysFont(self.alert_font_style, self.font_size)

    @property
    def score_font(self):
        return pygame.font.SysFont(self.score_font_style, self.font_size)

    def update_display(self):
        return pygame.display.update()

    def generate_caption(self):
        return pygame.display.set_caption(self.caption_text)

    def show_message(self, font, message, color):
        return show_message(self, font, message, color)

    def render_snake_body(self):
        for section in self.snake_body_sections:
            absissa, ordinate = section
            self.draw_block(colors.black, absissa, ordinate)

    def draw_block(
        self,
        color,
        absissa,
        ordinate,
    ):
        return draw(self, color, absissa, ordinate)

    def seed_food(self):
        return seed_food(self)

    def start_game(self):
        pygame.init()
        self.update_display()
        self.generate_caption()

    def disable_movement(self, direction):
        return disable_movements(self, direction)

    def update_game_frames(self):
        self.snake_absissa += self.snake_absissa_increment
        self.snake_ordinate += self.snake_ordinate_increment

        self.display.fill(colors.blue)
        self.draw_block(colors.green, self.food_absissa, self.food_ordinate)

        snake_head = []
        snake_head.append(self.snake_absissa)
        snake_head.append(self.snake_ordinate)

        self.snake_body_sections.append(snake_head)

        if len(self.snake_body_sections) > self.snake_length:
            del self.snake_body_sections[0]

            for element in self.snake_body_sections[:-1]:
                if element == snake_head:
                    self.game_close = True

        self.render_snake_body()
        self.show_score()
        self.update_display()

        if (
            self.snake_absissa == self.food_absissa
            and self.snake_ordinate == self.food_ordinate
        ):
            self.food_absissa, self.food_ordinate = self.seed_food()
            self.snake_length += 1

        self.clock.tick(self.snake_speed)

    def quit_game(self):
        pygame.quit()
        quit()

    def show_score(self):
        value = self.score_font.render(
            "Your Score: " + str(self.snake_length - 1), True, colors.yellow
        )
        self.display.blit(value, [0, 0])

    def generate_coordinates(self):
        return generate_coordinates(self)

    def run(self):
        self.generate_coordinates()

        self.food_absissa, self.food_ordinate = self.seed_food()

        while not self.game_over:
            while self.game_close is True:
                self.display.fill(colors.white)
                self.show_message(
                    "alert",
                    "[Q]-Exit [C]-Rematch",
                    colors.red,
                )
                self.update_display()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_over = True
                        self.game_close = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            self.__init__()
                            self.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.can_snake_go_left:
                        self.snake_absissa_increment = -self.snake_block_size
                        self.snake_ordinate_increment = 0
                        self.disable_movement("right")
                    elif event.key == pygame.K_RIGHT and self.can_snake_go_right:
                        self.snake_absissa_increment = self.snake_block_size
                        self.snake_ordinate_increment = 0
                        self.disable_movement("left")
                    elif event.key == pygame.K_UP and self.can_snake_go_up:
                        self.snake_absissa_increment = 0
                        self.snake_ordinate_increment = -self.snake_block_size
                        self.disable_movement("down")
                    elif event.key == pygame.K_DOWN and self.can_snake_go_down:
                        self.snake_absissa_increment = 0
                        self.snake_ordinate_increment = self.snake_block_size
                        self.disable_movement("up")
                    else:
                        continue

            if (
                self.snake_absissa >= self.display_size
                or self.snake_absissa < 0
                or self.snake_ordinate >= self.display_size
                or self.snake_ordinate < 0
            ):
                self.game_close = True

            self.update_game_frames()

        self.display.fill(colors.white)
        self.show_message("alert", "Bye!", colors.red)
        self.update_display()
        time.sleep(1)

        self.quit_game()


def main():
    snake = Snake()
    snake.run()


if __name__ == "__main__":
    main()

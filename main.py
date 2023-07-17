import random
import time

import pygame

from constants import colors


class Snake:
    def __init__(self):
        self.start_game()

    @property
    def clock(self):
        return pygame.time.Clock()

    @property
    def snake_block_size(self):
        return 25

    @property
    def snake_speed(self):
        return 7

    @property
    def display_width(self):
        return 800

    @property
    def display_height(self):
        return 600

    @property
    def snake_absissa(self):
        return self._snake_absissa

    @snake_absissa.setter
    def snake_absissa(self, value):
        self._snake_absissa = value

    @property
    def snake_absissa_increment(self):
        return self._snake_absissa_increment

    @snake_absissa_increment.setter
    def snake_absissa_increment(self, value):
        self._snake_absissa_increment = value

    @property
    def snake_ordinate(self):
        return self._snake_ordinate

    @snake_ordinate.setter
    def snake_ordinate(self, value):
        self._snake_ordinate = value

    @property
    def snake_ordinate_increment(self):
        return self._snake_ordinate_increment

    @snake_ordinate_increment.setter
    def snake_ordinate_increment(self, value):
        self._snake_ordinate_increment = value

    @property
    def snake_body_sections(self):
        return self._snake_body_sections

    @snake_body_sections.setter
    def snake_body_sections(self, value):
        self._snake_body_sections = value

    @property
    def snake_length(self):
        return self._snake_length

    @snake_length.setter
    def snake_length(self, value):
        self._snake_length = value

    @property
    def food_absissa(self):
        return self._food_absissa

    @food_absissa.setter
    def food_absissa(self, value):
        self._food_absissa = value

    @property
    def food_ordinate(self):
        return self._food_ordinate

    @food_ordinate.setter
    def food_ordinate(self, value):
        self._food_ordinate = value

    @property
    def game_over(self):
        return self._game_over

    @game_over.setter
    def game_over(self, value):
        self._game_over = value

    @property
    def game_close(self):
        return self._game_close

    @game_close.setter
    def game_close(self, value):
        self._game_close = value

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        self._display = value

    @property
    def alert_font(self):
        return self._alert_font

    @property
    def score_font(self):
        return self._score_font

    @property
    def initial_snake_absissa_position(self):
        return self.display_width / 2

    @property
    def initial_snake_ordinate_position(self):
        return self.display_height / 2

    def generate_display(self):
        self._display = pygame.display.set_mode(
            (self.display_width, self.display_height)
        )

    def update_display(self):
        return pygame.display.update()

    def generate_caption(self):
        return pygame.display.set_caption("Snake game by @crnvl96")

    def set_alert_font(self):
        self._alert_font = pygame.font.SysFont("bahnschrift", 25)

    def set_score_font(self):
        self._score_font = pygame.font.SysFont("comicsansms", 35)

    def show_message(self, font, msg, color):
        font_opts = {
            "alert": self.alert_font,
            "score": self.score_font,
        }

        self.display.blit(
            font_opts[font].render(msg, True, color),
            [
                self.initial_snake_absissa_position,
                self.initial_snake_ordinate_position,
            ],
        )

    def render_snake_body(self):
        for element in self.snake_body_sections:
            pygame.draw.rect(
                self.display,
                colors.black,
                [
                    element[0],
                    element[1],
                    self.snake_block_size,
                    self.snake_block_size,
                ],
            )

    def draw_block(
        self,
        color,
        snake_absissa_current_position,
        snake_ordinate_current_position,
    ):
        return pygame.draw.rect(
            self.display,
            color,
            [
                snake_absissa_current_position,
                snake_ordinate_current_position,
                self.snake_block_size,
                self.snake_block_size,
            ],
        )

    def start_game(self):
        self.game_over = False
        self.game_close = False
        self.snake_absissa = self.initial_snake_absissa_position
        self.snake_ordinate = self.initial_snake_ordinate_position

        self.snake_absissa_increment = 0
        self.snake_ordinate_increment = 0

        pygame.init()
        self.generate_display()
        self.update_display()
        self.generate_caption()
        self.set_alert_font()
        self.set_score_font()

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
            abs(self.snake_absissa - self.food_absissa) <= 5
            and abs(self.snake_ordinate - self.food_ordinate) <= 5
        ):
            self.food_absissa, self.food_ordinate = self.seed_food()
            self.snake_length += 1

        self.clock.tick(self.snake_speed)

    def seed_food(self):
        def seed(range):
            return (
                round(
                    random.randrange(0, range - self.snake_block_size)
                    / self.snake_block_size
                )
                * self.snake_block_size
            )

        return seed(self.display_width), seed(self.display_height)

    def quit_game(self):
        pygame.quit()
        quit()

    def show_score(self):
        value = self.score_font.render(
            "Your Score: " + str(self.snake_length - 1), True, colors.yellow
        )
        self.display.blit(value, [0, 0])

    def run(self):
        self.snake_body_sections = []
        self.snake_length = 1

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
                            self.start_game()
                            self.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake_absissa_increment = -self.snake_block_size
                        self.snake_ordinate_increment = 0
                    elif event.key == pygame.K_RIGHT:
                        self.snake_absissa_increment = self.snake_block_size
                        self.snake_ordinate_increment = 0
                    elif event.key == pygame.K_UP:
                        self.snake_absissa_increment = 0
                        self.snake_ordinate_increment = -self.snake_block_size
                    elif event.key == pygame.K_DOWN:
                        self.snake_absissa_increment = 0
                        self.snake_ordinate_increment = self.snake_block_size

            if (
                self.snake_absissa >= self.display_width
                or self.snake_absissa < 0
                or self.snake_ordinate >= self.display_height
                or self.snake_ordinate < 0
            ):
                self.game_close = True

            self.update_game_frames()

        self.show_message("alert", "Bye!", colors.red)
        pygame.display.update()
        time.sleep(1)

        self.quit_game()


snake = Snake()
snake.run()

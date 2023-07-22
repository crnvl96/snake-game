import pygame
from pygame import Rect

from constants import colors
from project import Snake, disable_movements, draw, show_message


def test_draw():
    pygame.init()
    snake = Snake()
    color = colors.black
    absissa = 0
    ordinate = 0
    rect = draw(snake, color, absissa, ordinate)
    assert isinstance(rect, Rect)
    assert rect.x == absissa
    assert rect.y == ordinate
    assert rect.width == snake.snake_block_size
    assert rect.height == snake.snake_block_size


def test_show_message():
    pygame.init()
    snake = Snake()
    font = "alert"
    message = "Test Message"
    color = colors.red
    text_rect = show_message(snake, font, message, color)
    assert isinstance(text_rect, Rect)
    assert text_rect.x == snake.initial_snake_absissa_position
    assert text_rect.y == snake.initial_snake_ordinate_position


def test_disable_movements():
    pygame.init()
    snake = Snake()
    direction = "up"
    disable_movements(snake, direction)
    assert snake.can_snake_go_up is False
    assert snake.can_snake_go_down is True
    assert snake.can_snake_go_left is True
    assert snake.can_snake_go_right is True

    direction = "down"
    disable_movements(snake, direction)
    assert snake.can_snake_go_up is True
    assert snake.can_snake_go_down is False
    assert snake.can_snake_go_left is True
    assert snake.can_snake_go_right is True

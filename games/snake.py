import pygame
import random
import sys
import winsound

# Инициализация Pygame
pygame.init()

# Константы экрана
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20

# Цвета
GRAPHITE = (54, 57, 63)
SOFT_GREEN = (120, 200, 120)
SOFT_ORANGE = (255, 165, 0)

# Создаём экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# FPS и начальные параметры змейки
clock = pygame.time.Clock()
snake = [(100, 100), (90, 100), (80, 100)]
direction = "RIGHT"
food_pos = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
            random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
food_spawn = True

def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(screen, SOFT_GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE), border_radius=2)

def draw_food(food_pos):
    pygame.draw.rect(screen, SOFT_ORANGE, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE), border_radius=8)

def game_over():
    font = pygame.font.SysFont('comicsans', 35)
    text = font.render('Новая игра -> Y .. Выйти -> Q', True, (255, 255, 255))
    screen.blit(text, (WIDTH // 10, HEIGHT // 2))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_y]:
                main()  # Перезапуск игры

def main():
    global snake, direction, food_pos, food_spawn
    snake = [(100, 100), (90, 100), (80, 100)]
    direction = "RIGHT"
    food_pos = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
    food_spawn = True

    while True:
        screen.fill(GRAPHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Управление змейкой
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != "DOWN":
            direction = "UP"
        if keys[pygame.K_DOWN] and direction != "UP":
            direction = "DOWN"
        if keys[pygame.K_LEFT] and direction != "RIGHT":
            direction = "LEFT"
        if keys[pygame.K_RIGHT] and direction != "LEFT":
            direction = "RIGHT"

        # Обновление позиции змейки
        x, y = snake[0]
        if direction == "UP":
            y -= CELL_SIZE
        if direction == "DOWN":
            y += CELL_SIZE
        if direction == "LEFT":
            x -= CELL_SIZE
        if direction == "RIGHT":
            x += CELL_SIZE
        new_head = (x, y)

        # Столкновение с границами и самим собой
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake:
            game_over()

        # Проверка поедания еды
        snake.insert(0, new_head)
        if new_head == food_pos:
            food_spawn = False
        else:
            snake.pop()

        # Спавн новой еды
        if not food_spawn:
            food_pos = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
            food_spawn = True

        # Отрисовка змейки и еды
        draw_snake(snake)
        draw_food(food_pos)

        # Обновление экрана
        pygame.display.update()
        clock.tick(10)

# Запуск игры
main()
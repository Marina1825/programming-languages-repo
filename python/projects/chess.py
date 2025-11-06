import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
FPS = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

def initialize_game():
    snake = [[WIDTH // 2, HEIGHT // 2]]
    direction = "RIGHT"
    food = generate_food(snake)
    score = 0
    game_over = False
    return snake, direction, food, score, game_over

def generate_food(snake):
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        if [x, y] not in snake:
            return [x, y]

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (WIDTH, y))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, (0, 200, 0), (segment[0], segment[1], CELL_SIZE, CELL_SIZE), 1)
    
    if snake:
        head = snake[0]
        pygame.draw.rect(screen, (0, 180, 0), (head[0], head[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

def show_score(score):
    score_text = font.render(f"Счет: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def show_game_over(score):
    screen.fill(BLACK)
    
    game_over_text = font.render("ИГРА ОКОНЧЕНА!", True, RED)
    score_text = font.render(f"Финальный счет: {score}", True, WHITE)
    restart_text = font.render("Нажмите R для рестарта", True, WHITE)
    quit_text = font.render("Нажмите Q для выхода", True, WHITE)
    
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 60))
    screen.blit(score_text, (WIDTH // 2 - 120, HEIGHT // 2 - 20))
    screen.blit(restart_text, (WIDTH // 2 - 140, HEIGHT // 2 + 20))
    screen.blit(quit_text, (WIDTH // 2 - 120, HEIGHT // 2 + 60))

def main():
    snake, direction, food, score, game_over = initialize_game()
    grow_snake = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        snake, direction, food, score, game_over = initialize_game()
                        grow_snake = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                else:
                    if event.key == pygame.K_UP and direction != "DOWN":
                        direction = "UP"
                    elif event.key == pygame.K_DOWN and direction != "UP":
                        direction = "DOWN"
                    elif event.key == pygame.K_LEFT and direction != "RIGHT":
                        direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction != "LEFT":
                        direction = "RIGHT"
        
        if not game_over:
            head = snake[0].copy()
            if direction == "UP":
                head[1] -= CELL_SIZE
            elif direction == "DOWN":
                head[1] += CELL_SIZE
            elif direction == "LEFT":
                head[0] -= CELL_SIZE
            elif direction == "RIGHT":
                head[0] += CELL_SIZE
            
            if (head[0] < 0 or head[0] >= WIDTH or 
                head[1] < 0 or head[1] >= HEIGHT or
                head in snake):
                game_over = True
            
            snake.insert(0, head)
            
            if head == food:
                score += 1
                grow_snake = True
                food = generate_food(snake)
            
            if not grow_snake:
                snake.pop()
            else:
                grow_snake = False
            
            screen.fill(BLACK)
            draw_grid()
            draw_snake(snake)
            draw_food(food)
            show_score(score)
        else:
            show_game_over(score)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
import pygame 
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("super maze")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()
FPS = 30

CELL_SIZE = 30
PLAYER_SIZE = 20

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
]

player_pos = [1, 1]
exit_pos = [18, 19]
win = False

def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if cell == 1:
                pygame.draw.rect(screen, RED, rect)
            elif cell == 2:
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)
                pygame.draw.rect(screen, WHITE, rect, 1)

def can_move(x, y):
    if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
        return False
    return maze[y][x] != 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not win:
            new_x, new_y = player_pos[0], player_pos[1]
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                new_x -= 1
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                new_x += 1
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                new_y -= 1
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                new_y += 1
            elif event.key == pygame.K_r:
                player_pos = [1, 1]
                win = False
            if can_move(new_x, new_y):
                player_pos = [new_x, new_y]
            if player_pos[0] == exit_pos[0] and player_pos[1] == exit_pos[1]:
                win = True

    screen.fill(BLACK)
    draw_maze()
    player_screen_x = player_pos[0] * CELL_SIZE + CELL_SIZE // 2
    player_screen_y = player_pos[1] * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, BLUE, (player_screen_x, player_screen_y), PLAYER_SIZE // 2)

    if win:
        win_text = pygame.font.Font(None, 72).render("ПОБЕДА!", True, YELLOW)
        text_rect = win_text.get_rect(center=(WIDTH // 2, 50))
        screen.blit(win_text, text_rect)
        restart_text = pygame.font.Font(None, 36).render("Нажми R для перезапуска", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, 100))
        screen.blit(restart_text, restart_rect)
    controls_text = pygame.font.Font(None, 24).render("Стрелки - движение, R - рестарт", True, WHITE)
    screen.blit(controls_text, (10, HEIGHT - 30))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
    
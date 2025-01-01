import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Konstanta
WIDTH, HEIGHT = 800, 600
BALL_SPEED = [4, 4]
PADDLE_SPEED = 6
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inisialisasi layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game - Bola Lebih Besar")

# Objek permainan
ball = pygame.Rect(WIDTH // 2 - 25, HEIGHT // 2 - 25, 50, 50)  # Bola lebih besar
player1 = pygame.Rect(20, HEIGHT // 2 - 70, 10, 140)
player2 = pygame.Rect(WIDTH - 30, HEIGHT // 2 - 70, 10, 140)

# Kecepatan
ball_speed = BALL_SPEED
player1_speed = 0
player2_speed = 0

# Skor
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 74)

# Fungsi menggambar
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    score_text = font.render(f"{player1_score}  {player2_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 50, 10))

# Logika bola
def ball_movement():
    global ball_speed, player1_score, player2_score

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] = -ball_speed[0]

    if ball.left <= 0:
        player2_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        player1_score += 1
        reset_ball()

# Reset bola
def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed[0] *= -1

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed = -PADDLE_SPEED
            if event.key == pygame.K_s:
                player1_speed = PADDLE_SPEED
            if event.key == pygame.K_UP:
                player2_speed = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                player2_speed = PADDLE_SPEED

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                player1_speed = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player2_speed = 0

    # Gerakan paddle
    player1.y += player1_speed
    player2.y += player2_speed

    # Batas paddle
    player1.y = max(min(player1.y, HEIGHT - player1.height), 0)
    player2.y = max(min(player2.y, HEIGHT - player2.height), 0)

    # Pergerakan bola
    ball_movement()

    # Gambar objek
    draw_objects()

    # Perbarui layar
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

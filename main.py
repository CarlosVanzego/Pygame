import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT  = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Wars")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
BLAST_WIDTH = 10
BLAST_HEIGHT = 20
BLAST_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, blasts):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "blue", player)

    for blast in blasts:
        pygame.draw.rect(WIN, "red", blast)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    blast_add_increment = 2000
    blast_count = 0

    blasts = []
    hit = False

    while run:
        blast_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if blast_count > blast_add_increment:
            for _ in range(3):
                blast_x = random.randint(0, WIDTH - BLAST_WIDTH)
                blast = pygame.Rect(blast_x, -BLAST_HEIGHT, BLAST_WIDTH, BLAST_HEIGHT)
                blasts.append(blast)

            blast_add_increment = max(200, blast_add_increment - 50)
            blast_count = 0    
              

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for blast in blasts[:]:
            blast.y += BLAST_VEL
            if blast.y > HEIGHT:
              blasts.remove(blast) 
            elif blast.y + blast.height >= player.y and blast.colliderect(player):
                blasts.remove(blast)
                hit = True
                break     

        if hit:
            lost_text = FONT.render("YOU LOST!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break     
                
            
        draw(player, elapsed_time, blasts)    
            
    pygame.QUIT()    

if __name__ == "__main__":
    main()        
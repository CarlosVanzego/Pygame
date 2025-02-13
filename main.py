# I start by importing the 'pygame' module; Pygame is a set of Python modules designed for writing games. It is written on top of the SDL (Simple DirectMedia Layer) library. This allows me to create fully featured games and multimedia programs in the python language.
import pygame
# Then I am imporing the 'time' module; the time module provides various functions to manipulate time values.
import time
# lastly, I am importing the 'random' module, this module allows me to generate random variables.
import random
pygame.font.init()
# Here I am setting up my pygame window; This is where I am drawing up the draw different objects of the game, and having the game running. For the window you need a width and a height so I wrote that here and set the width equal to 1000 and the height equal to 800. I wrote these each in all caps to make it clear that these are constant values and I do not want them to change; These numbers are in pixels.
WIDTH, HEIGHT  = 1000, 800
# 'WIN' stands for window, and I set this equal to pygame.display.set_mode then passed a tuple with the width and the height.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Here I am setting the caption that will display in the game window by using pygame.set.set_caption and the passing the string 'Galaxy Wars' which is the name of my game.
pygame.display.set_caption("Galaxy Wars")
# this line is for the background image of the game. 'BG' is a constant variable I created that is short for "background". I wrote pygame.transform.scale and passed the image to scale the image; I wanted the image to scale the size of the whoel screen so I passed 'WIDTH, HEIGHT'. I wrote pygame.image.load to load the image that I am using for the game that is within the 'bg.jpeg' file.
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))
# I created a constant variable called PLAYER_WIDTH (this is the width of the player) and I set it equal to 40.
PLAYER_WIDTH = 40
# I created a constant variable called PLAYER_HEIGHT (this is the height of the player) and I set it equal to 60.
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
BLAST_WIDTH = 10
BLAST_HEIGHT = 20
BLAST_VEL = 3
# Here I am setting the font of the text on the screen.
FONT = pygame.font.SysFont("comicsans", 30)
# I created a function called 'draw' where I am drawing the background image onto the screen. To do this I use the 'WIN' variable and '.blit'; Blit is a special method that you use when you want to draw an image or "surface" onto the screen (it is short for "Block Image Transfer" [this is an operation that coopies a rectangular block of pixels from one memory location to another]). After blit I am passing the coordiantes of the top left corner of the image, this is so that the image will cover the entire screen.
def draw(player, elapsed_time, blasts):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "yellow", player)

    for blast in blasts:
        pygame.draw.rect(WIN, "red", blast)
    # this line will refresh the display so that any draws that I do will be applied an put onto the screen. Everytime I update, it takes all of the draws and applies them. If I did not have this line then nothing would happen on the screen.
    pygame.display.update()
# I defined the function 'main', this is where the main game logic exists. Inside of this is the main game loop which allows the game to continue running while someone is playing. 
def main():
    run = True
    # I created the player variable to create the player for the game. pygame.Rect is just a rectanlge, after this I am passing the x and y positions along with the width and height of my player. Inside this I am passing the starting location of the player; 200 is just an arbitrary x coordinate; I use 'HEIGHT' which is the height of the screen, and then - PLAYER_HEIGHT(this gives me the top left corner where I draw the player).
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    blast_add_increment = 2000
    blast_count = 0

    blasts = []
    hit = False
    # Here I used a while loop containing the 'run' variable; This is the m
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
              
        # pygame.event.get creates a list that contains all the events that have occured in the last iteration of this while loop.
        for event in pygame.event.get():
            # Then I am checking for the x button event
            if event.type == pygame.QUIT:
                # this line ends the while loop.
                run = False
                # this line breaks out of the while loop because there is no need to continue checking the events if the user has hit the quit button.
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
    # this line closes the pygame window. 
    pygame.QUIT()    
# this line makes sure that I am directly running the main.py file and not importing because if I was importing this, or if I did not have this line, and I were to import the main.py file from another python file, Python would start running this game; When I only want this to run if I directly run the 'main.py' file. In short, this just checks to make sure I am running the main.py file directly.
if __name__ == "__main__":
    # this line calls the 'main' function.
    main()        
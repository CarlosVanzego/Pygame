# First I am importing the pygame module.
import pygame 
# Here I am setting the width and height for the surface of the game.
WIDTH, HEIGHT = 900, 500
# WIN is the window of the game.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# this line creates the caption that will appear at the top of the game window.
pygame.display.set_caption("Third Game!")

def main():

  run = True
  # this is the main game while loop that will start the game and allow it to continuosly run until the game is over.
  while run:
    # This line is giving me a list of all the events happening in the game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          # this line will end the game.
           run = False

    WIN.fill("Red")       
        
    pygame.quit()
# this line ensures that when I run this file, it will only run the main function from this file and not from anywhere else. Making it so the game can only be ran from this file directly. "__name__" is the name of the file, and "__main__" is main file that is run.
if __name__ == "__main__":
   main()



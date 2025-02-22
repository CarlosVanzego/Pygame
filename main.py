# Space Dodge Game
# 
# 
# 
# I start by importing the 'pygame' module; Pygame is a set of Python modules designed for writing games. It is written on top of the SDL (Simple DirectMedia Layer) library. This allows me to create fully featured games and multimedia programs in the python language.
import pygame
# Then I am imporing the 'time' module; the time module provides various functions to manipulate time values.
import time
# lastly, I am importing the 'random' module, this module allows me to generate random variables.
import random
# here I am initilaizing the font module, this is a requirement from pygame.
pygame.font.init()
# Here I am setting up my pygame window; This is where I am drawing up the draw different objects of the game, and having the game running. For the window you need a width and a height so I wrote that here and set the width equal to 1000 and the height equal to 800. I wrote these each in all caps to make it clear that these are constant values and I do not want them to change; These numbers are in pixels.
WIDTH, HEIGHT  = 1000, 800
# 'WIN' stands for window, and I set this equal to pygame.display.set_mode then passed a tuple with the width and the height.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Here I am setting the caption that will display in the game window by using pygame.set.set_caption and the passing the string 'Space Dodge' which is the name of my game.
pygame.display.set_caption("Space Dodge")
# this line is for the background image of the game. 'BG' is a constant variable I created that is short for "background". I wrote pygame.transform.scale and passed the image to scale the image; I wanted the image to scale the size of the whoel screen so I passed 'WIDTH, HEIGHT'. I wrote pygame.image.load to load the image that I am using for the game that is within the 'bg.jpeg' file.
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))
# I created a constant variable called PLAYER_WIDTH (this is the width of the player) and I set it equal to 40.
PLAYER_WIDTH = 40
# I created a constant variable called PLAYER_HEIGHT (this is the height of the player) and I set it equal to 60.
PLAYER_HEIGHT = 60
# I created a contant variable called "PLAYER_VEL" (short for player velocity); I set it equal to '5' so that it will move the player 5 pixels in whichever direction.
PLAYER_VEL = 5
# this line is the width of the blasts.
BLAST_WIDTH = 10
# this line is the height of the blasts.
BLAST_HEIGHT = 20
# this line is the velocity of the blasts.
BLAST_VEL = 3
# Here I am creating a font object to set the font of the text on the screen. I used the FONT constant variable as I do not want this to change, then I assigned 'pygame.font.SysFont' and passed the font 'comicsans', and the size of the font which I set to 30.
FONT = pygame.font.SysFont("comicsans", 30)
# I created a function called 'draw' where I am drawing the background image onto the screen. To do this I use the 'WIN' variable and '.blit'; Blit is a special method that you use when you want to draw an image or "surface" onto the screen (it is short for "Block Image Transfer" [this is an operation that coopies a rectangular block of pixels from one memory location to another]). After blit I am passing the coordiantes of the top left corner of the image, this is so that the image will cover the entire screen. I am also drawing the player, elasped time, and blasts on the screen.
def draw(player, elapsed_time, blasts):
    WIN.blit(BG, (0, 0))
    # Here I created a variable called time_text and assigned it FONT.render and passed the text that I want to render on the screen which is "Time: " showing the elapsed time since the start of the game. I am using an f string which allows me to embed a variable directly inside of a string and have it rendered as a string. Inside this I have the elapsed_time variable inside the round function which will round the time to the nearest second. "1" is for anti-aliasing which makes the text look better, and "white" is just the color I chose for the text.
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    # Here I am rendering the text on the screen. (10,10) is the position I am going to blit the text at, this allows for some padding from the top-left corner of the screen (10 pixels x, 10 pixels y) so this moves it slightly off the edge of the screen.
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
    # I created the clock variable and assigned it pygame.time.Clock(),  
    clock = pygame.time.Clock()
    # This start_time variable allows me to see how much time has elapsed since the start of the game; time.time() is giving me the current time once the game has started.
    start_time = time.time()
    elapsed_time = 0
    # this is line adds the blasts every 200 milliseconds.
    blast_add_increment = 2000
    # this is just telling me when to add the next blast to the screen.
    blast_count = 0
    # here I am storing all the blasts that will end up on the screen; then they will be drawn onto the screen.
    blasts = []
    # this is so that when this variable is checked later on, there wont be an error because 'hit' is undefined.
    hit = False
    # Here I used a while loop containing the 'run' variable; This is the m
    while run:
        # blast_count is counting how many seconds have occured since the last clock tick. clock.tick(60) is an object I created to set the maximum number of frames per second that I want the While Loop to be running.
        blast_count += clock.tick(60)
        # here I am storing the time that I started the while loop, then everytime there is an iteration, I am getting the current time and subtracting that from the start time which will give me the number of seconds that has elapsed since the start of the game (or while loop).
        elapsed_time = time.time() - start_time
        # this if statement is for if the blast count is zero, and 2000 ms has passed, then I am going to add more blasts to the screen.  
        if blast_count > blast_add_increment:
            # this for loop is adding 1 blast to the screen at a time.
            for _ in range(1):
                # I created the blast_x variable and assigned it an instance of the random module so that I can randomly position the blasts on the screen. random is the module, randint is a variable for a random integer in the range of 0 and the width minus the width of the screen and the blast width.
                blast_x = random.randint(0, WIDTH - BLAST_WIDTH)
                # I created the blast variable and assigned it pygame.rect which is the rectangular shape of the blast; then I pass blast_x which is the blast on the x-axis; I use -BLAST_HEIGHT so that the blast will start slightly above the top of the screen and then as it moves down, it will appear to enter the top of the screen.
                blast = pygame.Rect(blast_x, -BLAST_HEIGHT, BLAST_WIDTH, BLAST_HEIGHT)
                # then I am adding the star to the blasts list.
                blasts.append(blast)
            # this line adjusts the blast increments so that it will generate blasts faster; the 'max' function picks the maximum value out of 'blast_add_increment - 50' and 200; this allows for the minimum blast add increment I have is 200; This ulitmately is decreasing the increments at which the blast appear on the screen over time (subtracting by 50 from the original 2000).
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
        # I created the variable 'keys' and assigned it pygame.key.get_pressed(), this will give a dictionary of all the keys the user has pressed, and tell me if they have pressed them or not.
        keys = pygame.key.get_pressed()
        # This is an if statement for if a user presses the left arrow key; 'K_LEFT' is the code for the left arrow key. is a guard clause I made to ensure that the player can not move off of the screen. This ensures that I can subtract the players position and as long as the player's x coordinate is greater than 0, then we can continue to subtract; If it is not greater than 0 then it will not allow the player to move.
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            # then I am subtracting player.x which is the player on the x-axis, and I am subtracting the player velocity (which I defined above). The reason I am subtracting x is so that the player can move left, by subtracting the x coordiante, I am moving the player closer to the (0,0) coordinate. The player velocity is set to 5, so this line moves the player 5 pixels to the left.
            player.x -= PLAYER_VEL
        # This is an if statement for if a user presses the left arrow key; 'K_RIGHT' is the code for the right arrow key. This differs from the line above because here I need to account for the fact that player.x is the top left-hand corner of the player, and I need to account for the width.
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            # then I am adding to the x coordinate of player.x, and I am adding to the player velocity (which I defined above). The reason I am subtracting x is so that the player can move right, by subtracting the x coordiante, I am moving the player closer to the (0,0) coordinate. The player velocity is set to 5, so this line moves the player 5 pixels to the right.
            player.x += PLAYER_VEL
        # here I am interating through a copy of the blasts list.
        for blast in blasts[:]:
            # this line moves the blast downard in the 'y' direction (vertically) by the velocity I specified above.
            blast.y += BLAST_VEL
            # here I am saying if the blast.y is greater than the height of the sceen then..
            if blast.y > HEIGHT:
              # ..then I remove the blast.
              blasts.remove(blast) 
            # here I am saying if the blast.y is equal to the player.y AND the blast collides(using collide.rect) with the player (specifically at the bottom of the screen)... 
            elif blast.y + blast.height >= player.y and blast.colliderect(player):
                # .. then I am going to remove the blast because it hit the player.
                blasts.remove(blast)
                # then I am setting hit equal to true because I will look at this variable later to see if the player has been hit by a blast..
                hit = True
                # and finally breaking out of the loop.
                break     
        # this is the an if statement to check if the player was hit by a blast. 
        if hit:
            # I crreated the lost_text variable and assigned it a font with the message "YOU LOST!"
            lost_text = FONT.render("YOU LOST!", 1, "white")
            # this puts the message in the middle of the screen by taking the full width of the text object, divide that by 2, then subtract that from the width/2
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            # this line updates the sceen once the collision occurs
            pygame.display.update()
            # then I am delaying the update for 4000 ms so you can see the text before..
            pygame.time.delay(4000)
            # breaking out of the loop and ending the game.
            break     
                
        # this draw function draws the player, the elapsed time, and the blasts on the screen.
        draw(player, elapsed_time, blasts)    
    # this line closes the pygame window. 
    pygame.QUIT()    
# this line makes sure that I am directly running the main.py file and not importing because if I was importing this, or if I did not have this line, and I were to import the main.py file from another python file, Python would start running this game; When I only want this to run if I directly run the 'main.py' file. In short, this just checks to make sure I am running the main.py file directly.
if __name__ == "__main__":
    # this line calls the 'main' function.
    main()        
import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# This sets the name of the window
pygame.display.set_caption('CMSC 150 is cool')

clock = pygame.time.Clock()

# Before the loop, load the sounds:
click_sound = pygame.mixer.Sound("laser5.ogg")

# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("player.gif").convert()

done = False

x = 0
y = 0
x_speed = 0
y_speed = 0

while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                click_sound.play()
            elif event.key == pygame.K_LEFT:
                x_speed = -10
            elif event.key == pygame.K_RIGHT:
                x_speed = 10
            elif event.key == pygame.K_UP:
                y_speed = -10
            elif event.key == pygame.K_DOWN:
                y_speed = 10
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    # Copy image to screen:
    screen.blit(background_image, background_position)

    x += x_speed
    y += y_speed
    # Get the current mouse position. This returns the position
    # as a list of two numbers.

    # Copy image to screen:
    screen.blit(player_image, [x, y])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
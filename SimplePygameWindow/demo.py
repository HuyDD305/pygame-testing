#This file is for practicing and testing pygame
#!/usr/bin/python3.4  # Specifies the Python interpreter version to use
# setup #
import pygame, sys  # Import pygame and system modules

# setup pygame/window #
mainClock = pygame.time.Clock()  # Create a clock object to manage the frame rate
from pygame.locals import *  # Import constants and functions from pygame.locals

pygame.init()  # Initialize all pygame modules
pygame.display.set_caption('Physics Explanation')  # Set the title of the window
screen = pygame.display.set_mode((500, 500), 0, 32)  # Create a 500x500 window

player = pygame.Rect(100, 100, 40, 80)  # Define a rectangle for the player (x, y, width, height)

tiles = [pygame.Rect(200, 350, 50, 50), pygame.Rect(260, 320, 50, 50)]  # List of tiles (obstacles)

# Function to test for collisions between the player and tiles
def collision_test(rect, tiles):
    collisions = []  # List to store collided tiles
    for tile in tiles:  # Loop through all tiles
        if rect.colliderect(tile):  # Check if the rectangle collides with a tile
            print("Collide")
            collisions.append(tile)  # Add the tile to the collision list
    return collisions  # Return the list of collided tiles

# Function to handle movement and collision resolution
def move(rect, movement, tiles):  # rect = player, movement = [x_change, y_change]
    rect.x += movement[0]  # Move the rectangle horizontally
    collisions = collision_test(rect, tiles)  # Check for horizontal collisions
    for tile in collisions:  # Resolve horizontal collisions
        if movement[0] > 0:  # Moving right
            rect.right = tile.left  # Align player to the left of the tile
        if movement[0] < 0:  # Moving left
            rect.left = tile.right  # Align player to the right of the tile
    rect.y += movement[1]  # Move the rectangle vertically
    collisions = collision_test(rect, tiles)  # Check for vertical collisions
    for tile in collisions:  # Resolve vertical collisions
        if movement[1] > 0:  # Moving down
            rect.bottom = tile.top  # Align player to the top of the tile
        if movement[1] < 0:  # Moving up
            rect.top = tile.bottom  # Align player to the bottom of the tile
    return rect  # Return the updated rectangle

# Movement control flags
right = False  # Moving right
left = False  # Moving left
up = False  # Moving up
down = False  # Moving down

# loop #
while True:  # Main game loop

    # clear display #
    screen.fill((0, 0, 0))  # Fill the screen with black to clear previous frames

    movement = [0, 0]  # Reset movement to no change
    if right == True:  # If moving right
        movement[0] += 5  # Add 5 to horizontal movement
    if left == True:  # If moving left
        movement[0] -= 5  # Subtract 5 from horizontal movement
    if up == True:  # If moving up
        movement[1] -= 5  # Subtract 5 from vertical movement
    if down == True:  # If moving down
        movement[1] += 5  # Add 5 to vertical movement

    player = move(player, movement, tiles)  # Update player position with movement and collision handling

    pygame.draw.rect(screen, (255, 255, 255), player)  # Draw the player as a white rectangle

    for tile in tiles:  # Draw each tile
        pygame.draw.rect(screen, (255, 0, 0), tile)  # Draw tiles as red rectangles

    # event handling #
    for event in pygame.event.get():  # Process all events
        if event.type == QUIT:  # If the quit event is triggered
            pygame.quit()  # Uninitialize all pygame modules
            sys.exit()  # Exit the program
        if event.type == KEYDOWN:  # If a key is pressed
            if event.key == K_RIGHT:  # Right arrow key
                right = True  # Start moving right
            if event.key == K_LEFT:  # Left arrow key
                left = True  # Start moving left
            if event.key == K_DOWN:  # Down arrow key
                down = True  # Start moving down
            if event.key == K_UP:  # Up arrow key
                up = True  # Start moving up
        if event.type == KEYUP:  # If a key is released
            if event.key == K_RIGHT:  # Right arrow key
                right = False  # Stop moving right
            if event.key == K_LEFT:  # Left arrow key
                left = False  # Stop moving left
            if event.key == K_DOWN:  # Down arrow key
                down = False  # Stop moving down
            if event.key == K_UP:  # Up arrow key
                up = False  # Stop moving up

    # update display #
    pygame.display.update()  # Update the display with new frame
    mainClock.tick(60)  # Maintain frame rate at 60 FPS

import pygame
from Commodore_64_color_palettes import *
from Spritesheet import *



pygame.init()
#settings
screen_width = 640  
screen_height = 480
sprite_height=32
sprite_width=32
scale=1 

TITLE = "Flying Toaster"
BGCOLOR = CC_BLACK

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption(TITLE)


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

spritesheet0 = Spritesheet("toaster0.png", sprite_height=sprite_height
                           , sprite_width=sprite_width, sprites_per_row=1
                           , colorkey=(0,0,0) ,scale=scale)
spritesheet1 = Spritesheet("toaster1.png", sprite_height=sprite_height
                           , sprite_width=sprite_width, sprites_per_row=1
                           , colorkey=(0,0,0) ,scale=scale)
spritesheet2 = Spritesheet("toaster2.png", sprite_height=sprite_height
                           , sprite_width=sprite_width, sprites_per_row=1
                           , colorkey=(0,0,0) ,scale=scale)

t0 = spritesheet0.load_animation(0,1)
t1 = spritesheet1.load_animation(0,1)
t2 = spritesheet2.load_animation(0,1)

toaster=[]
toaster.append(t0[0])
toaster.append(t1[0])
toaster.append(t2[0])
toaster.append(t1[0])


animation_index = 0
animation_max_index = 3
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
            
    # Clear the screen
    screen.fill(BGCOLOR)


    x = screen_width //2 - (sprite_height * scale)//2
    y = screen_height //2 - (sprite_width * scale) //2

    screen.blit(toaster[animation_index], ((x,y)))
    
    animation_index = animation_index +1
    
    if animation_index > animation_max_index:
        animation_index = 0


    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(8)

pygame.quit()

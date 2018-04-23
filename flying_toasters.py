import pygame
import random
from Commodore_64_color_palettes import *
from datetime import datetime
random.seed(datetime.now())

#settings
TITLE = "Flying Toasters"
BGCOLOR = CC_BLACK
screen_width = 640  
screen_height = 480
sprite_height=64
sprite_width=64
scale=1

class Toast(pygame.sprite.Sprite):
    def __init__(self):
        super(Toast,self).__init__()
        
        self.image = pygame.image.load("toast64x64.png").convert()
        self.image.set_colorkey(CC_BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        self.rect.x -= 1

        if self.rect.y > screen_height + sprite_height or self.rect.x < 0-sprite_width:
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randrange(screen_width)
        self.rect.y = random.randrange(screen_height)

        coin_flip = random.randrange(2)
            
        if coin_flip == 1:
            self.rect.x = screen_width+sprite_width
        else:
            self.rect.y = 0-sprite_height

        for sprt in all_sprites_list:
            if sprt.rect != self.rect: 
                if pygame.sprite.collide_rect(self,sprt):
                    # Collision Detected
                    #print("!")
                    self.reset_position()

class Toaster(Toast):
    animation_frames=[]
    animation_index = 0
    
    def load_animations (self):
        self.animation_frames.append(pygame.image.load("toaster0_64x64.png").convert())
        self.animation_frames.append(pygame.image.load("toaster1_64x64.png").convert())
        self.animation_frames.append(pygame.image.load("toaster2_64x64.png").convert())
        self.animation_frames.append(pygame.image.load("toaster3_64x64.png").convert())
        return self.animation_frames
    
    def __init__(self):

        # Call the parent class (Sprite) constructor
        super(Toaster,self).__init__()
       
        # Load the image
        self.load_animations()
        self.animation_index = random.randrange(3)
        self.image = self.animation_frames[self.animation_index]

        # Set our transparent color
        self.image.set_colorkey(CC_BLACK)

        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        self.animation_index = self.animation_index + 1
        if self.animation_index > 3:
            self.animation_index = 0
        self.image = self.animation_frames[self.animation_index]
        
        self.rect.y += 1
        self.rect.x -= 1

        if self.rect.y > screen_height + sprite_height or self.rect.x < 0-sprite_width:
            self.reset_position()

          
pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption(TITLE)

all_sprites_list = pygame.sprite.Group()

while len(all_sprites_list) < 12:
    toaster =  Toaster()
    toaster.rect.x = random.randrange(screen_width)
    toaster.rect.y = random.randrange(screen_height)
    if pygame.sprite.spritecollideany(toaster, all_sprites_list, collided = None)  == None:
        all_sprites_list.add(toaster)
    #else:
        # Collision Detected
        # print("!")
    
while len(all_sprites_list) < 15:
    toast = Toast()
    toast.rect.x = random.randrange(screen_width)
    toast.rect.y = random.randrange(screen_height)
    if pygame.sprite.spritecollideany(toast, all_sprites_list, collided = None)  == None:
        all_sprites_list.add(toast)
    #else:
        # Collision Detected
        #print("!")
        
#print(len(all_sprites_list))


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
            
    # Clear the screen
    screen.fill(BGCOLOR)

    all_sprites_list.update()
    
    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(8)

pygame.quit()

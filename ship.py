import pygame
from settings import Settings

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings   #attributes
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect.
    
        self.original_image = pygame.image.load('/home/elishadominic/Downloads/rocket-306209_1280.bmp')
        self.image = pygame.transform.scale(self.original_image,(50,50))
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom centre of the screen 
        self.rect.midbottom = self.screen_rect.midbottom 
        
        # store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)
        
      
        # movement flags; start with a ship thats not moving 
        
        self.moving_right = False #attribute 
        self.moving_left = False
        
    def update(self):
            """update the ships position based on the movement flags"""
            # update the ships x value instead of rect
            if self.moving_right:
                self.rect.x += self.settings.ship_speed
            if self.moving_left:
                self.rect.x -= self.settings.ship_speed
                
            if self.moving_right and self.rect.right < self.screen_rect.right: 
                self.x += self.settings.ship_speed 
            if self.moving_left and self.rect.left > 0: 
                self.x -= self.settings.ship_speed 
                
            self.rect.x = self.x 
            
        # Adjust ships position 
    # self.rect.y = self.screen_rect.bottom - self.rect.height
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)              

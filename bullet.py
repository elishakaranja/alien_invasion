import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage the bullets fired from ship"""
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        # Initialize game attributes
        self.screen = ai_game.screen  # Setting which screen it belongs to 
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color 
        
        # Create a bullet rect at (0,0) and then set the correct position 
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's position as a float 
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up the screen"""
        # Update the y value based on the settings, i.e., update the position of the bullet
        self.y -= self.settings.bullet_speed 
        
        # Update the rect position 
        self.rect.y = self.y 
h
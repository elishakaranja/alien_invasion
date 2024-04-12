import pygame 
from settings import Settings 

class Mario:
    """overall class to manage the game behavious"""
    def __init__(self, ai_game):
     """initialize game"""
     self.screen = ai_game.screen
     self.screen_rect = ai_game.screen.getaa_rect()
     self.settings = Settings()
     # load image of mario and get its
     self.image = pygame.image.load('/home/elishadominic/Downloads/Ph03nyx-Super-Mario-Paper-Mario.256.png')
     self.rect = self.image.get_rect()
     self.bg_color = self.settings.bg_color
     
    #  Position mario at the centre of the screen 
    self.rect.centre = self.screen_rect.centre 
    
    
    def blitme(self):
        """draw mario at his current location"""
        self.screen.blit(self.image, self.rect)
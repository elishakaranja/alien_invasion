import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()   
        self.settings = Settings()
        # Set up the display
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        # set background color
        self.bg_color = self.settings.bg_color
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   
                    sys.exit()
                    
            # Redraw the screen during each pass through loop.
            self.screen.fill(self.settings.bg_color)
                    
            # Make the mostrecently drawn screen visible 
            pygame.display.flip()
            
if __name__ =='__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
                
        
        
        
    
    

    
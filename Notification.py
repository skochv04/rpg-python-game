from Settings import *

# create a class for the notification that will be displayed on the screen. Notification appears in a rectangle that scrolls
# from the top of the screen to chosen position and then disappears
class Notification(pygame.sprite.Sprite):
    def __init__(self, message, y, font_size=30, color=(255, 255, 255), background_color=(0, 0, 0), time=50):
        super().__init__()

        self.message = message
        self.x = WINDOW_WIDTH//2
        self.y = y
        self.font_size = font_size
        self.color = color
        self.background_color = background_color
        self.time = time

        # Create text for the notification
        font = pygame.font.Font(None, font_size)
        self.text = font.render(message, True, color)
        self.x -= self.text.get_width() // 2

        # Create rectangle for the notification with black border
        self.image = pygame.Surface((self.text.get_width() + 10, self.text.get_height() + 10))
        self.image.fill(background_color)
        pygame.draw.rect(self.image, color, (0, 0, self.text.get_width() + 10, self.text.get_height() + 10), 2)

        self.time_passed = 0

    def update(self, dt):
        self.time_passed += dt.get() * 1000
        if self.time_passed >= self.time:
            return True

    def draw(self, display_surface):
        display_surface.blit(self.image, (self.x, self.y))
        display_surface.blit(self.text, (self.x + 5, self.y + 5))


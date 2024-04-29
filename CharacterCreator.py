from Settings import *
from Spritessheet import SpritesSheet

def create_character():
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(WINDOW_WIDTH/2 - 110, 150, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    current_skin = 0
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    text = ''
    default_text = font.render("Nazwa Postaci", True, color)
    while True:
        for event in pygame.event.get():
            # Obsługa zamykania okna
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return text, current_skin
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

                if event.key == pygame.K_LEFT:
                    current_skin = (current_skin - 1) % 8
                elif event.key == pygame.K_RIGHT:
                    current_skin = (current_skin + 1) % 8

        # Rysowanie okienka z nazwą
        display_surface.fill((30, 30, 30))
        if len(text) == 0:
            txt_surface = default_text
        else:
            txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        display_surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(display_surface, color, input_box, 2)

        # Rysowanie obecnej postaci
        my_spritesheet = SpritesSheet(join('graphics', 'player', f'{current_skin + 1}', 'texture.png'))
        sprite_down = my_spritesheet.parse_sprite('2.png')
        skin_view = pygame.transform.scale(sprite_down, (200, 200))
        display_surface.blit(skin_view, (WINDOW_WIDTH/2 - 110, 300))

        #Rysowanie strzałek wyboru
        arrows_image = pygame.image.load(join("graphics", "buttons", "arrow_keys.png")).convert_alpha()
        arrows_width, arrows_height = arrows_image.get_size()
        left_arrow = arrows_image.subsurface(0, 0, arrows_width / 4, arrows_height)
        right_arrow = arrows_image.subsurface(arrows_width / 4 * 3, 0, arrows_width / 4, arrows_height)
        display_surface.blit(pygame.transform.scale(left_arrow, (100, 100)), (450, 400))
        display_surface.blit(pygame.transform.scale(right_arrow, (100, 100)), (700, 400))

        pygame.display.flip()
        clock.tick(30)
import pygame, os, random

# Game window settings
pygame.display.set_caption("გასწრობანა")
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
HORSE_WIDTH, HORSE_HEIGHT = 140, 90
FINISH = WIDTH - HORSE_WIDTH

# Assets (horse images)

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'Assets')

HORSE_IMAGE_1 = pygame.image.load(
    os.path.join(assets_path, 'zuka-cxeni.png'))
HORSE_1 = pygame.transform.scale(HORSE_IMAGE_1, (HORSE_WIDTH, HORSE_HEIGHT))

HORSE_IMAGE_2 = pygame.image.load(
    os.path.join(assets_path, 'luka-cxeni.png'))
HORSE_2 = pygame.transform.scale(HORSE_IMAGE_2, (HORSE_WIDTH, HORSE_HEIGHT))

HORSE_IMAGE_3 = pygame.image.load(
    os.path.join(assets_path, 'nodo-cxeni.png'))
HORSE_3 = pygame.transform.scale(HORSE_IMAGE_3, (HORSE_WIDTH, HORSE_HEIGHT))

HORSE_IMAGE_4 = pygame.image.load(
    os.path.join(assets_path, 'dato-cxeni.png'))
HORSE_4 = pygame.transform.scale(HORSE_IMAGE_4, (HORSE_WIDTH, HORSE_HEIGHT))

HORSE_IMAGE_5 = pygame.image.load(
    os.path.join(assets_path, 'yulo-cxeni.png'))
HORSE_5 = pygame.transform.scale(HORSE_IMAGE_5, (HORSE_WIDTH, HORSE_HEIGHT))

HORSE_IMAGE_6 = pygame.image.load(
    os.path.join(assets_path, 'rati-cxeni.png'))
HORSE_6 = pygame.transform.scale(HORSE_IMAGE_6, (HORSE_WIDTH, HORSE_HEIGHT))

HORSE_IMAGE_7 = pygame.image.load(
    os.path.join(assets_path, 'nika-cxeni.png'))
HORSE_7 = pygame.transform.scale(HORSE_IMAGE_7, (HORSE_WIDTH, HORSE_HEIGHT))

BACKGROUND_IMAGE = pygame.image.load(
    os.path.join(assets_path, 'background.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

START_SCREEN_IMAGE = pygame.image.load(
    os.path.join(assets_path, 'start-screen.jpg'))
START_SCREEN = pygame.transform.scale(START_SCREEN_IMAGE, (WIDTH, HEIGHT))

FONT = pygame.font.SysFont('3D Unicode', 70)
FONT_2 = pygame.font.SysFont('3D Unicode', 25)
FONT_3 = pygame.font.SysFont('3D Unicode', 30)

RATI = pygame.image.load(os.path.join(assets_path, 'rati.jpg'))
YULO = pygame.image.load(os.path.join(assets_path, 'yulo.jpg'))
LUKA = pygame.image.load(os.path.join(assets_path, 'luka.jpg'))
NODO = pygame.image.load(os.path.join(assets_path, 'nodo.jpg'))
ZUKA = pygame.image.load(os.path.join(assets_path, 'zuka.jpg'))
NIKA = pygame.image.load(os.path.join(assets_path, 'nika.jpg'))
DATO = pygame.image.load(os.path.join(assets_path, 'dato.jpg'))

FENCE = pygame.image.load(
    os.path.join(assets_path, 'fence.png'))

# Music
pygame.mixer.music.load('/Users/datokhvedelidze/PYTHON/pygame_horses/Assets/racing.ogg')

# Text
welcome_text = FONT.render('გასწრობანა', False, (0, 0, 0))
welcome_text_2 = FONT_2.render('დააჭირე სფეისს თამაშის დასაწყებად', False, (0, 0, 0))
creators_1 = FONT_3.render('დოღის ორგანიზატორი დავითა', False, (0, 0, 0))
creators_2 = FONT_3.render('ჩაცმულობაზე იზრუნა რატიმ', False, (0, 0, 0))


def draw_window(horse_1, horse_2, horse_3, horse_4, horse_5, horse_6, horse_7):
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    WIN.blit(HORSE_1, (horse_1.x, horse_1.y))
    WIN.blit(HORSE_2, (horse_2.x, horse_2.y))
    WIN.blit(HORSE_3, (horse_3.x, horse_3.y))
    WIN.blit(HORSE_4, (horse_4.x, horse_4.y))
    WIN.blit(HORSE_5, (horse_5.x, horse_5.y))
    WIN.blit(HORSE_6, (horse_6.x, horse_6.y))
    WIN.blit(HORSE_7, (horse_7.x, horse_7.y))
    WIN.blit(welcome_text, (285, 50))
    WIN.blit(welcome_text_2, (270, 160))
    WIN.blit(FENCE, (0, 10))
    pygame.display.update()


# Main logic
def main():
    pygame.mixer.music.play(-1)
    horse_1 = pygame.Rect(0, 250, HORSE_WIDTH, HORSE_HEIGHT)
    horse_2 = pygame.Rect(0, 294, HORSE_WIDTH, HORSE_HEIGHT)
    horse_3 = pygame.Rect(0, 338, HORSE_WIDTH, HORSE_HEIGHT)
    horse_4 = pygame.Rect(0, 382, HORSE_WIDTH, HORSE_HEIGHT)
    horse_5 = pygame.Rect(0, 426, HORSE_WIDTH, HORSE_HEIGHT)
    horse_6 = pygame.Rect(0, 470, HORSE_WIDTH, HORSE_HEIGHT)
    horse_7 = pygame.Rect(0, 514, HORSE_WIDTH, HORSE_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        pygame.init()
        participants = {'zuka': horse_1.x, 'luka': horse_2.x, 'nodo': horse_3.x, 'dato': horse_4.x, 'yulo': horse_5.x,
                        'rati': horse_6.x, 'nika': horse_7.x}
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        start = pygame.key.get_pressed()
        if start[pygame.K_SPACE]:
            horse_1.x += random.randrange(3)
            horse_2.x += random.randrange(3)
            horse_3.x += random.randrange(3)
            horse_4.x += random.randrange(3)
            horse_5.x += random.randrange(3)
            horse_6.x += random.randrange(3)
            horse_7.x += random.randrange(3)
            # Using x coordinate of horse image to determine a winner
            if horse_1.x >= FINISH or horse_2.x >= FINISH or horse_3.x >= FINISH or horse_4.x >= FINISH or \
                    horse_5.x >= FINISH or horse_6.x >= FINISH or horse_7.x >= FINISH:
                winner = max(participants, key=participants.get)
                if winner == 'zuka':
                    WIN.blit(ZUKA, (0, 0))
                elif winner == 'luka':
                    WIN.blit(LUKA, (0, 0))
                elif winner == 'nodo':
                    WIN.blit(NODO, (0, 0))
                elif winner == 'dato':
                    WIN.blit(DATO, (0, 0))
                elif winner == 'yulo':
                    WIN.blit(YULO, (0, 0))
                elif winner == 'rati':
                    WIN.blit(RATI, (0, 0))
                elif winner == 'nika':
                    WIN.blit(NIKA, (0, 0))
                pygame.mixer.music.stop()
                WIN.blit(creators_1, (270, 350))
                WIN.blit(creators_2, (270, 390))
                pygame.display.update()
                pygame.time.delay(7000)
                break

        draw_window(horse_1, horse_2, horse_3, horse_4, horse_5, horse_6, horse_7)

    main()


if __name__ == '__main__':
    main()

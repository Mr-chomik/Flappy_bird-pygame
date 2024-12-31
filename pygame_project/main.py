import pygame, os, sys
from random import choice


COLORS = [(244, 164, 96), (255, 160, 122), (221, 160, 221), (107, 142, 35), (65, 105, 225)]

COLOR = choice(COLORS)
MENU = True
PROFILE = False
LEVELS = False
GAME = False
LOGIN = None
INPUT_LOGIN = False
INPUT_PASSWORD = False
TEXT_LOGIN = ""
TEXT_PASSWORD = ""


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class menu:
    def __init__(self, screen, width=999, height=558):
        self.background = load_image("background_menu.jpg")
        self.background_rect = self.background.get_rect(bottomright=(width, height))
        self.render()

    def render(self):
        screen.fill((0, 0, 0))

        screen.blit(self.background, self.background_rect)

        pygame.draw.rect(screen, (160, 82, 50), (350, 200, 300, 60), 0)
        pygame.draw.rect(screen, (120, 0, 0), (350, 200, 300, 60), 4)
        pygame.draw.rect(screen, (0, 0, 0), (350, 200, 300, 60), 2)
        font = pygame.font.Font(None, 50)
        text = font.render("Играть", True, (200, 200, 200))
        screen.blit(text, (445, 215))

        pygame.draw.ellipse(screen, COLOR, (945, 10, 45, 45))
        pygame.draw.ellipse(screen, (211, 211, 211), (945, 10, 45, 45), 2)
        font = pygame.font.Font(None, 50)
        text = font.render("?", True, (30, 30, 30))
        screen.blit(text, (957, 17))

    def changes(self, pos):
        global MENU, LEVELS, PROFILE
        x, y = pos[0], pos[1]
        if x >= 350 and x <= 650 and y >= 200 and y <= 260:
            MENU = False
            LEVELS = True
            levels(screen)

        elif x >= 945 and x <= 990 and y >= 10 and y <= 55:
            MENU = False
            PROFILE = True
            profile(screen)


class game:
    pass


class levels:
    def __init__(self, screen, width=999, height=558):
        self.background_3 = load_image("min_background_3.jpg")
        self.background_rect_3 = self.background_3.get_rect(bottomright=(width, height))

        self.background_2 = load_image("min_background_2.jpg")
        self.background_rect_2 = self.background_2.get_rect(bottomright=(width - (width // 3), height))

        self.background_1 = load_image("min_background_1.jpg")
        self.background_rect_1 = self.background_1.get_rect(bottomright=(width // 3, height))

        self.render()

    def render(self):
        screen.fill((0, 0, 0))

        screen.blit(self.background_3, self.background_rect_3)
        screen.blit(self.background_2, self.background_rect_2)
        screen.blit(self.background_1, self.background_rect_1)

        pygame.draw.rect(screen, (40, 40, 40), (0, 0, 333, 558), 4)
        pygame.draw.rect(screen, (40, 40, 40), (333, 0, 333, 558), 4)
        pygame.draw.rect(screen, (40, 40, 40), (666, 0, 333, 558), 4)

        pygame.draw.ellipse(screen, (230, 125, 80), (10, 10, 45, 45))
        pygame.draw.ellipse(screen, (205, 133, 63), (10, 10, 45, 45), 5)
        pygame.draw.ellipse(screen, (211, 211, 211), (10, 10, 45, 45), 2)
        font = pygame.font.Font(None, 50)
        text = font.render("<", True, (0, 0, 0))
        screen.blit(text, (21, 13))

    def changes(self, pos):
        global MENU, LEVELS, PROFILE, GAME
        x, y = pos[0], pos[1]
        if x < 55 and y < 55:
            LEVELS = False
            MENU = True
            menu(screen)

        elif x < 333:
            LEVELS = False
            GAME = True
            game()

        elif x > 333 and x < 666:
            LEVELS = False
            GAME = True
            game()

        elif x > 666:
            LEVELS = False
            GAME = True
            game()



class profile:
    def __init__(self, screen, width=999, height=558):
        self.background = load_image("background_profile.jpg")
        self.background_rect = self.background.get_rect(bottomright=(width, height))
        self.render()

    def render(self):
        global LOGIN, input_box_log, input_box_pas
        screen.fill((0, 0, 0))

        screen.blit(self.background, self.background_rect)

        pygame.draw.rect(screen, (160, 82, 50), (50, 80, 600, 400), 0)
        pygame.draw.rect(screen, (120, 0, 0), (50, 80, 600, 400), 5)
        pygame.draw.rect(screen, (0, 0, 0), (50, 80, 600, 400), 1)

        pygame.draw.ellipse(screen, COLOR, (70, 100, 80, 80))
        pygame.draw.ellipse(screen, (211, 211, 211), (70, 100, 80, 80), 2)

        pygame.draw.ellipse(screen, (230, 125, 80), (10, 10, 45, 45))
        pygame.draw.ellipse(screen, (205, 133, 63), (10, 10, 45, 45), 5)
        pygame.draw.ellipse(screen, (211, 211, 211), (10, 10, 45, 45), 2)
        font = pygame.font.Font(None, 50)
        text = font.render("<", True, (0, 0, 0))
        screen.blit(text, (21, 13))


        if LOGIN:
            pass

        else:
            font = pygame.font.Font(None, 100)
            text = font.render("?", True, (30, 30, 30))
            screen.blit(text, (89, 110))

            font = pygame.font.Font(None, 70)
            text = font.render("Гость", True, (230, 230, 230))
            screen.blit(text, (200, 125))

            font = pygame.font.Font(None, 50)
            text = font.render("Логин:", True, (230, 230, 230))
            screen.blit(text, (80, 215))

            pygame.draw.rect(screen, (250, 250, 250), (240, 215, 260, 35), 2)

            text = font.render("Пароль:", True, (230, 230, 230))
            screen.blit(text, (80, 265))

            pygame.draw.rect(screen, (250, 250, 250), (240, 265, 260, 35), 2)

            pygame.draw.rect(screen, (200, 122, 90), (465, 320, 110, 40))
            pygame.draw.rect(screen, (180, 102, 70), (465, 320, 110, 40), 5)
            pygame.draw.rect(screen, (180, 180, 180), (465, 320, 110, 40), 1)
            font = pygame.font.Font(None, 40)
            text = font.render("Войти", True, (230, 230, 230))
            screen.blit(text, (477, 327))

    def changes(self, pos):
        global INPUT_LOGIN, INPUT_PASSWORD, MENU, PROFILE, TEXT_LOGIN, TEXT_PASSWORD
        x, y = pos[0], pos[1]

        if x < 55 and x > 10 and y > 10 and y < 55:
            INPUT_LOGIN = False
            TEXT_LOGIN = ""
            INPUT_PASSWORD = False
            TEXT_PASSWORD = ""
            PROFILE = False
            MENU = True
            menu(screen)

        elif x < 500 and x > 240 and y < 250 and y > 215:
            INPUT_LOGIN = True
            INPUT_PASSWORD = False

            pygame.draw.rect(screen, (200, 200, 200), (240, 215, 260, 35), 2)
            pygame.draw.rect(screen, (250, 250, 250), (240, 265, 260, 35), 2)

        elif x < 500 and x > 240 and y < 300 and y > 265:
            INPUT_PASSWORD = True
            INPUT_LOGIN = False

            pygame.draw.rect(screen, (250, 250, 250), (240, 215, 260, 35), 2)
            pygame.draw.rect(screen, (200, 200, 200), (240, 265, 260, 35), 2)

        else:
            INPUT_LOGIN = False
            INPUT_PASSWORD = False

            pygame.draw.rect(screen, (250, 250, 250), (240, 215, 260, 35), 2)
            pygame.draw.rect(screen, (250, 250, 250), (240, 265, 260, 35), 2)

    def inputting(self, isLogin, isPassword):
        global TEXT_LOGIN, TEXT_PASSWORD
        font = pygame.font.Font(None, 40)
        if isLogin:
            text = font.render(TEXT_LOGIN, True, (210, 210, 210))
            if event.key == pygame.K_RETURN:
                print(TEXT_LOGIN)
            elif event.key == pygame.K_BACKSPACE:
                TEXT_LOGIN = TEXT_LOGIN[:-1]
            else:
                alpha = event.unicode
                if alpha not in " .,!@#$%^&*()+=-?:%;№`~{}[]<>" and text.get_width() < 235:
                    TEXT_LOGIN += alpha

            pygame.draw.rect(screen, (160, 82, 50), (240, 215, 260, 35), 0)
            pygame.draw.rect(screen, (200, 200, 200), (240, 215, 260, 35), 2)
            text = font.render(TEXT_LOGIN, True, (210, 210, 210))
            screen.blit(text, (245, 220))

        if isPassword:
            text = font.render(TEXT_PASSWORD, True, (210, 210, 210))
            if event.key == pygame.K_RETURN:
                print(TEXT_PASSWORD)
            elif event.key == pygame.K_BACKSPACE:
                TEXT_PASSWORD = TEXT_PASSWORD[:-1]
            else:
                alpha = event.unicode
                if alpha not in " .,!@#$%^&*()+=-?:%;№`~{}[]<>" and text.get_width() < 235:
                    TEXT_PASSWORD += alpha

            pygame.draw.rect(screen, (160, 82, 50), (240, 265, 260, 35), 0)
            pygame.draw.rect(screen, (200, 200, 200), (240, 265, 260, 35), 2)
            text = font.render(TEXT_PASSWORD, True, (210, 210, 210))
            screen.blit(text, (245, 270))


if __name__ == "__main__":
    pygame.init()
    size = width, height = 999, 558
    screen = pygame.display.set_mode(size)
    running = True
    menu(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if MENU:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu.changes(screen, event.pos)

            elif LEVELS:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    levels.changes(screen, event.pos)

            elif PROFILE:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    profile.changes(screen, event.pos)
                if (INPUT_PASSWORD or INPUT_LOGIN) and event.type == pygame.KEYDOWN:
                    profile.inputting(screen, INPUT_LOGIN, INPUT_PASSWORD)

        pygame.display.flip()

    pygame.quit()
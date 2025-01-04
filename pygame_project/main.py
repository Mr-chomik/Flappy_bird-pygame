import pygame, os, sys, random, csv
from random import choice


pygame.init()
size = width, height = 999, 558
screen = pygame.display.set_mode(size)


COLORS = [(244, 164, 96), (255, 160, 122), (221, 160, 221), (107, 142, 35), (65, 105, 225)]

COLOR = choice(COLORS)
FPS = 30
MENU = True
PROFILE = False
LEVELS = False
GAME = False
LOGIN = ""
INPUT_LOGIN = False
INPUT_PASSWORD = False
REGISTRATION = False
TEXT_LOGIN = ""
TEXT_PASSWORD = ""
LVL = 1
SCORE = 0


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
        global LOGIN
        screen.fill((0, 0, 0))

        screen.blit(self.background, self.background_rect)

        pygame.draw.rect(screen, (160, 82, 50), (350, 200, 300, 60), 0)
        pygame.draw.rect(screen, (120, 0, 0), (350, 200, 300, 60), 4)
        pygame.draw.rect(screen, (0, 0, 0), (350, 200, 300, 60), 2)
        font = pygame.font.Font(None, 50)
        text = font.render("Играть", True, (215, 215, 215))
        screen.blit(text, (445, 215))

        pygame.draw.ellipse(screen, COLOR, (945, 10, 45, 45))
        pygame.draw.ellipse(screen, (211, 211, 211), (945, 10, 45, 45), 2)
        if LOGIN:
            font = pygame.font.Font(None, 50)
            text = font.render(LOGIN[0], True, (30, 30, 30))
            screen.blit(text, (945 + ((46 - text.get_width()) // 2), 17))
        else:
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
    def __init__(self, level, width=999, height=558):
        self.background = load_image("background_" + str(level) + ".jpg")
        self.background_rect = self.background.get_rect(bottomright=(width, height))
        screen.blit(self.background, self.background_rect)
        bird_sprites.draw(screen)
        pipe_up_sprites.draw(screen)
        pipe_down_sprites.draw(screen)


class Bird(pygame.sprite.Sprite):
    image = load_image("bird.png")
    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bird.image
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

    def update(self, tap=-1):
        global LVL
        print(pygame.sprite.collide_mask(self, pipe_down))
        if pygame.sprite.collide_mask(self, pipe_down):
            print(1)

        if tap != -1 and bird.rect.top >= 25:
            self.rect.y -= 35
        elif tap != -1:
            self.rect.y -= bird.rect.top

        if LVL == 1:
            if bird.rect.bottom >= 557 and tap == -1:
                pass
            else:
                self.rect.y += 3

        elif LVL == 2:
            if bird.rect.bottom >= 557 and tap == -1:
                pass
            else:
                self.rect.y += 3

        elif LVL == 3:
            if bird.rect.bottom >= 557 and tap == -1:
                pass
            else:
                self.rect.y += 4


class Pipe_up(pygame.sprite.Sprite):
    image = load_image("pipe_up.png")
    def __init__(self, *group, y_cord=-600):
        super().__init__(*group)
        self.image = Pipe_up.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 999
        self.rect.y = y_cord

    def update(self, tap=-1):
        self.rect.x -= 6


class Pipe_down(pygame.sprite.Sprite):
    image = load_image("pipe_down.png")
    def __init__(self, *group, y_cord=300):
        super().__init__(*group)
        self.image = Pipe_down.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 999
        self.rect.y = y_cord

    def update(self):
        self.rect.x -= 6


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
        global MENU, LEVELS, PROFILE, GAME, LVL
        x, y = pos[0], pos[1]
        if x < 55 and y < 55:
            LEVELS = False
            MENU = True
            menu(screen)

        elif x < 333:
            LEVELS = False
            GAME = True
            LVL = 1
            game(1)

        elif x > 333 and x < 666:
            LEVELS = False
            GAME = True
            LVL = 2
            game(2)

        elif x > 666:
            LEVELS = False
            GAME = True
            LVL = 3
            game(3)


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
            count_of_tries = 0
            record = 0
            with open('pygame_data.csv', encoding="utf8") as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for row in reader:
                    if LOGIN.lower() == row[0]:
                        count_of_tries = row[2]
                        record = row[3]
                        break

            font = pygame.font.Font(None, 90)
            text = font.render(LOGIN[0], True, (30, 30, 30))
            screen.blit(text, (70 + ((81 - text.get_width()) // 2), 112))

            font = pygame.font.Font(None, 70)
            text = font.render(LOGIN, True, (210, 210, 210))
            screen.blit(text, (200, 125))

            font = pygame.font.Font(None, 50)
            text = font.render(f"Всего попыток:     {count_of_tries}", True, (230, 230, 230))
            screen.blit(text, (80, 240))

            text = font.render(f"Рекорд:            {record}", True, (230, 230, 230))
            screen.blit(text, (80, 300))

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

            pygame.draw.rect(screen, (200, 122, 90), (465, 325, 110, 40))
            pygame.draw.rect(screen, (180, 102, 70), (465, 325, 110, 40), 5)
            pygame.draw.rect(screen, (180, 180, 180), (465, 325, 110, 40), 1)
            font = pygame.font.Font(None, 40)
            text = font.render("Войти", True, (230, 230, 230))
            screen.blit(text, (478, 332))

            pygame.draw.rect(screen, (200, 122, 90), (300, 415, 280, 45))
            pygame.draw.rect(screen, (180, 102, 70), (300, 415, 280, 45), 5)
            pygame.draw.rect(screen, (180, 180, 180), (300, 415, 280, 45), 1)
            font = pygame.font.Font(None, 37)
            text = font.render("Зарегистрироваться", True, (220, 220, 220))
            screen.blit(text, (314, 424))

    def changes(self, pos):
        global INPUT_LOGIN, INPUT_PASSWORD, MENU, PROFILE, TEXT_LOGIN, TEXT_PASSWORD, LOGIN, REGISTRATION
        x, y = pos[0], pos[1]
        REGISTRATION = False

        if x < 55 and x > 10 and y > 10 and y < 55: # кнопка 'назад'
            INPUT_LOGIN = False
            TEXT_LOGIN = ""
            INPUT_PASSWORD = False
            TEXT_PASSWORD = ""
            PROFILE = False
            MENU = True
            menu(screen)

        elif x < 500 and x > 240 and y < 250 and y > 215: # поле ввода логина
            INPUT_LOGIN = True
            INPUT_PASSWORD = False

            pygame.draw.rect(screen, (200, 200, 200), (240, 215, 260, 35), 2)
            pygame.draw.rect(screen, (250, 250, 250), (240, 265, 260, 35), 2)
            pygame.draw.rect(screen, (160, 82, 50), (200, 180, 300, 25), 0)

        elif x < 500 and x > 240 and y < 300 and y > 265: # поле ввода пароля
            INPUT_PASSWORD = True
            INPUT_LOGIN = False

            pygame.draw.rect(screen, (250, 250, 250), (240, 215, 260, 35), 2)
            pygame.draw.rect(screen, (200, 200, 200), (240, 265, 260, 35), 2)
            pygame.draw.rect(screen, (160, 82, 50), (200, 180, 300, 25), 0)

        elif x < 580 and x > 300 and y < 460 and y > 415: # кнопка 'Зарегистрироваться'
            REGISTRATION = True
            TEXT_LOGIN = ""
            TEXT_PASSWORD = ""
            pygame.draw.rect(screen, (160, 82, 50), (300, 415, 280, 45))
            pygame.draw.rect(screen, (160, 82, 50), (465, 325, 110, 40))

            pygame.draw.rect(screen, (160, 82, 50), (240, 265, 260, 35), 0)
            pygame.draw.rect(screen, (220, 220, 220), (240, 265, 260, 35), 2)
            pygame.draw.rect(screen, (160, 82, 50), (240, 215, 260, 35), 0)
            pygame.draw.rect(screen, (220, 200, 220), (240, 215, 260, 35), 2)

            pygame.draw.rect(screen, (200, 122, 90), (350, 325, 270, 40))
            pygame.draw.rect(screen, (180, 102, 70), (350, 325, 270, 40), 5)
            pygame.draw.rect(screen, (180, 180, 180), (350, 325, 270, 40), 1)
            font = pygame.font.Font(None, 35)
            text = font.render("Зарегистрироваться", True, (230, 230, 230))
            screen.blit(text, (363, 332))

            profile.inputting(screen, False, False)  # registration

        elif x < 575 and x > 465 and y < 360 and y > 320 and not REGISTRATION: # 'Войти'
            with open('pygame_data.csv', encoding="utf8") as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for row in reader:
                    if TEXT_LOGIN.lower() == row[0] and TEXT_PASSWORD == row[1]:
                        LOGIN = (TEXT_LOGIN.lower()).capitalize()
                        profile(screen)
                    else:
                        font = pygame.font.Font(None, 30)
                        text = font.render("Неверный логин или пароль", True, (180, 10, 10))
                        screen.blit(text, (220, 185))

        else:
            INPUT_LOGIN = False
            INPUT_PASSWORD = False

            pygame.draw.rect(screen, (250, 250, 250), (240, 215, 260, 35), 2)
            pygame.draw.rect(screen, (250, 250, 250), (240, 265, 260, 35), 2)

    def registration(self, pos):
        global INPUT_LOGIN, TEXT_LOGIN, INPUT_PASSWORD, TEXT_PASSWORD, PROFILE, MENU, LOGIN
        x, y = pos[0], pos[1]

        if x < 620 and x > 350 and y < 365 and y > 325: # кнопка 'Зарегистрироваться'
            if TEXT_LOGIN == "" or len(TEXT_PASSWORD) < 4 or TEXT_LOGIN.lower() == "login" or TEXT_PASSWORD.lower() == "password":
                font = pygame.font.Font(None, 30)
                text = font.render("Неверный логин или пароль", True, (180, 10, 10))
                screen.blit(text, (220, 185))

            else:
                flajok = True
                matrix = []
                with open('pygame_data.csv', encoding="utf8") as csvfile:
                    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                    for row in reader:
                        matrix.append(row)
                        if TEXT_LOGIN.lower() == row[0]:
                            flajok = False

                if flajok:
                    with open('pygame_data.csv', 'w', newline="", encoding="utf8") as csvfile:
                        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        for row in matrix:
                            writer.writerow(row)
                        writer.writerow([TEXT_LOGIN.lower(), TEXT_PASSWORD, 0, 0])
                        LOGIN = (TEXT_LOGIN.lower()).capitalize()

                        profile(screen)
                else:
                    font = pygame.font.Font(None, 30)
                    text = font.render("Этот логин занят", True, (180, 10, 10))
                    screen.blit(text, (220, 185))

        elif x < 55 and x > 10 and y > 10 and y < 55: # кнопка 'назад'
            INPUT_LOGIN = False
            TEXT_LOGIN = ""
            INPUT_PASSWORD = False
            TEXT_PASSWORD = ""
            PROFILE = False
            MENU = True
            menu(screen)


        elif x < 500 and x > 240 and y < 300 and y > 265:  # поле ввода пароля
            INPUT_PASSWORD = True
            INPUT_LOGIN = False
            pygame.draw.rect(screen, (250, 250, 250), (240, 215, 260, 35), 2)
            pygame.draw.rect(screen, (200, 200, 200), (240, 265, 260, 35), 2)
            pygame.draw.rect(screen, (160, 82, 50), (200, 180, 300, 25), 0)

        elif x < 500 and x > 240 and y < 250 and y > 215: # поле ввода логина
            INPUT_LOGIN = True
            INPUT_PASSWORD = False

            pygame.draw.rect(screen, (200, 200, 200), (240, 215, 260, 35), 2)
            pygame.draw.rect(screen, (250, 250, 250), (240, 265, 260, 35), 2)
            pygame.draw.rect(screen, (160, 82, 50), (200, 180, 300, 25), 0)

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

        elif isPassword:
            text = font.render(TEXT_PASSWORD, True, (210, 210, 210))
            if event.key == pygame.K_RETURN:
                print(TEXT_PASSWORD)
            elif event.key == pygame.K_BACKSPACE:
                TEXT_PASSWORD = TEXT_PASSWORD[:-1]
            else:
                alpha = event.unicode
                if alpha not in " .,!@#$%^&*()+=-?:%;№`~{}[]<>_" and text.get_width() < 235:
                    TEXT_PASSWORD += alpha

            pygame.draw.rect(screen, (160, 82, 50), (240, 265, 260, 35), 0)
            pygame.draw.rect(screen, (200, 200, 200), (240, 265, 260, 35), 2)
            text = font.render(TEXT_PASSWORD, True, (210, 210, 210))
            screen.blit(text, (245, 270))


if __name__ == "__main__":
    clock = pygame.time.Clock()

    bird_sprites = pygame.sprite.Group()
    bird = Bird(bird_sprites)

    pipe_up_sprites = pygame.sprite.Group()
    pipe_up = Pipe_up(pipe_up_sprites)

    pipe_down_sprites = pygame.sprite.Group()
    pipe_down = Pipe_down(pipe_down_sprites)

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
                if event.type == pygame.MOUSEBUTTONDOWN and REGISTRATION:
                    profile.registration(screen, event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    profile.changes(screen, event.pos)
                if (INPUT_PASSWORD or INPUT_LOGIN) and event.type == pygame.KEYDOWN:
                    profile.inputting(screen, INPUT_LOGIN, INPUT_PASSWORD)

            elif GAME:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird_sprites.update(0)
                        game(LVL)

        if GAME:
            bird_sprites.update()
            pipe_up_sprites.update()
            pipe_down_sprites.update()
            if pipe_down.rect.x < 500:
                y_cords = random.randrange(-670, -420)
                new_pipe_down = Pipe_down(pipe_down_sprites, y_cord=y_cords + 900)
                pipe_down = new_pipe_down
                pipe_up = Pipe_up(pipe_up_sprites, y_cord=y_cords)

            game(LVL)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
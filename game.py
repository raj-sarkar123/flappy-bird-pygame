import pygame as pg
import sys, time, os
from bird import Bird
from pipe import Pipe

pg.init()
pg.mixer.init()

class Game:
    def __init__(self):

        self.width = 600
        self.height = 768
        self.win = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Flappy Bird Pro")

        self.clock = pg.time.Clock()
        self.scale_factor = 1.5
        self.move_speed = 200

        self.state = "MENU"  # MENU, PLAYING, GAME_OVER

        self.bird = Bird(self.scale_factor)
        self.pipes = []

        self.score = 0
        self.high_score = self.load_high_score()

        self.font = pg.font.Font("assets/font.ttf", 32)
        self.small_font = pg.font.Font("assets/font.ttf", 20)

        # Sounds
        # self.sfx_flap = pg.mixer.Sound("assets/sfx/uhh.wav")
        self.sfx_flap = pg.mixer.Sound("assets/sfx/flap.wav")
        self.sfx_score = pg.mixer.Sound("assets/sfx/score.wav")
        self.sfx_dead = pg.mixer.Sound("assets/sfx/fahhh.wav")
        # self.sfx_dead = pg.mixer.Sound("assets/sfx/dead.wav")


        # pg.mixer.music.load("assets/sfx/bg_music.wav")
        # pg.mixer.music.set_volume(0.4)
        # pg.mixer.music.play(-1)

        self.setupbackground()
        self.gameloop()

    def load_high_score(self):
        if not os.path.exists("highscore.txt"):
            return 0
        with open("highscore.txt", "r") as f:
            return int(f.read())

    def save_high_score(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.high_score))

    def gameloop(self):
        last_time = time.time()

        while True:
            dt = time.time() - last_time
            last_time = time.time()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if self.state == "MENU":
                        self.start_game()

                    elif self.state == "PLAYING":
                        if event.key == pg.K_SPACE:
                            self.bird.flap()
                            self.sfx_flap.play()

                    elif self.state == "GAME_OVER":
                        self.restart_game()

            if self.state == "PLAYING":
                self.update(dt)

            self.draw()
            pg.display.update()
            self.clock.tick(60)

    def start_game(self):
        self.state = "PLAYING"
        self.bird.update_on = True

    def restart_game(self):
        self.state = "MENU"
        self.score = 0
        self.move_speed = 200
        self.pipes.clear()
        self.bird.resetposition()

    def update(self, dt):

        self.move_speed += 5 * dt  # difficulty scaling

        if len(self.pipes) == 0 or self.pipes[-1].rect_up.x < 350:
            self.pipes.append(Pipe(self.scale_factor, self.move_speed))

        for pipe in self.pipes[:]:
            pipe.update(dt)

            if pipe.rect_up.right < 0:
                self.pipes.remove(pipe)

            if not pipe.passed and pipe.rect_up.right < self.bird.rect.left:
                pipe.passed = True
                self.score += 10
                # self.sfx_score.play()

        self.bird.update(dt)

        # Collision
        if self.bird.rect.bottom > 568:
            self.game_over()

        for pipe in self.pipes:
            if (self.bird.rect.colliderect(pipe.rect_up) or
                self.bird.rect.colliderect(pipe.rect_down)):
                self.game_over()

    def game_over(self):
        self.sfx_dead.play()
        self.state = "GAME_OVER"
        self.bird.update_on = False

        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def draw(self):

        self.win.blit(self.bg_img, (0, -300))

        for pipe in self.pipes:
            pipe.draw(self.win)

        self.win.blit(self.ground1_img, self.ground1_rect)
        self.win.blit(self.bird.img, self.bird.rect)

        if self.state == "MENU":
            text = self.font.render("Press Any Key", True, (255,255,255))
            self.win.blit(text, text.get_rect(center=(300,300)))

        elif self.state == "PLAYING":
            score_text = self.font.render(str(self.score), True, (255,255,255))
            self.win.blit(score_text, score_text.get_rect(center=(300,50)))

        elif self.state == "GAME_OVER":
            over = self.font.render("Game Over", True, (255,50,50))
            hs = self.small_font.render(f"High Score: {self.high_score}", True, (255,255,255))
            restart = self.small_font.render("Press Any Key", True, (0,0,0))

            self.win.blit(over, over.get_rect(center=(300,250)))
            self.win.blit(hs, hs.get_rect(center=(300,320)))
            self.win.blit(restart, restart.get_rect(center=(300,380)))

    def setupbackground(self):
        self.bg_img = pg.transform.scale_by(
            pg.image.load("assets/bg.png").convert(),
            self.scale_factor
        )

        self.ground1_img = pg.transform.scale_by(
            pg.image.load("assets/ground.png").convert(),
            self.scale_factor
        )

        self.ground1_rect = self.ground1_img.get_rect()
        self.ground1_rect.y = 568


Game()
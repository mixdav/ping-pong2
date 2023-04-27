from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y, player_speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x,y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        glav_window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_1(self):
        key_push = key.get_pressed()
        if key_push[K_UP] and self.rect.y<10:
            self.rect.y += self.speed
        if key_push[K_DOWN] and self.rect.y>5:
            self.rect.x -= self.speed
    def move_1(self):
        key_push = key.get_pressed()
        if key_push[k_w] and self.rect.y<10:
            self.rect.x += self.speed
        if key_push[k_s] and self.rect.y>5:
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx, self.rect.top, 10, 10, 15)
        bullets.add(bullet)



glav_window = display.set_mode((700,500))
display.set_caption('pygame window')
background = transform.scale(image.load('fon.PNG'), (700,500))



game = True
clock = time.Clock()
FPS = 60
finish = False



player_1 = Player('racetka.png', 100, 420, 15, 60, 65)
player_2 = Player('racetka.png', 650, 420, 15, 60, 65)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        glav_window.blit(background, (0,0))



        player_1.move()
        player_1.reset()

        player_2.move()
        player_2.reset()       






        display.update()
        clock.tick(FPS)
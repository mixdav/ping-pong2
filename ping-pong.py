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
        if key_push[K_UP] and self.rect.y>10:
            self.rect.y -= self.speed
        if key_push[K_DOWN] and self.rect.y<380:
            self.rect.y += self.speed
    def move_2(self):
        key_push = key.get_pressed()
        if key_push[K_w] and self.rect.y>10:
            self.rect.y -= self.speed
        if key_push[K_s] and self.rect.y<380:
            self.rect.y += self.speed


fon = (200,250,240)
glav_window = display.set_mode((800,600))
glav_window.fill(fon)



game = True
clock = time.Clock()
FPS = 100
finish = False
speed_x = 3
speed_y = 3

score_1 = 0
score_2 = 0

font.init()
font_1 = font.SysFont('Arial',50)
font_2 = font.SysFont('Arial',40)
pobeda_1 = font_2.render('Победил первый игрок!', True, (255,215,3))
pobeda_2 = font_2.render('Победил второй игрок!', True, (255,215,3))

ball = GameSprite('appel.png',250,200,5,90,90)
player_1 = Player('111.png',650,350,15,150,200)
player_2 = Player('111.png',10,350,15,150,200)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        glav_window.fill(fon)


        player_1.move_1()
        player_2.move_2()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player_1,ball) or sprite.collide_rect(player_2,ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y>400 or ball.rect.y<0:
            speed_y *= -1

        if ball.rect.x < 10:
            glav_window.blit(pobeda_1,(30,20))
        if ball.rect.x > 800:
            glav_window.blit(pobeda_2,(30,20))          
        
        

        ball.reset()
        player_1.reset()
        player_2.reset()

    display.update()
    clock.tick(FPS)
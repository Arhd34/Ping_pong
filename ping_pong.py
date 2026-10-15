#Импортирование
from pygame import *
from random import randint
font.init()

#Создание классов
class game_sprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(game_sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__(player_image, player_speed, player_x, player_y, (32,96))
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 405:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 405:
            self.rect.y += self.speed
class Enemy(game_sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__(player_image, player_speed, player_x, player_y, (65*1.6,65))
    def res(self):
        self.rect.y = -66
        self.rect.x = randint(0, 635)
        self.speed = randint(10,20)*0.1
    def update(self,ufo):
        self.rect.y += self.speed

#Создание всего
window = display.set_mode((750, 500))
display.set_caption('Пинг-Понг')
window.fill((200,200,240))
ball = game_sprite('ball.png', 4, 150, 150, (40,40))
player1 = Player('racket.png', 3, 50, 200)
player2 = Player('racket.png', 3, 668, 200)
font1 = font.Font(None, 50)
player1_lose = font1.render('Игрок номер 2 выйграл!', True, (0, 200, 70))
player2_lose = font1.render('Игрок номер 1 выйграл!', True, (0, 200, 70))

#Игровой цикл
speed_x = 4
speed_y = 4
clock = time.Clock()
run = True
game = True
while game:
    events = event.get()
    for e in events:
        if e.type == QUIT:
            game = False
    if key.get_pressed()[K_c] and run == False:
        speed_x, speed_x, run = 4, 4, True
        ball.rect.x, ball.rect.y = 150, 150
        player1.rect.x, player1.rect.y = 50, 200
        player2.rect.x, player2.rect.y = 668, 200
    clock.tick(60)
    display.update()
    if run:
        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1
        if ball.rect.y <= 0 or ball.rect.y >= 460:
            speed_y *= -1
        window.fill((200,200,240))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        player1.update_L()
        player2.update_R()
        ball.reset()
        player1.reset()
        player2.reset()
        if ball.rect.x <= 0:
            window.blit(player1_lose, (200, 200))
            run = False
        if ball.rect.x >= 710:
            window.blit(player2_lose, (200, 200))
            run = False

import pygame
import sys
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BACKGROUND = pygame.image.load('plane.png')

class Wall:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (w, h))
    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

class Snake():
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (w, h))

    def move(self):
        if lud == "right":
            self.rect.x += 5
        elif lud == "left":
            self.rect.x -= 5
        elif lud == "up":
            self.rect.y -= 5
        elif lud == "down":
            self.rect.y += 5

    def collide(self, obj):
        return self.rect.colliderect(obj.rect)
            
    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

class Apple():
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (w, h))
    
    def draw(self):
        screen.blit(self.img, (self.rect.x, se
def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

lud = "none"

snake = Snake(50, 50, 70, 70, "Snakeright.png")
apple = Apple(400, 400, 60, 60, "apple.png")

map1 = []

with open("map.txt", "r") as map:
    row, col = 0, 0
    for line in map.read().split("\n"):
        x = list(line)
        col = 0
        for i in x:
            if i == "1":
                map1.append(Wall(col * 20, row * 20, 20, 20, "wall.png"))
                print(row, col)
            col += 1
row += 1

while True:
    screen.blit(BACKGROUND, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_RIGHT:
            lud = "right"

        elif e.key == pygame.K_LEFT:
            lud = "left"

        elif e.key == pygame.K_UP:
            lud = "up"

        elif e.key == pygame.K_DOWN:
            lud = "down"

    if snake.collide(apple):
        apple.rect.x = randint(0, 640
apple.rect.x = randint(0, 640)
        apple.rect.y = randint(0, 640)

    snake.move()
    snake.draw()

    apple.draw()     

    for i in map1:
        i.draw()

    pygame.display.update()
    clock.tick(60)
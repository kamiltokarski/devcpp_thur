#!/usr/bin/env python3
import pygame

# inicjalizacja biblioteki
pygame.init()

# tworzymy okienko
okno = pygame.display.set_mode((640, 480))

def shift(l):
    return l[1:] + l[:1]

# klasa wonsza
class Wonsz:
    SPEED = 3

    def __init__(self, okno):
        self.x = 320
        self.y = 240
        self.okno = okno

        self.kierunek = 0
        self.glowy = []
    
    def move(self):
        if len(self.glowy) != 0:
            self.glowy = shift(self.glowy)
            self.glowy[0] = (self.x, self.y)

        if self.kierunek == 0:
            self.moveRight()
        if self.kierunek == 1:
            self.moveLeft()
        if self.kierunek == 2:
            self.moveUp()
        if self.kierunek == 3:
            self.moveDown()
        
    def addHead(self):
        if len(self.glowy) != 0:
            self.glowy.append((self.glowy[-1][0], self.glowy[-1][1]))
        else:
            self.glowy.append((self.x, self.y))

    def moveRight(self):
        self.x += self.SPEED
    def moveLeft(self):
        self.x -= self.SPEED
    def moveUp(self):
        self.y -= self.SPEED
    def moveDown(self):
        self.y += self.SPEED

    def render(self):
        pygame.draw.circle(self.okno, (0, 255, 0), (self.x, self.y), 10)
        for head in self.glowy:
            pygame.draw.circle(self.okno, (0, 255, 0), head, 10)

wonsz = Wonsz(okno)

# zegar
clock = pygame.time.Clock()

# czy powinno sie zamknac
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                wonsz.kierunek = 0
            if event.key == pygame.K_LEFT:
                wonsz.kierunek = 1
            if event.key == pygame.K_UP:
                wonsz.kierunek = 2
            if event.key == pygame.K_DOWN:
                wonsz.kierunek = 3
            if event.key == pygame.K_a:
                for i in range(100):
                    wonsz.addHead()
    okno.fill((255, 255, 255))

    wonsz.render()
    pygame.display.flip()

    wonsz.move()
    clock.tick(60)


# zamkniecie programu
pygame.quit()
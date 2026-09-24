import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800, 447             ))
clock = pygame.time.Clock()
# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True
pygame.display.set_caption("Feyzas erstes Phython Game")
bg = pygame.image.load(os.path.join('images','bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()

def redrawWindow():
    screen.blit(bg, (bgX, 0))  # draws our first bg image
    screen.blit(bg, (bgX2, 0))  # draws the seconf bg image
    pygame.display.update()  # updates the screen

# Call this from the game loop!

while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")
            if event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrückt")
            elif event.key == pygame.K_LEFT:
                print("Spieler hat Pfeiltaste links gedrückt")
            elif event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste hoch gedrückt")
            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrückt")

    # screen.fill((255, 140, 0))
    redrawWindow()
    clock.tick(60)


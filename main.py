import pygame

pygame.init()

ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("brickpy")


playing = True

while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    ventana.fill((255, 255, 255))
    
    pygame.display.flip()

    pygame.time.Clock().tick(60)


pygame.quit()
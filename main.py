import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Setup start')
while True:
    # Checagem de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Fechar janela
            quit() # Encerrar pygame


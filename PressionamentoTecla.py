import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((500, 500))


def getKey(tecla):
    ans = False
    for eve in pygame.event.get(): pass
    teclaInput = pygame.key.get_pressed()
    teclaP = getattr(pygame, 'K_{}'.format(tecla))
    print('K_{}'.format(tecla))

    if teclaInput[teclaP]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getKey("LEFT"):
        print("Tecla esquerda pressionada.")
    if getKey("RIGHT"):
        print("Tecla direita pressionada.")
    if getKey("UP"):
        print("Tecla superior pressionada.")
    if getKey("DOWN"):
        print("Tecla inferior pressionada.")


if __name__ == "__main__":
    init()
    while True:
        main()

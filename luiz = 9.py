import pygame
import time
import random

pygame.init()

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Tela do jogo (Modo Fullscreen)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Modo Fullscreen
pygame.display.set_caption('Jogo da Cobrinha')

# Dimensões da tela (Agora as variáveis largura e altura são definidas dinamicamente)
largura, altura = pygame.display.get_surface().get_size()

# Relógio
clock = pygame.time.Clock()

# Tamanho da cobra e da comida
tamanho_cobra = 10
velocidade = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Função para desenhar a cobra
def nossa_cobra(tamanho_cobra, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(screen, verde, [x[0], x[1], tamanho_cobra, tamanho_cobra])

# Função para mostrar a pontuação
def sua_pontuacao(pontos):
    valor = score_font.render("Pontuação: " + str(pontos), True, preto)
    screen.blit(valor, [0, 0])

# Função de mensagem
def mensagem(msg, cor):
    mesg = font_style.render(msg, True, cor)
    screen.blit(mesg, [largura / 6, altura / 3])

# Função principal do jogo
def gameLoop():
    game_over = False
    game_close = False

    # Posições iniciais da cobra
    x1 = largura / 2
    y1 = altura / 2

    x1_mudanca = 0
    y1_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(azul)
            mensagem("Você perdeu! Pressione R para jogar novamente ou Q para sair", vermelho)
            sua_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_cobra
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_cobra
                    y1_mudanca = 0
                elif event.key == pygame.K_UP:
                    y1_mudanca = -tamanho_cobra
                    x1_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_cobra
                    x1_mudanca = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            game_close = True
        x1 += x1_mudanca
        y1 += y1_mudanca
        screen.fill(azul)
        pygame.draw.rect(screen, vermelho, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])
        lista_cobra.append([x1, y1])
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for x in lista_cobra[:-1]:
            if x == [x1, y1]:
                game_close = True

        nossa_cobra(tamanho_cobra, lista_cobra)
        sua_pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

gameLoop()


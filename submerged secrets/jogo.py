import pygame
import random

pygame.init()

LARGURA, ALTURA = 800, 600

AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
CINZA_CLARO = (200, 200, 200)

TIPOS_ITENS = [
    {"cor": VERMELHO, "tipo": "vida"},
    {"cor": VERDE, "tipo": "moeda"},
    {"cor": AMARELO, "tipo": "bonus"}
]

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Coletáveis Diferentes")

fonte_menu = pygame.font.SysFont("arial", 36)
fonte_jogo = pygame.font.SysFont("arial", 16)

def criar_item():
    tipo = random.choice(TIPOS_ITENS)
    x = random.randint(0, LARGURA - 20)
    y = random.randint(0, ALTURA - 20)
    rect = pygame.Rect(x, y, 20, 20)
    return {"rect": rect, "cor": tipo["cor"], "tipo": tipo["tipo"]}

def tela_menu():
    rodando_menu = True
    fonte_titulo = pygame.font.Font("Pieces of Eight.ttf", 92)
    fonte_instrucao = pygame.font.SysFont("arial", 28)
    imagem_menu = pygame.image.load("tela menu.jpg")
    imagem_menu = pygame.transform.scale(imagem_menu, (LARGURA, ALTURA))
    

    while rodando_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    rodando_menu = False
        
        tela.blit(imagem_menu, (0, 0))

        
        # Título
        titulo_texto = fonte_titulo.render("Submerged Secrets", True, BRANCO)
        titulo_rect = titulo_texto.get_rect(center=(LARGURA // 2, ALTURA // 3))
        tela.blit(titulo_texto, titulo_rect)
        
        # Instrução para começar
        instrucao_texto = fonte_instrucao.render("Pressione ENTER para começar", True, BRANCO)
        instrucao_rect = instrucao_texto.get_rect(center=(LARGURA // 2, ALTURA // 2))
        tela.blit(instrucao_texto, instrucao_rect)
        
        pygame.display.flip()

def main():
    # Variáveis do jogo
    jogador_size = 40
    jogador = pygame.Rect(100, 100, jogador_size, jogador_size)
    velocidade = 5

    itens = [criar_item() for _ in range(3)]
    contadores = {"vida": 0, "moeda": 0, "bonus": 0}

    TEMPO_GERACAO = 3000
    pygame.time.set_timer(pygame.USEREVENT, TEMPO_GERACAO)

    clock = pygame.time.Clock()
    rodando = True
    imagem_jogo = pygame.image.load("tela jogo.png")
    imagem_jogo = pygame.transform.scale(imagem_jogo, (LARGURA, ALTURA))

    while rodando:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.USEREVENT:
                itens.append(criar_item())

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jogador.x -= velocidade
        if teclas[pygame.K_RIGHT]:
            jogador.x += velocidade
        if teclas[pygame.K_UP]:
            jogador.y -= velocidade
        if teclas[pygame.K_DOWN]:
            jogador.y += velocidade

        jogador.clamp_ip(tela.get_rect())

        for item in itens[:]:
            if jogador.colliderect(item["rect"]):
                contadores[item["tipo"]] += 1
                itens.remove(item)

        tela.blit(imagem_jogo, (0, 0))
        pygame.draw.rect(tela, BRANCO, jogador)
        for item in itens:
            pygame.draw.ellipse(tela, item["cor"], item["rect"])

        texto_vida = fonte_jogo.render(f"Baú: {contadores['vida']}", True, CINZA_CLARO)
        texto_moeda = fonte_jogo.render(f"Pérola: {contadores['moeda']}", True, CINZA_CLARO)
        texto_bonus = fonte_jogo.render(f"Garrafa: {contadores['bonus']}", True, CINZA_CLARO)

        tela.blit(texto_vida, (10, 10))
        tela.blit(texto_moeda, (10, 30))
        tela.blit(texto_bonus, (10, 50))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    tela_menu()

    main()


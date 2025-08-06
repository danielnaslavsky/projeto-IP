import pygame
import random
import os

pygame.init()

MARGEM_LATERAL = 90
MARGEM_SUPERIOR = 90

LARGURA, ALTURA = 800, 600

AZUL = (0, 0, 255)                      
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
CINZA_CLARO = (200, 200, 200)

TIPOS_ITENS = ["Bau", "Perola", "Garrafa"]

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Coletáveis Diferentes")

fonte_menu = pygame.font.SysFont("arial", 36)
fonte_jogo = pygame.font.SysFont("arial", 24)

# Carregar imagens dos itens
imagens_itens = {
    "Bau": pygame.image.load("bau.png"),
    "Perola": pygame.image.load("perola.png"),
    "Garrafa": pygame.image.load("garrafa.png") 
}
imagem_tubarao = pygame.image.load("tubarao.png")
imagem_tubarao = pygame.transform.scale(imagem_tubarao, (160, 160))
imagem_mergulhador = pygame.image.load("mergulhador.png")
imagem_mergulhador = pygame.transform.scale(imagem_mergulhador, (80, 80))

contadores = {"Bau": 0, "Perola": 0, "Garrafa": 0}

# Redimensionar imagens dos itens
for chave in imagens_itens:
    imagens_itens[chave] = pygame.transform.scale(imagens_itens[chave], (40, 40))
    
def criar_item():
    tipo = random.choice(TIPOS_ITENS)
    largura_item = 20
    altura_item = 20
    x = random.randint(MARGEM_LATERAL, LARGURA - MARGEM_LATERAL - largura_item)
    y = random.randint(MARGEM_SUPERIOR, ALTURA - MARGEM_SUPERIOR - altura_item)
    rect = pygame.Rect(x, y, 20, 20)
    return {"rect": rect, "tipo": tipo}

def tela_menu():
    rodando_menu = True

    if not os.path.exists("Pieces of Eight.ttf"):
        fonte_titulo = pygame.font.SysFont("arial", 92)
    else:
        fonte_titulo = pygame.font.Font("Pieces of Eight.ttf", 92)

    fonte_instrucao = pygame.font.SysFont("arial", 28)
    imagem_menu = pygame.image.load("tela menu.jpg")
    imagem_menu = pygame.transform.scale(imagem_menu, (LARGURA, ALTURA))

    mostrar_texto = True
    tempo_anterior = pygame.time.get_ticks()
    intervalo_piscar = 500  # milissegundos

    while rodando_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    rodando_menu = False

        # Atualiza o timer para piscar
        agora = pygame.time.get_ticks()
        if agora - tempo_anterior > intervalo_piscar:
            mostrar_texto = not mostrar_texto
            tempo_anterior = agora

        tela.blit(imagem_menu, (0, 0))

        # Título
        titulo_texto = fonte_titulo.render("Submerged Secrets", True, BRANCO)
        titulo_rect = titulo_texto.get_rect(center=(LARGURA // 2, ALTURA // 3))
        tela.blit(titulo_texto, titulo_rect)

        # Mostrar ou esconder a instrução para piscar
        if mostrar_texto:
            instrucao_texto = fonte_instrucao.render("Pressione ENTER para começar", True, BRANCO)
            instrucao_rect = instrucao_texto.get_rect(center=(LARGURA // 2, ALTURA // 2))
            tela.blit(instrucao_texto, instrucao_rect)

        pygame.display.flip()

def tela_game_over():
    fonte_game_over = pygame.font.Font("Pieces of Eight.ttf", 96)
    instrucao = pygame.font.SysFont("arial", 28)
    imagem_game_over = pygame.image.load("tela menu.jpg")  # Você pode trocar por outra imagem se quiser
    imagem_game_over = pygame.transform.scale(imagem_game_over, (LARGURA, ALTURA))
    
    relatorio_bau = pygame.font.Font("Pieces of Eight.ttf", 30)
    relatorio_perola = pygame.font.Font("Pieces of Eight.ttf", 30)
    relatorio_garrafa = pygame.font.Font("Pieces of Eight.ttf", 30)
    
    mostrar_texto = True
    tempo_anterior = pygame.time.get_ticks()
    intervalo_piscar = 500  # milissegundos
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    rodando = False  # Volta para o menu
        
        # Atualiza o timer para piscar
        agora = pygame.time.get_ticks()
        if agora - tempo_anterior > intervalo_piscar:
            mostrar_texto = not mostrar_texto
            tempo_anterior = agora
        
        tela.blit(imagem_game_over, (0, 0))
        texto = fonte_game_over.render("Game Over", True, VERMELHO)
        texto_rect = texto.get_rect(center=(LARGURA // 2, ALTURA // 3))
        tela.blit(texto, texto_rect)

        relatorio_bau_texto = relatorio_bau.render(f"Baús coletados: {contadores['Bau']}", False, (255,124,0))
        relatorio_bau_rect = relatorio_bau_texto.get_rect(center=(LARGURA // 2, ALTURA / 2.2))
        tela.blit(relatorio_bau_texto, relatorio_bau_rect)
        
        relatorio_perola_texto = relatorio_perola.render(f"Pérolas coletadas: {contadores['Perola']}", False, (255,124,0))
        relatorio_perola_rect = relatorio_perola_texto.get_rect(center=(LARGURA // 2, ALTURA / 1.9))
        tela.blit(relatorio_perola_texto, relatorio_perola_rect)
        
        relatorio_garrafa_texto = relatorio_garrafa.render(f"Garrafas coletadas: {contadores['Garrafa']}", False, (255,124,0))
        relatorio_garrafa_rect = relatorio_garrafa_texto.get_rect(center=(LARGURA // 2, ALTURA / 1.65))
        tela.blit(relatorio_garrafa_texto, relatorio_garrafa_rect)
        
        # Mostrar ou esconder o texto da instrução para piscar
        if mostrar_texto:
            instrucao_texto = instrucao.render("Pressione ENTER para voltar ao menu", True, BRANCO)
            instrucao_rect = instrucao_texto.get_rect(center=(LARGURA // 2, ALTURA / 1.4))
            tela.blit(instrucao_texto, instrucao_rect)            

        pygame.display.flip()



def main():
    contadores["Bau"] = 0
    contadores["Garrafa"] = 0
    contadores['Perola'] = 0 
    # Dimensões das imagens
    mergulhador_largura, mergulhador_altura = 80, 80
    tubarao_largura_img, tubarao_altura_img = 160, 160

    # Hitbox do mergulhador (menor que imagem)
    hitbox_largura, hitbox_altura = 20, 20
    # Hitbox do tubarão (menor que imagem)
    hitbox_largura_t, hitbox_altura_t = 80, 80

    # Posição inicial do jogador (topo esquerdo da imagem)
    pos_x, pos_y = 100, 100
    # Criar hitbox centralizada
    jogador = pygame.Rect(
        pos_x + (mergulhador_largura - hitbox_largura) // 2,
        pos_y + (mergulhador_altura - hitbox_altura) // 2,
        hitbox_largura,
        hitbox_altura
    )

    velocidade = 5

    # Posição inicial do tubarão
    pos_x_t = random.randint(0, LARGURA - tubarao_largura_img)
    pos_y_t = random.randint(0, ALTURA - tubarao_altura_img)

    tubarao = pygame.Rect(
        pos_x_t + (tubarao_largura_img - hitbox_largura_t) // 2,
        pos_y_t + (tubarao_altura_img - hitbox_altura_t) // 2,
        hitbox_largura_t,
        hitbox_altura_t
    )

    direcao_tubarao= [random.choice([-1, 1]), random.choice([-1, 1])]
    velocidade_tubarao = 5

    itens = [criar_item() for _ in range(3)]

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
            pos_x -= velocidade
        if teclas[pygame.K_RIGHT]:
            pos_x += velocidade
        if teclas[pygame.K_UP]:
            pos_y -= velocidade
        if teclas[pygame.K_DOWN]:
            pos_y += velocidade

        # Manter dentro da tela (imagem)
        pos_x = max(0, min(pos_x, LARGURA - mergulhador_largura))
        pos_y = max(0, min(pos_y, ALTURA - mergulhador_altura))

        # Atualizar hitbox do jogador centralizada
        jogador.x = pos_x + (mergulhador_largura - hitbox_largura) // 2
        jogador.y = pos_y + (mergulhador_altura - hitbox_altura) // 2

        # Movimento do tubarão
        pos_x_t += direcao_tubarao[0] * velocidade_tubarao
        pos_y_t += direcao_tubarao[1] * velocidade_tubarao

        # Manter dentro da tela (imagem tubarão)
        if pos_x_t < 0 or pos_x_t > LARGURA - tubarao_largura_img:
            direcao_tubarao[0] *= -1
        if pos_y_t < 0 or pos_y_t > ALTURA - tubarao_altura_img:
            direcao_tubarao[1] *= -1

        pos_x_t = max(0, min(pos_x_t, LARGURA - tubarao_largura_img))
        pos_y_t = max(0, min(pos_y_t, ALTURA - tubarao_altura_img))

        # Atualizar hitbox do tubarão centralizada
        tubarao.x = pos_x_t + (tubarao_largura_img - hitbox_largura_t) // 2
        tubarao.y = pos_y_t + (tubarao_altura_img - hitbox_altura_t) // 2

        # Colisão jogador-tubarão
        if jogador.colliderect(tubarao):
            tela_game_over()
            return 

        # Coletar itens
        for item in itens[:]:
            if jogador.colliderect(item["rect"]):
                contadores[item["tipo"]] += 1
                itens.remove(item)

        tela.blit(imagem_jogo, (0, 0))
        tela.blit(imagem_mergulhador, (pos_x, pos_y))  # desenha imagem na posição real

        for item in itens:
            imagem = imagens_itens[item["tipo"]]
            tela.blit(imagem, item["rect"])

        texto_Bau = fonte_jogo.render(f"Baú: {contadores['Bau']}", True, CINZA_CLARO)
        texto_Perola = fonte_jogo.render(f"Pérola: {contadores['Perola']}", True, CINZA_CLARO)
        texto_Garrafa = fonte_jogo.render(f"Garrafa: {contadores['Garrafa']}", True, CINZA_CLARO)
        
        tela.blit(texto_Bau, (10, 10))
        tela.blit(texto_Perola, (10, 30))
        tela.blit(texto_Garrafa, (10, 50))

        tela.blit(imagem_tubarao, (pos_x_t, pos_y_t))  # desenha imagem na posição real

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    while True:
        tela_menu()
        main()
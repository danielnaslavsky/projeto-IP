import pygame
import random
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Iniciando o jogo
pygame.init()
pygame.mixer.init()
#Música (trilha sonora, efeito de quando coleta um ítem, efeito de quando perde)
pygame.mixer.music.load(os.path.join("..","audios","musica.mp3"))
som_coleta = pygame.mixer.Sound(os.path.join("..", "audios", "coletar.mp3"))
som_gameover = pygame.mixer.Sound(os.path.join("..", "audios", "gameover.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

#Medidas da tela
MARGEM_LATERAL = 90
MARGEM_SUPERIOR = 90

LARGURA, ALTURA = 800, 600

#Cores 
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
CINZA_CLARO = (200, 200, 200)
COR_OXIGENIO = (0, 255, 255)

#Coletáveis disponíveis 
TIPOS_ITENS = ["Bau", "Perola", "Garrafa", "Oxigenio"]

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Submerged Secrets")

fonte_menu = pygame.font.SysFont("arial", 36)
fonte_jogo = pygame.font.SysFont("arial", 24)

#Colocando as imagens no jogo
imagens_itens = {
    "Bau": pygame.image.load(os.path.join("..", "Sprites", "bau.png")),
    "Perola": pygame.image.load(os.path.join("..", "Sprites", "perola.png")),
    "Garrafa": pygame.image.load(os.path.join("..", "Sprites", "garrafa.png")),
    "Oxigenio": pygame.image.load(os.path.join("..", "Sprites", "oxigenio.png"))
}

imagem_tubarao = pygame.transform.scale(pygame.image.load(os.path.join("..", "Sprites", "tubarao.png")), (160, 160))
imagem_mergulhador = pygame.transform.scale(pygame.image.load(os.path.join("..", "Sprites", "mergulhador.png")), (80, 80))

for chave in imagens_itens:
    imagens_itens[chave] = pygame.transform.scale(imagens_itens[chave], (40, 40))

#Contadores e pontuação
contadores = {"Bau": 0, "Perola": 0, "Garrafa": 0}
pontuacoes = [0, 5]

#Criando a função para onde os coletáveis vão aparecer na tela
def criar_item():
    tipo = random.choice(TIPOS_ITENS)
    largura_img, altura_img = imagens_itens[tipo].get_size()
    x = random.randint(MARGEM_LATERAL, LARGURA - MARGEM_LATERAL - largura_img)
    y = random.randint(MARGEM_SUPERIOR, ALTURA - MARGEM_SUPERIOR - altura_img)
    rect = pygame.Rect(x, y, largura_img, altura_img)
    return {"rect": rect, "tipo": tipo}

#Criando função para a tela do menu 
def tela_menu():
    rodando_menu = True
    fonte_titulo = pygame.font.Font(os.path.join("..", "Fonte", "Pieces of Eight.ttf"), 92)
    fonte_instrucao = pygame.font.SysFont("arial", 28)
    imagem_menu = pygame.transform.scale(pygame.image.load(os.path.join("..", "Fundos de tela", "tela menu.jpg")), (LARGURA, ALTURA))
    mostrar_texto = True
    tempo_anterior = pygame.time.get_ticks()
    intervalo_piscar = 500

    while rodando_menu:
        for resposta in pygame.event.get():
            if resposta.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if resposta.type == pygame.KEYDOWN and resposta.key == pygame.K_RETURN:
                rodando_menu = False

        agora = pygame.time.get_ticks()
        if agora - tempo_anterior > intervalo_piscar:
            mostrar_texto = not mostrar_texto
            tempo_anterior = agora

        tela.blit(imagem_menu, (0, 0))
        titulo = fonte_titulo.render("Submerged Secrets", True, BRANCO)
        tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, ALTURA // 3)))
        if mostrar_texto:
            instr = fonte_instrucao.render("Pressione ENTER para começar", True, BRANCO)
            tela.blit(instr, instr.get_rect(center=(LARGURA // 2, ALTURA // 2)))

        pygame.display.flip()

#Função para criar a tela quando o jogador perder o jogo
def tela_game_over():
    #Definindo as fontes
    fonte_go = pygame.font.Font(os.path.join("..", "Fonte", "Pieces of Eight.ttf"), 96)
    fonte_rel = pygame.font.Font(os.path.join("..", "Fonte", "Pieces of Eight.ttf"), 30)
    fonte_pontuacao = pygame.font.Font(os.path.join("..", "Fonte", "Pieces of Eight.ttf"), 50)
    fonte_instr = pygame.font.SysFont("arial", 28)
    imagem_go = pygame.transform.scale(pygame.image.load(os.path.join("..", "Fundos de tela", "tela jogo.png")), (LARGURA, ALTURA))
    mostrar = True
    ant = pygame.time.get_ticks()
    intervalo = 500

    while True:
        for resposta in pygame.event.get():
            if resposta.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if resposta.type == pygame.KEYDOWN and resposta.key == pygame.K_RETURN:
                return

        agora = pygame.time.get_ticks()
        if agora - ant > intervalo:
            mostrar = not mostrar
            ant = agora

        tela.blit(imagem_go, (0, 0))
        go = fonte_go.render("Game Over", True, VERMELHO)
        tela.blit(go, go.get_rect(center=(LARGURA // 2, ALTURA // 3)))
        tela.blit(fonte_rel.render(f"Baús coletados: {contadores['Bau']}", True, (255,124,0)), (300, 250))
        tela.blit(fonte_rel.render(f"Pérolas coletadas: {contadores['Perola']}", True, (255,124,0)), (282, 290))
        tela.blit(fonte_rel.render(f"Garrafas coletadas: {contadores['Garrafa']}", True, (255,124,0)), (275, 330))
        tela.blit(fonte_pontuacao.render(f"Pontuação Total: {pontuacoes[0]}", True, (100,150,0)), (219, 360))
        if mostrar:
            inst = fonte_instr.render("ENTER para voltar ao menu", True, BRANCO)
            tela.blit(inst, inst.get_rect(center=(LARGURA // 2, ALTURA / 1.35)))
        pygame.display.flip()

def main():
    for chave in contadores:
        contadores[chave] = 0
        
    #zera a pontuação total ao iniciar novo jogo e o bonus
    pontuacoes = [0,5]
    #Posição do jogador no eixo x e y 
    pos_x, pos_y = 100, 100
    jogador = pygame.Rect(pos_x + 30, pos_y + 30, 20, 20)
    #velocidade jogador
    velocidade = 3

    #Posição do tubarão no eixo x e y
    pos_xt = random.randint(0, LARGURA - 160)
    pos_yt = random.randint(0, ALTURA - 160)
    tubarao = pygame.Rect(pos_xt + 40, pos_yt + 40, 80, 80)
    dirs = [random.choice([-1, 1]), random.choice([-1, 1])]
    #velocidade tubarão
    vel_t = 5

    itens = [criar_item() for _ in range(3)]
    pygame.time.set_timer(pygame.USEREVENT, 3000)

    #Controle do oxigenio
    oxigenio_max = 30000
    oxigenio_rest = oxigenio_max
    ant_oxigenio = pygame.time.get_ticks()

    #Temporizador
    clock = pygame.time.Clock()
    img_jt = pygame.transform.scale(pygame.image.load("../Fundos de tela/tela jogo.png"), (LARGURA, ALTURA))

    rodando = True
    while rodando:
        clock.tick(60)

        for resposta in pygame.event.get():
            if resposta.type == pygame.QUIT:
                rodando = False
            if resposta.type == pygame.USEREVENT:
                itens.append(criar_item())

        #Identificando se o jogador apertou a setinha para cima, para baixo, para a direita ou para a esquerda
        botao = pygame.key.get_pressed()
        if botao[pygame.K_LEFT]: pos_x -= velocidade
        if botao[pygame.K_RIGHT]: pos_x += velocidade
        if botao[pygame.K_UP]: pos_y -= velocidade
        if botao[pygame.K_DOWN]: pos_y += velocidade

        pos_x = max(0, min(pos_x, LARGURA - 80))
        pos_y = max(0, min(pos_y, ALTURA - 80))
        jogador.x, jogador.y = pos_x + 30, pos_y + 30

        pos_xt += dirs[0] * vel_t
        pos_yt += dirs[1] * vel_t
        if pos_xt < 0 or pos_xt > LARGURA - 160: dirs[0] *= -1
        if pos_yt < 0 or pos_yt > ALTURA - 160: dirs[1] *= -1
        tubarao.x, tubarao.y = pos_xt + 40, pos_yt + 40

        #Caso o jogador colida com o tubarão
        if jogador.colliderect(tubarao):
            som_gameover.play()
            tela_game_over()
            return

        now = pygame.time.get_ticks()
        passada = now - ant_oxigenio
        oxigenio_rest -= passada
        ant_oxigenio = now
        #Verifica se o tempo acabou e o jogador morre por falta de ar 
        if oxigenio_rest <= 0:
            som_gameover.play()
            tela_game_over()
            return
        #Verifica se o jogador coletou o oxigênio 
        for item in itens[:]:
            if jogador.colliderect(item["rect"]):
                if item["tipo"] == "Oxigenio":
                    # Adiciona 10 segundos para o tempo do oxigênio
                    oxigenio_rest = min(oxigenio_rest + 10000, oxigenio_max)
                else:
                    contadores[item["tipo"]] += 1
                som_coleta.play()
                itens.remove(item)
            #Se o jogador coletar certos itens, ocorrem mudanças no jogo
            if jogador.colliderect(item["rect"]):
                if item["tipo"] == "Garrafa":
                    velocidade += velocidade * 0.07
                if item["tipo"] == 'Perola':
                    vel_t += vel_t * 0.1
                    pontuacoes[1] += 5
                if item["tipo"] == 'Bau':
                    pontuacoes[0] += pontuacoes[1]
        
        tela.blit(img_jt, (0, 0))
        tela.blit(imagem_mergulhador, (pos_x, pos_y))
        tela.blit(imagem_tubarao, (pos_xt, pos_yt))
        for it in itens:
            tela.blit(imagens_itens[it["tipo"]], it["rect"])

        #Contador com imagens e números ao lado
        x_base = 10
        y_base = 10
        espaco_entre = 60

        for i, chave in enumerate(["Bau", "Perola", "Garrafa"]):
            tela.blit(imagens_itens[chave], (x_base + i * espaco_entre, y_base))
            texto = fonte_jogo.render(str(contadores[chave]), True, CINZA_CLARO)
            tela.blit(texto, (x_base + 40 + i * espaco_entre, y_base + 10))

        #Oxigênio em texto separado
        tela.blit(fonte_jogo.render(f"Oxigênio: {max(0, oxigenio_rest // 1000)}s", True, COR_OXIGENIO), (10, 70))

        #Mostrar pontuação no final do jogo
        tela.blit(fonte_jogo.render(f"Pontuação: {pontuacoes[0]}", True, BRANCO), (10, 95))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    while True:
        tela_menu()

        main()






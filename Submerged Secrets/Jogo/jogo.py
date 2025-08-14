import pygame
import random
import os
import sys

#Início
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
pygame.mixer.init()

#Dimensões do jogo
LARGURA, ALTURA = 800, 600
MARGEM_LATERAL, MARGEM_SUPERIOR = 90, 90

#Lista de cores 
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
CINZA_CLARO = (200, 200, 200)
COR_OXIGENIO = (0, 255, 255)

TIPOS_ITENS = ["Bau", "Perola", "Garrafa", "Oxigenio"]

#Sons usados 
pygame.mixer.music.load(os.path.join("..", "audios", "musica.mp3"))
som_coleta = pygame.mixer.Sound(os.path.join("..", "audios", "coletar.mp3"))
som_gameover = pygame.mixer.Sound(os.path.join("..", "audios", "gameover.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

#Fontes usadas
fonte_menu = pygame.font.SysFont("arial", 36)
fonte_jogo = pygame.font.SysFont("arial", 24)

#Imagens utilizadas
imagens_itens = {
    "Bau": pygame.image.load(os.path.join("..", "Sprites", "bau.png")),
    "Perola": pygame.image.load(os.path.join("..", "Sprites", "perola.png")),
    "Garrafa": pygame.image.load(os.path.join("..", "Sprites", "garrafa.png")),
    "Oxigenio": pygame.image.load(os.path.join("..", "Sprites", "oxigenio.png"))
}
for chave in imagens_itens:
    imagens_itens[chave] = pygame.transform.scale(imagens_itens[chave], (40, 40))

imagem_tubarao = pygame.transform.scale(pygame.image.load(os.path.join("..", "Sprites", "tubarao.png")), (160, 160))
imagem_mergulhador = pygame.transform.scale(pygame.image.load(os.path.join("..", "Sprites", "mergulhador.png")), (80, 80))


#Usando as classes
class Item:
    #Tela 
    def __init__(self):
        self.tipo = random.choice(TIPOS_ITENS)
        largura_img, altura_img = imagens_itens[self.tipo].get_size()
        x = random.randint(MARGEM_LATERAL, LARGURA - MARGEM_LATERAL - largura_img)
        y = random.randint(MARGEM_SUPERIOR, ALTURA - MARGEM_SUPERIOR - altura_img)
        self.rect = pygame.Rect(x, y, largura_img, altura_img)

    def desenhar(self, tela):
        tela.blit(imagens_itens[self.tipo], self.rect)

#Para o mergulhador
class Jogador:
    #Posicao inicial do jogador em x e y e a velocidade dele 
    def __init__(self):
        self.pos_x, self.pos_y = 100, 100
        self.velocidade = 3
        self.rect = pygame.Rect(self.pos_x + 30, self.pos_y + 30, 20, 20)

    #Movimento jogador
    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.pos_x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.pos_x += self.velocidade
        if teclas[pygame.K_UP]:
            self.pos_y -= self.velocidade
        if teclas[pygame.K_DOWN]:
            self.pos_y += self.velocidade

        self.pos_x = max(0, min(self.pos_x, LARGURA - 80))
        self.pos_y = max(0, min(self.pos_y, ALTURA - 80))
        self.rect.x, self.rect.y = self.pos_x + 30, self.pos_y + 30

    #Adicionar a animação do jogador
    def desenhar(self, tela):
        tela.blit(imagem_mergulhador, (self.pos_x, self.pos_y))

#Para o tubarão
class Tubarao:
    def __init__(self):
        self.pos_x = random.randint(0, LARGURA - 160)
        self.pos_y = random.randint(0, ALTURA - 160)
        self.rect = pygame.Rect(self.pos_x + 40, self.pos_y + 40, 80, 80)
        self.direcao = [random.choice([-1, 1]), random.choice([-1, 1])]
        self.velocidade = 5

    #Movimento do tubarão
    def mover(self):
        self.pos_x += self.direcao[0] * self.velocidade
        self.pos_y += self.direcao[1] * self.velocidade

        if self.pos_x < 0 or self.pos_x > LARGURA - 160:
            self.direcao[0] *= -1
        if self.pos_y < 0 or self.pos_y > ALTURA - 160:
            self.direcao[1] *= -1

        self.rect.x, self.rect.y = self.pos_x + 40, self.pos_y + 40

    #Atribuir a imagem do tubarão
    def desenhar(self, tela):
        tela.blit(imagem_tubarao, (self.pos_x, self.pos_y))


class Jogo:
    def __init__(self):
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Submerged Secrets")
        self.clock = pygame.time.Clock()
        self.img_fundo = pygame.transform.scale(pygame.image.load("../Fundos de tela/tela jogo.png"), (LARGURA, ALTURA))
        self.resetar()

    #Após resetar a partida
    def resetar(self):
        self.contadores = {"Bau": 0, "Perola": 0, "Garrafa": 0}
        self.pontuacoes = [0, 5]
        self.jogador = Jogador()
        self.tubarao = Tubarao()
        self.itens = [Item() for _ in range(3)]
        pygame.time.set_timer(pygame.USEREVENT, 3000)
        self.oxigenio_max = 30000
        self.oxigenio_rest = self.oxigenio_max
        self.tempo_oxigenio = pygame.time.get_ticks()

    #Comando da tela de menu incial 
    def tela_menu(self):
        rodando_menu = True
        fonte_titulo = pygame.font.Font(os.path.join("..", "Fonte", "Pieces of Eight.ttf"), 92)
        fonte_instrucao = pygame.font.SysFont("arial", 28)
        imagem_menu = pygame.transform.scale(pygame.image.load(os.path.join("..", "Fundos de tela", "tela menu.jpg")), (LARGURA, ALTURA))
        mostrar_texto = True
        tempo_anterior = pygame.time.get_ticks()
        intervalo_piscar = 500

        while rodando_menu:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                    rodando_menu = False

            agora = pygame.time.get_ticks()
            if agora - tempo_anterior > intervalo_piscar:
                mostrar_texto = not mostrar_texto
                tempo_anterior = agora
            #Texto e fonte
            self.tela.blit(imagem_menu, (0, 0))
            titulo = fonte_titulo.render("Submerged Secrets", True, BRANCO)
            self.tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, ALTURA // 3)))
            if mostrar_texto:
                instr = fonte_instrucao.render("Pressione ENTER para começar", True, BRANCO)
                self.tela.blit(instr, instr.get_rect(center=(LARGURA // 2, ALTURA // 2)))

            pygame.display.flip()

    #Tela de game over (fim do jogo)
    def tela_game_over(self):
        fonte_go = pygame.font.Font(os.path.join("..", "Fonte", "Pieces of Eight.ttf"), 96)
        fonte_rel = pygame.font.Font(os.path.join("..", "Fonte", "Pieces of Eight.ttf"), 30)
        fonte_pontuacao = pygame.font.Font(os.path.join("..", "Fonte", "Pieces of Eight.ttf"), 50)
        fonte_instr = pygame.font.SysFont("arial", 28)
        imagem_go = pygame.transform.scale(pygame.image.load(os.path.join("..", "Fundos de tela", "tela jogo.png")), (LARGURA, ALTURA))
        mostrar = True
        ant = pygame.time.get_ticks()
        intervalo = 500

        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                    return

            agora = pygame.time.get_ticks()
            if agora - ant > intervalo:
                mostrar = not mostrar
                ant = agora

            #Texto e fonte 
            self.tela.blit(imagem_go, (0, 0))
            go = fonte_go.render("Game Over", True, VERMELHO)
            self.tela.blit(go, go.get_rect(center=(LARGURA // 2, ALTURA // 3)))
            self.tela.blit(fonte_rel.render(f"Baús coletados: {self.contadores['Bau']}", True, (255,124,0)), (300, 250))
            self.tela.blit(fonte_rel.render(f"Pérolas coletadas: {self.contadores['Perola']}", True, (255,124,0)), (282, 290))
            self.tela.blit(fonte_rel.render(f"Garrafas coletadas: {self.contadores['Garrafa']}", True, (255,124,0)), (275, 330))
            self.tela.blit(fonte_pontuacao.render(f"Pontuação Total: {self.pontuacoes[0]}", True, (100,150,0)), (219, 360))
            if mostrar:
                inst = fonte_instr.render("ENTER para voltar ao menu", True, BRANCO)
                self.tela.blit(inst, inst.get_rect(center=(LARGURA // 2, ALTURA / 1.35)))
            pygame.display.flip()

    #Jogo rodando 
    def rodar(self):
        rodando = True
        while rodando:
            self.clock.tick(60)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    rodando = False
                if e.type == pygame.USEREVENT:
                    self.itens.append(Item())

            self.jogador.mover()
            self.tubarao.mover()

            # Colisão com tubarão
            if self.jogador.rect.colliderect(self.tubarao.rect):
                som_gameover.play()
                self.tela_game_over()
                return

            # Oxigênio
            agora = pygame.time.get_ticks()
            passada = agora - self.tempo_oxigenio
            self.oxigenio_rest -= passada
            self.tempo_oxigenio = agora
            if self.oxigenio_rest <= 0:
                som_gameover.play()
                self.tela_game_over()
                return

            # Coletar itens
            for item in self.itens[:]:
                if self.jogador.rect.colliderect(item.rect):
                    if item.tipo == "Oxigenio":
                        self.oxigenio_rest = min(self.oxigenio_rest + 10000, self.oxigenio_max)
                    else:
                        self.contadores[item.tipo] += 1
                    som_coleta.play()

                    #Velocidade do mergulhador aumenta 7%
                    if item.tipo == "Garrafa":
                        self.jogador.velocidade *= 1.07
                    #Velocidade do tubarão aumenta 10%
                    if item.tipo == "Perola":
                        self.tubarao.velocidade *= 1.1
                        self.pontuacoes[1] += 5
                    #Incrementa a pontuação 
                    if item.tipo == "Bau":
                        self.pontuacoes[0] += self.pontuacoes[1]
                    #Remove os itens depois de coletados
                    self.itens.remove(item)

            #Desenho
            self.tela.blit(self.img_fundo, (0, 0))
            self.jogador.desenhar(self.tela)
            self.tubarao.desenhar(self.tela)
            for it in self.itens:
                it.desenhar(self.tela)

            #Informações críticas do mergulhador
            x_base, y_base, espaco_entre = 10, 10, 60
            for i, chave in enumerate(["Bau", "Perola", "Garrafa"]):
                self.tela.blit(imagens_itens[chave], (x_base + i * espaco_entre, y_base))
                texto = fonte_jogo.render(str(self.contadores[chave]), True, CINZA_CLARO)
                self.tela.blit(texto, (x_base + 40 + i * espaco_entre, y_base + 10))

            self.tela.blit(fonte_jogo.render(f"Oxigênio: {max(0, self.oxigenio_rest // 1000)}s", True, COR_OXIGENIO), (10, 70))
            self.tela.blit(fonte_jogo.render(f"Pontuação: {self.pontuacoes[0]}", True, BRANCO), (10, 95))
            pygame.display.flip()

        pygame.quit()


#Loop principal 
if __name__ == "__main__":
    jogo = Jogo()
    while True:
        jogo.tela_menu()
        jogo.resetar()
        jogo.rodar()

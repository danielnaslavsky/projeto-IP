# Relatório

## Título: *Submerged Secrets*

### Equipe 5
- Daniel José Naslavsky Aguiar <djna2>
- Diogo Dias Guimarães de Almeida <ddga>
- Joelle Calado Venâncio <jcv2>
- Marcela Paranhos Massa <mpm4>
- Paulo Gustavo Melo Braz e Silva <pgmbs>
- Pedro Henrique de Araújo Pimentel Neves <phapn>

---

## Sobre o jogo

O jogo **Submerged Secrets** transporta o jogador para o misterioso mundo submerso de Atlântida, onde ele assume o papel de um mergulhador em busca de tesouros escondidos nas profundezas do oceano.  
O objetivo é **coletar itens espalhados pelo cenário** para acumular pontos, mas o desafio é sobreviver antes que o oxigênio acabe ou que o mergulhador colida com o tubarão.

### Tipos de itens e funções
- **Baú** → Aumenta a pontuação.
- **Pérola** → Aumenta a velocidade do tubarão em 10%.
- **Garrafa** → Aumenta a velocidade de movimento do mergulhador em 7%.
- **Tanque de oxigênio** → Restaura parte do tempo de oxigênio disponível (+10 segundos).

O jogador deve se movimentar rapidamente para coletar o máximo possível, **administrando o oxigênio e evitando o contato com o tubarão**.  
Ao final da partida, é exibida uma tela de *game over* com a contagem de itens coletados e a pontuação total.

---

## Divisão do trabalho

O trabalho foi desenvolvido **de forma colaborativa**, com funções específicas:

- **Marcela e Diogo**: Ideação e parte artística (imagens, cenários, sprites), relatório final e tela de menu.
- **Daniel, Paulo e Pedro**: Mecânicas centrais (movimento, colisões, tubarão, sons, fontes), organização inicial do projeto, repositório GitHub e funções dos itens colecionáveis.
- **Joelle**: Ideação, tela de *game over*, criação dos slides e acompanhamento geral para coesão e clareza na entrega.

---

## Conceitos aprendidos em IP utilizados

A disciplina **Introdução à Programação** foi essencial para o desenvolvimento. Entre os conceitos aplicados:

- **Métodos / Funções**:
  - Item.__init__() → cria coletáveis aleatórios.  
  - Jogo.tela_menu() → exibe a tela inicial.  
  - Jogo.tela_game_over() → mostra o fim do jogo.  
  - Jogo.rodar() → controla o loop principal da gameplay.  
  - Jogador.mover() → movimenta o jogador.  
  - Tubarao.mover() → movimenta o tubarão.  

- **Condicionais (if/else)**:
  - Detectar colisões entre jogador e itens ou tubarão.  
  - Adicionar oxigênio ou atualizar pontuação ao coletar itens.  
  - Inverter direção do tubarão ao bater nas bordas.  
  - Encerrar o jogo quando oxigênio acabar ou houver colisão com tubarão.  

- **Estruturas de repetição (while, for)**:
  - Loop principal do jogo (Jogo.rodar()).  
  - Percorrer lista de itens para verificar colisões.  
  - Exibir contagem de itens coletados na tela.  

- **Dicionários**:
  - Armazenar quantidade de itens coletados: self.contadores = {"Bau": 0, "Perola": 0, "Garrafa": 0}.  
  - Armazenar pontuações: self.pontuacoes = [0, 5].

---

## Desafios, erros e lições

- **Erro inicial**: todos programando juntos → trabalho mais lento.  
  - Solução: divisão de tarefas por habilidade → mais eficiência.
- **Desafio técnico**: colisões entre personagem, itens e tubarão.  
  - Problemas resolvidos com pesquisas, vídeos e ajuda de monitores.  
- **Lições aprendidas**:  
  - Paciência para ajustes  
  - Comunicação clara  
  - Planejamento prévio  
  - Colaboração e escuta ativa

---

## Arquitetura do projeto

**Linguagem e biblioteca principal**: Python + Pygame  
Organizado em um único arquivo principal com:

### Definições iniciais e configuração
- Cores, dimensões e margens
- Inicialização do Pygame
- Carregamento e redimensionamento de imagens
- Dicionário contadores para itens

## Partes Modularizadas
- Função Jogo.tela_menu() 
   Exibe o menu inicial no início do jogo a cada nova partida.
- Função Jogador.mover() e Tubarao.mover()
   Controla o movimento do personagem analisado. Foi usada para o jogador e para o tubarão.
- Função Jogo.tela_game_over()
   Exibe a tela final do jogo, mostrando a pontuação final do jogador junto com o número de coletáveis conquistados.
- Função Jogo.rodar() 
   Executa o loop principal e integra os outros módulos.
- Função Jogador.desenhar()
   Auxilia na arte visual do jogo.
  - Função Jogo.resetar() 
  Reinicia as variáveis do jogo permitindo começar uma nova partida

---

## Orientação a Objetos (OO)
- Classe Jogador 
   Atribui a posição X e Y, a velocidade, a hitbox e a imagem.
- Classe Tubarao
   Atribui a posição X e Y, a velocidade, a hitbox e a imagem.
- Classe Item
   Atribui os coletáveis (suas imagens, posições e hitbox).
- Classe Jogo 
   Atribui o jogador, o tubarão, os coletáveis, as pontuações, os sons, as imagens, etc.


### Fluxo de Execução
1. Inicia com Jogo.tela_menu().
2. Ao pressionar **ENTER** → executa Jogo.rodar().
3. Se colidir com o tubarão ou o oxigênio acabar → Jogo.tela_game_over().
4. A partir da tela de menu, o jogador pode reiniciar uma nova partida.

---

## Bibliotecas, ferramentas e frameworks

- **Python** → linguagem principal
- **Pygame** → janelas, eventos, gráficos e sons
- **OS** → verificar existência de arquivos
- **Random** → gerar posições e direções aleatórias
- **Sys** → finalização limpa

**Outros recursos**:
- Fonte personalizada *Pieces of Eight.ttf*  
- Áudio: musica.mp3, coletar.mp3, gameover.mp3

---

## Imagens do Jogo

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 50px;">

  <img src="imagens_readme/foto inicio.png" alt="foto inicio" width="460"/>
  <img src="imagens_readme/foto meio.png" alt="foto meio" width="460"/>
  <img src="imagens_readme/foto fim.png" alt="foto meio" width="460"/>

</div>


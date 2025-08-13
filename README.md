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

- **Funções**:
  - criar_item() → gera coletáveis aleatórios  
  - tela_menu() → exibe a tela inicial  
  - tela_game_over() → mostra o fim do jogo  
  - main() → controla o loop principal da gameplay

- **Condicionais (if/else)**:
  - Detectar colisões  
  - Adicionar oxigênio ou pontuação  
  - Inverter direção do tubarão  
  - Encerrar o jogo  

- **Estruturas de repetição (while, for)**:
  - Loop principal do jogo  
  - Percorrer itens para verificar colisões  
  - Exibir contagem de itens  

- **Dicionários**:
  - Armazenar quantidade de itens coletados  
  - Ex.: contadores = {"Bau": 0, "Perola": 0, "Garrafa": 0}

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

### Funções principais
- criar_item() → gera posição e tipo de item
- tela_menu() → exibe tela inicial
- tela_game_over() → mostra resultados finais
- main() → loop principal (movimento, colisões, exibição)

### Fluxo de execução
1. Inicia com tela_menu()
2. Ao pressionar ENTER → executa main()
3. Se colidir com tubarão ou acabar oxigênio → tela_game_over()
4. Pode reiniciar a partir do menu

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


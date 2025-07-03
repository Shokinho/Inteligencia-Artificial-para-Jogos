# Inteligencia-Artificial-para-Jogos
Este repositório é dedicado a entrega de exercícios e trabalhos da disciplina de Inteligência Artificial para Jogos.

![tumblr_1aff4c9f7c8c765d4f4dc548dc4934ea_062fa789_2048](https://github.com/user-attachments/assets/f5dbd15d-df72-489f-9d81-adbdc6d861d4)

## Pesquisa de Ferramentas para Implementação de IA em Jogos
| Nome da Ferramenta | Descrição | Técnicas de IA | Link Oficial | Licença |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Procedural NPC Crowds Pro V2  | A ferramenta permite que o desenvolvedor implemente de forma rápida e fácil sistemas de IA de multidões e pedestres realistas em larga escala utilizando comportamentos procedurais com alto desempenho para a Unreal Engine.  | Behavior tree e sistema de pathfinding procedural  | [Link da ferramenta](https://www.fab.com/listings/6212ccdd-1352-44e8-a545-7646042f0887)  | Licença Padrão  |
| Overtone - Realistic AI Offline Text to Speech (TTS)  | Com o Overtone, o desenvolvedor pode adicionar facilmente vozes realistas geradas por IA aos seus jogos, dando vida aos seus personagens e aprimorando a experiência geral do jogo.  | Não foi citado pelo autor quais técnicas de IA foram utilizadas  | [Link da ferramenta](https://www.fab.com/listings/605ad66e-0bae-411c-859e-36ac07e78b10)  | Licença Padrão  |
| MindMaker Machine Learning AI Plugin  | O MindMaker AI Plugin é um plugin de código aberto que permite que jogos e simulações dentro do UE4 e UE5 funcionem como ambientes para treinar agentes autônomos de aprendizado de máquina.  | Redes neurais, por meio de blueprints  | [Link da ferramenta](https://github.com/krumiaa/MindMaker)  | Licença de Código Aberto  |
| GOAP NPC: Goal-Oriented Action Planning for Non-Player Characters (Code Plugin)  | Goal-Oriented Action Planning (GOAP) fornece uma maneira genérica e natural de construir Personagens Não-Jogadores (NPCs) com Inteligência Artificial (IA). Usado em jogos comerciais modernos (Shooters, Action RPGs, etc.), ele oferece tomada de decisão inteligente com grande escalabilidade.  | Algoritmo de busca heurística A*  | [Link da ferramenta](https://www.fab.com/listings/9a9f66b4-26f0-4a83-a758-3d8d4dd94ec5)  | UE Marketplace  |

Para mim, o mais interessante é o Procedural NPC Crowds Pro V2, pois com ele a pessoa pode fazer um sistema de pedrestres em uma parte pequena do jogo cujo este não seja o elemento principal, por exemplo, em um projeto meu, existe uma parte em que o jogo se passa no meio de uma cidade para que se tenha mais interação no decorrer da história, porém essa é uma parte bem pequena se for considerar o jogo inteiro. O Overtone - Realistic AI Offline Text to Speech (TTS) também é interessante para aqueles que traduzem jogos, já que, em alguns casos, foi usado uma IA para fazer a dublagem de jogos que não estavam em português, ou para pessoas que não tem muito dinheiro que queiram colocar vozes em seus jogos.

![tumblr_649449eec79486a4664978381458275b_393ba63c_2048](https://github.com/user-attachments/assets/1c1ee84d-ba6a-4116-8269-4ab3d0f1a4e4)

## Implementação de Steering Behaviors

### Explicação dos Steering Behaviors implementados
Steering Behaviors ou comportamentos de navegação são um conjunto de técnicas de Inteligência Artificial usados para fazer com que os movimentos de um agente pareçam realistas. Eles são baseados nas Leis da Mecânica e utilizam algoritmos simples. Em 1986, Craig Reynolds publicou um artigo no qual mostrava os comportamentos sendo usados para simular o movimento de um grupo de pássaros.

Seek and Flee ou Busca e Fuga são dois comportamentos nos quais o agente segue em direção a um alvo, que está imóvel, até chegar nele e se distância de um alvo, que está imóvel, pela direção oposta do mesmo, infinitamente, respectivamente.

Arrival ou Chegada é um comportamento no qual o agente segue em direção a um alvo que está imóvel e quando chega perto dele diminui sua velocidade até ficar parado. Ele é uma extensão do comportamento de Busca.

Pursuit and Evade ou Perseguição e Esquiva são dois comportamentos nos quais o agente segue em direção a um alvo, que está em movimento, até chegar nele e se distancia de um alvo, que está em movimento, pela direção oposta do mesmo, infinitamente, respectivamente. Ambos são uma extensão dos comportamentos de Busca e de Fuga e preveêm a trajetória que o alvo irá fazer no futuro, assim, antecipando o movimento dele.

Wander ou Vagar é um comportamento onde o agente anda aleatoriamente e sem rumo pelo local no qual se encontra.

Obstacle Avoidance ou Evitação de Obstáculos é um comportamento no qual o agente identifica a presença de obstáculos em seu ambiente e toma decisões para contorná-los de forma segura e eficiente, evitando colisões.

### Como utilizar o programa
O programa contém a visualização de cada um dos comportamentos implementados por meio das teclas. Para entender o contexto, é usado uma abelha para ser o agente e um pote de mel para ser o alvo. Abaixo encontramos a lista de teclas e suas funções:

F1 - Seek

F2 - Flee

F3 - Arrival

F4 - Pursuit

F5 - Evade

F6 - Wander

F7 - Obstacle Avoidance

Observação: No Pursuit e no Evade, os alvos são movimentados pelo mouse do usuário e no Wander, o alvo não é mostrado por se tratar de um comportamento somente em relação ao agente.

Para usar o programa é necessário baixar os arquivos da pasta Steering Behaviors e baixar a linguagem de programação Python e a biblioteca Pygame, além de executar o arquivo Game.py quando for usá-lo. Infelizmente, não houve tempo de fazer o executável do programa.

### Estrutura do código e principais arquivos
O programa está dividido em três partes: o Behaviors, o Agent e o Game. O Behaviors contém a classe pai dos comportamentos e as classes herdadas de cada um dos comportamentos. O Agent contém a classe do agente, o qual possui a posição do agente, a velocidade do agente, a velocidade máxima do agente, a força máxima do agente e o comportamento que o mesmo usa, além das funções de atualizar a posição do agente e de desenhá-lo na tela. O Game contém a classe do jogo, a qual inicia o programa e faz toda a execução dele.

### Desafios encontrados e como foram resolvidos
Não há muito conteúdo na internet sobre Steering Behaviors, principalmente em Python e em português. Portanto, foi necessário usar estudos de diferentes sites e livros e adaptá-los a linguagem de programação Python.

### Lista de referências consultadas
Livro AI for games Third Edition de Ian Millington

https://materialpublic.imd.ufrn.br/curso/disciplina/5/69/2/5

https://web.archive.org/web/20231202210651/https://dicionariotec.com/posts/busca-seek-fuga-flee-e-chegada-arrival

https://dicionariotec.com/posts/perseguir-pursuit-e-desviar-evade

https://dicionariotec.com/posts/vagar-wander

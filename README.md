# 8-Puzzle-AgentesAutonomos



## Configurando um ambiente virtual:

````bash
python3 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
````

## Executar teste:

````bash
pytest test_puzzle.py --capture=tee-sys
````

## Executar arquivo:

````bash
python main.py 
````

## Descricao do projeto
Projeto que gera os passos para chegar no estado final desejado para os estados inicias possiveis, apartir do algoritmo A*.

### Estados
Os estados sao representados por:
  * uma lista de listas, a qual tem como objetivo simular uma matriz (3X3)
  * e um operador, o qual descreve qual acao foi realizada. As acoes sao em relacao ao espaco vazio (representado como 0), por exemplo: o espaco vazio desce o numero de baixo sobe. Sendo as opcoes de operador: up, down, right e left

### Sucessores
Para gerar os sucessores e analisado a localizacao do espaco vazio, para assim listar as possibilidades de movimentacao. Sendo elas:
  * se a linha do espaco vazio for diferente da primeira, ele pode se movimentar para cima
  * se a linha do espaco vazio for diferente da ultima, ele pode se movimentar para baxo
  * se a coluna do espaco vazio for diferente da primeira, ele pode se movimentar para esquerda
  * se a coluna do espaco vazio for diferente da ultima, ele pode se movimentar para direita
 
 ### Heuristica
 A primeira implementacao foi verificando se os numeros estavam na posicao desejada, se nao estivesse aumentava um no valor de h. Porem, essa heuristica nao achava solucao para estados iniciais dificeis.
 
 Dessa forma foi implementada a heuristica com a distancia de manhattan. A qual calcula a distancia da posicao atual para a posicao desejada. Assim sendo possivel solucionar os estados iniciasi dificeis.
 
  Ja para uma resposta coerente para os problemas impossiveis, foi calculada a inversao (explicada nas seguintes fontes:https://www.youtube.com/watch?v=bhmCmbj9VAg, https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable)

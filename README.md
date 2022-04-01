# 8-Puzzle-AgentesAutonomos



## Configurando um ambiente virtual:

````bash
python3 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
sudo apt-get install python3-tk
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
Projeto que gera os passos para chegar no estado final desejado para os estados inicias possíveis, apartir do algoritmo A*.

### Estados
Os estados são representados por:
  * uma lista de listas, a qual tem como objetivo simular uma matriz (3X3)
  * e um operador, o qual descreve qual ação foi realizada. As ações são em relação ao espaço vazio (representado como 0), por exemplo: o espaço vazio desce o numero de baixo sobe. Sendo as opções de operador: up, down, right e left

### Sucessores
Para gerar os sucessores é analisado a localizacao do espaço vazio, para assim listar as possibilidades de movimentação. Sendo elas:
  * se a linha do espaco vazio for diferente da primeira, ele pode se movimentar para cima
  * se a linha do espaco vazio for diferente da ultima, ele pode se movimentar para baxo
  * se a coluna do espaco vazio for diferente da primeira, ele pode se movimentar para esquerda
  * se a coluna do espaco vazio for diferente da ultima, ele pode se movimentar para direita
 
 ### Heuristica
 A primeira implementação foi verificando se os numeros estavam na posição desejada, se não estivesse aumentava um no valor de h. Porem, essa heuristica nao achava solução para estados iniciais dificeis.
 
 Dessa forma foi implementada a heuristica com a distância de manhattan. A qual calcula a distância da posição atual para a posição desejada. Assim sendo possivel solucionar os estados iniciais difíceis.
 
  Já para ter uma resposta coerente para os problemas impossiveis, foi calculada a inversão (explicada nas seguintes fontes:https://www.youtube.com/watch?v=bhmCmbj9VAg, https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable)

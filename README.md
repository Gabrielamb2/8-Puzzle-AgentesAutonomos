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

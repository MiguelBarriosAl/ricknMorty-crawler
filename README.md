![](/rickmorty.png)
# Rick and Morty Crawler
Api crawler and stores Rick and Morty characters in a database Elasticsearch through asynchronous tasks

# Requirements

- Use this api https://rickandmortyapi.com/ to learn about where to find the Rick and Morty.

- Store Character (design your own schema) and some attributes:
    1. Character name
    2. Status
    3. Rick and Morty

# Installation
The installation intrusions are designed for an Ubuntu OS. For other OS you will have to change the necessary commands.

1. Install python==3.9

    `sudo apt update`
    
    `sudo apt install python3.9`
    
    `python --version`


2. Clone the repository

    `git clone https://github.com/MiguelBarriosAlvarez/RicknMorty-Crawler.git`


4. Install the virtualenv:

    `sudo apt-get install python3-pip`

    `sudo pip3 install virtualenv`
    
    `virtualenv venv `
    
    `source venv/bin/activate`


5. Install requirements

    `pip install -r requirements.txt`


5. Run the crawler

    `python3 main.py`
    
    `curl -X POST http://192.168.1.130:5000/v1`

6. Results

`{'name': 'Rick Sanchez', 'status': 'Alive', 'species': 'Human'}
{'name': 'Morty Smith', 'status': 'Alive', 'species': 'Human'}
{'name': 'Summer Smith', 'status': 'Alive', 'species': 'Human'}
{'name': 'Beth Smith', 'status': 'Alive', 'species': 'Human'}
{'name': 'Jerry Smith', 'status': 'Alive', 'species': 'Human'}`


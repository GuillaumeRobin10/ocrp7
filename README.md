version de python :3.8.5

Ce dépot regroupe un ensemble de script python qui permettent de réaliser un choix d'inverstissement.
Le choix d'inverstissment sera réaliser vers les données d'un fichier CSV.

# Application d'inverstissement.


## Fonctionnement

Pour que le script analyse les données de d'un fichier csv, les données doivent être dans l'ordre suivant: nom/prix/pourcentage de profit.
Le fichier csv doit contenir une en-tête et être nommé "Données.csv". Le fichier csv doit également être dans le même dossier que le script.

Lancer le script (voir la partie sur l'installation ) 


#### installation annexe
telecharger [python](https://www.python.org/downloads/ "python") et installez-le en suivant les instructions.


#### installation de l'application
#### Windows
1. rendez-vous dans le dossier ou ce situe le programme
2. Tout en maintenant la touche Maj ⇧ enfoncée, faites un clic droit et sélectionnez Ouvrir la fenêtre PowerShell ici.
3. entrez la commande : ``pip install virtualenv``
4. entrez la commande : ``virtualenv -p $env:python3 env``
5. entrez la commande : ``./env/scripts/activate.ps1``
6. entrez la commande : ``pip install -r requirements.txt``
7. entrez la commande : ``python optimized.py``
`
#### linux/mac
1. ouvrir le terminal (vous pouvez trouver l'outil directement en tapant “terminal” dans la barre de recherche des applications.(finder sous mac))
2. Rendez vous dans le dossier api (commande cd)
3. entrez la commande : ``pip3 install virtualenv``
4. entrez la commande : ``virtualenv -p python3 env``
5. entrez la commande :``source env/bin/activate``
6. entrez la commande : ``pip3 install -r requirements.txt``
7. entrez la commande : ``python3 optimized.py``

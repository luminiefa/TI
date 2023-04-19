# Projets
## Fonctions de main.py (partie1)

def load_log_from_file(relative_path):
"""
La fonction permet de récupérer les logs se trouvant dans un
fichier grâce au chemin relatif passé en argument de la fonction.
La fonction NE peut PAS lancer d’erreur. Si le chemin n'existe
pas, la fonction affiche "Le chemin n'existe pas" et donne le chemin
ABSOLU du fichier demandé.
S'il y a eu une exception, renvoyez explicitement un "None"
:param relative_path: String représentant un chemin relatif
(vers un fichier) par rapport au dossier courant.
:return: Renvoie un tableau de strings qui sont les logs
contenant les logs.



def load_logs_from_folder(folder_path):
"""
La fonction permet de charger les logs de tous les fichiers
présents dans un dossier. Le chemin
relatif en argument de la fonction est le chemin relatif
vers un dossier.
La fonction NE peut PAS lancer d’erreur. Si le chemin
n'existe pas, la fonction affiche "Le chemin n'existe pas" et
retourne le chemin ABSOLU du dossier demandé.
S'il y a eu une exception, renvoyez explicitement un "None".
:param folder_path: String représentant un chemin relatif
(vers un dossier) par rapport au
dossier courant
:return: Renvoie un tableau de strings qui sont les logs contenant les logs ou None en cas d'erreur


 def get_folders_and_subfolders(folder_path):
"""
La fonction renvoie une liste de chemins relatifs avec le chemin
folder_path et ses sous-dossiers.
La fonction NE peut PAS lancer d’erreur. Si le chemin n'existe pas, la
fonction affiche "Le chemin n'existe pas" et donne le chemin ABSOLU du
dossier demandé.
S'il y a eu une exception, renvoyez explicitement un "None".
:param folder_path: String représentant le chemin relatif vers le
dossier cible
:return: une liste de chemins relatifs avec le chemin folder_path et
ses sous-dossier


7
Cette troisième fonction permet de récupérer une liste contenant le chemin relatif du
dossier passé en paramètre de la fonction et de ses sous-dossiers. Prenons un exemple :
Si la fonction reçoit comme paramètre « ./ », la fonction renverra:
["./", "./dossier1", "./dossier2"]
Si la fonction reçoit comme paramètre « ./dossier1 », la fonction renverra :
[./dossier1]
Par contre, si la fonction reçoit comme paramètre « ./dossier3 » (qui n’existe pas), la
fonction affichera : « Le chemin du dossier n'existe pas. Vous avez essayé d’accéder à :
c:/user/R2D2/projet/dossier3 » (exemple de chemin absolu possible).
def get_folders_and_subfolders(folder_path):
"""
La fonction renvoie une liste de chemins relatifs avec le chemin
folder_path et ses sous-dossiers.
La fonction NE peut PAS lancer d’erreur. Si le chemin n'existe pas, la
fonction affiche "Le chemin n'existe pas" et donne le chemin ABSOLU du
dossier demandé.
S'il y a eu une exception, renvoyez explicitement un "None".
:param folder_path: String représentant le chemin relatif vers le
dossier cible
:return: une liste de chemins relatifs avec le chemin folder_path et
ses sous-dossiers
"""
Cette 4ème fonction permet de charger les logs présents dans un dossier ainsi que ses sous-
dossiers.
def load(path_folder):
"""
La fonction renvoie un tableau de logs à partir des fichiers
dans le dossier (obtenu via le chemin relatif) et les sous-
dossiers de ce dossier.
:param path_folder: String représe

def __init__ (self, text, source)
"""

Constructeur de la classe Log
:param text: String - Contenu de la ligne de log
:parem source: String - chemin vers le fichier qui contenait cette ligne de log"""

def get_program(self):
"""
:return: Le nom du programme contenu dans la ligne de log.
Si la ligne ne contient
pas de nom, "Unknown" sera renvoyé
"""

def __str__ (self)
"""
:return: String - renvoie le contenu du log
"""


def__init__ (self, searched_program, available_programs)
"""
Renvoie une chaîne de caractères représentant l'erreur
exemple:
Impossible de trouver le programme Prog dans la liste :
Programme 1
Programme 2
Programme 3
:return: String
"""


@staticmethod
def sort_by_program(logs):
"""
Renvoie un dictionnaire où chaque clé est un programme et la valeur
associée à la clé est une liste contenant les logs du programme.
:param logs: Une liste de Logs
:return: Un dictionnaire
"""


def __init__(self, logs=None):
"""
:param logs: Une liste de logs (string) - Optionnel
"""

def clear(self):
"""
Remplace le contenu de self.logs par {}
:return: None

def add_logs


def search_logs(self, program_name)

property
def nbr_logs(self):
    """
    Renvoie la totalité des logs stockés dans le log_manager
    :return: Un entier représentant la totalité des logs dans le log_manager"""

def __str__(self):
    """
    Renvoie une représentation en chaîne de caractères du log_manager et le nombre total de logs stockés dans le log_manager
    Exemple:
        Programme1:
            Log1
            Log2
        Programme2:
            Log3
            Log4
            Log5
        TOTAL LOGS: 5
    :return: String
    """

def menu(avaible_choices)
    """
    Affiche un menu et demande à l'utilisateur de taper un nombre correspondant à l'un des des choix.
    La fonctioon repose la question tant que l'utilisateur n'entre pas un nombre parmi les choix possibles.
    :param available_choices: Un dictionnaire où les clés sont des nombres et les valeurs sont du texte.
    :return: Renvoie un entier correspond au choix de l'utilisateur
    """

def main
    """
    Fonction principale du programme qui permet d'afficher le menu avec les différents choix possibles ainsi que la gestion de ses choix.
    :return: None
    """
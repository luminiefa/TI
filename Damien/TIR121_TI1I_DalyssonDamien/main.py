"""projet progra """

def lines_from_file(path):
    """ Pre : path (str) est le chemin menant au fichier à lire
                (à partir du dossier courant)
    Post : Retourne une liste où chaque élément est une ligne du fichier.
            En cas d'erreur, retourne une liste vide
    """
    try :
        with open(path) as file:
            log = file.readlines()
            return log
    except Exception as exception :
        print(exception)
        return []


def get_host(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le hostname
    """
    list_line = line.split(" ")

    host = list_line[3]
    return host


def get_complete_date(line) :
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne la date et l’heure sous forme de chaine de caractère
sans changer le format.
    """
    list_line = line.split(" ")
    date_heure  = list_line[0:3]
    return date_heure[0] + " " + date_heure[1] + " " + date_heure[2]


def get_message(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le message de la lignetest
           !!! le message peut être composé de sous messages (séparés pas d’autres « : »),
               dans ce cas, il faut tout
"""
    message = line.split(':', 3)

    return message [-1]


def get_program(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le nom du programme
"""
    list_line = line.split(" ")

    program_process = list_line[4]
    program_process_list = program_process.split('[')
    program = program_process_list[0]
    program = program.split(':')[0]


    return program

def get_process_id(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le numéro du processus. Si aucun id n’est disponible
(dans le cas d’un kernel par exemple), -1 est retourné.
    """

    list_line = line.split(" ")
    program_process = list_line[4]
    if '[' in program_process :
        program_process_list = program_process.split("[")
        process_id_crochet = program_process_list[1]
        process_id_crochet_list = process_id_crochet.split("]")
        process_id = process_id_crochet_list[0]
        return int(process_id)
    else :
        return -1
# partie 2
def logs_by_day(logs, day):
    """ Pre :
        - logs est une liste où chaque élément est une ligne de log bien formée
        - day (str) est une date au format « Moi JJ »
       Post :
        - retourne une liste de logs qui concernent uniquement le jour
    correspondant à day.
    """
    # pour chaque log dans la liste de logs = FOR
    # récup la date du log  # si la date correspond : = If
    # j'ajoute le log à logs_to_keep = logs_to_keep.append(X)   le happend va servir a ajouter un élément dans une liste


def formated_date(date):
    """
    Pre : date (str) est la date au format "Mois JJ HH:MM:SS" où :
                - Mois : est les 3 première lettres du mois en anglais
                    commencant par une majuscule)
                - JJ : est le numéro du jour (sur 2 chiffres)
                - HH : est l'heure (sur 2 chiffres)
                - MM : sont les minutes (sur 2 chiffres)
                - SS : sont les secondes (sur 2 chiffres)
    Post : Retourne la date sous le format "XX:JJ HH:MM:SS"
                où XX est le nombre du mois (sur 2 chiffres)
"""

def logs_between(logs, date_min="00:00 00:00:00", date_max="99:99 00:00:00"):
   """ Pre :
        - logs est une liste où chaque élément est une ligne de log bien formée
        - date_min et _max sont des str représentant une date (et heure) au
format "XX:JJ HH:MM:SS". Par défaut, ils ont de valeurs absurdes permettant de
prendre tout.
       - date_min est plus petit que date_max
       Post :
        - retourne une liste de logs qui concernent des dates entre date_min et
date_max (inclus).

"""
#partie 3 
def logs_with_tag(logs, tag="error"):
    """ Pre :
       - logs est une liste où chaque élément est une ligne de log bien formée
       - tag est une chaine de caractères à trouver dans le message.
            Par défaut : "error"
    Post :
       - retourne une liste de logs qui concernent uniquement des logs
             contenant le tag (minuscule ou majuscule) dans le message
"""

def logs_from_program(logs, program):
    """ Pre :
       - logs est une liste où chaque élément est une ligne de log bien formée
       - program (str) est le programme à trouver
    Post :
       - retourne une liste de logs qui concernent uniquement les programmes 
correspondant à "program"
"""
def list_process_for_program(logs, program):
    """ Pre :
       - logs est une liste où chaque élément est une ligne de log bien formée
       - program (str) est le programme à trouver
    Post :
       - retourne une liste des process_id gérés par le programme.
            La liste ne contient aucun doublon.
"""
def suspects(logs, limit):
    """ Pre :
       - logs est une liste où chaque élément est une ligne de log bien formée
       - limit est le nombre limite d'erreurs tolérées pour un programme
    Post :
       - retourne une liste des programmes (sans doublons) qui ont généré
       plus que le nombre limite de log signalant des erreurs (error).
"""






if __name__ == "__main__" :
    logs = lines_from_file("log/syslog")

    print(get_host(logs[0]))

    print(get_complete_date(logs[0]))

    print(get_message(logs[0]))

    print(get_program(logs[0]))

    print(get_process_id(logs[0]))

    print((logs_by_day(logs,"Oct 26")))

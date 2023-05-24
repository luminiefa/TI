""" Ce module contien des fonctions par défaut pour lire le contenu d'un fichier log"""


def lines_from_file(path):
    """Pre : path (str) est le chemin menant au fichier à lire
        (à partir du dossier courant)
    Post : Retourne une liste où chaque élément est une ligne du fichier.
    En cas d'erreur, retourne une liste vide"""
    try:
        with open(path) as file:
            log = file.readlines()
            return log
    except Exception as e:
        print(e)
        return []


# Fonction 1 Partie1
def get_host(line):
    """Pre : line est une ligne de log bien formée (str)
    Post : Retourne le hostname"""

    list_line = line.split(' ')
    host = list_line[3]
    return host


# Fonction 2 Partie1
def get_complete_date(line):
    """ Pre : line est une ligne de log bien formée (str)
    Post : Retourne la date et l’heure sous forme de chaine de caractère
    sans changer le format.
    """

    date = ' '.join(line.split(' ')[0:3])
    return date


# Fonction 3 Partie1
def get_message(line):
    """Pre : line est une ligne de log bien formée (str)
    Post : Retourne le message de la ligne
     !!! le message peut être composé de sous messages (séparés pas d’autres « : »),
     dans ce cas, il faut tout
    """

    message = ' '.join(line.split(' ')[5:])
    return message


# Fonction 4 Partie1
def get_program(line):
    """Pre : line est une ligne de log bien formée (str)
       Post : Retourne le nom du programme
    """
    programme = line.split(' ')[4].split(':')[0].split('[')[0]
    return programme


# Fonction 5 Partie1
def get_process_id(line):
    """Pre : line est une ligne de log bien formée (str)
    Post : Retourne le numéro du processus. Si aucun id n’est disponible
    dans le cas d’un kernel par exemple), -1 est retourné.
    """

    if line.split(" ")[4] == "program:":
        return -1
    return int(line.split(" ")[4].split('[')[1].split(']')[0])


# fonction1 partie2
def logs_by_day(logs, day):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - day (str) est une date au format « Moi JJ »
Post :
    - retourne une liste de logs qui concernent uniquement le jour
correspondant à day.
"""
    log_du_jour = []
    for log in logs:
        if day in log:
            log_du_jour.append(log)
    return log_du_jour


# fonction 2 partie 2
def formated_date(date):
    """
    Pre : date (str) est la date au format "Mois JJ HH:MM:SS" où :
    - Mois : est les 3 première lettres du mois en anglais
    (commencant par une majuscule)
    - JJ : est le numéro du jour (sur 2 chiffres)
    - HH : est l'heure (sur 2 chiffres)
    - MM : sont les minutes (sur 2 chiffres)
    - SS : sont les secondes (sur 2 chiffres)
    Post : Retourne la date sous le format "XX:JJ HH:MM:SS"
    où XX est le nombre du mois (sur 2 chiffres)
    """
    mois = ""
    match date.split(" ")[0]:
        case 'Jan':
            mois = "01:"
        case 'Feb':
            mois = "02:"
        case 'Mar':
            mois = "03:"
        case 'Apr':
            mois = "04:"
        case 'May':
            mois = "05:"
        case 'Jun':
            mois = "06:"
        case 'Jul':
            mois = "07:"
        case 'Aug':
            mois = "08:"
        case 'Sep':
            mois = "09:"
        case 'Oct':
            mois = "10:"
        case 'Nov':
            mois = "11:"
        case 'Dec':
            mois = "12:"
    return str(mois) + str(date[4:99])


# fonction 3 partie 2
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
    # "25 octobre 02:34:27" == "01:16 26:31:15"
    # if date_min < date_max
    # ...
    log_between = []
    for log in logs:
        date_du_log = str(formated_date(log).split(" ")[0]) \
                      + " " + str(formated_date(log).split(" ")[1])
        if date_min <= date_du_log <= date_max:
            log_between.append(log)
    return log_between


# fonction 4 partie 2

def logs_with_tag(logs, tag="error"):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - tag est une chaine de caractères à trouver dans le message.
     Par défaut : "error"
    Post :
    - retourne une liste de logs qui concernent uniquement des logs
    contenant le tag (minuscule ou majuscule) dans le message
    """

    log_with_tag = []
    for log in logs:
        if tag.lower() in get_message(
                log).lower():
            log_with_tag.append(log)
    return log_with_tag


def logs_from_program(logs, program):
    """ Pre :
       - logs est une liste où chaque élément est une ligne de log bien formée
       - program (str) est le programme à trouver
    Post :
       - retourne une liste de logs qui concernent uniquement les programmes
correspondant à "program"
"""
    log_from_program = []
    for log in logs:
        if get_program(log) == program:
            log_from_program.append(log)
    return log_from_program


def list_process_for_program(logs, program):
    """ Pre :
        - logs est une liste où chaque élément est une ligne de log bien formée
        - program (str) est le programme à trouver
    Post :
        - retourne une liste des process_id gérés par le programme.
        La liste ne contient aucun doublon.
    """
    proces_id =[]
    for log in logs:
        if get_program(log) == program:
            # récupère le process id et le fou dans un tableau
            pid = get_process_id(log)
            if pid != -1:
                proces_id.append(pid)
    return proces_id
# list_process_for_program

def suspects(logs, limit):
    """ Pre :
       - logs est une liste où chaque élément est une ligne de log bien formée
       - limit est le nombre limite d'erreurs tolérées pour un programme
    Post :
       - retourne une liste des programmes (sans doublons) qui ont généré
            plus que le nombre limite de log signalant des erreurs (error).
"""
    # si programe n'a pas de doublon  plus que le nombre limite alor je l'ajoute a mon tableau
    tableau_programmes_avec_erreurs = []
    logs_seulement_avec_error = logs_with_tag(logs, "error") + logs_with_tag(logs, "errors")
    logs_seulement_avec_erreur = logs_with_tag(logs, "erreur") + logs_with_tag(logs, "erreurs")
    logs_e = logs_seulement_avec_error + logs_seulement_avec_erreur
    tableau_avec_trop_d_erreurs = []

    for logAvecErreur in logs_e:  # On bouclera sur 97 lignes au lieu de 7200
        tableau_programmes_avec_erreurs.append(get_program(logAvecErreur))

    for progError in tableau_programmes_avec_erreurs:
        if tableau_programmes_avec_erreurs.count(progError) > limit and progError not in tableau_avec_trop_d_erreurs:
            tableau_avec_trop_d_erreurs.append(progError)
    return tableau_avec_trop_d_erreurs

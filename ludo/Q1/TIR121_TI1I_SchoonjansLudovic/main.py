
"""Accueil les fonctions"""
def lines_from_file(path):
    #test modif
    """ Pre : path (str) est le chemin menant au fichier à lire
    (à partir du dossier courant)
    Post : Retourne une liste où chaque élément est une ligne du fichier.
    En cas d'erreur, retourne une liste vide
    """
    try :
        with open(path) as file:
            log = file.readlines()
            return log
    except Exception as erreur :
        print(erreur)
        return None

def get_host(line):
    """ Pre : line est une ligne de log bien formée (str)
    Post : Retourne le hostname
    """
    # Séparer la chaîne selon des espaces
    # Récupèrer la 4ème valeur de la liste
    host = line.split()[3]
    return host

def get_complete_date(line):
    """ Pre : line est une ligne de log bien formée (str)
    Post : Retourne la date et l’heure sous forme de chaine de caractère
    sans changer le format.
    """
    split = line.split()
    # On récupère le mois (1er élém), le jour (2ème élém) et l'heure (3ème élém) et on les concatène
    chaine_caractere = split[0] + " " + split[1] + " " + split[2]
    return chaine_caractere

def get_message(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le message de la ligne
        !!! le message peut être composé de sous messages (séparés pas d’autres « : »),
        dans ce cas, il faut tout
    """
    # On récupère une liste de sous-messages
    list_line = line.split(":")
    # On join les sous-messages après le 3eme élément de la liste
    message = list_line[3:]
    message = ":".join(message)
    return message


def get_program(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le nom du programme
    """
    # On crée une liste de chaque champ de la ligne de log
    list_line = line.split(" ")
    # Extrait le nom du programme à partir du champ
    program = list_line[4].split("[")
    program = program[0].split(":")
    # Retourne le nom du programme
    return program[0]


def get_process_id(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le numéro du processus. Si aucun id n’est disponible
        (dans le cas d’un kernel par exemple), -1 est retourné.
    """
    # On vérifie d'abord que la liste renvoyée par le split
    # contient bien plus de 4 elements.
    list_line = line.split(" ")
    if len(list_line) <= 4:
        return -1
    # On récupère ensuite l'element à la position 4 de la liste
    # et on le split
    process_id = list_line[4].split("[")
    # puis on verifie que le split a crée plus d'un element
    if len(process_id) <= 1:
        return -1
    # On récupère ensuite le premier élement du split
    # et on le strip
    process_id = process_id[1].strip("]:")
    # Puis on verifie que cet element est issu d'un number
    if not process_id.isdigit():
        return -1
    # Sinon on retourne l'id
    return int(process_id)

def logs_by_day(logs, day):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - day (str) est une date au format « Moi JJ »
    Post :
    - retourne une liste de logs qui concernent uniquement le jour
    correspondant à day.
    """
    # Initialiser une liste qui contiendra les logs de la journée donnée
    logs_day = []
    # Parcourir la liste des logs
    for line in logs:
        # Obtenir la date d'une ligne séparée en 3 parts (mois, jour et année)
        split = line.split()
        date = split[0] + " " + split[1]
        # Si la date dans la ligne correspond à celle fournie par l'utilisateur
        if date == day :
            # Ajouter la ligne aux logs de la journée
            logs_day.append(line)
    # Retourner la liste des logs de la journée donnée
    return logs_day


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
    # Découpage de la chaîne de caractères en différents éléments
    split = date.split()
    # Récupération du mois
    mois = split[0]
    # Initialisation de la variable qui contiendra le numero du mois
    numero_mois = ""
    # Affectation du numéro du mois en fonction du mois fourni
    if mois == "Jan":
        numero_mois = "01"
    elif mois == "Feb":
        numero_mois = "02"
    elif mois == "Mar":
        numero_mois = "03"
    elif mois == "Apr":
        numero_mois = "04"
    elif mois == "May":
        numero_mois = "05"
    elif mois == "Jun":
        numero_mois = "06"
    elif mois == "Jul":
        numero_mois = "07"
    elif mois == "Aug":
        numero_mois = "08"
    elif mois == "Sep":
        numero_mois = "09"
    elif mois == "Oct":
        numero_mois = "10"
    elif mois == "Nov":
        numero_mois = "11"
    elif mois == "Dec":
        numero_mois = "12"
    # Retourne le numéro du mois, le jour et l'heure
    return numero_mois + ":" + split[1] + " " + split[2]

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
    # Initialise une liste qui retiendra les logs comprise entre date_min et date_max
    all_logs_between = []
    # alloue chaque élément de la liste logs à la variable 'line'
    for line in logs:
        # obtenir la date formatée pour la ligne de log
        date = formated_date(get_complete_date(line))
        # vérifier si cette date est comprise entre la date_min et la date_max
        # sinon, continuer à la prochaine ligne
        if date_min <= date <= date_max:
            all_logs_between.append(line)

    # Retourne la liste des logs comprise entre la date_min et date_max
    return all_logs_between

def logs_with_tag(logs, tag="error"):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - tag est une chaine de caractères à trouver dans le message.
    Par défaut : "error"
    Post :
    - retourne une liste de logs qui concernent uniquement des logs
    contenant le tag (minuscule ou majuscule) dans le message
    """
    list_log = []
    tag = tag.lower()
    # Itération sur les logs passés en paramètres
    for log in logs:
        # Récupération de la partie du log après la date exprimée sur 4 caractère
        contents = log.split()
        contents = contents[4:]
        contents = str(contents)
        # Vérification si le tag est contenu dans le message du log et s'il est conforme à la casse
        if tag in contents.lower():
            list_log.append(log)
    return list_log


def logs_from_program(logs, program):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - program (str) est le programme à trouver
    Post :
    - retourne une liste de logs qui concernent uniquement les programmes
    correspondant à "program"
    """
    # initialisation des variables
    programmes = []
    # compteur pour relire chaque element du tableau
    compteur = 0
    # Tant que le compteur est plus petit que la taille du tableau de logs
    while compteur <= len(logs) -1:
        # On récupère le nom du programme
        reponse_programme = get_program(logs[compteur])
        # Si le nom du programme correspond à celui recherché
        if reponse_programme == program:
            # On ajoute la ligne de log au tableau
            programmes.append(logs[compteur])
        # incrémenter le compteur
        compteur += 1
    # retourner le tableau
    return programmes


def list_process_for_program(logs, program):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - program (str) est le programme à trouver
    Post :
    - retourne une liste des process_id gérés par le programme.
    La liste ne contient aucun doublon.
    """
    # on commence par créer une liste vide pour y stocker les process
    list_log = []
    # On parcourt tous les éléments de la liste des logs
    for log in logs:
        # On découpe en morceaux la ligne courante qui correspond aux informations sur un processus
        log_program = log.split()
        # On regarde si le nom du programme correspond à celui que nous recherchons
        log_program = log_program[4].split("[")
        if log_program[0] == program:
            # Si c'est le cas on découpe la partie du processus en morceaux
            list_line = log.split()
            list_line = list_line[4].split("[")
            # On récupère le process id et on le converti en entier
            list_line = int(list_line[1].strip("]:"))
            # On ajoute le process à la liste
            list_log.append(list_line)
    # Une fois qu'on a parcouru la liste des logs et recupéré les bon processus on retourne la liste
    return list_log

def suspects(logs, limit):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - limit est le nombre limite d'erreurs tolérées pour un programme
    Post :
    - retourne une liste des programmes (sans doublons) qui ont généré
    plus que le nombre limite de log signalant des erreurs (error).
    """
    # liste stockant les programmes et leur nombre d'erreurs
    errors = []
    # on filtre le log pour ne garder que ceux avec le tag "error"
    filtered_logs = logs_with_tag(logs)
    # pour chaque log contenant un tag error
    for log in filtered_logs:
        # on récupère le progamme ayant créé le log
        program = get_program(log)
        # On cherche si le programme se trouve déjà dans la liste
        found = False
        for item in errors:
            if program == item[0]:
                # Si le prog se trouve déjà dans la liste, on incrémente sa valeur du nombre de logs
                item[1] += 1
                found = True
        # Sinon on ajoute le programme dans la liste avec sa première erreur
        if not found:
            errors.append([program, 1])
    # enfin on retourne la liste des programmes dont le nombre d'erreurs dépasse le limit
    return [program for program, count in errors if count > limit]

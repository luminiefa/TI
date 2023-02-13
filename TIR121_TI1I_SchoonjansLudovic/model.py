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
    except Exception as e :
        print(e)
        return 

def get_host(line):
    """ Pre : line est une ligne de log bien formée (str)
    Post : Retourne le hostname
    """
    host = line.split()[3]
    return host

def get_complete_date(line):
    """ Pre : line est une ligne de log bien formée (str)
    Post : Retourne la date et l’heure sous forme de chaine de caractère
    sans changer le format.
    """
    split = line.split()
    chaineCaract = split[0] + " " + split[1] + " " + split[2]
    return chaineCaract

def get_message(line):
    """ Pre : line est une ligne de log bien formée (str)
    Post : Retourne le message de la ligne
    """
    split = line.split(': ', 2)
    message = split[-1].strip()
    return message


def get_program(line):
    """ Pre : line est une ligne de log bien formée (str)
    Post : Retourne le nom du programme
    """
    split = line.split()
    for i in range(len(split)):
        if "[" in split[i]:
            program = split[i]
            return program.split("[")[0]
    return split[4]


def get_process_id(line):
    """ Pre : line est une ligne de log bien formée (str)
    Post : Retourne le numéro du processus. Si aucun id n’est disponible
    (dans le cas d’un kernel par exemple), -1 est retourné.
    """
    split = line.split()
    program = split[4]
    if '[' in program:
        process_id = program.split('[')[1].split(']')[0]
        return process_id
    else:
        return -1




def logs_by_day(logs, day):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - day (str) est une date au format « Moi JJ »
    Post :
    - retourne une liste de logs qui concernent uniquement le jour
    correspondant à day.
    """
    logs_day = []
    for line in logs:
        split = line.split()
        date = split[0] + " " + split[1]
        if date == day :
            logs_day.append(line)
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
    split = date.split()
    Mois = split[0]

    numero_mois = ""

    if Mois == "Jan":
        numero_mois = "01"
    elif Mois == "Feb":
        numero_mois = "02"
    elif Mois == "Mar":
        numero_mois = "03"
    elif Mois == "Apr":
        numero_mois = "04"
    elif Mois == "May":
        numero_mois = "05"
    elif Mois == "Jun":
        numero_mois = "06"
    elif Mois == "Jul":
        numero_mois = "07"
    elif Mois == "Aug":
        numero_mois = "08"
    elif Mois == "Sep":
        numero_mois = "09"
    elif Mois == "Oct":
        numero_mois = "10"
    elif Mois == "Nov":
        numero_mois = "11"
    elif Mois == "Dec":
        numero_mois = "12"
    else:
        print("erreur")

    return numero_mois + ":" + split[1] + " " + split[2]

    #return le mois transformé plus le reste
    
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

    logs_between = []
    for line in logs:
        date = formated_date(get_complete_date(line))
        if date >= date_min and date <= date_max:
            logs_between.append(line)
    return logs_between








def logs_with_tag(logs, tag="error"):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - tag est une chaine de caractères à trouver dans le message.
    Par défaut : "error"
    Post :
    - retourne une liste de logs qui concernent uniquement des logs
    contenant le tag (minuscule ou majuscule) dans le message
    """
    tag_lower = tag.lower()
    tag_upper = tag.upper()
    logs_with_tag = []
    for log in logs:
        split = log.split(' ', 5)
        if len(split) < 6:
            continue
        message = split[5]
        if tag_lower in message or tag_upper in message:
            logs_with_tag.append(log)
    return logs_with_tag


def logs_from_program(logs, program):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - program (str) est le programme à trouver
    Post :
    - retourne une liste de logs qui concernent uniquement les programmes
    correspondant à "program"
    """
    programmes = []
    compteur = 0
    while compteur <= len(logs) -1:
        reponse_programme = get_program(logs[compteur])
        print("réponse")
        print(reponse_programme)
        print(program)
        if reponse_programme == program:
            programmes.append(logs[compteur])
        compteur += 1
    return programmes


def list_process_for_program(logs, program):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - program (str) est le programme à trouver
    Post :
    - retourne une liste des process_id gérés par le programme.
    La liste ne contient aucun doublon.
    """
    process_id = []
    compteur = 0
    while compteur <= len(logs) -1:
        reponse_programme = get_program(logs[compteur])
        if reponse_programme == program:
            
            id = get_process_id(logs[compteur])
            print(id)
            process_id.append(id)
            
        compteur += 1
    return process_id
        
def suspects(logs, limit):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - limit est le nombre limite d'erreurs tolérées pour un programme
    Post :
    - retourne une liste des programmes (sans doublons) qui ont généré
    plus que le nombre limite de log signalant des erreurs (error).
    """
    programs = {}
    for log in logs:
        program, level, message = log.split()
        if level == "error":
            if program in programs:
                programs[program] += 1
            else:
                programs[program] = 1
    
    suspects = []
    for program, error_count in programs.items():
        if error_count > limit:
            suspects.append(program)
    
    return suspects
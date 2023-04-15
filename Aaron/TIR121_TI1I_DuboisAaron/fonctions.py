""" Ce module contien des fonctions par défaut pour lire le contenu d'un fichier log"""

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
        return []

def get_host(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le hostname"""
    list_line = line.split(" ")
    host = list_line[3]
    return host

def get_complete_date(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne la date et l’heure sous forme de chaine de caractère
        sans changer le format.
    """
    list_line = line.split(" ")
    complete_date = list_line[0] + " " + list_line[1] + " " + list_line[2]
    return complete_date

def get_message(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le message de la ligne
        !!! le message peut être composé de sous messages (séparés pas d’autres « : »),
        dans ce cas, il faut tout
    """
    list_line = line.split(":")
    message = list_line[3:]
    message = ":".join(message)
    return message

def get_program(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le nom du programme
    """
    list_line = line.split(" ")
    program = list_line[4].split("[")
    program = program[0].split(":")
    return program[0]

def get_process_id(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le numéro du processus. Si aucun id n’est disponible
        (dans le cas d’un kernel par exemple), -1 est retourné.
    """
    list_line = line.split(" ")
    try:
        list_line = list_line[4].split("[")
        list_line = int(list_line[1].strip("]:"))
    except (IndexError, ValueError):
        return -1

    else :
        if list_line != " " :
            return list_line

def logs_by_day(logs, day):
    """ Pre :
     - logs est une liste où chaque élément est une ligne de log bien formée
     - day (str) est une date au format « Moi JJ »
    Post :
    - retourne une liste de logs qui concernent uniquement le jour
    correspondant à day.
    """
    list_log = []
    for log in logs:
        if day in log:
            list_log.append(log)
    return list_log

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
    #récupérer mois, jours et le temps séparément.
    date = date.split()
    mois_recup, jour_recup, temp_recup = date[0], date[1], date[2]
    match mois_recup:
        case "Jan":
            format_mois = "01"
        case "Feb":
            format_mois = "02"
        case "Mar":
            format_mois = "03"
        case "Apr":
            format_mois = "04"
        case "May":
            format_mois = "05"
        case "Jun":
            format_mois = "06"
        case "Jul":
            format_mois = "07"
        case "Aug":
            format_mois = "08"
        case "Sep":
            format_mois = "09"
        case "Oct":
            format_mois = "10"
        case "Nov":
            format_mois = "11"
        case "Dec":
            format_mois = "12"
    format_date = format_mois + ":" + jour_recup + " " + temp_recup
    return format_date

def logs_between(logs_complete, date_min="00:00 00:00:00", date_max="99:99 00:00:00"):
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
    def date_decomposeur(date):
        date = date.split()
        mojo, hemise = date[0], date[1]
        moi , jou = mojo.split(":")
        heure, minute, seconde = hemise.split(":")
        decomp = moi,jou,heure,minute,seconde
        return decomp


    def date_converteur(mois, jours):
        format_mois = ""
        match mois:
            case "01":
                format_mois = "Jan"
            case "02":
                format_mois = "Feb"
            case "03":
                format_mois = "Mar"
            case "04":
                format_mois = "Apr"
            case "05":
                format_mois = "May"
            case "06":
                format_mois = "Jun"
            case "07":
                format_mois = "Jul"
            case "08":
                format_mois = "Aug"
            case "09":
                format_mois = "Sep"
            case "10":
                format_mois = "Oct"
            case "11":
                format_mois = "Nov"
            case "12":
                format_mois = "Dec"
            case _ :
                format_mois = "none"
        date = format_mois, jours
        return date

    date_min_decomp = date_decomposeur(date_min)
    date_max_decomp = date_decomposeur(date_max)
    date_min_convert = date_converteur(date_min_decomp[0],date_min_decomp[1])
    date_max_convert = date_converteur(date_max_decomp[0],date_max_decomp[1])

    complete_date_min = f"{date_min_convert[0]} {date_min_convert[1]}\
    {date_min_decomp[2]}:{date_min_decomp[3]}:{date_min_decomp[4]}"
    complete_date_max = f"{date_max_convert[0]} {date_max_convert[1]}\
    {date_max_decomp[2]}:{date_max_decomp[3]}:{date_max_decomp[4]}"

    def liste_de_date(date):
        date_parts = date.split()
        day_of_month, time = date_parts[1], date_parts[2]
        heu, min, sec = time.split(":")
        return (day_of_month, heu, min, sec)

    min_date = liste_de_date(complete_date_min)
    max_date = liste_de_date(complete_date_max)

    result = []
    for log in logs_complete:
        log_date_tuple = liste_de_date(log)
        if min_date <= log_date_tuple <= max_date:
            result.append(log)

    return result

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
    for log in logs:
        list_line = log
        list_line = list_line.split()
        list_line = list_line[4:]
        list_line = str(list_line)
        if tag in list_line.lower():
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
    list_log = []
    for log in logs:
        log_program = log.split()
        log_program = log_program[4].split("[")
        log_program = log_program[0].split(":")
        if log_program[0] == program:
            list_log.append(log)
    return list_log

def list_process_for_program(logs, program):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - program (str) est le programme à trouver
    Post :
    - retourne une liste des process_id gérés par le programme.
    La liste ne contient aucun doublon.
    """
    list_log = []
    for log in logs:
        log_program = log.split()
        log_program = log_program[4].split("[")
        if log_program[0] == program:
            try:
                list_line = log.split()
                list_line = list_line[4].split("[")
                list_line = int(list_line[1].strip("]:"))
                list_log.append(list_line)
            except:
                list_log.append(log)
    return list_log


def suspects(logs, limit):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - limit est le nombre limite d'erreurs tolérées pour un programme
    Post :
    - retourne une liste des programmes (sans doublons) qui ont généré
    plus que le nombre limite de log signalant des erreurs (error).
    """
    error_count = {}
    list_log = []
    for entry in logs:
        fields = entry.split(' ')
        program = fields[4]
        program = program.split("[")
        program = program[0].split(":")
        program = program[0]
        if 'error' in entry.lower():
            if program in error_count:
                error_count[program] += 1
            else:
                error_count[program] = 1
    for program, count in error_count.items():
        if count > limit:
            list_log.append(program)
    return list_log

if __name__ == "__main__" :
    #logs = lines_from_file("log/syslog.txt")
    #print(logs[0])
    #print(get_host(logs[0]))

    #logs = lines_from_file("log/syslog.txt")
    #print(logs[0])
    #print(get_complete_date(logs[0]))

    #logs = lines_from_file("log/syslog.txt")
    #print(logs[0])
    #print(get_message(logs[0]))

    #logs = lines_from_file("log/syslog.txt")
    #print(logs[0])
    #print(get_program(logs[0]))

    #logs = lines_from_file("log/syslog.txt")
    #print(logs[0])
    #print(get_process_id(logs[0]))

    logs = lines_from_file("log/syslog.txt")
    print(suspects(logs,15))
    #print(formated_date("Jan 18 22:30:15"))

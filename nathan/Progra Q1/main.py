def lines_frome_file(path):
    """ Pre : path (str) est le chemin menant au fichier à lire
(à partir du dossier courant)
Post : Retourne une liste où chaque élément est une ligne du fichier.
 En cas d'erreur, retourne une liste vide
    """
    try :
        with open(path) as file :
            log = file.readlines()
            return log
    except Exception as e :
        print(e)
        return []

path = "./log/syslog.txt"
logs = lines_frome_file(path)
#print (log[0]) permet de print la premier ligne du fichier
# splitage des donnees en date heure ,...

def get_message(line):
    message_in_line = line.split(':', 3)[-1]
    return message_in_line

#La fonction .split permet de séparer une chaine de caractères en plusieurs
#éléments distincts. Ex: x =txt.split("#", 1). Le # est l'élément sur lequel
#Le split va couper donc A#B = ['A', 'B']. Le 1 est le nombre de split total (donc 2 éléments).
#Le [-1] veut dire qu'il prend le dernier élément séparé par le split.

def get_complete_date(line):
    date_in_log = line.split(maxsplit=4)
    date = date_in_log[:3]
    return date[0]+" "+date[1]+" "+date[2]

#Le .split(maxsplit=4) veut dire que la ligne est divisée en mots avec les espaces
#Comme séparateur ET qu'elle s'arrête après avoir effectué au plus 4 divisions.
#Le [:3] = Les 3 premiers éléments sont assignés à la variable date.
#Le return date[0]+" "+date[1]+" "+date[2] concatène les éléments de date avec un espace entre chaque.


def get_host(line):
    host_in_log = line.split(maxsplit=4)
    host = host_in_log [3]
    return host

# host = host_in_log [3] assigne le 4e élément de host_in_log à Host

def get_program(line):

    program_in_log = line.split()
    program1 = program_in_log[4]
    program2 = program1.split("[")
    program3 = program2[0]
    program4 = program3.split(":")
    program5 = program4[0]
    return program5

# program_in_log = line.split() :  La ligne est divisée en mots en utilisant des espaces comme séparateurs.
# program_in_log serait ["Oct", "25", "02:34:30", "kali", "systemd[705]:", "Reached", "target", "Sockets."].
# program1 = program_in_log[4] : Prend le 5e élément donc "systemd[705]"
# program2 = program1.split("[") : Divisé en utilisant "[" comme séparateur donc : ["systemd", "705]"].
# program3 = program2[0] : Prend le 1er élément donc "systemd".
# program4 = program3.split(":") : Divisé en utilisant ":" comme séparateur (pour kernel: => ["kernel"])


def get_process_id(line):
    process_id_in_liste = line.split()
    process_id_in_line = process_id_in_liste[4]
    process_id_in_split_1 = process_id_in_line.split("[")
    if len(process_id_in_split_1)== 2:
        process_id_in_split_2 = process_id_in_split_1 [1]
        id0 = process_id_in_split_2.split("]")
        id1 = int(id0[0])
        return id1
    else :
        return -1
    
# process_id_in_liste = line.split() : Divise avec espace comme séparateur.
# process_id_in_line = process_id_in_liste[4] : Prend le 5e élément donc ["systemd[705]"]
# process_id_in_split_1 = process_id_in_line.split("[") : Divise avec "[" comme séparateur donc ["systemd" , "705]"]
# if len(process_id_in_split_1)== 2: : Si longueur =/ 2 alors else.
#  process_id_in_split_2 = process_id_in_split_1 [1] : Prend le 2e élément donc "705]"
# id0 = process_id_in_split_2.split("]") : Sépare avec "]" Donc ["705"]
# id1 = int(id0[0]) = Prend 1er élément et le converti en entier
# else : return -1 : Renvoie -1 si aucun identifiant n'a été extrait.


def formated_date(date):
    date_format1=date.split()

    match date_format1[0]:
        case "Jan":
            month = "01"
        case "Feb":
            month = "02"
        case "Mar":
            month = "03"
        case "Apr":
            month = "04"
        case "May":
            month = "05"
        case "Jun":
            month = "06"
        case "Jul":
            month = "07"
        case "Aug":
            month = "08"
        case "Sep":
            month = "09"
        case "Oct":
            month = "10"
        case "Nov":
            month = "11"
        case "Dec":
            month = "12"

    date_format2 = month + ":" + date_format1[1] + " " + date_format1[2]

    return date_format2

# date_format1=date.split() : Utilise variable date de la fonction "def get_complete_date(line):"  ["Oct", "25", "02:34:30"]
# match date_format1[0]: Prend le premier mot de la liste (donc le mois), puis assigne chaque mois à un numéro
# date_format2 = month + ":" + date_format1[1] + " " + date_format1[2] : 10:25 02:34:30"
# return date_format2 : Appelle la variable date_format2

def logs_by_day(logs, day):
    """fonction qui permet recuperer dans une liste les logs entre trier par jour"""
    day_list = []
    for line in logs :
        full_date = get_complete_date(line)
        month_day=full_date.split()
        day_split_end = month_day[0] + " " + month_day[1]
        if day_split_end == day:
            day_list.append(line)
    return day_list

# day_list = [] : Créé une liste vide pour stocker les logs correspondant au jour spécifié
# for line in logs : Parcours chaque ligne de log
# full_date = get_complete_date(line) : Permet de prendre date[0]+" "+date[1]+" "+date[2]
# month_day=full_date.split() : date divisé par espace comme séparateur donc ["Oct", "25", "02:34:30"]
# day_split_end = month_day[0] + " " + month_day[1] : Juxtapose les 2e premiers termes avec un espace donc "Oct 25"
# if day_split_end == day : Comparaison entre date formatée et valeur du jour "day"
# day_list.append(line) : Ajout de la ligne de log à liste day_list 

def logs_between(logs, date_min="00:00 00:00:00", date_max="99:99 00:00:00"):
    """fonction qui permet recuperer dans une liste les logs entre 2 date"""
    between_list = []
    for line in logs :
        date_betwen = get_complete_date(line)
        date_betwen2 = formated_date(date_betwen)
        if date_min <= date_betwen2 <= date_max:
            between_list.append(line)
    return between_list

# between_list = [] : Créé une liste vide pour stocker les logs correspondant aux heures spécifiés.
# for line in logs : Parcours chaque ligne de log
# date_betwen = get_complete_date(line) : Permet de prendre date[0]+" "+date[1]+" "+date[2]
# date_betwen2 = formated_date(date_betwen) : Utilise la fonction formated_date pour avoir un format MM:DD HH:MM.
# if date_min <= date_betwen2 <= date_max: : Vérification que date formaté est entre les 2 dates demandées.
# between_list.append(line) : Ajout de la ligne de log à liste between_list 

def logs_with_tag(logs, tag="error"):
    """
    fontion qui permet recuperer dans une liste les ligne concerner par un tag
    qui non introduit sera pas defaut error
    """
    logs_with_tag_list = []
    if tag == "":
        return logs
    for line in logs :
        tag1 = tag.lower()
        logs_with_tag_min = line.lower()
        simpel_split = logs_with_tag_min.split(maxsplit=5)
        finish_split = simpel_split[5]
        if finish_split.count(tag1) >= 1:
            logs_with_tag_list.append(line)
    return logs_with_tag_list

# logs_with_tag_list = [] : Créé une liste vide pour stocker les logs concerner par le tag
# if tag == "": Vérification de la présence d'un tag, sinon return la liste de logs sans filtrage supplémentaire.
# for line in logs : Parcours chaque ligne de log
# tag1 = tag.lower() : tag converti en minuscule pour assurer une correspondance insensible à la casse.
# logs_with_tag_min = line.lower() : ligne de log converti en minuscule.
# simpel_split = logs_with_tag_min.split(maxsplit=5) : Divise avec les espaces comme séparateur la ligne de log en maximum 5 terme
# finish_split = simpel_split[5] : Prend le 6e élément de la liste
# if finish_split.count(tag1) >= 1: Vérification de la présence du tag dans la ligne
#  logs_with_tag_list.append(line) : Ajoute les lignes de log concernées par le tag dans la liste log_with_tag_list

def logs_from_program(logs, program):
    """fonction permet de recuperer les ligne qui possede qui concerne un programme en particulier"""
    logs_from_program_list = []
    for line in logs :
        logs_from_program = get_program(line)
        if logs_from_program == program :
            logs_from_program_list.append(line)
    return logs_from_program_list

# logs_from_program_list = [] : Créé une liste vide pour stocker les ligne avec un programme en particulier
# for line in logs : Parcours chaque ligne de log
# logs_from_program = get_program(line) : Extrait le nom du programme à partir de la fonction get_program. Ex : ["Kernel"]
# if logs_from_program == program : Comparaison du nom du programme extrait avec programme recherché
# logs_from_program_list.append(line) : Ajout des ligne de log si le nom du programme extrait = celui recherché.


def list_process_for_program(logs, program):
    final_list = []
    for line in logs:
        get_program_process = get_program(line)
        if get_program_process == program:
            id = get_process_id(line)
            if id != -1:
                final_list.append(id)
    return final_list

# final_list = [] : Créé une liste vide pour stocker les identifiants de processus associés au programme spécifié.
# for line in logs : Parcours chaque ligne de log
# get_program_process = get_program(line) : Extrait le nom du programme à partir de la fonction get_program. Ex : ["Kernel"]
# if get_program_process == program : Comparaison du nom du programme extrait avec programme recherché
# id = get_process_id(line) : Extrait identifiant du processus associé à partir de la fontion get_process_id. Ex : 705 (car c'est un entier)
# if id != -1: Vérification que programme a bien au minimum un identifiant.
# final_list.append(id) : Ajout des différents identifiants du programme concerné

def suspects(logs, limit):
    """
Pre :
- logs est une liste où chaque élément est une ligne de log bien formée
- limit est le nombre limite d'erreurs tolérées pour un programme
Post :
- retourne une liste des programmes (sans doublons) qui ont généré
plus que le nombre limite de log signalant des erreurs (error).
    """
    list_suspect = []
    error_list = logs_with_tag(logs)
    for line in error_list:
        program = get_program (line)
        if program not in list_suspect:
            logs_program = logs_from_program(error_list,program)
            if len(logs_program) > limit:
                list_suspect.append(program)
    return list_suspect


# list_suspect = [] : Créé une liste vide pour stocker les programmes qui ont généré des erreurs.
# error_list = logs_with_tag(logs) : Extrait les lignes de log qui ont le tag "error"
# for line in error_list :  Parcours chaque ligne de la lite d'erreur
# program = get_program (line) : Extrait le nom du programme à partir de la fonction get_program. Ex : ["Kernel"]
# if program not in list_suspect: Vérification que le programme n'est pas dans la list_suspect
# logs_program = logs_from_program(error_list,program) : Définition d'une variable qui
#   retourne une liste contenant les lignes de log avec erreur d'un programme en particulier.
# if len(logs_program) > limit : Vérification que nombre de lignes de log en erreur est supérieur à la limite.
# list_suspect.append(program) : Si c'est le cas, ajout à la liste des programmes suspects (sans doublons)
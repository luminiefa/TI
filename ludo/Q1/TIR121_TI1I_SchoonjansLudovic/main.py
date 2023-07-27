import model
from model import *
#test

"""
path = "log/logs.txt"

logs = model.lines_from_file(path)
#print(logs)

#test = suspects(logs, 3)
#print(test)

test2 = network_message_times(logs)
print(test2)

"""

logs = [
        "Oct JJ 08:08:08 host sudo: Hello :)",
        "Nov JJ 12:44:55 host sudooo: session opened for user root ",
        "Jan JJ 12:32:44 host sudo: session opened for user root",
        "Feb JJ 12:32:44 host NetworkManager[5]: <warn> : FATAL ERRoR",
        "Mar JJ HH:MM:SS host program: message",
        "Mar JJ HH:MM:SS host program: Demande au canard !?",
        "Mar JJ HH:MM:SS host CRON[1307]: Ca va ? Tu t'en sors ?",
        "Mar JJ HH:MM:SS host CRON[1307]: olala eRRoR",
        "Dec JJ HH:MM:SS host unSuspect[5]: session opened for user root",
        "Jan JJ HH:MM:SS host unSuspect[42]: session opened for user root",
        "Apr JJ HH:MM:SS host unAutreSuspect[18]: session opened for user root...",
        "May JJ 00:00:12 host NetworkManager[42]: <info> : warn : La progra c'est génial ! Youpie !",
        "Jun JJ HH:MM:SS host unSuspect[5]: session closed for user root",
        "Jul JJ 12:34:56 host NetworkManager[7]: <warn> : Saperlipopette",
        "Jul JJ 12:34:56 host NetworkManager[7]: <warn> : didondidonc... ça ne fonctionne pas",
        "Jul JJ 12:34:57 host NetworkManager[7]: <warn> : hum... ennuyeux",
        "Jul JJ 12:34:56 host NetworkManager[1]: <warn> : fICHTRE, encore un... et en plus, j'étais CAPS lock",
        "Jul JJ 12:34:50 host NetworkManager[1]: <info> : c'est bon",
        "Jul JJ 12:34:56 host NetworkManager[1]: <warnnnn> : c'est bon",
        "Sept JJ HH:MM:SS host CRON[1300]: session opened for user root mais lui, il peut !"
    ]

def network_message_times(logs):
    """ Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    Post :
    - retourne une liste des moments (date et heure) sans doublon
    où le programme NetworkManager a émi un "<warn>"
    """
    #Oct 25 09:11:14 kali NetworkManager[425]: <warn>  [1666703474.2982] config: unknown key 'wifi.cloned-mac-address' in section [device-mac-addr-change-wifi] of file '/usr/lib/NetworkManager/conf.d/no-mac-addr-change.conf'

    a = logs_from_program(logs, "NetworkManager")
    b = logs_with_tag(a, "<warn>")
    
    listeDesDates = []
    for dates in b:
        c = get_complete_date(dates)
        listeDesDates.append(c)
    listeDesDates = list(set(listeDesDates))
    return listeDesDates

print(network_message_times(logs))

#a = logs_by_day(logs, "Oct 28")

#b = formated_date("Oct 28 12:40:20")
#print(b)

"""
c = logs_between(logs, "10:28 00:00:00", "10:29 00:00:00")
print(c)
    """
#d = logs_with_tag(logs, "org")
#print(d)

#(good)
"""
for log in logs:
    host = get_host(log)
    print(host)
    """

#(good)
"""
for log in logs:
    complete_date = get_complete_date(log)
    print(complete_date)
    """

#(good)
"""
for log in logs:
    program = get_program(log)
    print(program)
    """
    
#(good)
"""
for log in logs:
    process_id = get_process_id(log)
    print(process_id)
    """

#(good)    
"""
for log in logs:
    message = get_message(log)
    print(message)
    """
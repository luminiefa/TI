import model
from model import *
#test

path = "ludo/TIR121_TI1I_SchoonjansLudovic/log/logs.txt"

logs = model.lines_from_file(path)

print("hello")
test = suspects(logs, 3)
print(test)
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
#try :
#    print("Bonjour")
#
#    num = int(input("Numérateur : "))
#    den = int(input("Dénominateur : "))
#    print(num,"/",den,"=",num/den)
#
#except ValueError as e:
#    print("Problème de valeur")
#    print(e.__dir__())
#    print(e.__str__())
#
#except ZeroDivisionError :
#    print("on ne peut pas diviser par 0 ! ")
#
#finally :
#    print("Merci et à bientôt")

class Mon_exception (Exception):
    def __init__(self, message:str="Message d'erreur") :
        self.message = message

    def __str__(self) :
        return self.message

try:
    n = int(input("Entrez un nombre entre 1 et 10 : "))
    if n>10 or n<1 :
        raise Mon_exception()
    print("ok")

except Mon_exception as e:
    print(e)

labo effet doppler:

script pour la formule v = c * ∆f / (2 * fém) :
fém représente la fréquence du signal émis par l'émetteur utilisé dans la manipulation. Dans le contexte de cette manipulation, fém est donné comme étant égal à 40 kHz, soit une fréquence de 40 000 Hz.

Dans cette fonction, df correspond à la différence de fréquence mesurée à l'oscilloscope en Hertz (Hz),
et f_em correspond à la fréquence du signal émis en Hertz (Hz).
La fonction calcule ensuite la vitesse v du chariot en m/s, en utilisant la formule présentée précédemment.

def calcul_vitesse(df, f_em):
    c = 340 # vitesse du son dans l'air en m/s
    v = c * df / (2 * f_em)
    return v

df = 1000 # différence de fréquence mesurée à l'oscilloscope en Hz
f_em = 40000 # fréquence du signal émis en Hz

vitesse = calcul_vitesse(df, f_em)

print("La vitesse du chariot est de", vitesse, "m/s")
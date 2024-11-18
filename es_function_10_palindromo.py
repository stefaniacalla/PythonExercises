#Scrivere una funzione che stabilisce se una parola (o una frase) è
#palindroma (es. radar, i topi non avevano nipoti)


def inversa (s):
    s = s.replace(' ', '')    #si eliminano gli spazi della parola in input
    res = ''
    for i in s:
        res = i + res         #la parola invertita è senza spazi
    return res



def main ():
    print ("Digitare una parola")
    s = input ()
    rev = inversa (s)
    s_trim = s.replace(' ', '')    #si eliminano gli spazi della parola in input
    if (s_trim == rev):            #se la parola trimmata è uguale al risultato della funzione inversa che è trimmato
        print (f"La parola '{s}' è palindroma")
    else:
        print (f"La parola '{s}' NON è palindroma")


main ()
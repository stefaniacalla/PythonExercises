#Gioco dell'impiccato. Scegli una parola e l'utente 
#dovrà indovinarla in max n tentativi (solo un carattere per tentativo)


'''
def tentativi ( parola):
    FORMAT = (
    """  
     ___
    |   {}
    |   {}
    |  {}{}{}
    |__{} {}
    """)
    n_tent = len (parola)
    l =[]
    i = 0
    err = 0
    print (f"Hai {n_tent} per provare a indovinare la parola segreta")
    while (i< n_tent) or (err <7):
        print ("Scegli una lettera per indovinare la parola")
        lett = input ()
        l.append (lett)
        if (lett in parola):
            print ("La lettera è presente nella parola")
        else:
            print ("Mi dispiace. La lettera non è presente nella parola")
            err +=1
            print(FORMAT.format(("|" if err == 1 else ""),
            ("O" if err > 1 else ""),
            ("/" if err > 2 else ""),("|" if err > 3 else ""),
            ("\\" if err > 4 else ""),
            ("/" if err > 5 else ""),
              ,("\\"if err > 6 else "")))
        i+=1
    return l
'''


def check_fine ():
    nl = "\n"
    imp1 = print (f" ___{nl}"
                 f"|   |{nl}"
                 f"|{nl}"
                 f"|{nl}"
                 f"|__")
    

    imp2 = print (f" ___{nl}"
                 f"|   |{nl}"
                 f"|   O{nl}"
                 f"|{nl}"
                 f"|__")




""" print(f" ___{nl}"
      f"|   |{nl}"
      f"|   O{nl}"
      f"|   |{nl}"
      f"|__")


print(f" ___{nl}"
      f"|   |{nl}"
      f"|   O{nl}"
      f"|   |\{nl}"
      f"|__")

print(f" ___"
      f"|   |{n1}"
      f"|   O{nl}"
      f"|   |\{nl}"
      f"|__")


print(f" ___{nl}"
      f"|   |{nl}"
      f"|   O{nl}"
      f"|  /|\{nl}"
      f"|__   ")


print(f" ___{nl}"
      f"|   |{nl}"
      f"|   O{nl}"
      f"|  /|\{nl}"
      f"|__  \ ") """





print(FORMAT.format(("|" if error > 0 else ""),("O" if error > 1 else ""),"/","|","\\","/","\\"))




'''

def tentativi ( parola):
    n_tent = len (parola)   #il num tentativi è uguale alla lunghezza della parola
    l =[]                   #l è la lista che contiene le lettere scelte dall'utente
    i = 0
    print (f"Hai {n_tent} tentativi per provare a indovinare la parola segreta")
    while (i< n_tent):
        print ("Scegli una lettera per indovinare la parola")
        lett = input ()
        l.append (lett)
        if (lett in parola):
            print (f"La lettera è presente nella parola. Le lettere scelte finora sono: {l}")
        else:
            print (f"Mi dispiace. La lettera non è presente nella parola. Le lettere scelte finora sono: {l}")
        i+=1
    #print ("Ora prova ad indovinare la parola")
    return l
'''
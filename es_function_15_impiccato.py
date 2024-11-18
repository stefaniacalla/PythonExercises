#Gioco dell'impiccato. Scegli una parola e l'utente 
#dovrà indovinarla in max n tentativi (solo un carattere per tentativo)


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
    #print (f"Hai {n_tent} per provare a indovinare la parola segreta")
    while (i< n_tent) or (err <7):
        print ("Scegli una lettera per indovinare la parola")
        lett = input ()
        l.append (lett)
        if (lett in parola):
            print ("La lettera è presente nella parola")
        else:
            print ("Mi dispiace. La lettera non è presente nella parola")
            err +=1
            print (FORMAT.format(("|" if err > 0 else ""),
            ("O" if err > 1 else ""),
            ("/" if err > 2 else ""),("|" if err > 3 else ""),
            ("\\" if err > 4 else ""),
            ("/" if err > 5 else ""),
            ("\\"if err > 6 else "")))
        i+=1
    return l


def check_ok (parola):
    #l = ['c', 'f', 'a']
    l = tentativi (parola)                      #l è la lista che contiene le lettere scelte dall'utente
    ind_parola = [i for i,v in enumerate (parola)] #sono gli indici della stringa parola
    l_diz = {}
    for j in l:
        for i, v in enumerate (parola):
            if (j == parola[i]):
                l_diz[i]=v
    return l_diz, ind_parola

def final (parola):
    ld, l2 = check_ok (parola)
    s = []
    s = [ld[i] if i in ld else '_' for i in l2 ]
    cnt = 0
    for l in s:
        if (l == '_'):
            cnt +=1
    if (cnt == 0):
        print ("Complimenti! Hai indovinato la parola!")
    else:
        print ("Ora prova ad indovinare la parola")
    return s



'''
def final (l1 = {0: 'c', 1: 'a', 3: 'a'}, l2=[0,1,2,3]):
    s = []
    s = [l1[i] if i in l1 else '_' for i in l2 ]
    return s
'''

        
        

#print (gioco ("helloworld"))


print (final ("helloworld"))

'''Scrivi una semplice funzione rimario, a cui viene passato un elenco di 
parole come parametro e che riceva una parola inserita dall'utente tramite 
la funzione input.
La funzione rimario dovrà confrontare la parola inserita dall'utente con quelle 
presenti nell'elenco passato, alla ricerca di rime, intese come parole le cui 
ultime 3 lettere siano uguali alla parola inserita dall'utente.'''

def rimario (parola, l_par):
    rima = parola [-3:]
    l_out = []
    for l in l_par:
        if (l [-3:]==rima):
            l_out.append(l)
    return l_out


#print (rimario ("sera", ["pera", "carota", "canottiera"]))


lis = []
print ("Digita una parola")
parola = input ()
lis = rimario ("sera", ["pera", "carota", "canottiera"])
print (f"La parola {parola} fa rima con: {lis}")


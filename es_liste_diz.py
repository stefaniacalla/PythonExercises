'''Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola. 
Ogni dizionario rappresenta uno studente e contiene nome, cognome, classe e voti.
 La funzione deve stampare 
un elenco di tutti gli studenti e calcolare la media dei voti di ciascuno.'''

def diz (ld = [{}]):
    avg_voti = 0
    sum_voti = 0
    n_stud = len (ld)
    for i in ld:
        sum_voti += i["voto"]
        print (i["nome"] + " " + i["cognome"])
    avg_voti = sum_voti / n_stud
    print (f"La media dei voti è {avg_voti}")


diz ([{"nome": "Mario", "cognome": "Rossi", "voto": 9}, {"nome": "Luigi", "cognome": "Bianchi", "voto": 7},
      {"nome": "Luca", "cognome": "Verdi", "voto": 9}])





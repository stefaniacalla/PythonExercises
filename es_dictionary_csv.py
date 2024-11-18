'''Scrivi un programma che crei un file CSV per memorizzare in un dizionario i dati
 degli utenti registrati su un sito web. I dati richiesti per ogni utente sono: 
 username, password, email e data di registrazione. Il programma deve permettere
 di salvare le informazioni nel file, leggere i dati e stamparli a schermo.'''

import csv

def diz (dict={}):
    with open ("user_web.csv", "w", newline="") as file:
        w = csv.writer(file)
        w.writerow(dict.keys())
        w.writerow(dict.values())

diz ({"username": "stefc", "password": "xhjb", "email": "stef.c@gm.it", "dt_reg": "10/10/2023 00:00:00"})
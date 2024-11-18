'''Scrivi una funzione vendi_libri(), che aiuti nella gestione della vendita di libri 
in una libreria:
Controlla se il libro richiesto è presente sugli scaffali della libreria
Qualora il libro sia presente, ne decrementa il numero di copie 
(eventualmente rimuovendo il titolo) e ci segnala che la vendita ha avuto successo
Se il libro non è disponibile, viene messo in un elenco di libri da ordinare e ci 
viene comunicato che la vendita non ha avuto successo
La funzione deve restituire valore booleanoTrue o False in base all'esito della 
vendita.'''


def vendi_libri ():
    scaffale = {"Cime tempestose": 5, "Jane Eyre":2, "Orgoglio e Pregiudizio":1, "Persuasione":12}
    libro_req = input ("Quale libro desidera acquistare?")
    vendita_ok = False
    book_to_ord = []
    if libro_req in scaffale:
        print ("il libro c'è")
        scaffale [libro_req] -=1
        if (scaffale [libro_req]==0):
            del(scaffale [libro_req])
        vendita_ok = True
        print (f"La vendita è andata a  buon fine. I libri ancora disponibili sono i seguneti {scaffale}")
        print (vendita_ok)
    else:
        book_to_ord.append (libro_req)
        vendita_ok = False
        print (f"La vendita non ha avuto successo.")
        print (vendita_ok)

vendi_libri()
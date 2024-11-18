'''Scrivi un programma per gestire una libreria. La libreria dovrà gestire due 
entità principali: i libri e i clienti.

I libri sono una classe che hanno come proprietà le informazioni del libro stesso 
(id, titolo, autore, …). Inoltre all’interno del libro è necessario avere 
proprietà per capire se il libro è in questo momento preso in prestito
e avrà una funzione che permetterà di recuperare lo storico dei prestiti.

I clienti allo stesso modo avranno le informazioni del cliente 
(id, nome, cognome, età, …) e servirà delle funzione per recuperare 
i libri attualmente presi in prestito e lo storico dei libri presi.

La classe libreria gestirà queste due classi gestendo creazione, movimentazione e dati delle due classi. Funzioni pricipali:
•	Registra libro
•	Registra cliente
•	Presta libro i a cliente j
•	Ritorna libro i da cliente j
•	Recupero lista libri prestati
•	Recupera lista libri disponibili'''


from typing import Any, Dict, List
import datetime


class Cliente:  
    def __init__(self, id, nome, cognome):
        self.nome: str = nome
        self.cognome: str = cognome
        self.id: str = id

class Libro:
    def __init__(self, id, titolo, autore):
        self.titolo: str = titolo
        self.autore: str = autore
        self.id: str = id
        self.registro: List[Dict[str, Any]] = [] # [{"cliente", "start", "end"}]
        

    @property
    def disponibile(self) -> bool: #proprietà che dipende da un'altra (una sola) variabile interna alla classe
        stato = True
        for prestito in self.registro:
            if (prestito["end"]>= datetime.datetime.now()):
                stato = False
        return stato
    
    def presta(self, cliente: Cliente):
        if not self.disponibile:
            print("Non disponibile")
            return
        registro_temp = {}
        registro_temp["cliente"]= cliente 
        registro_temp["start"]= datetime.datetime.now()
        registro_temp["end"]= datetime.datetime(2099,12,31)
        self.registro.append(registro_temp)

    def ritorna(self):
        for registro in self.registro:
            if(registro["end"]==datetime.datetime(2099,12,31)):
                registro["end"]=datetime.datetime.now()


class Libreria:  
    def __init__(self, clienti: List[Cliente], libri: List [Libro]):
        self.clienti: List[Cliente] = clienti
        self.libri: List[Libro] = libri
        #self.registro: List[Dict[str, Any]] = [] # [{"start", "end"}]
        #self.registro = []

    def cerca_libro(self, libro_titolo: str) -> Libro:
        libri = [item for item in self.libri if item.titolo == libro_titolo]
        if len(libri) == 1:
            return libri[0]
        print("Non abbiamo questo libro")
        return None
    
    def cerca_cliente(self, cliente_id: str) -> Cliente:
        clienti = [item for item in self.clienti if item.id == cliente_id]
        if len(clienti) == 1:
            return clienti[0]
        print("Il cliente non è registrato")
        return None

    def presta_libro(self, cliente_id: Cliente, libro_titolo: str):
        libro = self.cerca_libro(libro_titolo)
        cliente = self.cerca_cliente(cliente_id)
        libro.presta(cliente)

    def ritorna_libro(self, cliente_id: Cliente, libro_titolo: str):
        libro = self.cerca_libro(libro_titolo)
        cliente = self.cerca_cliente(cliente_id)
        if libro.disponibile:
            print("Il libro non è stato prestato")
            return
        libro.ritorna()


libri = [
    Libro(1, "Ciccio", "Cocco"),
    Libro(2, "Ciccio 2", "Cocco"),
    Libro(3, "Panza", "Carino")
]

clienti = [
    Cliente(1, "Andrea", "Carino"),
    Cliente(2, "La", "Steffi"),
    Cliente(3, "Teodoro", "Riboldi")
]

libreria = Libreria(clienti, libri)
print(libreria.clienti[0].nome)
print(libreria.libri[0].titolo)

libreria.presta_libro(1, "Panza")
print(libreria.libri[2].titolo)
print(libreria.libri[2].registro)
print(libreria.libri[2].disponibile)

libreria.ritorna_libro(1, "Ciccio")
print(libreria.libri[0].titolo)
print(libreria.libri[0].registro)
print(libreria.libri[0].disponibile)

libreria.ritorna_libro(1, "Panza")
print(libreria.libri[2].titolo)
print(libreria.libri[2].registro)
print(libreria.libri[2].disponibile)


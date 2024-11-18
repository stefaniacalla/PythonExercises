#Progettiamo una classe conto corrente bancario
#1) Definisci una classe ContoCorrente
#2) All’interno della classe definisci un inizializzatore per la classe
#conto corrente, con tre parametri(nome, conto e importo)
#3) La classe deve avere tre attributi di istanza(nome, conto e
#importo)
#4) Definisci un metodo «preleva» con parametro «importo»
#5) Definisci un metodo di istanza «deposita» con parametro
#«importo»
#6) Definisci un metodo «descrizione», che non ha parametri ma
#che deve visualizzare in una sequenza il nome, il conto e il saldo

from typing import Any, Dict, List
import os
import re

class ContoCorrente:
    def __init__(self, nome, conto, importo):
        self.nome: str = nome
        self.conto: str = conto
        self.importo: float = importo
        self.ultimo_saldo: float = 0
        self.movimenti: List[str] = []
        self.txs_saldo: List[Dict[str, Any]] = []

    def preleva(self, importo):
        if (importo<= self.ultimo_saldo):
            self.ultimo_saldo = self.ultimo_saldo - importo
            print (f"Puoi prelevare l'importo di {importo} euro desiderato. Il nuovo saldo disponibile è {self.ultimo_saldo}.")
            movimento = f"Hai prelevato {importo} euro."
            self.movimenti.append (movimento)
            self.txs_saldo.append({"movimento": movimento, "saldo": self.ultimo_saldo})
        else:
            print ("Non è possibile prelevare l'importo desiderato poichè è superiore al saldo disponibile.")

    def deposita(self, importo):
        self.ultimo_saldo = self.ultimo_saldo + importo
        movimento = f"Hai depositato {importo} euro."
        self.movimenti.append (movimento)
        self.txs_saldo.append({"movimento": movimento, "saldo": self.ultimo_saldo})

        print (f"Hai depositato {importo}, il nuovo saldo disponibile è: {self.ultimo_saldo}")

    def descrizione(self):
        #nome = self.nome

        print (f"{self.nome} è in possesso del conto: {self.conto} con saldo: {self.ultimo_saldo} ")

    def estratto_conto(self):
        with open("estratto_conto.txt", "w") as file:
            for m in self.txs_saldo:
                file.write(m["movimento"] + "\n")
                file.write("Il saldo disponibile è: " + str (m["saldo"]) + "\n")

    def last_cc (self, nome_file):
        lista_saldi = []
        len_s = len (lista_saldi) - 1
        if (os.path.exists (nome_file)):
            with open(nome_file, "r") as file:
                for lines in file:
                    if ("saldo" in lines.lower()):
                        saldo_trovato = re.findall(r'[0-9]+', lines)
                        lista_saldi.append(saldo_trovato)
                        self.ultimo_saldo = lista_saldi [len_s]
        return self.ultimo_saldo
    
#print (last_cc("estratto_conto.txt"))

conto1 = ContoCorrente("Stefania", "001", 1000)
print (conto1.last_cc("estratto_conto.txt"))
#conto1.descrizione()
#conto1.deposita(100)
#conto1.preleva(8.9)
#conto1.descrizione()
#conto1.estratto_conto()
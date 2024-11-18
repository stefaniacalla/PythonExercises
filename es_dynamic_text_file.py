'''Scrivi una funzione che permetta di inserire una canzone e salvarla in un file 
di testo. Il programma deve chiedere all'utente di inserire il titolo e il testo 
della canzone, 
e poi salvare quest'ultimo in un file intitolato titolo_canzone.txt.'''

def file_song (tit_in, testo):
    #print ("Qual è il titolo della canzone?")
    #tit_in = input ()
    tit = tit_in + "_canzone.txt"
    #print ("Qual è il testo della canzone?")
    #testo = input ()
    with open (tit, "w") as t:
        t.write (testo)




print ("Qual è il titolo della canzone?")
tit_in = input ()
print ("Qual è il testo della canzone?")
testo = input ()
file_song (tit_in, testo)


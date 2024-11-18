#Scrivere una funzione che converta un determinato numero di giorni,
#  ore e minuti (forniti in input) in secondi 

def conv_sec ():
    sec=0
    ris =""
    print ("Fornire un numero di giorni")
    g = int (input ())
    print ("Fornire un numero di ore")
    h = int (input ())   
    print ("Fornire un numero di minuti")
    m = int (input ())
    if (g>0 or h >0 or m >0):
        sec += (g*24*3600)+(h*3600)+(m*60)
        print (f"I secondi totali sono {sec}")
    else:
        print ("I secondi totali sono 0")
    #return ris


conv_sec()




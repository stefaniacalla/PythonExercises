#Crea un bot che, dato il tuo nome e anno di nascita, 
# ti risponda con «Ciao , hai anni! PUOI (o NON PUOI) guidare un’auto» 

import datetime

print ("Come ti chiami?")
nome = input ()

print ("Qual è il tuo anno di nascita?")
anno = input ()
current_year = datetime.datetime.now().year
eta = current_year - int (anno)

if (eta >=18):
    drive_s = "PUOI guidare un'auto"
else:
    drive_s = "NON PUOI guidare un'auto"

print (f"Ciao {nome}, hai {eta} anni! {drive_s}")


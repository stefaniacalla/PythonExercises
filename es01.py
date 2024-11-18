#perimetro e area rettangolo

print ("Fornire base rettangolo: ")
base = input ()
print ("Fornire altezza rettangolo: ")
altezza = input ()

perimetro = (int (base) *2) + (int (altezza)*2)
area = int (base) * int (altezza)

print ("Il perimetro del rettangolo è " + str (perimetro) + " .L'area del rettangolo è " + str (area))

#print (perimetro)


#quadrato e cubo di un numero

print ("Digitare un numero ")

numero = int (input ())
quadrato = pow (numero, 2)
cubo = pow (numero, 3)

#print (quadrato)
print ("Il quadrato del numero digitato è " + str (quadrato) + " . Il cubo del numero digitato è " + str (cubo))
print (f"Il quadrato del numero digitato è {quadrato} . Il cubo del numero digitato è {cubo}")
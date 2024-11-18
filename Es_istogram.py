'''Scrivi una semplice funzione che, data una lista di numeri, fornisca 
in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.'''

def repet (lett, lis =[]):
    ist = ''
    for i in lis:
        ist += lett * i
        print (ist)
        ist  = ''       #after each print the ist string has to be restarted


repet ('*', [3,7,9,5])

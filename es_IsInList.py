'''Scrivi un programma che a partire da un elemento e una
 lista di elementi dica in output se l'elemento passato 
 sia presente o meno nella lista.

Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci 
l'indice dell'elemento tramite il metodo index.
'''


def is_in_list (el, lista_el=[]):
    cont = 0
    for i in lista_el:
        if (i == el):
            cont +=1
        else:
            cont += cont
    
    if (cont >0):
        print (f"L'elemento {el} è presente nella lista in posizione {lista_el.index (el)}")
    else:
        print (f"L'elemento {el} non è presente nella lista")


n =0
lis = [4,5,6,0]
is_in_list (n,lis)

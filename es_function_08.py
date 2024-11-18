#Scrivere una funzione "sommatrice" che somma tutti gli elementi di
#una lista di numeri e una funzione «moltiplicatrice" che li moltiplica.
#La lista di numeri deve essere creata da input


def sommatrice ():
    l1=[]
    print ("Fornire una lista di numeri")
    num = int (input())
    for i in range (0,num):
        ele = int (input ())
        l1.append(ele)
    return print (l1)
    '''s = 0
    for i in l1:
        s += i
    return s
'''
def moltiplicatrice (l1=[]):
    m = 1
    for j in l1:
        m *= j
    return m

'''
print (sommatrice (l1=[1,2,3]))
print (moltiplicatrice (l1=[1,2,3]))  
print (sommatrice (l1=[2,2,3]))   
print (moltiplicatrice (l1=[2,2,3]))   
'''

print (sommatrice )
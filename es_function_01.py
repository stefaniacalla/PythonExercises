#Si definisca una funzione che prende in input due liste l1 e l2 
# e ritorna una lista l3. l3 contiene la differenza delle due liste. Il 
# parametro l2 deve avere come parametri di default valori da 1 a 5.

'''
def diff (l1=[], l2 = [1,2,3,4,5]):
    if len(l1) != len(l2):
        print("list need same lenght")
    else:
        l3 = [l1[i]-l2[i] for i in range(0,len(l1))]
    return print (l3)



#diff (l1= [5,10,23,12,3], l2=[30, 30,30, 30, 30])
diff (l1= [5,10,23,12,3])

'''
# [1, 2, 3] [2, 3, 4] -> 1,4
# [2, 3] [2, 3, 4] -> 4
# [1, 2, 3] [2, 3, 1] -> null
# [1, 2, 3] [2, 2, 3, 1] -> 2

def diff_el (l1=[], l2=[]):
    l3=[]
    for i in l1:
        if (i not in l2):
            l3.append (i)
    for j in l2:
        if (j not in l1):
            l3.append (j)
    return l3

#print (diff_el (l1=[1, 2, 3], l2=[2, 3, 4]))
#print (diff_el (l1=[2, 3], l2=[2, 3, 4]))
#print (diff_el (l1=[1, 2, 3], l2=[2, 3, 1]))
print (diff_el (l1=[1, 2, 3], l2=[2, 2, 3, 1]))
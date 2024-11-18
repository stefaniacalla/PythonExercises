#creazione di una tabella sql e delle funzioni di insert, delete e update parametriche

#Nell'esercizio sono state create le funzioni di insert, delete e update
#che restituiscono la stringa sql da lanciare


import sqlite3

#pip install sqlite3
def insert_tb (tab_name, l_col=[], l_val=[]):
    try:
        lun_col= len (l_col)
        lun_val = len (l_val)
        s_col =""
        s_val =""
        sep = "','"
        if (lun_col == lun_val):
        #assert lun_col!= lun_val, "La lunghezza dei campi è diversa dalla lunghezza dei valori"
            for i in range (0, lun_col):
                s_col = s_col +sep+ l_col[i]
                s_val = s_val +sep+ l_val[i]
            s_col = s_col[2:]+"'"
            s_val = s_val[2:]+"'"
            sql_ins_q = f'''INSERT INTO {tab_name} ({s_col}) VALUES ( {s_val});
                        '''
        else:
            raise
    except:
        print ("La lunghezza delle colonne e dei valori non è uguale")
    return sql_ins_q

def delete_tb (tab_name, where_con ):
    sep = "','"
    sql_del_q = f'''DELETE FROM {tab_name} 
                    WHERE {where_con};
                        '''
    return sql_del_q


def update_tb (tab_name, l_col=[], l_val=[], where_con= None):
    lun_col= len (l_col)
    lun_val = len (l_val)
    s_set =""
    for i in range (0, lun_col):
        s_set = s_set + l_col[i] + "='" + l_val[i] + "',"
    s_set = s_set [:-1]
    sql_upd_q = f'''UPDATE {tab_name} SET {s_set}
                    WHERE {where_con};
                '''
    return sql_upd_q

db = None
db = sqlite3.connect('test.db')
print ("Apertura db avvenuta con successo")
db.execute ('''drop table rubrica;''')
db.execute ('''CREATE TABLE RUBRICA (ID INT PRIMARY KEY NOT NULL,
            COGNOME TEXT NOT NULL,
            NOME TEXT NOT NULL,
            TELEFONO TEXT NOT NULL);''' )
print ("Tabella creata con successo")


#with db:
cur = db.cursor()
cur.execute(insert_tb ('rubrica', ['id', 'cognome', 'nome','telefono'],['1', 'calla', 'stefania','123455']))
cur.execute(insert_tb ('rubrica', ['id', 'cognome', 'nome','telefono'],['2', 'Rossi', 'Mario','02456894']))
cur.execute(update_tb ('rubrica', ['nome', 'cognome'], ['Stefania', 'Callà'], "ID='1'"))
cur.execute(delete_tb ('rubrica', 'ID=2'))
db.commit()

sql_select_Query='''SELECT * FROM RUBRICA'''     #la select dei record la salvo in una variabile
cur.execute(sql_select_Query)

records = cur.fetchall()
#print("Total number of rows in table: ", cur.rowcount)

for row in records: 
    print(row, '\n') 
db.close 



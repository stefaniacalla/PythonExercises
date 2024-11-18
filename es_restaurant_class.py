'''Write a Python class Restaurant with attributes like menu_items, book_table, 
and customer_orders, and methods like add_item_to_menu, book_tables, 
and customer_order.
Perform the following tasks now:
Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders.
Note: Use dictionaries and lists to store the data.'''

from typing import Any, Dict, List

class Restaurant:
    def __init__(self,menu_items=[], book_table={}):
        self.menu_items: list [str] = menu_items
        self.book_table: Dict[str:bool]= book_table
        self.customer_orders: Dict[str, Any] = {} #{tavolo: ordine}

    def add_item_to_menu(self, item=[]):
        self.menu_items.extend(item) #si usa extend quando alla lista voglio aggiungere elementi che si trovano in una lista
                                     #si usa append quando a una lista voglio aggiungere un solo elemento 

    def book_tables(self,tavolo:str):
        for tavolo in self.book_table:
            if self.book_table[tavolo]==False:
                self.book_table[tavolo]=True
            else:
                print("Il tavolo è già occupato, non è possibile prenotarlo")

    def print_menu(self):
        print(f"Il menu del giorno è il seguente: {', '.join(self.menu_items)}")
        
    def print_tab_reservations(self):
        for key, values in self.book_table.items():
            if(values==False):
                print (f"Il tavolo {key} è libero")
            else:
                print (f"Il tavolo {key} è occupato")

    

rest1=Restaurant(["carne", "pasta pesto"], {"1": False, "2":False, "3":False})
rest1.print_menu()
rest1.add_item_to_menu(["zucchine", "carote"])
rest1.print_tab_reservations()



    


    



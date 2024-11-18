#diz = {"workmail": "emp1@accenture.com", "eta": "33", "role": "Analyst"}
#dict = (["workmail": "emp1@accenture.com", "eta": "33", "role": "Analyst"])
#a = dict ([("workmail"=="emp1@accenture.com", "eta"==33, "role" =="Specialist")
           #("workmail","emp2@accenture.com", "eta",23, "role" ,"Analyst")
           #("workmail"="emp3@accenture.com", "eta"=20, "role" ="Analyst"),
           #("workmail"="emp4@accenture.com", "eta"=30, "role" ="Manager"),
           #("workmail"="emp5@accenture.com", "eta"=40, "role" ="Senior Manager")
#])


#diz = {"workmail": ["emp1@accenture.com", "emp2@accenture.com", "3@accenture.com", "emp4@accenture.com", "emp5@accenture.com" ]
#       , "eta": [33,23,20,30,40]
#       , "role": ["Specialist", "Analyst","Analyst", "Manager", "Senior Manager"] 
#       }


dict = {}
dict["MarioRossi"] = {"eta": "33", "role": "Analyst"}
dict["CC"] = {"eta": "33", "role": "Analyst"}
dict["AA"] = {"eta": "33", "role": "Analyst"}
dict["FF"] = {"eta": "33", "role": "Analyst"}
dict["CC"] = {"eta": "33", "role": "Analyst"}

print(dict)

for key in dict.keys():
    print(f"{key} ha {dict[key]['eta']} e ha ruolo {dict[key]['role']}")

for key, value in dict.items():
    print(f"{key} ha {value['eta']} e ha ruolo {value['role']}")

del dict["AA"]
for key, value in dict.items():
    print(f"{key} ha {value['eta']} e ha ruolo {value['role']}")

dict["AA"] = {"eta": "33", "role": "Analyst"}
for key, value in dict.items():
    print(f"{key} ha {value['eta']} e ha ruolo {value['role']}")

dict["AA"] = {"eta": "23", "role": "Senior Analyst"}
for key, value in dict.items():
    print(f"{key} ha {value['eta']} e ha ruolo {value['role']}")

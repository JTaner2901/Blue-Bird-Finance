# -*- coding: UTF-8 -*-
# Aufgabe: 
# Name: Mert Can Kodal
# Klasse: DQI20
# Datum: 
# macOS Python 3.9


def create_list(*a):
    debt = []
    debt.append(a)
    return debt




def show_list(list):
    for x in list:
        print(x)
    pass

def test():
    pass





if __name__ == "__main__":
    user_input = str(input("Do you want to add something or to delete something in your liabilities-list?: "))
    if user_input == "add" :
        while not user_input == "no":
            add = str(input("How much debt do you owe and to who?"))
            create_list(add)
            user_input = str(input("Do you have more to add?"))
    print("checked")
    print(create_list(add))



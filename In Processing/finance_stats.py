# -*- coding: UTF-8 -*-
# Aufgabe: Finance Stats
# Name: Mert Can Kodal
# Klasse: DQI20
# Datum: 
# macOS Python 3.9

def menu():
    print("(1) Balance \n(2) Transfer Money to Save Book \n(3) Add Money to the Balance \n(x) Exit ")
    out_of_range = True
    while out_of_range:
        user_input = input()
        if user_input == "1":
            show_stats()
        elif user_input == "2":
            print(savings_book())
        elif user_input == "3":
            save_stats()
        elif user_input == "x" or "X":
            out_of_range = False


def show_stats():
    print("Succesful")


def savings_book():
    pass


def save_stats():
    with open("stats.txt", "a") as file:
        print(input("Please Enter your name: "))
        file.write()


if __name__ == "__main__":
    menu()

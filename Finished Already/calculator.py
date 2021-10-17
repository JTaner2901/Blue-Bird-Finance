# -*- coding: UTF-8 -*-
# Aufgabe: 
# Name: Mert Can Kodal
# Klasse: DQI20
# Datum: 
# macOS Python 3.9

def salary_month(a, b):
    salary_per_month = a * b * 13 / 3
    print(f"You earn {round(salary_per_month, 1)}€ per month!")


def salary_per_hour(a, b):
    salary_per_hour = 3 * a / 13 / b
    print(f"You earn {round(salary_per_hour, 1)}€ per hour!")


def menu():
    print("What should be calculated? What your earn per months or what you earn per hour?")
    user_input = str(input("Enter the earn way please "))

    if user_input == "month":
        user_salary_hour = int(input("What do you earn per hour?: "))
        user_work_time = int(input("How many hours do you work per week?: "))
        salary_month(user_salary_hour, user_work_time)

    if user_input == "hour":
        user_month = int(input("What is your monthly salary?: "))
        user_work_time = int(input("How many hours do you work per week?: "))
        salary_per_hour(user_month, user_work_time)


if __name__ == "__main__":
    menu()
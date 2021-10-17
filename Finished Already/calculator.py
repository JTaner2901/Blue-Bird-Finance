# -*- coding: UTF-8 -*-
# Aufgabe: 
# Name: Mert Can Kodal
# Klasse: DQI20
# Datum: 
# macOS Python 3.9

class Calculator:
    """This is a class for a calculator"""
    def __init__(self):
        self.month = ""
        self.hour = ""
        self.work_time = ""

    def salary_month(self):
        salary_per_month = self.hour * self.work_time * 13 / 3
        print(f"You earn {round(salary_per_month, 1)}€ per month!")


    def salary_per_hour(self):
        salary_per_hour = 3 * self.month / 13 / self.work_time
        print(f"You earn {round(salary_per_hour, 1)}€ per hour!")


def menu():
    calc = Calculator()
    print("What should be calculated? What your earn per months or what you earn per hour?")
    user_input = str(input("Enter the earn way please "))

    if user_input == "month":
        user_salary_hour = int(input("What do you earn per hour?: "))
        user_work_time = int(input("How many hours do you work per week?: "))
        calc.hour = user_salary_hour
        calc.work_time = user_work_time
        calc.salary_month()

    if user_input == "hour":
        user_month = int(input("What is your monthly salary?: "))
        user_work_time = int(input("How many hours do you work per week?: "))
        calc.month = user_month
        calc.work_time = user_work_time
        calc.salary_per_hour()


if __name__ == "__main__":
    menu()
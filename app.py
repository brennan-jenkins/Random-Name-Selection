# import random
# random_employee = random.choice(employee)
# print(random_employee)

import random


def print_data(employee):
    print(random.choice(employee))


def main():
    employee = ["adam", "Scott", "Michael", "Andrew", "Mark", "Fernando", "Faith", "Steve", "Lee", "Amani", "Liv", "Nick A", "James", "Jake", "Brett", "Graham", "Fraser", "Jacob", "Chelsea", "Phil", "George", "Charley", "Emma", "Steph"]
    print_data(employee)


main()


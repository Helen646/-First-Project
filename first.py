import datetime
import enum
import random


class Type(enum.Enum):
    laptop = 1
    phone = 2
    tv = 3


class Status(enum.Enum):
    ready = 3
    given = 2
    repair = 1


class Person:
    def __init__(self, name, surname, parent_name):
        self.name = name
        self.surname = surname
        self.parent_name = parent_name

    def __str__(self):
        return f"{self.name} {self.surname} {self.parent_name}"

class Receipt:
    counter = 0

    def __init__(self, person: Person):
        Receipt.counter += 1
        self.receipt_number = Receipt.counter
        self.person = person

    def set_object(self, object):
        self.object = object
        self.date = datetime.date.today()
        self.date2 = self.date + datetime.timedelta(random.choice([1, 2, 3, 4, 5]))
        self.status = Status.ready

    def __str__(self):
        return f"Receipt number: {self.receipt_number}\n  Type: {self.object.__class__.__name__}\n" \
               f"  Date: {self.date}\nDate2: {self.date2}\n  Person: {self.person}\n" \
               f"  Status: {self.status}"


class Laptop:
    def __init__(self, mark: str, os: str, description: str, release_year: int):
        self.mark = mark
        self.os = os
        self.description = description


class Phone:
    def __init__(self, mark: str, os: str, description: str):
        self.mark = mark
        self.os = os
        self.description = description


class TV:
    def __init__(self, mark: str, os: str, description: str):
        self.mark = mark
        self.os = os
        self.description = description


def create_phone():
    print("Please input mark of the phone:\n")
    mark = input()
    print("Please input os of the phone:\n")
    os = input()
    print("Please input description of the brake:\n")
    description = input()
    return Phone(mark, os, description)


receipts = dict()
receipts_name = dict()
while 1:
    print("\nWhat do you want:\n1 - Repair device\n2 - Watch receipts\n")
    operation = input()
    if (operation == '1'):
        print("Please, enter your name, surname and parent name")
        person = Person(input(), input(), input())
        print("Please, choose device type:\n1 - Phone\n2 - Laptop\n3 - TV\n")
        type = input()
        receipt = Receipt(person)
        if (type == '1'):
            receipt.set_object(create_phone())
        if (type == '2'):
            print("Please input mark of the laptop:\n")
            mark = input()
            print("Please input os of the laptop:\n")
            os = input()
            print("Please input release year of the laptop:\n")
            release_year = int(input())
            print("Please input description of the brake:\n")
            description = input()
            laptop = Laptop(mark, os, release_year, description)
            receipt.set_object(laptop)
        if (type == '3'):
            print("Please input mark of the TV:\n")
            mark = input()
            print("Please input os of the TV:\n")
            os = input()
            print("Please input description of the brake:\n")
            description = input()
            tv = TV(mark, os, description)
            receipt.set_object(tv)
        print(receipt)
        receipts[receipt.receipt_number] = receipt
        if receipt.person not in receipts_name:
            receipts_name[receipt.person.__str__()] = {receipt}
        else:
            receipts_name[receipt.person.__str__()].add(receipt)
    if (operation == '2'):
        print("Input via what you want to watch receipts:\n1 - Receipt number\n2 - Person's name\n")
        a=input()
        if a=='2':
            print("Input name")
            person = Person(input(), input(), input())
            for receipt in receipts_name[person.__str__()]:
                print(receipt)
        elif a=='1':
            print("Imput receipt numder")
            r = input()
            print(receipts[int(r)])


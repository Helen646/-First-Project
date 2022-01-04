import models


def create_phone():
    print("Please input mark of the phone:\n")
    mark= input()
    print("Please input os of the phone:\n")
    os = input()
    print("Please input description of the brake:\n")
    description = input()
    return models.Phone(mark, os, description)


def create_laptop():
    print("Please input mark of the laptop:\n")
    mark = input()
    print("Please input os of the laptop:\n")
    os = input()
    print("Please input release year of the laptop:\n")
    release_year = int(input())
    print("Please input description of the brake:\n")
    description = input()
    return models.Laptop(mark, os, release_year, description)


def create_tv():
    print("Please input mark of the TV:\n")
    mark = input()
    print("Please input os of the TV:\n")
    os = input()
    print("Please input description of the brake:\n")
    description = input()
    return models.TV(mark, os, description)


receipts = dict()
receipts_name = dict()
while True:
    print("\nWhat do you want:\n1 - Repair device\n2 - Watch receipts\n")
    operation = input()
    if operation == '1':
        print("Please, enter your name, surname and parent name")
        person = models.Person(input(), input(), input())
        print("Please, choose device type:\n1 - Phone\n2 - Laptop\n3 - TV\n")
        category = input()
        receipt = models.Receipt(person)
        if category == '1':
            receipt.set_object(create_phone())
        elif category == '2':
            receipt.set_object(create_laptop())
        elif category == '3':
            receipt.set_object(create_tv())
        else:
            print("please you need to choose 1,2 or 3")
        print(receipt)
        receipts[receipt.receipt_number] = receipt
        if receipt.person not in receipts_name:
            receipts_name[receipt.person.__str__()] = {receipt}
        else:
            receipts_name[receipt.person.__str__()].add(receipt)
    if operation == '2':
        print("Input via what you want to watch receipts:\n1 - Receipt number\n2 - Person's name\n")
        change = input()
        if change == '2':
            print("Please, enter your name, surname and parent name")
            person = models.Person(input(), input(), input())
            for receipt in receipts_name[person.__str__()]:
                print(receipt)
        elif change == '1':
            print("Input receipt number")
            number_receipt = input()
            print(receipts[int(number_receipt)])
        else:
            print("please you need to choose 1 or 2")


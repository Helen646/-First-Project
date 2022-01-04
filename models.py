import datetime
import enum
import random


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

    def __init__(self, person):
        Receipt.counter += 1
        self.receipt_number = Receipt.counter
        self.person = person

    def __str__(self):
        return f"  Receipt number: {self.receipt_number}\n  Type: {self.equipment.__class__.__name__}\n" \
               f"  Date: {self.date}\n  Date2: {self.datetime_end}\n  Person: {self.person}\n" \
               f"  Status: {self.status}"

    def set_object(self, equipment):
        self.equipment = equipment
        self.date = datetime.date.today()
        self.datetime_end = self.date + datetime.timedelta(random.choice([1, 2, 3, 4, 5]))
        self.status = Status.given


def __str__(self):
    return f"Receipt number: {self.receipt_number}\n  Type: {self.object.__class__.__name__}\n" \
           f"  Date: {self.date}\nDate2: {self.datetime_end}\n  Person: {self.person}\n" \
           f"  Status: {self.status}"


class Laptop:
    def __init__(self, mark: str, os: str, description: str, release_year: int):
        self.mark = mark
        self.os = os
        self.description = description
        self.release_year = release_year


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

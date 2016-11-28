from datetime import date
from datetime import datetime


class Person:
    ''' Defines a person '''

    def __init__(self, firstname, surname, dob):
        ''' Assigns instance variables for later use '''

        self.firstname = firstname
        self.surname = surname
        self.dob = datetime.strptime(dob, '%b %d %Y').date()
        self.age = self.calculate_age(self.dob)

    def calculate_age(self, born):
        ''' Method to work out persons age from their date of birth '''

        today = date.today()
        years_difference = today.year - born.year
        is_before_birthday = (today.month, today.day) <(born.month, born.day)
        elapsed_years = years_difference - int(is_before_birthday)
        return elapsed_years

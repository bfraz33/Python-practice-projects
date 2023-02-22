class Bill:
    """
    This object contains data about the bill, such as total amount
    and the period
    """
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount

class Roommate:
    """
       This object has the names of the roommates who live in the house
       a long with the amount of days each roommate has  been in the house
       per that period and what they will need to pay for.
       """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill):
        return bill.amount / 2

class PdfReport:
    """
        This Object creates a PDF file that will display what each roommate
        owes for the period of time they were in the house.
        """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pass


the_bill = Bill(amount = 175, period = "February 2023" )
brandon = Roommate(name = "Brandon", days_in_house=21)
emily = Roommate(name = "Emily", days_in_house=29)

print(brandon.pays(bill=the_bill))




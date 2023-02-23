class Bill:
    """
    This object contains data about the bill, such as total amount
    and the period
    """
    def __init__(self, amount, period):
         self.amount = amount
         self.period = period

class Roommate:
    """
       This object has the names of the roommates who live in the house
       a long with the amount of days each roommate has  been in the house
       per that period and what they will need to pay for.
       """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        

    def pays(self, bill,roommate2):
        weight = self.days_in_house / (self.days_in_house + roommate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
        This Object creates a PDF file that will display what each roommate
        owes for the period of time they were in the house.
        """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pass


the_bill = Bill(amount = 180, period = "February 2023" )
brandon = Roommate(name = "Brandon", days_in_house=22)
emily = Roommate(name = "Emily", days_in_house=29)

print("Brandon pays:",brandon.pays(bill=the_bill,roommate2=emily))
print("Emily pays:", emily.pays(bill=the_bill,roommate2=brandon))

""""
The above code will output what each tenant owes based on the amount
of days each tenant spends in the house.
"""


from fpdf import FPDF

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
        pdf = FPDF(orientation='P', unit='pt', format="A4")
        pdf.add_page()

        # Adding image
        pdf.image("house.png", w=100, h=100)

        # Adding text
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="RENT", border=0, align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Name of tenants and amount due for each tenant
        pdf.cell(w=100, h=40, txt=roommate1.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(roommate1.pays(bill, roommate2), 2)), border=0, ln=1)

        pdf.cell(w=100, h=40, txt=roommate2.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(roommate2.pays(bill, roommate1), 2)), border=0, ln=1)

        pdf.output(self.filename)


the_bill = Bill(amount = 180, period = "February 2023" )
brandon = Roommate(name = "Brandon", days_in_house=22)
emily = Roommate(name = "Emily", days_in_house=29)

print("Brandon pays:",brandon.pays(bill=the_bill,roommate2=emily))
print("Emily pays:", emily.pays(bill=the_bill,roommate2=brandon))

#This generates the PDF
pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(roommate1=brandon, roommate2=emily, bill=the_bill)

""""
The above code will output what each tenant owes based on the amount
of days each tenant spends in the house.
"""


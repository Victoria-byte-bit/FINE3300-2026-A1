# Part 1: Making the Exchange rate Calculator

class ExchangeRates:

    def __init__(self, filename):
        self.filename = filename
# Here, I created a class for the exchange rate calculator. I wanted to refer back to the exchange rate file by an easier name, and using the textbook, I found the common parameter "filename" to be a good choice. It's stored using "self" so that an object can use it later, as learned in class.

        exchange_file = open(self.filename, "r")
        rows = exchange_file.readlines()
        exchange_file.close()
#Now that I have to get the exchange rate from the file, I used readome "r" (from the textbook) to read the file. I was going to turn the lines of rows into a list when Python suggested "readlines()", a built-in function. Then, I closed the file because the first time I ran it, I got an error later that the file was open.

        headings = rows[0].strip().split(",")
        latest_row = rows[-1].strip().split(",")
#Here, I used indexing to select the headings and latest row, taught in class. Then, because I need to seperate values to choose a specific item, I used strip() and split(",") to remove extra line endings and separate each row into individual values, taught in the textbook.

        column_number = 0

        for heading in headings:
            if heading == "FXAUSDCAD":
                break
            column_number += 1
#Since the exchange rate could be in a different column, I used a loop to find the FXAUSDCAD heading and keep track of its position. Maybe I could've tried indexing again, but I wanted to use a loop to practice what I learned in class. I also used break to stop the loop when it found the heading. 

        self.rate = float(latest_row[column_number])
#With the column secured, I found the latest exchange rate, then converted it to a float so Python could calculate with it.

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            converted_amount = amount

        elif from_currency == "USD":
            converted_amount = amount * self.rate

        else:
            converted_amount = amount / self.rate
#I've now defined the convert method. Conditional statements was a fun one, where I used if, elif, and else to create the calculation for currencies. Matching currencies shouldn't be converted, USD to CAD needs multiplication, and CAD to USD needs division.

        return converted_amount
#I simply returned the calculated amount so the rest of my Python could use and display the answer.

exchange_rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")
#Now,  I am out of the class and able to use an ExchangeRates object and pass it in the name of the CSV file that it should read.

amount = float(input("Enter the amount you want to convert: "))
from_currency = input("Convert from USD or CAD? (Enter USD or CAD): ").upper()
to_currency = input("Convert to USD or CAD? (Enter USD or CAD): ").upper()
#Right here, I used input() to collect every amount and currency that the user types. The amount was converted into a float again and I came up with some basic command statements. Also, I ran it once using "usd" and "cad" naturally, and because it wasn't uppercase, it treated it as my "else" statement, so I fixed that using "upper()", taught from a friend.

result = exchange_rates.convert(amount, from_currency, to_currency)

print("${:.2f} {} = ${:.2f} {}".format(
    amount, from_currency, result, to_currency
))
#Now it's time to use the covert method to calculate the conversion and print the result! Formatting the dollar signs, 2 decimal places, and currency names was a nightmare, but I used Docs.Python as a source. It's another built-in method called str.format, and you just place the variables in the order you want them to appear.
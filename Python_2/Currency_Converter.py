import requests

url = "https://api.exchangeratesapi.io/latest?base=USD"

class CurrencyCalculator:

    def __init__(self):
        #kurs na valuta
        self.rates = requests.get(url).json()["rates"]
        self.commision = 0.03

    def convert (self, from_currency, to_currency, amount):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount

        to_c = self.rates[to_currency]
        from_c = self.rates[from_currency]


        if from_currency == "USD":
            calc_amount = amount*to_c

        else:
            calc_amount = 1/(from_c/to_c)*amount

        return calc_amount


calculator = CurrencyCalculator()

print(calculator.convert("CAD", "EUR", 1))

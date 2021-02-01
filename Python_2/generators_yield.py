# import Currency_Converter
#
# my_calc = Currency_Converter.CurrencyCalculator()
#
# my_calc.convert("EUR", "USD", 100)

# def myRange(start, stop):
#     current_val = start
#
#     while current_val < stop:
#
#         yield current_val   #so yield ne izlegva od funkcijata (za razlika od RETURN)
#
#         current_val += 1
#
#
# for x in myRange(1, 11 ):
#     print(x)

# def Factoriel(n):
#
#     if n == 0:
#         return 1
#     else:
#         return n * Factoriel(n-1)     #rekurzija
#
# print(Factoriel(4))

# def anagram(word1, word2):
#
#     if len(word1) == len(word2):
#         for i in word1:
#             if not i in word2:
#                 return False
#         return True
#     else:
#         return False
#
# print(anagram("silent", "listein"))

class SortedList:

    def __init__(self, list):
        self.list = list

    def find_element_for(self, position):
        return self.list[position]

    def find_position_for(self, element):
        for i in range(0, len(self.list)):
            if element == self.list[i]:
                print(f'{self.list[i]} se naogja na {i} pozicija')
            # print(i, self.list[i])

        #razmisli
        #da se najde pozicija na element
        # zadavame element, funkcijata ja vrakja pozicijata

    # def insert(self):
    #
    #     position = self.find_position_for(element)

s = SortedList([8.3, 3, "5", 6.256, 8, "a111aa", "Filip"])


print(s.find_element_for(3))

print(s.find_position_for("5"))

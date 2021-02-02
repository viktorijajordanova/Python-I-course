

class SomeList:

    def __init__(self, list):
        self.list = list

    def find_element_for(self, position):
        return f'Na pozicija #{position} se naogja {self.list[position]}'

    def find_position_for(self, element):
        for i in range(0, len(self.list)):
            if element == self.list[i]:
                return f'{self.list[i]} se naogja na pozicija #{i} '
            else:
                return "Ne posoti takov element vo listata"


s = SomeList([8.3, 3, "5", 6.256, 8, "a111aa", "Filip"])


print(s.find_element_for(3))

print(s.find_position_for("5"))

class cell():
    def __init__(self, my_cell):
        self.my_cell = my_cell

    def __add__(self, other):
        if (self.my_cell > 0):
            return self.my_cell + other.my_cell
        else:
            return "Число должно быть больше 0"

    def __sub__(self, other):
        if (self.my_cell > 0):
            return self.my_cell - other.my_cell
        else:
            return "Число должно быть больше 0"

    def __mul__(self, other):
        if (self.my_cell > 0):
            return self.my_cell * other.my_cell
        else:
            return "Число должно быть больше 0"

    def __truediv__(self, other):
        if (self.my_cell > 0):
            return self.my_cell // other.my_cell
        else:
            return "Число должно быть больше 0"

    def make_order(self, in_row):
        if (in_row < 1):
            print("Число должно быть больше 0")
        else:
            c = ('\n'.join([''.join(['*' for i in range(in_row)])
                            for n in range(self.my_cell // in_row)]))
            c += '\n'
            c += ''.join(['*' for n in range(self.my_cell % in_row)])
            print(c)


a = cell(26)
b = cell(2)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
a.make_order(-4)
b.make_order(4)

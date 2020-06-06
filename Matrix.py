class Matrix():
    mass = []

    def __init__(self, number):
        self.number = number
        number

    def __str__(self):
        return " ".join("  ".join([str(i) for line in self.number for i in line]))

    def __add__(self, other):
        try:
            m = [[(int(self.number[l][n]) + int(other.number[l][n])) for n in range(len(self.number[l]))]
                 for l in range(len(self.number))]
            return Matrix(m)
        except IndexError:
            print('Ошибка кол-во индексов.')


m1 = [[2, 3, ], [4, 5]]
m2 = [['2', '1'], [5, 3]]
a = Matrix(m1)
b = Matrix(m2)
print(a.__str__())
print(b.__str__())
newM = (a + b)
print(newM)

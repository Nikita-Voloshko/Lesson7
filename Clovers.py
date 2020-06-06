from abc import abstractmethod


class Clovers():
    size = 0

    @abstractmethod
    def __init__(self, size):
        pass

    @abstractmethod
    def my_clover(self):
        pass


class Clover1(Clovers):
    def __init__(self, size):
        if (size == "XS"):
            Clovers.size = 20
        elif (size == "S"):
            Clovers.size = 25
        elif (size == "M"):
            Clovers.size = 30
        elif (size == "L"):
            Clovers.size = 35
        elif (size == "XL"):
            Clovers.size = 40
        else:
            print("Ошибка! Неправельный размер.")
        Clovers.__init__(self, size="M")

    @property
    def my_clover(self):
        if (Clovers.size > 0):
            return f'{(Clovers.size / 6.5 + 0.5)} квадратных метров ткани на костюм {a.size}-го размера.'
        else:
            return 0


class Clover2(Clovers):
    def __init__(self, size):
        if (size == 20):
            Clovers.size = 20
        elif (size == 25):
            Clovers.size = 25
        elif (size == 30):
            Clovers.size = 30
        elif (size == 35):
            Clovers.size = 35
        elif (size == 40):
            Clovers.size = 40
        else:
            print("Ошибка! Неправельный размер.")

    @property
    def my_clover(self):
        if (Clovers.size > 0):
            return f'{(2 * Clovers.size + 0.3)} квадратных метров ткани на пальто {a.size}-го размера.'
        else:
            return 0


a = Clover2(20)
a.__init__(20)
print(a.my_clover, f'квадратных метров ткани на пальто {a.size}-го размера.')



calculators = []


class Calculator(object):
    def __init__(self, idn, model, price, name, ram, videocart):
        self.idn = idn
        self.model = model
        self.price = price
        self.name = name
        self.ram = ram
        self.videocart = videocart
    



    def deleteCalculator(model, name):
        for i in range(len(calculators) - 1):
            if model == calculators[i].model and name == calculators[i].name:
                calculators.pop(i)

    def EditCalculator(model, name):
        for i in range(len(calculators) - 1):
            if model == calculators[i].model and name == calculators[i].name:
                idn = int(input("input ID"))
                model = input("model")
                price = int(input("price"))
                name = input("name")
                ram = input("ram")
                videocart = input("videocart")
                calculators[i].idn = idn
                calculators[i].model = model
                calculators[i].price = price
                calculators[i].ram = ram
                calculators[i].videocart = videocart
                calculators[i].name = name
        return calculators


class NoteBook(Calculator):
    def _init_(self, idn, model, price, name, ram, videocart, keyboard, touchpad):
        super()._init_(idn)
        super()._init_(model)
        super()._init_(price)
        super()._init_(name)
        super()._init_(ram)
        super()._init_(videocart)
        self.keyboard = keyboard
        self.touchpad = touchpad


class Gamecomputer(Calculator):
    def _init_(self, idn, model, price, name, ram, videocart, secondVideocard, audioChanel):
        super()._init_(idn)
        super()._init_(model)
        super()._init_(price)
        super()._init_(name)
        super()._init_(ram)
        super()._init_(videocart)
        self.secondVideocard = secondVideocard
        self.audioChanel = audioChanel
def AddCalculator():
    idn = int(input("input ID"))
    model = input("model")
    price = int(input("price"))
    name = input("name")
    ram = input("ram")
    videocart = input("videocart")
    calculator = Calculator(idn, model, price, name, ram, videocart)
    calculators.append(calculator)
calculator = Calculator(5,5,5,5,5,5)
calculators.append(calculator)
calculator = Calculator(3,3,3,3,3,3)
calculators.append(calculator)
calculator = Calculator(2,2,2,2,2,2)
calculators.append(calculator)
calculator = Calculator(1,1,1,1,1,1)
calculators.append(calculator)
calculator = Calculator(8,8,8,8,8,8)
calculators.append(calculator)
calculator = Calculator(9,9,9,9,9,9)
calculators.append(calculator)
calculator = Calculator(5,5,5,5,5,5)
calculators.append(calculator)
calculator = Calculator(1,1,1,1,1,1)
calculators.append(calculator)
calculator = Calculator(4,4,4,4,4,4)
calculators.append(calculator)
menu = "1.Add Calculator\n2.Delete calculator\n3.Edit calculator\n4.Sort by price\n5.Print Data"
k = 1
i = 0
def byPrice_key(calculators):
    return calculators.price
while 1:
    print(menu)
    selector = int(input('Select option\n'))
    if selector == 1:
        AddCalculator()
    if selector == 2:
        model = input("model")
        name = input("name")
        Calculator.deleteCalculator(model, name)
    if selector == 3:
        model = input("model")
        name = input("name")
        Calculator.EditCalculator(model, name, )
    if selector == 4:
       calculators.sort(key = byPrice_key)
    if selector == 5:
        for i in range(len(calculators)- 1):
            print("ID = ")
            print(calculators[i].idn)
            print("Model = ")
            print(calculators[i].model)
            print("Price = ")
            print(calculators[i].price)
            print("Name = ")
            print(calculators[i].name)
            print("Ram = ")
            print(calculators[i].ram)
            print("Videocart = ")
            print(calculators[i].videocart )
    if selector == 6:
        for i in range(len(calculators)- 1):
            print("Price = ")
            print(calculators[i].price)
          

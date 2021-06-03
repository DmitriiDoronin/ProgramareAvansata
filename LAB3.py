
import sqlite3
from sqlite3 import Error

connection = sqlite3.connect('Films.db')
cursor = connection.cursor()





calc = []
calculators = []
bussiness = []

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
                idn1 = calculators[i].idn
                model1 = calculators[i].model
                price1 = calculators[i].price
                ram1 = calculators[i].ram
                videocart1 = calculators[i].videocart
                name1 = calculators[i].name
                calculators[i].idn = idn
                calculators[i].model = model
                calculators[i].price = price
                calculators[i].ram = ram
                calculators[i].videocart = videocart
                calculators[i].name = name
                sql_update_query = """Update Calculators set Id = ? where Id = ?"""
                data = (idn, idn1)
                cursor.execute(sql_update_query, data)           
                connection.commit()
                sql_update_query = """Update Calculators set Model = ? where Model = ?"""
                data = (model, model1)
                cursor.execute(sql_update_query, data)           
                connection.commit()
                sql_update_query = """Update Calculators set Price = ? where Price = ?"""
                data = (price, price1)
                cursor.execute(sql_update_query, data)           
                connection.commit()
                sql_update_query = """Update Calculators set Name = ? where Name = ?"""
                data = (name, name1)
                cursor.execute(sql_update_query, data)           
                connection.commit()
                sql_update_query = """Update Calculators set videocart = ? where videocart = ?"""
                data = (videocart, videocart1)
                cursor.execute(sql_update_query, data)           
                connection.commit()
                sql_update_query = """Update Calculators set Ram = ? where Ram = ?"""
                data = (ram, ram1)
                cursor.execute(sql_update_query, data)           
                connection.commit()
        


class NoteBook(Calculator):
    def __init__(self, keyboard, touchpad,*args):
        Calculator.__init__(self,*args)
        self.keyboard = keyboard
        self.touchpad = touchpad
class Gamecomputer(Calculator):
    def __init__(self,secondVideocard, audioChanel,*args):
        Calculator.__init__(self,*args)
        self.secondVideocard = secondVideocard
        self.audioChanel = audioChanel
class Bussinescomputer(Calculator):
    def __init__(self,operationalSystem,software,*args):
        self.operationalSystem = operationalSystem
        self.software = software
        Calculator.__init__(self,*args)
def AddCalculator():
    idn = int(input("input ID"))
    calc.append(idn)
    model = input("model")
    calc.append(model)
    price = int(input("price"))
    calc.append(price)
    name = input("name")
    calc.append(name)
    ram = input("ram")
    calc.append(ram)
    videocart = input("videocart")
    calc.append(videocart)
    calc1 = tuple(calc)
    calculator = Calculator(idn, model, price, name, ram, videocart)
    calculators.append(calculator)
    cursor.executemany("INSERT INTO Computers VALUES (?,?,?,?,?,?)", (calc1,))           
    connection.commit()
    calc1 = tuple()
    calc.clear()
    
def AddBussinesCalculator():
    idn = int(input("input ID"))
    model = input("model")
    price = int(input("price"))
    name = input("name")
    ram = input("ram")
    videocart = input("videocart")
    opertionalSystem = input("opertionalSystem")
    software = input("software")
    Bussinescalculator = Bussinescomputer(idn, model, price, name, ram, videocart,opertionalSystem,software)
    bussiness.append(Bussinescalculator)
    

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
        idn2 = int(input("ID"))
        for i in range(len(calculators)-1):
            if idn2 == calculators[i].idn:
                idn = int(input("input ID"))
                model = input("model")
                price = int(input("price"))
                name = input("name")
                ram = input("ram")
                videocart = input("videocart")
                idn1 = calculators[i].idn
                model1 = calculators[i].model
                price1 = calculators[i].price
                ram1 = calculators[i].ram
                videocart1 = calculators[i].videocart
                name1 = calculators[i].name
                calculators[i].idn = idn
                calculators[i].model = model
                calculators[i].price = price
                calculators[i].ram = ram
                calculators[i].videocart = videocart
                calculators[i].name = name
                sql_update_query = """Update Computers set Id = ? where Id = ?"""
                data1 = (idn, idn1)
                cursor.execute(sql_update_query, data1)           
                connection.commit()
                sql_update_query = """Update Computers set Model = ? where Model= ?"""
                data2 = (model,model1)
                cursor.execute(sql_update_query, data2)           
                connection.commit()
                sql_update_query = """Update Computers set Price = ? where Price = ?"""
                data3 = (price, price1)
                cursor.execute(sql_update_query, data3)           
                connection.commit()
                sql_update_query = """Update Computers set Name = ? where Name = ?"""
                data4 = (name, name1)
                cursor.execute(sql_update_query, data4)           
                connection.commit()
                sql_update_query = """Update Computers set videocart = ? where videocart = ?"""
                data5 = (videocart, videocart1)
                cursor.execute(sql_update_query, data5)           
                connection.commit()
                sql_update_query = """Update Computers set Ram = ? where Ram = ?"""
                data6 = (ram,ram1)
                cursor.execute(sql_update_query, data6)           
                connection.commit()
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
    if selector == 7:
        
        idn = int(input("input ID"))
        
        model = input("model")
        
        price = int(input("price"))
        
        name = input("name")
        
        ram = input("ram")
        
        videocart = input("videocart")
        calculator = Calculator(idn, model, price, name, ram, videocart)
        calculators.append(calculator)

          

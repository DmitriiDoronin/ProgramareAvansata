import sqlite3
from sqlite3 import Error
Elements = []
calc = []
connection = sqlite3.connect('Films.db')
cursor = connection.cursor()

def AddElement():
    videocart = input("videocart")
    calc.append(videocart)
    ram = input("ram")
    calc.append(ram)
    name = input("name")
    calc.append(name)
    price = int(input("price"))
    calc.append(price)
    idn = int(input("input ID"))
    calc.append(idn)
    model = input("model")
    calc.append(model)


    calc1 = tuple(calc)
    cursor.executemany("INSERT INTO Computers VALUES (?,?,?,?,?,?)", (calc1,))           
    connection.commit()
    calc1 = tuple()
    calc.clear()
def EditElement():
    idn = int(input('Id of element'))
    node = input('Node to edit')
    value = input('Value')
    sql_update_query = """Update Computers set """+node+""" = ? where Id = ?"""
    data = (value,idn)
    cursor.execute(sql_update_query, data)           
    connection.commit()
def ReadElement():
    idn = input('Id of element')
    node = input('Node to read')
    sql_update_query = """SELECT """+node+""" FROM Computers WHERE Id = """+idn
    cursor.execute(sql_update_query)
    one_result = cursor.fetchone()
    connection.commit()
    print(one_result)
    return one_result
def ReadElements():
    i = 0
    NumberOfQueryes = int(input("Input number of elements"))
    while(i < NumberOfQueryes):
        idn = input('Id of element')
        node = input('Node to read')
        sql_update_query = """SELECT """+node+""" FROM Computers WHERE Id = """+idn
        cursor.execute(sql_update_query)
        one_result = cursor.fetchone()
        connection.commit()
        Elements.append(one_result)
        print (Elements)
        i+=1
    return Elements
def DeleteElement():
    idn = input('Id of element')
    sql_update_query = """DELETE  FROM Computers WHERE Id = """+idn
    cursor.execute(sql_update_query)
    connection.commit()
def DeleteAllElements():
    sql_update_query = """DELETE  FROM Computers """
    cursor.execute(sql_update_query)
    connection.commit()
AddElement()

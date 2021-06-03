import sqlite3
from sqlite3 import Error
Elements = []
books = []
connection = sqlite3.connect('Films.db')
cursor = connection.cursor()

def AddElement():
    author = input("author")
    books.append(author)
    bookTitle = input("bookTitle")
    books.append(bookTitle)
    publicationYear = input("publicationYear")
    books.append(publicationYear)
    bookGenre = input("bookGenre")
    books.append(bookGenre)
   ## idn = int(input("input ID"))
    ##calc.append(idn)
    ##model = input("model")
    ##calc.append(model)


    book1 = tuple(books)
    cursor.executemany("INSERT INTO Books VALUES (?,?,?,?)", (book1,))           
    connection.commit()
    book1 = tuple()
    books.clear()
def EditElement():
    bookTitle = input('Title of the book')
    node = input('Node to edit')
    value = input('Value')
    sql_update_query = """Update Books set """+node+""" = ? where bookTitle = ?"""
    data = (value,bookTitle)
    cursor.execute(sql_update_query, data)           
    connection.commit()
def ReadElement():
    bookTitle = input('Title of the book')
    node = input('Node to read')
    sql_update_query = """SELECT """+node+""" FROM Books WHERE bookTitle = """+bookTitle
    cursor.execute(sql_update_query)
    one_result = cursor.fetchone()
    connection.commit()
    print(one_result)
    return one_result
def ReadElements():
    i = 0
    NumberOfQueryes = int(input("Input number of elements"))
    while(i < NumberOfQueryes):
        bookTitle = input('Title of the book')
        node = input('Node to read')
        sql_update_query = """SELECT """+node+""" FROM Books WHERE bookTtitle = """+bookTitle
        cursor.execute(sql_update_query)
        one_result = cursor.fetchone()
        connection.commit()
        Elements.append(one_result)
        print (Elements)
        i+=1
    return Elements
def DeleteElement():
    bookTitle = input('Ttitle of the book ')
    sql_update_query = """DELETE  FROM Books WHERE bookTitle = """+bookTitle
    cursor.execute(sql_update_query)
    connection.commit()
def DeleteAllElements():
    sql_update_query = """DELETE  FROM Books """
    cursor.execute(sql_update_query)
    connection.commit()
AddElement()

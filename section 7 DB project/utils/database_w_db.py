# Concerned with storing and retrieving books from csv file
# format: name,author,read\n
import sqlite3

"""

"""
books_file = "books.json"
# functions below are the content of the interface communicating with business logic

def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books (name text primary key,author text,read integer)') #create table #real is floating point number in sqlite3; PK = no duplicates + faster search
    connection.commit()
    connection.close()

def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    #f string isn't recommended approach since it enables SQL injectons
    #cursor.execute(f'INSERT INTO books VALUES("{name}","{author}",0)') #" are used to tell sqlite that data is string, not table name
    #safer way to use tuple of parameters
    #TODO add try - except to not insert duplicated books (due to stupid business logic)
    cursor.execute('INSERT INTO books VALUES(?,?,0)', (name, author))
    connection.commit()
    connection.close()

def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * from books')  # " are used to tell sqlite that data is string, not table name
    #books = cursor.fetchall() #or fetch one or limit with SQL; #fetchall = list of tuples [()]
    books = [{'name':row[0],'author':row[1],'read':row[2]} for row in cursor.fetchall()] #convert to dictionary so that same data constructs are used in-app
    connection.close()
    return books

def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET read=1 WHERE name=?",(name,)) #still a tuple in parameters
    connection.commit()
    connection.close()

def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE name=?", (name,)) #still a tuple in parameters
    connection.commit()
    connection.close()

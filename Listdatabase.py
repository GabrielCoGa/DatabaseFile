#https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p
"""
Concerned with storing and retrieving books from a csv file.
Format of the csv file:
name,author,read\n
"""

books_file = 'book.txt'

def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author}'0) #Cero for false, one for true

def get_all_books():
    #[[name, author,read], [name, author,read]]
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    
    """books = [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]
    return books
    """
    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]

def mark_book_as_read(name):
    pass
def delete_book(name):
   pass
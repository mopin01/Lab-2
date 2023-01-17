from dataclasses import dataclass

class Author:
    #init method to create Author object with a given name and an empty book list
    def __init__(self, name):
        self.name = name
        self.books = []
    
    #publish method adds a book to the book list except if the book is already in the list
    def publish(self, title):
        if title not in self.books:
            self.books.append(title)
        else:
            print("Error: Book already exists")
    
    #str method prints the author name as well as the book list
    def __str__(self):
        return f'Author name: {self.name}, Books: {self.books}'

def main():
    #creates author object
    author = Author('person')
    #adds 2 books
    author.publish('book')
    author.publish('other book')
    #prints author and books
    print(author)

main()
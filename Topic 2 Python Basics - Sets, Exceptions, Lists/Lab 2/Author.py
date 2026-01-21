class Author:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def Publish(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            print('Book is already present')

    def __str__(self):
        return f'Author name: {self.name}, Books Published: {self.books}'
    
shakespeare = Author('shakespeare', ['Othello', 'Hamlet', 'A Midsummer Night Dream'])
shakespeare.Publish('Romeo and Juliet')
jamessacorey = Author('James S. A. Corey', ['Leviathan Wakes', 'Caliban\'s War', 'Cibola Burn'])
jamessacorey.Publish('Nemesis Games')
jamessacorey.Publish('Leviathan Wakes')

print(shakespeare)
print(jamessacorey)


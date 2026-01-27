
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)
    
    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        # titles will be whichever of the two options is true
        # if the truthy (first option) then it will be printed
        #otherwise, the falsy (second option) will be printed.
        return f'Name: {self.name}, Books Published: {titles}'

shakespeare = Author('William Shakespeare')
shakespeare.publish('Hamlet')
shakespeare.publish('Othello')

print(shakespeare)


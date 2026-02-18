from flask import Flask, request, jsonify

# Create a server to be used as an API server
app = Flask(__name__)

# empty list of books an author has published
books_published = []
# real api would use persistant storage such as a database


@app.route('/books')
def all_books():
    return jsonify(books_published)

@app.route('/book', methods=['POST'])
def add_book():
    new_book = request.form
    name = new_book.get('name')
    if not name:
        return 'No book name provided', 400
    if name not in books_published:
        books_published.append(name)
        return 'Added', 201
    else:
        return 'Duplicate book', 400
    
if __name__ == '__main__':
    app.run()
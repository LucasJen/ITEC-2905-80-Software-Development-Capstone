import requests

new_book = {'name': 'Example'}
add_book_response = requests.post('http://127.0.0.1:5000/book', data=new_book)
print(add_book_response.status_code)

all_books_response = requests.get('http://127.0.0.1:5000/books')
print(all_books_response.json())
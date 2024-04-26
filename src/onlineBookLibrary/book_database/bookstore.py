import json


books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)  # initialize json file as empty list


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def add_book(book_name, author, user_name):
    books = get_all_books()
    books.append({'book_name': book_name, 'author': author,
                  'users': [{'user_name': user_name, 'user_role': 'admin', 'read': False}]})
    save_all_books(books)


def mark_book_as_read(book_name, user_name):
    books = get_all_books()
    for book in books:
        if book['book_name'] == book_name:
            users = book['users']
            users.append({'user_name': user_name, 'user_role': 'reader', 'read': '1'})
    save_all_books(books)


def delete_book(book_name):
    books = get_all_books()
    books = [book for book in books if book['book_name'] != book_name]
    save_all_books(books)

import json
from src.onlineBookLibrary.rating_calculator import logic


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


def add_book(book_name, author, description, user_name):
    books = get_all_books()
    is_found = False
    for book in books:
        if book['book_name'] == book_name:
            is_found = True
    if not is_found:
        books.append({'book_name': book_name, 'author': author, 'description': description,
                      'average_rating': 0, 'total_rating_score': 0, 'number_of_read_times': 0,
                      'users': [{'user_name': user_name, 'user_role': 'admin', 'read': False}]})
        save_all_books(books)
        print("The book successfully added to the library.")
    else:
        print(f"{book_name} is already exists in the library.")


def mark_book_as_read(book_name, user_name, book_rating):
    books = get_all_books()
    is_found = False
    for book in books:
        if book['book_name'] == book_name:
            is_found = True
            number_of_reads = book['number_of_read_times']
            number_of_read_times = logic.calculate_number_of_read_times(number_of_reads)
            book['number_of_read_times'] = number_of_read_times
            total_rating = book['total_rating_score']
            total_rating_score = logic.calculate_total_rating_score(total_rating, book_rating)
            book['total_rating_score'] = total_rating_score
            average_rating = logic.calculate_average_rating(total_rating_score, number_of_read_times)
            book['average_rating'] = average_rating
            users = book['users']
            users.append({'user_name': user_name, 'user_role': 'reader', 'read': '1'})
            print(f"{book['book_name']} by {book['author']} — Rating : {average_rating}")
    save_all_books(books)
    if not is_found:
        print(f"{book_name} is not exists in the library.")


def delete_book(book_name):
    books = get_all_books()
    is_found = False
    for book in books:
        if book['book_name'] == book_name:
            is_found = True
    if is_found:
        books = [book for book in books if book['book_name'] != book_name]
        save_all_books(books)
        print("The book successfully deleted from the library.")
    else:
        print(f"{book_name} is not exists in the library.")

from book_database import bookstore
from book_database import user

USER_CHOICE = """
Please Enter:
- 'a' to add a new book
- 'l' to list all books
- 'sn' to search a book by name
- 'sa' to search a book by author
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Please Enter Your Choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'sn':
            search_a_book_by_name()
        elif user_input == 'sa':
            search_a_book_by_author()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)


def is_admin(user_name) -> bool:
    return user.verify_admin_user(user_name)


def prompt_add_book():
    user_name = input('Enter your name: ')
    book_name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')
    description = input('Enter the new book description: ')

    if is_admin(user_name):
        bookstore.add_book(book_name, author, description, user_name)
    else:
        print('You must have admin privileges to add a book.')


def list_books():
    book_list = bookstore.get_all_books()
    for book in book_list:
        print(f"{book['book_name']} by {book['author']} — Rating : {book['average_rating']}")


def search_a_book_by_name():
    book_name = input('Enter the book name: ')
    book_list = bookstore.get_all_books()
    is_found = False
    for book in book_list:
        if book['book_name'] == book_name:
            print(f"{book['book_name']} by {book['author']} — Rating : {book['average_rating']}")
            is_found = True
    if not is_found:
        print("The book is not in the library.")


def search_a_book_by_author():
    author = input('Enter the book author: ')
    book_list = bookstore.get_all_books()
    is_found = False
    for book in book_list:
        if book['author'] == author:
            print(f"{book['book_name']} by {book['author']} — Rating : {book['average_rating']}")
            is_found = True
    if not is_found:
        print(f"There is not any book written by {author} in the library.")


def prompt_read_book():
    user_name = input('Enter your name: ')
    book_name = input('Enter the name of the book you just finished reading: ')
    book_rating = float(input('Enter your rating ( 1 - 5 ): '))

    bookstore.mark_book_as_read(book_name, user_name, book_rating)


def prompt_delete_book():
    user_name = input('Enter your name: ')
    book_name = input('Enter the name of the book you wish to delete: ')

    if is_admin(user_name):
        bookstore.delete_book(book_name)
    else:
        print('You must have admin privileges to delete a book.')


menu()

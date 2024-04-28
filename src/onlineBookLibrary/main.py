from book_database import bookstore
from book_database import user

USER_CHOICE = """
Please Enter:
- 'a' to add a new book
- 's' to search a book by name or author
- 'l' to list all books
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
        print(f"{book['book_name']} by {book['author']}")


def prompt_read_book():
    user_name = input('Enter your name: ')
    book_name = input('Enter the name of the book you just finished reading: ')

    bookstore.mark_book_as_read(book_name, user_name)


def prompt_delete_book():
    user_name = input('Enter your name: ')
    book_name = input('Enter the name of the book you wish to delete: ')

    if is_admin(user_name):
        bookstore.delete_book(book_name)
    else:
        print('You must have admin privileges to delete a book.')


menu()

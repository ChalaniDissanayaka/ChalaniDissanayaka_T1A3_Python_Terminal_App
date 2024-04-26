from book_database import bookstore


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


def prompt_add_book():
    book_name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    bookstore.add_book(book_name, author)


def list_books():
    for book in bookstore.get_all_books():
        read = 'YES' if book['read'] == '1' else 'NO'  # if book 'read' == false then Read: NO
        print(f"{book['book_name']} by {book['author']} — Read: {read}")


def prompt_read_book():
    book_name = input('Enter the name of the book you just finished reading: ')

    bookstore.mark_book_as_read(book_name)


def prompt_delete_book():
    book_name = input('Enter the name of the book you wish to delete: ')

    bookstore.delete_book(book_name)


menu()

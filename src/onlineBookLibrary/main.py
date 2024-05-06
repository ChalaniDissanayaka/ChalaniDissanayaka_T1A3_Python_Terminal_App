from book_database import bookstore
from book_database import user
from rating_calculator import logic
from tabulate import tabulate
from operator import itemgetter
import sys
import time


# Rainbow colors (ANSI escape codes)
colors = [
    "\033[31m",   # Red
    "\033[91m",   # Light Red
    "\033[33m",   # Yellow
    "\033[93m",   # Light Yellow
    "\033[32m",   # Green
    "\033[92m",   # Light Green
    "\033[34m",   # Blue
    "\033[94m",   # Light Blue
    "\033[35m",   # Magenta
    "\033[95m",   # Light Magenta
    "\033[36m",   # Cyan
    "\033[96m"    # Light Cyan
]


# ASCII art for "Chapter Haven"
def create_ascii_logo():
    ascii_art = r"""

                    {y}          /$$$$$$ /$$                          /$$                             /$$   /$$                                    
                    {g}         /$$__  $| $$                         | $$                            | $$  | $$                                    
                    {m}        | $$  \__| $$$$$$$  /$$$$$$  /$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$       | $$  | $$ /$$$$$$ /$$    /$$/$$$$$$ /$$$$$$$ 
                    {b}        | $$     | $$__  $$|____  $$/$$__  $|_  $$_/  /$$__  $$/$$__  $$      | $$$$$$$$|____  $|  $$  /$$/$$__  $| $$__  $$
                    {c}        | $$     | $$  \ $$ /$$$$$$| $$  \ $$ | $$   | $$$$$$$| $$  \__/      | $$__  $$ /$$$$$$$\  $$/$$| $$$$$$$| $$  \ $$
                    {m}        | $$    $| $$  | $$/$$__  $| $$  | $$ | $$ /$| $$_____| $$            | $$  | $$/$$__  $$ \  $$$/| $$_____| $$  | $$
                    {y}        |  $$$$$$| $$  | $|  $$$$$$| $$$$$$$/ |  $$$$|  $$$$$$| $$            | $$  | $|  $$$$$$$  \  $/ |  $$$$$$| $$  | $$
                    {r}         \______/|__/  |__/\_______| $$____/   \___/  \_______|__/            |__/  |__/\_______/   \_/   \_______|__/  |__/
                    {g}                                   | $$                                                                                     
                    {m}                                   | $$                                                                                     
                    {c}                                   |__/                                                                                                                                                                                  

    """

    print(ascii_art.format(r=colors[0], g=colors[4], y=colors[2], b=colors[6], c=colors[10], m=colors[8]))

    # Text to display
    text = "WELCOME TO CHAPTER HAVEN ONLINE BOOK LIBRARY"

    # Display rainbow-colored text
    for i, char in enumerate(text):
        color = colors[i % len(colors)]  # Cycle through colors
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.1)  # Delay between characters
    sys.stdout.write("\033[0m\n")  # Reset color and move cursor to next line


def list_books():
    book_list = bookstore.get_all_books()
    primary_key = itemgetter("book_name")
    book_list.sort(key=primary_key)
    header = ['Book Name', 'Author', 'Rating']
    book_data = []
    book_data_values = []

    for book in book_list:
        if book['average_rating'] == 0 and book['number_of_read_times'] == 0:
            book_data.append({'book_name': book['book_name'], 'author': book['author'],
                              'average_rating': 'Reader has not rated this book yet.'})
        else:
            book_data.append({'book_name': book['book_name'], 'author': book['author'],
                              'average_rating': book['average_rating']})

    for data in book_data:
        book_data_values.append(list(data.values()))

    print(' ')
    print(tabulate(book_data_values, headers=header, tablefmt='fancy_grid'))


create_ascii_logo()
list_books()

USER_CHOICE = """
Please Enter:
\033[1;32;40m- 'a' to add a new book\033[1;37;40m
\033[1;33;40m- 'l' to list all books\033[1;37;40m
\033[1;34;40m- 'sn' to search a book by name\033[1;37;40m
\033[1;35;40m- 'sa' to search a book by author\033[1;37;40m
\033[1;36;40m- 'r' to mark a book as read\033[1;37;40m
\033[1;31;40m- 'd' to delete a book\033[1;37;40m
\033[1;37;40m- 'q' to quit\033[1;37;40m

\033[1;36;40mPlease Enter Your Choice:\033[1;37;40m """


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
        list_books()
    else:
        print("You must have admin privileges to add a book.")


def search_a_book_by_name():
    book_name = input('Enter the book name: ')
    book_list = bookstore.get_all_books()
    is_found = False
    for book in book_list:
        if book['book_name'].strip().lower() == book_name.strip().lower():
            is_found = True
            if book['average_rating'] == 0 and book['number_of_read_times'] == 0:
                print(f"{book['book_name']} by {book['author']} — Rating : Reader has not rated this book yet.")
            else:
                print(f"{book['book_name']} by {book['author']} — Rating : {book['average_rating']}")
    if not is_found:
        print("The book is not in the library.")


def search_a_book_by_author():
    author = input('Enter the book author: ')
    book_list = bookstore.get_all_books()
    primary_key = itemgetter("book_name")
    book_list.sort(key=primary_key)
    header = ['Book Name', 'Author', 'Rating']
    book_data = []
    book_data_values = []
    is_found = False
    for book in book_list:
        if book['author'].strip().lower() == author.strip().lower():
            is_found = True
            if book['average_rating'] == 0 and book['number_of_read_times'] == 0:
                book_data.append({'book_name': book['book_name'], 'author': book['author'],
                                  'average_rating': 'Reader has not rated this book yet.'})
            else:
                book_data.append({'book_name': book['book_name'], 'author': book['author'],
                                  'average_rating': book['average_rating']})

    for data in book_data:
        book_data_values.append(list(data.values()))

    print(' ')
    print(tabulate(book_data_values, headers=header, tablefmt='fancy_grid'))

    if not is_found:
        print(f"There is not any book written by {author} in the library.")


def prompt_book_rating():
    while True:
        try:
            book_rating = float(input('Enter your rating ( 1 - 5 ): '))
            return book_rating
        except ValueError:
            print("Invalid rating score. Please Enter rating between 1 - 5 ")


def prompt_book_rating_when_invalid():
    while True:
        try:
            book_rating = float(input('Invalid rating score. Please Enter rating between 1 - 5 '))
            return book_rating
        except ValueError:
            print("Invalid rating score. Please Enter rating between 1 - 5 ")


def prompt_read_book():
    user_name = input('Enter your name: ')
    book_name = input('Enter the name of the book you just finished reading: ')
    book_rating = prompt_book_rating()
    is_valid_rating = logic.validate_rating_score(book_rating)

    if is_valid_rating:
        bookstore.mark_book_as_read(book_name, user_name, book_rating)
    else:
        book_rating = prompt_book_rating_when_invalid()
        while not logic.validate_rating_score(book_rating):
            prompt_book_rating_when_invalid()
            book_rating = prompt_book_rating_when_invalid()
        bookstore.mark_book_as_read(book_name, user_name, book_rating)


def prompt_delete_book():
    user_name = input('Enter your name: ')
    book_name = input('Enter the name of the book you wish to delete: ')

    if is_admin(user_name):
        bookstore.delete_book(book_name)
        list_books()
    else:
        print("You must have admin privileges to delete a book.")


menu()

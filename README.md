## ChalaniDissanayaka_T1A3_Python_Terminal_App - (Coder Academy Term 1 Assignment 3)

### LINKS

- https://github.com/ChalaniDissanayaka/ChalaniDissanayaka_T1A3_Python_Terminal_App

## Authors

Chalani Dissanayaka

### PURPOSE

The purpose of creating an online library Python terminal application is to showcase my Python knowledge and demonstrate my skills in full-stack (backend) development as a student and potential employee. By developing a user-friendly interface for the online library, I aim to impress employers and secure opportunities to contribute effectively as a front-end developer in the industry. This project will highlight my ability to create robust and efficient backend systems while also emphasizing my understanding of user experience and interface design. Through this application, I seek to exhibit my proficiency in Python programming, backend development, and my dedication to delivering high-quality solutions that meet user needs and expectations.

### TARGET AUDIENCE

The target audience for the Python online book library terminal application includes both readers and library administrators. For readers, this application provides a convenient and accessible platform to explore, search for, and interact with a vast collection of books. It caters to individuals who enjoy reading and seek a user-friendly interface to discover new titles, search by author or book name, and track their reading progress. Additionally, the application appeals to library administrators who require efficient tools to manage and organize the library's collection. By offering features such as adding, deleting, and listing books, as well as calculating average ratings and tracking read times, the application addresses the needs of administrators responsible for maintaining a comprehensive and organized library system. Overall, the application serves as a valuable resource for both readers and administrators, enhancing their reading experience and streamlining library management tasks.

### SITE MAP

![Site Map](docs/portfolio_flowchart.png "Site Map")

### BRAINSTORM THE IDEA (Identifying the Problem)

I identified that many online book libraries required payment to access them, which I found to be a problem. As someone who loves reading and wants to become a full-stack developer, I decided to solve this issue by creating a free online book library using Python. My goal was to showcase my programming skills while also providing a helpful service to fellow book lovers. Inspired by the simplicity of digital libraries, I began developing a terminal-based application that would allow users to explore and organize their virtual book collections without any fees. Drawing from my own experiences as both a reader and a developer, I focused on creating a user-friendly, engaging platform that would offer an enjoyable reading experience for everyone.

## FUNCTIONALITY & FEATURES

The Python online book library terminal app boasts a user-friendly interface and caters to two types of users: administrators and readers.

- FEATURES

  - ADD A BOOK
  - DELETE A BOOK
  - LIST ALL BOOKS
  - SEARCH BOOK BY BOOK NAME
  - SEARCH BOOK BY BOOK AUTHOR NAME
  - READER CAN MARK A BOOK AS READ AND GIVE THE RATING FOR A BOOK (1 - 5)

- Administrators have the ability to Add, Delete, and List all books, marking books as read and providing ratings, as well as book search by name or search by author.

- Meanwhile, readers can also List all books and book search by name or search by author, in addition to marking books as read and providing ratings.

These features ensure efficient management of the library for administrators and a seamless browsing experience for readers, enhancing overall usability and satisfaction within the app.

## PLANNING PHASE.

- **Step One**
  I need to seek approval from my academic lecturer for the online book library project, and they approved it. Their support gave me the confidence to continue developing the platform.

- **Step Two**
  I drew a use case diagram to identify the user scenarios in this online library. Drawing a use case diagram for an online book library helps in understanding the different interactions and scenarios that users may encounter while using the system. It allows for the visualization of various user roles, their goals, and the functionalities they require from the library.

![Use Case Diagram](docs/portfolio_flowchart.png "Use Case Diagram")

- **Step Three**
  Drawing a flow chart helps in visualizing the logical flow of operations within the online library system. It allows me to identify key processes, decision points, and the sequence of actions that occur when users interact with the system. This flowchart serves as a roadmap for implementing the system's functionality and ensures that all necessary steps are accounted for in the development process. Additionally, it helps in troubleshooting and debugging the system by providing a clear overview of its logic and operation. Overall, creating a flow chart is an essential step in designing and developing a robust online library system.

![Flow Chart](docs/portfolio_flowchart.png "Flow Chart")

- **Step Four**
  After drawing the flow chart and understanding the functionality of the online book library, I created Trello board cards to kickstart my development process and track the progress.

![Link to Trello Board](docs/portfolio_flowchart.png "Trello Board")

## DEVELOPMENT PHASE.

## PSEUDOCODE FOR THE PYTHON ONLINE BOOK LIBRARY

    store books: online book library (books.json)

        Loop:
            Print menu options:
                'a': Add a new book
                'l': List all books
                'sn': Search for a book by name
                'sa': Search for a book by author
                'r': Mark a book as read
                'd': Delete a book
                'q': Quit

            Get user choice input


        -If user choice is: 'a'
            Get user input
                Enter your name:
                Enter new book name:
                Enter description:
                Enter author name:
            If user is not an admin:
                Print error message:
                    "You must have admin privileges to add a book."
                Go back to Menu
            Else:
                Get new book details: book name, book author, book description
                Add book to the library (List - books.json, List Item - single book)
                Print message:
                    "The book successfully added to the library."
            Go back to Menu

        -If user choice is: 'd'
            Get user input
                Enter your name:
                Enter the name of the book you wish to delete:
            If user is not an admin:
                Print error message:
                    "You must have admin privileges to delete a book."
                Go back to Menu
            Else:
                Get book name input
                If book exists in library:
                    Delete book from library (List - books.json, List Item - single book)
                    Print success message:
                        "The book successfully deleted from the library."
                Else:
                    Print error message:
                        "{book name} is not exists in the library."
            Go back to Menu

        -If user choice is: 'l'
            If library is empty:
                Print message:
                    "The library is empty."
            Else:
                Print all books in the library with Name, Author and Rating
            Go back to Menu


        -If user choice is 'sn':
            Get user input
                Enter book name:
            If book name exists in library:
                Print book Name, Author, and Rating
            Else:
                Print error message:
                    "The book is not in the library."
            Go back to Menu


        -If user choice is 'sa':
            Get user input
                Enter the book author:
            If author name exists in library:
                Print all books written by the author with Name, Author and Rating
            Else:
                Print error message:
                    "There is not any book written by {author name} in the library."
            Go back to Menu


        -If user choice is 'r':
            Get user input
                Enter your name:
                Enter the name of the book you just finished reading:
                Enter your rating ( 1 - 5 ):
            If book exists in library:
                Get rating input
                If rating is between 1 and 5:
                    Update book rating in library (List - books.json, List Item - single book)
                    Print message:
                         Book Name, Author, and New Rating
                Else:
                    Print error message:
                        "Invalid rating score. Please enter a rating between 1 - 5."
                Go back to Menu
            Else:
                Print error message:
                        "{book name} is not exists in the library."
            Go back to Menu


        -If user choice is 'q':
            Quit the application

# HOW TO RUN THIS APP IN YOU COMPUTER

Here are the step-by-step instructions to run your Python online book library app on any computer using a virtual environment:

    1. Clone or Download the Repository:
        First, make sure you have the source code of online library app available on your computer. You can either clone the repository from a version control system like GitHub or download the source code as a ZIP file and extract it to a directory on your computer.

    2. Install Python:
        Ensure that Python is installed on your computer. You can download and install Python from the official Python website (https://www.python.org/). Follow the installation instructions for your operating system.

import json
# import yaml


class Book:

    def __init__(self, title: str, author: str, is_available: bool = True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        return f"Titre : {self.title} Auteur : {self.author} Disponibilité :{self.is_available}"

class Library:

    books = []

    def add_book(self, title: str, author: str):
        book = Book(title, author)
        self.books.append(book)

    def list_books(self):
        return [str(book) for book in self.books]

    def show_books(self):
        for book in self.list_books():
            print(book)


    def save_books(self, file_path: str):
        with open(file_path, 'w') as f:
            book_data = [{"title": book.title, "author": book.author, "available": book.is_available} for book in self.books]
            json.dump(book_data, f)
            print(f"État de la bibliothèque sauvegardé dans {file_path}")

    def load_books(self, file_path: str):
        with open(file_path, 'r') as f:
            book_data = json.load(f)
            self.books.clear()
            for data in book_data:
                self.books.append(Book(data["title"], data["author"], data["available"]))
            print(f"État de la bibliothèque chargé depuis {file_path}")



    def lend_book(self, book_title: str, student: 'Student') -> bool:

        for book in student.borrowed_books:
            if book.title == book_title:
                print(f"Déjà emprunté : {book_title}")
                return False
            

        for book in self.books:
            if book.title == book_title:
                if book.is_available:
                    student.borrowed_books.append(book)
                    book.is_available = False
                    print(f"{book_title} emprunté par {student.name}")
                    return True
                else:
                    print(f"{book_title} est déjà emprunté")
                    return False
                

        print(f"{book_title} introuvable")
        return False
    

    def accept_return(self, book_title: str, student: 'Student'):
        for book in student.borrowed_books:
            if book.title == book_title:
                student.borrowed_books.remove(book)
                book.is_available = True
                print(f"{book_title} rendu par {student.name}")
                return
        print(f"{student.name} n'a pas emprunté {book_title}")


    def search_books(self, query: str):
        result = [str(book) for book in self.books if query in book.title or query in book.author]
        return result

class Student:

    def __init__(self, name: str, borrow_limit : int = 3):
        self.name = name
        self.borrowed_books = []
        self.borrow_limit = borrow_limit

    def borrow_book(self, book_title: str, library: Library):

        if len(self.borrowed_books) >= self.borrow_limit:
            print("L'étudiant a déjà emprunté trop de livres")
            return


        for book in library.books:
            if book.title == book_title and book.is_available:
                self.borrowed_books.append(book)
                book.is_available = False
                print(f"{self.name} emprunte {book_title}")
                return
        print(f"{book_title} non disponible")

    def return_book(self, book_title: str, library: Library):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                book.is_available = True
                print(f"{self.name} rend {book_title}")
                return
        print(f"{self.name} n'a pas emprunté {book_title}")


library = Library()

library.add_book("Le Petit Prince", "Antoine de Saint-Exupéry")
library.add_book("Les Misérables", "Victor Hugo")
library.add_book("L'Étranger", "Albert Camus")

library.save_books("librairie.json")

new_library = Library()
new_library.load_books("library_state.json")

new_library.show_books()




library.add_book("1984", "George Orwell")
library.add_book("Le Petit Prince", "Antoine de Saint-Exupéry")

student = Student("Louis")

student.borrow_book("1984", library)

student.borrow_book("1984", library)
student.return_book("1984", library)

student.return_book("1984", library)


student.borrow_book("1984", library) 
student.borrow_book("Le Petit Prince", library) 
student.borrow_book("Les Misérables", library) 
student.borrow_book("L'Étranger", library)

library.show_books()
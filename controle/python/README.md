
# Library System

## Description
Ce projet simule un système de gestion de bibliothèque. Il permet d'ajouter des livres, de les prêter, de les rendre, de chercher des livres par titre ou auteur, et de sauvegarder/charger l'état de la bibliothèque dans un fichier JSON.

## Classes

### `Book`
La classe `Book` représente un livre dans la bibliothèque. Chaque livre possède :
- **title** : Le titre du livre.
- **author** : L'auteur du livre.
- **is_available** : Indique si le livre est disponible à l'emprunt (par défaut `True`).

Méthodes :
- `__str__()`: Affiche une représentation sous forme de chaîne du livre avec son titre, auteur et sa disponibilité.

### `Library`
La classe `Library` représente une bibliothèque contenant une liste de livres. Elle permet de gérer les livres et leur état.

Méthodes :
- `add_book(title: str, author: str)`: Ajoute un livre à la bibliothèque.
- `list_books()`: Renvoie une liste de tous les livres sous forme de chaînes.
- `show_books()`: Affiche tous les livres de la bibliothèque.
- `save_books(file_path: str)`: Sauvegarde l'état actuel de la bibliothèque dans un fichier JSON.
- `load_books(file_path: str)`: Charge l'état de la bibliothèque à partir d'un fichier JSON.
- `lend_book(book_title: str, student: 'Student')`: Permet à un étudiant d'emprunter un livre s'il est disponible et que l'étudiant ne dépasse pas sa limite d'emprunts.
- `accept_return(book_title: str, student: 'Student')`: Permet à un étudiant de rendre un livre qu'il a emprunté.
- `search_books(query: str)`: Recherche les livres par titre ou auteur en fonction de la requête donnée.

### `Student`
La classe `Student` représente un étudiant qui peut emprunter et rendre des livres.

Méthodes :
- `borrow_book(book_title: str, library: Library)`: Permet à l'étudiant d'emprunter un livre de la bibliothèque, si le livre est disponible et si l'étudiant n'a pas dépassé sa limite d'emprunts.
- `return_book(book_title: str, library: Library)`: Permet à l'étudiant de rendre un livre qu'il a emprunté.

## Fonctionnalités

- **Ajout de livres** : Vous pouvez ajouter des livres à la bibliothèque avec `add_book()`.
- **Emprunt de livres** : Les étudiants peuvent emprunter des livres, mais ils doivent respecter une limite d'emprunts (par défaut 3 livres).
- **Retour de livres** : Les étudiants peuvent rendre des livres qu'ils ont empruntés.
- **Recherche de livres** : Vous pouvez rechercher un livre en fonction de son titre ou de son auteur avec `search_books()`.
- **Sauvegarde et chargement de l'état** : Vous pouvez sauvegarder l'état de la bibliothèque dans un fichier JSON avec `save_books()` et charger l'état depuis un fichier JSON avec `load_books()`.
  
## Exemple d'utilisation

### Ajouter des livres
```python
library = Library()
library.add_book("Le Petit Prince", "Antoine de Saint-Exupéry")
library.add_book("Les Misérables", "Victor Hugo")
library.add_book("L'Étranger", "Albert Camus")
```

### Sauvegarder et charger l'état
```python
library.save_books("library_state.json")
new_library = Library()
new_library.load_books("library_state.json")
new_library.show_books()
```

### Emprunter des livres
```python
student = Student("Louis")
student.borrow_book("1984", library)
student.borrow_book("Le Petit Prince", library)
student.borrow_book("Les Misérables", library)  # dépasse la limite
```

### Retourner un livre
```python
student.return_book("1984", library)
student.return_book("Le Petit Prince", library)
```

### Rechercher un livre
```python
search_result = library.search_books("Victor Hugo")
print(search_result)
```

## Fonctionnalité d'emprunt maximum

Les étudiants peuvent emprunter jusqu'à 3 livres au maximum par défaut. Vous pouvez définir cette limite lors de la création d'un étudiant en passant un autre nombre à l'argument `borrow_limit`.

```python
student = Student("Louis", borrow_limit=3)
```

## Licence
Ce projet est distribué sous la licence MIT. Vous pouvez l'utiliser et le modifier librement sous les termes de cette licence.

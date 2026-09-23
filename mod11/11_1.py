class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


class Magazine(Publication):
    def __init__(self, name, editor_in_chief):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Editor-in-chief: {self.editor_in_chief}")


magazine = Magazine("Aku Ankka", "Aki Hyyppä")
book = Book("Hytti n:o 6", "Rosa Liksom", 200)

magazine.print_information()
print()
book.print_information()

class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

class StudentMember(Member):
    def __init__(self, name, membership_id):
        super().__init__(name, membership_id)
        self.books_borrowed = 0

    def add_book(self):
        self.books_borrowed += 1
        print(f"{self.name} borrowed a book.")

    def return_book(self):
        if self.books_borrowed > 0:
            self.books_borrowed -= 1
            print(f"{self.name} returned a book.")
        else:
            print("No books to return.")

    def display_status(self):
        print(f"{self.name} has currently borrowed {self.books_borrowed} book(s).")

# Demo
student = StudentMember("Amruth", "M102")
student.add_book()
student.display_status()
student.return_book()
student.display_status()

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        
book1 = Book(title="To Kill a Mockingbird", author="Harper Lee", year_published=1960)
book2 = Book(title="1984", author="George Orwell", year_published=1949)
book3 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year_published=1925)
print("Book Details:")
print("--------------")
book1.describe()
print()
book2.describe()
print()
book3.describe()

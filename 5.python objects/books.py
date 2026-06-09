class Book:
    def __init__(self,title):
        self.title = title
    def create_book_list():
        return [Book("python 101"),Book("A1 Basics"),Book("Data science")]
        books =Book.create_book_list()
        for b in books:
            print("Book title:",b.title)
errors

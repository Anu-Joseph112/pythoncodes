class Publisher:
    def __init__(self, publisher):
        self.publisher = publisher


class Book(Publisher):
    def __init__(self, publisher, title, author):
        Publisher.__init__(self, publisher)
        self.title = title
        self.author = author

    def display(self):
        print("Publisher:", self.publisher)
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, publisher, title, author, price):
        Book.__init__(self, publisher, title, author)
        self.price = price

    # Method overriding
    def display(self):
        super().display()
        print("Price:", self.price)


# Creating Python book object
p = Python("BPB Publications", "Learning Python",
           "Mark Lutz", 550)

# Displaying book information
print("Python Book Details")
p.display()


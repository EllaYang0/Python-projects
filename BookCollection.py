from Book import Book
from BookCollectionNode import BookCollectionNode
class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count


    def insertBook(self, book):
        new_node = BookCollectionNode(book)
        current = self.head

        if self.head is None:
            self.head = new_node
            return
        if self.head.data >new_node.data:
            new_node.next = self.head
            self.head = new_node
            return

        while current.next is not None and new_node.data > current.next.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def getBooksByAuthor(self, author):
        current = self.head
        book = []
        while current is not None:
            if author.lower() == current.data.author.lower():
                book.append(current.data.getBookDetails())

            current = current.next
        return '\n'.join((book)) + '\n' if book else ''

    def removeAuthor(self, author):
        current = self.head
        prev = None
        author_lower = author.lower()
        while current is not None:
            if current.data.author.lower() == author_lower:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
            else:
                prev = current
            current = current.next

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode is None:
            return False

        if bookNode.data.title.lower() == title.lower():
            return True

        return self.recursiveSearchTitle(title, bookNode.next)

    def getAllBooksInCollection(self):
            current = self.head
            books = []

            while current is not None:
                books.append(current.data.getBookDetails())
                current = current.next
            return '\n'.join(books) + '\n' if books else ''


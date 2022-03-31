import Num1

with open('books.txt', 'r') as books:
    books=open('books.txt','r', encoding='utf8')
    stack = Num1.Stack()
    for book in books:
        book = book.strip()
        print(book)
        stack.push(book)
    print()
    while not stack.is_empty():
        print(stack.pop())
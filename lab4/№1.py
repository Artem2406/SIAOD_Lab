import Num1;
with open('books.txt','r') as books:
    books=open('books.txt','r',encoding="utf8")
    q1 = Num1.Deque()
    q2 = Num1.Deque()
    for book in books:
        q1.push(book)
    while not q1.is_empty():
        x = q1.pop()
        while not q2.is_empty() and q2.peek() > x:
            q1.push_left(q2.pop())
        q2.push(x)
    while not q2.is_empty():
        print(q2.pop())
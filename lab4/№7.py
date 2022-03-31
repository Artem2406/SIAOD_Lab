import random

import Num1

numbers = [random.randint(-50, 50) for i in range(10)]
print(numbers)
deque = Num1.Deque()
for n in numbers:
    if n < 0:
        deque.push_left(n)
    else:
        deque.push(n)
while not deque.is_empty():
    x = deque.pop_left()
    if x < 0:
        deque.push(x)
    else:
        deque.push_left(x)
        break
while not deque.is_empty():
    x = deque.pop()
    if x < 0:
        print(x)
    else:
        deque.push(x)
        break
while not deque.is_empty():
    print(deque.pop_left())
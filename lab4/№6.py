import Num1

text = 'Добрый вечер 123  345 спасимюо!!!'
letters = Num1.Stack()
digits = Num1.Stack()
others = Num1.Stack()
for c in text:
    if c.isalpha():
        letters.push(c)
    elif c.isdigit():
        digits.push(c)
    else:
        others.push(c)
new_text = ''
letters.reverse()
digits.reverse()
others.reverse()
while not digits.is_empty():
    new_text += digits.pop()
while not letters.is_empty():
    new_text += letters.pop()
while not others.is_empty():
    new_text += others.pop()
print(new_text)
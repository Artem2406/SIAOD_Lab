import random

import Num1

alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
random.shuffle(alphabet)    #Перемешивает изменяемую последовательность случайным образом
alphabet = ''.join(alphabet) #join для того, чтобы конвертировать список букв алфавита (без разделений) в строку для сохранения
print(alphabet)
key = Num1.Deque()
for letter in alphabet:
    key.push(letter)

#кодировка
def encode(c):
    for i in range(len(key)):
        x = key.pop_left()
        if x == c:
            key.push(x)
            val = key.pop_left()
            key.push(val)
            return val
        key.push(x)
#декодировка
def decode(c):
    for i in range(len(key)):
        x = key.pop()
        if x == c:
            key.push_left(x)
            val = key.pop()
            key.push_left(val)
            return val
        key.push_left(x)

text = 'куда я тут жмал...'.lower()

encoded = ''
for letter in text:
    if encoded_letter := encode(letter):
        encoded += encoded_letter
    else:
        encoded += letter

print(encoded)

decoded = ''
for letter in encoded:
    if decoded_letter := decode(letter):
        decoded += decoded_letter
    else:
        decoded += letter
print(decoded)
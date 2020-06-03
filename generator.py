import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = int(input('Количество паролей?'))
length = int(input('Длина пароля?'))

for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)
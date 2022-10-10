# Pierwszy skrypt w Pythonie
import os
import sys

print(sys.platform)
print(os.system('chcp'))
print(os.system('chcp 1252'))
print('2 do potęgi 100 = ', 2 ** 100)
# print(2 ** 100)

strName = 'Marco '

print(strName * 8)

nextInput = input('Podaj swoje imię')
print('\nHello', nextInput)

input('Naciśnij klawisz "ENTER", aby zakończyć program')

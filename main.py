from race_o_meter import visualize
from add_athelite import add, check_eligiblity
import pandas
from tkinter import *

print('Select what you want to do')
print('0: Add player')
print('1: Modify player')
print('2: Remove Player')
print('3: Visualize race between two players')
print('4: Check Elegiblity')
print('5: Show Data')
data = pandas.read_excel('runner_data.xlsx', index_col='Name')
while True:
    print('-'*50)
    a = input('Enter No: ')
    if a == '0': add()
    elif a == '1':
        name = input('What is the name: ')
        f = input('Which feature to modify: ')
        data.loc[f, name] = input('What is new value: ')
    elif a == '2': del data[input("Person's name: ")]
    elif a == '3': visualize(input("What is first player's name: "), input("What is second player's name: "))
    elif a == '4': check_eligiblity()
    elif a == '5':
        target = list(data[input('Your Name: ')])
        print('-'*50)
        print(f'Age: {target[0]}')
        print(f'Gender: {target[1]}')
        print(f'Race participated last year: {target[2]} meters')
        print(f'Time You took Last year: {target[3]} seconds')
        print(f'Past Height: {target[4]} meters')
        print(f'Current Height: {target[5]} meters')
        print(f'Past BMI: {target[6]}')
        print(f'Current BMI: {target[7]}')
        print('-'*50)
    print('-'*50)
data.to_excel('runner_data.xlsx')

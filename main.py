from race_o_meter import visualize
from add_athelite import add, check_eligiblity
import pandas
from tkinter import *

while True:
    data = pandas.read_excel('runner_data.xlsx', index_col='Name')
    data_ = pandas.read_excel('elegiblity records.xlsx', index_col='Name')
    print('-'*50)
    print('Select what you want to do')
    print('0: Add player')
    print('1: Modify player')
    print('2: Remove Player')
    print('3: Visualize race between two players')
    print('4: Check Elegiblity')
    print('5: Show Information')
    print('6: Quit')
    a = input('Enter No: ')
    if a == '0': add()
    elif a == '1':
        name = input('What is the name: ')
        f = input(f'Which feature to modify {list(data.index)} (write whole correctly): ')
        try: data[name]
        except: print('Name not found')
        try: data.loc[f, name] = int(input('What is new value: '))
        except: data.loc[f, name] = input('What is new value: ')
        data.to_excel('runner_data.xlsx')
    elif a == '2':
        try:
            data.pop(input("Person's name: "))
        except:
            print('Name not found')
        data.to_excel('runner_data.xlsx')
        data = pandas.read_excel('runner_data.xlsx', index_col='Name')
    elif a == '3': visualize(input("What is first player's name: "), input("What is second player's name: "))
    elif a == '4': check_eligiblity()
    elif a == '5':
        name = input('What is your name: ')
        try:
            target = data[name]
            
            print(f'Age: {target["Age"]}')
            print(f'Gender: {target["Gender"]}')
            print(f'Race: {"Not Participated" if target["Race"] == 0 else target["Race"]}')
            print(f'Time: {"Not Participated" if target["Race"] == 0 else target["Time"]}')
            print(f'Past height: {target["Past height"]}')
            print(f'Current height: {target["Current height"]}')
            print(f'Past BMI: {target["Past BMI"]}')
            print(f'Current BMI: {target["Current BMI"]}')
            try:
                target1 = data_[name]
                print(f'BFP: {target1[0]}')
                print(f'PARQ: {target1[1]}')
                print(f'Is elegible: {target1[2]}')
            except:
             print('Eligibility test not done, Not showing Eligibility data')
        except:
            print('Name not Found')

    elif a == '6':
        quit()
    print('-'*50)

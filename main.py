from race_o_meter import visualize
from add_athelite import add
import pandas

print('Select what you want to do')
print('0: Add player')
print('1: Modify player')
print('2: Remove Player')
print('3: Visualize race between two players')
a = input('Enter No: ')
data = pandas.read_excel('runner_data.xlsx')
if a == '0': add()
elif a == '2':
    del data[input("Person's name: ")]
elif a == '3': visualize(input("What is first player's name: "), input("What is second player's name: "))
data.to_excel('runner_data.xlsx', index=False)
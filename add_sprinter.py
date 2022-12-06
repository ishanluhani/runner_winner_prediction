import pandas

name = input('Your Name: ')
race = int(input('Race you participate in last year (meters): '))
time = float(input('How much time it took you to complete that race (sec): '))
last_weight = int(input('What was your weight last year (kg): '))
weight = int(input('What is your current weight (kg): '))
last_height = int(input('What was your height last year (cm): '))/100
height = int(input('What is your current height (cm): '))/100
past_bmi = last_weight/(last_height*last_height)
current_bmi = weight/float(height*height)
data = pandas.read_excel('runner_data.xlsx', 'Sheet1')
data[name] = [race, time, last_height*100, height*100, past_bmi, current_bmi]
data.to_excel('runner_data.xlsx', index=False)
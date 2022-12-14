import pandas
from tkinter import *
from survey import submit

def add():
    try:
        name = input('Your Name: ')
        age = int(input('Your Age: '))
        gender = input('Your gender (m or f): ').upper()
        race = input('which Race you participated last year (Relay, 100m, 200m, 400m, Notselected) (Do Not include "m"): ').lower()
    except:
        print('Invalid Data')
        
    if race == 'relay':
        race = 100
    elif race == 'notselected':
        race = 0
    else:
        race = int(race)
    if race != 0: time = int(input('How much time you took to complete that race (sec): '))
    else: time = 0
    past_weight = int(input('What is your last year weight (kg): '))
    weight = int(input('What is your current weight (kg): '))
    past_height = int(input('What is your last year height (cm): '))/100
    height = int(input('What is your current height (cm): '))/100
    past_bmi = past_weight/(past_height*past_height)
    current_bmi = weight/(height*height)
    answers = []
    data = pandas.read_excel('runner_data.xlsx', index_col='Name')
    data[name] = [age, gender, race, time, past_height, height, past_bmi, current_bmi]
    data.to_excel('runner_data.xlsx')
answer = False
def check_eligiblity():
    global answer
    name = input('Your Name: ')
    data_ = pandas.read_excel('runner_data.xlsx', index_col='Name')[name]
    age = data_[0]
    gender = data_[1]
    current_bmi = data_[7]
    bfp_done = True
    check_dict = {True: 'Eligible', False: 'Not Eligible'}
    if gender == 'M':
        current_BFP = 1.51*current_bmi-.7*age-2.2
        if 18 <= current_BFP <= 24:
            bfp_done = False
            print('According to the American Council of exercise, Your body fat comes to Average Category, You need to improve, thats why you are not eligible')
        if current_BFP > 24:
            bfp_done = False
            print('According to the American Council of exercise, Your body fat comes to Obuse Category, thats why you are not eligible')
    else:
        current_BFP = 1.51*current_bmi-.7*age-2.2
        if 25 <= current_BFP <= 31:
            bfp_done = False
            print('According to the American Council of exercise, Your body fat comes to Average Category, You need to improve, thats why you are not eligible')
        if current_BFP > 31:
            bfp_done = False
            print('According to the American Council of exercise, Your body fat comes to Obuse Category, thats why you are not eligible')
    if not bfp_done:
        return
    input('Press Enter to continue: ')
    def sub():
        global answer
        answer = submit()
        root.destroy()
    root = Tk()
    Button(root, text='Start PARQ Test', command=sub).pack()
    root.mainloop()
    if not all([bfp_done, answer]):
        final = False
        print('Not Eligible')
    else:
        final = True
        print('Eligible')
    data = pandas.read_excel('elegiblity records.xlsx', index_col='Name')
    data[name] = [check_dict[bfp_done], check_dict[answer], check_dict[final]]
    data.to_excel('elegiblity records.xlsx')
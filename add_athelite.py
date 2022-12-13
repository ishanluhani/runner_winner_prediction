import pandas
from tkinter.messagebox import askyesno
from survey import submit

def add():
    name = input('Your Name: ')
    age = int(input('Your Age: '))
    gender = input('Your gender (m or f): ').upper()
    race = int(input('which Race you participated last year (meters): '))
    time = int(input('How much time you took to complete that race (sec): '))
    past_weight = int(input('What is your last year weight (kg): '))
    weight = int(input('What is your current weight (kg): '))
    past_height = int(input('What is your last year height (cm): '))/100
    height = int(input('What is your current height (cm): '))/100
    past_bmi = past_weight/(past_height*past_height)
    current_bmi = weight/(height*height)
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

    input('Press Enter to continue: ')
    answers = []
    submit()
    data = pandas.read_excel('runner_data.xlsx')
    data[name] = [age, gender, race, time, past_height, height, past_bmi, current_bmi, check_dict[bfp_done], check_dict[any(answers)]]
    data.to_excel('runner_data.xlsx', index=False)

import pandas

name = input('Your Name: ')
age = int(input('Your Age: '))
gender = input('Your gender (m or f): ').upper()
weight = int(input('What is your current weight (kg): '))
height = int(input('What is your current height (cm): '))/100
current_bmi = weight/(height*height)
if gender == 'M':
    BFP = 1.51*current_bmi-.7*age-2.2
    if 18 <= BFP <= 24:
        print('According to the American Council of exercise, Your body fat comes to Average Category, You need to improve, thats why you are not eligible')
    if BFP > 24:
        print('According to the American Council of exercise, Your body fat comes to Obuse Category, thats why you are not eligible')
else:
    BFP = 1.51*current_bmi-.7*age+1.4
    if 25 <= BFP <= 31:
        print('According to the American Council of exercise, Your body fat comes to Average Category, You need to improve, thats why you are not eligible')
    if BFP > 31:
        print('According to the American Council of exercise, Your body fat comes to Obuse Category, thats why you are not eligible')
print(BFP)
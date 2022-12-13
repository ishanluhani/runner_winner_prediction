import pandas

speed_for_every_centimeter = .005
speed_for_every_bmi = .4


def mps_calculate(age, gender, race_meters, time_took_last_year, past_height, height, past_bmi, bmi, bfp):
    mps = race_meters/time_took_last_year
    diff_height = height - past_height
    mps += diff_height*speed_for_every_centimeter
    if 18.5 <= past_bmi < 25:
        if bmi < 18.5 or 25 < bmi:
            mps -= speed_for_every_bmi
        if bmi > 30:
            mps -= speed_for_every_bmi
    else:
        if 18.5 <= bmi < 25:
            mps += speed_for_every_bmi
    return mps

from turtle import *

def visualize(name1, name2):
    players_data_file = pandas.read_excel('runner_data.xlsx', sheet_name='Sheet1')
    p1_data = list(players_data_file[name1])
    p2_data = list(players_data_file[name2])
    player1_mps = mps_calculate(*p1_data)
    player2_mps = mps_calculate(*p2_data)


    speed(10)

    penup()

    # (1)
    trevor = Turtle()
    trevor.color('red')
    trevor.shape('turtle')

    trevor.penup()
    trevor.goto(-150, -250)
    trevor.left(90)
    trevor.pendown()

    bruce = Turtle()
    bruce.color('blue')
    bruce.shape('turtle')

    bruce.penup()
    bruce.goto(150, -250)
    bruce.left(90)
    bruce.pendown()

    for turn in range(1000):
        trevor.forward(player1_mps)
        bruce.forward(player2_mps)

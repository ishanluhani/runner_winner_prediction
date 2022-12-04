from random import random

import pandas

speed_for_every_centimeter = .005
from openpyxl import load_workbook


def mps_calculate(race_meters, time_took_last_year, past_height, height):
    mps = race_meters/time_took_last_year
    diff_height = height - past_height
    mps += diff_height*speed_for_every_centimeter
    return mps

# player1_name = input('First Runner name: ')
# player1_race_last_year = int(input('How many meters race he/she ran last year: '))
# player1_time_took_last_year = float(input('How much time did he/she took last year (in seconds): '))
# player1_past_height = float(input('His/her past year height (in centimeter): '))
# player1_height = float(input('His/her current height (in centimeter): '))
#
# player2_name = input('Second Runner name: ')
# player2_race_last_year = int(input('How many meters race he/she ran last year: '))
# player2_time_took_last_year = float(input('How much time did he/she took last year (in seconds): '))
# player2_past_height = float(input('His/her past year height (in centimeter): '))
# player2_height = float(input('His/her current height (in centimeter): '))



players_data_file = pandas.read_excel('runner_data.xlsx', sheet_name='Sheet1')
p1_data = list(players_data_file['Ishan'])
p2_data = list(players_data_file['Usain'])
player1_mps = mps_calculate(*p1_data)
player2_mps = mps_calculate(*p2_data)

from turtle import *


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
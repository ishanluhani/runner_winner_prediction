from random import random

import pandas

speed_for_every_centimeter = .005
from openpyxl import load_workbook


def mps_calculate(race_meters, time_took_last_year, past_height, height):
    mps = race_meters/time_took_last_year
    diff_height = height - past_height
    mps += diff_height*speed_for_every_centimeter
    return mps

#
#
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

player1_mps = mps_calculate(*list(players_data_file['Ishan']))
player2_mps = mps_calculate(*list(players_data_file['Usain']))
player3_mps = mps_calculate(*list(players_data_file['Nehal']))
player4_mps = mps_calculate(*list(players_data_file['Papa']))


from turtle import *

speed(10)

penup()

# (1)
trevor = Turtle()
trevor.color('red')
trevor.shape('turtle')

trevor.penup()
trevor.goto(-240, -250)
trevor.left(90)
trevor.pendown()

bruce = Turtle()
bruce.color('blue')
bruce.shape('turtle')

bruce.penup()
bruce.goto(-150, -250)
bruce.left(90)
bruce.pendown()

jojo = Turtle()
jojo.color('green')
jojo.shape('turtle')

jojo.penup()
jojo.goto(-60, -250)
jojo.left(90)
jojo.pendown()

gogo = Turtle()
gogo.color('black')
gogo.shape('turtle')

gogo.penup()
gogo.goto(30, -250)
gogo.left(90)
gogo.pendown()

for turn in range(1000):
    trevor.forward(player1_mps - random()/2)
    bruce.forward(player2_mps - random()/2)
    jojo.forward(player3_mps - random()/2)
    gogo.forward(player4_mps - random()/2)
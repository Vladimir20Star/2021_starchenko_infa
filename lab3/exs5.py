from random import randint
import turtle as t

number_of_turtles = 10
steps_of_time_number = 1000
pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
coords = []
speeds = []
for unit in pool:
    unit.penup()
    unit.speed(0)
    x, y = randint(-364, 364), randint(-299, 299)
    coords.append([x, y])
    unit.goto(x, y)
    speeds.append([randint(-5, 5), randint(-5, 5)])

for _ in range(steps_of_time_number):
    for j in range(len(pool)):
        unit = pool[j]
        coords[j][0], coords[j][1] = coords[j][0] + speeds[j][0], coords[j][1] + speeds[j][1]
        unit.goto(coords[j][0], coords[j][1])
        if coords[j][0] <= -365 or coords[j][0] >= 365:
            speeds[j][0] = -speeds[j][0]
        if coords[j][1] <= -300 or coords[j][1] >= 300:
            speeds[j][1] = -speeds[j][1]

import time

from enviroment import *

e = Environment("map.txt")

water = e.world[1][5]
robot1 = e.world[1][7]


for i in range(550):
    print(robot1.water_level)
    # print(e)
    water.act(e, robot1)
    robot1.act(e, robot1)
    time.sleep(0.1)
    print(robot1.display_map())

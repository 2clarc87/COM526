from agent import Agent
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        for cell in percept:
            if utils.is_robot(percept[cell]):
                return "robot"
        else:
            return "idle"

    def act(self, environment, robot):
        cell = self.sense(environment)
        decision = self.decide(cell)

        if decision == "robot":
            robot.fill()


    def __str__(self):
        return '💧'
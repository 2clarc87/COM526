import flame
import water_station
from agent import Agent
import utils
import random
import heapq


class Robot(Agent):

    def __init__(self, position: tuple[int, int]):
        super().__init__(position)
        self.water_level = 5
        self.water_station_location = None
        self.map = [["?" for _ in range(10)] for _ in range(10)]

    def display_map(self):
        out = ""
        for row in self.map:
            for col in row:
                out += f"{col}\t"
            out += "\n"
        return out

    def decide(self, percept: dict[tuple[int, int], ...]):
        if self.water_station_location and self.water_level == 0:
            path = self.calc_path(self.position, self.water_station_location)
            return "move", path[1]
        moves = []
        flames = []
        for cell in percept:
            if utils.is_flame(percept[cell]):
                self.map[cell[1]][cell[0]] = '🔥'
                flames.append(cell)
            elif utils.is_water_station(percept[cell]):
                self.water_station_location = cell
                self.map[cell[1]][cell[0]] = '💧'
            elif percept[cell] == "x":
                self.map[cell[1]][cell[0]] = "x"
            else:
                self.map[cell[1]][cell[0]] = " "
                moves.append(cell)
        if flames and self.water_level != 0:
            return "flame", random.choice(flames)
        return "move", random.choice(moves)

    def act(self, environment, robot):
        cell = self.sense(environment)
        decision = self.decide(cell)

        if decision[0] == "move":
            environment.move_robot(self, decision[1])
            self.position = decision[1]
        elif decision[0] == "flame":
            robot.water_level -= 5
            environment.world[decision[1][1]][decision[1][0]] = " "

    def fill(self):
        self.water_level = 5

    def __str__(self):
        return '🚒'

    # MANHATTAN DISTANCE FUNCTIONS
    def calc_path(self, start, goal):
        p_queue = []
        heapq.heappush(p_queue, (0, start))

        directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }
        predecessors = {start: None}
        g_values = {start: 0}

        while len(p_queue) != 0:
            current_cell = heapq.heappop(p_queue)[1]

            if current_cell == goal:
                return self.get_path(predecessors, start, goal)
            for direction in ["up", "right", "down", "left"]:
                row_offset, col_offset = directions[direction]
                neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)

                if self.viable_move(neighbour[0], neighbour[1]) and neighbour not in g_values:
                    cost = g_values[current_cell] + 1
                    g_values[neighbour] = cost
                    f_value = cost + self.calc_distance(goal, neighbour)
                    heapq.heappush(p_queue, (f_value, neighbour))
                    predecessors[neighbour] = current_cell

    def get_path(self, predecessors, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = predecessors[current]
        path.append(start)
        path.reverse()
        return path

    def viable_move(self, x, y):
        if self.map[y][x] == ' ' or self.map[y][x] == '💧':
            return True
        return False

    def calc_distance(self, point1: tuple[int, int], point2: tuple[int, int]):
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)

    # END OF MANHATTAN DISTANCE FUNCTIONS
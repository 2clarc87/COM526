import utils
import heapq

from utils import manhattan_distance


def a_star(maze, start, goal):
    # Create an empty list tha will act as our priority queue
    priority_queue = []

    # Using heapq.heappush - add the starting node to the queue with a priority of 0
    heapq.heappush(priority_queue, (0, start))

    # Providing some code for you as they will be helpful shortly
    directions = {
        "right": (1, 0),
        "left": (-1, 0),
        "up": (0, -1),
        "down": (0, 1)
    }
    predecessors = {start: None}    # Enables the get_path function to backtrack
    g_values = {start: 0}   # The g score for each cell

    # loop through the queue, this is an infinite loop that will only stop if the queue is empty
    while len(priority_queue) != 0:
        # get this from the priority queue
        cur_f, current_cell = heapq.heappop(priority_queue)

        # Check if the current cell is the goal:
        if current_cell == goal:
            # if it is, run this command:
            return get_path(predecessors, start, goal)

        # Now lets look at where we can move to from the current cell.
        # For each direction do the following:
        for direction in directions:
            # Figure out the coordinates of the neighbouring cell - the offsets are provided above.
            # For example, if the direction is 'up' then you would deduct 1 from the y coordinate
            cur_x, cur_y = current_cell
            x = cur_x + directions[direction][0]
            y = cur_y + directions[direction][1]
            neighbour = (x, y)

            # Check that this neighbouring cell is actually a valid move.
            # An invalid move would be one that goes outside the bounds of the map.
            # A cell that contains an 'x' is also invalid.
            # It should also not consider a cell that already has a value stored in the g_values dict created above
            # If the cell is viable:
            if maze[neighbour[1]][neighbour[0]] != "x" and neighbour not in predecessors:
                # We need to calculate the cost of the move!
                # Our current cell and its cost should be stored in the dictionary g_values
                # Retrieve that value - add 1 to it, and we have our cost for the neighbouring cell
                g_cost = g_values[current_cell] + 1

                # Add the neighbouring cell and its cost to the g_values dictionary,
                # Where the (x, y) coordinates are the key and the cost is the value
                g_values[neighbour] = g_cost

                # Now calculate the H score.
                # In the utils.py file there is a manhatten_distance function.
                # Use this to calculate the distance between the neighbouring cell and the goal.
                # The value it returns will be the H score
                h_cost = manhattan_distance(neighbour, goal)

                # Using that we can calculate the overall F score by adding the cost and the H score
                f_score = g_cost + h_cost

                # Now we have its F-Score we can add this neighbouring cell (a viable move) to our priority queue
                # You should add the cell coords (x, y) to the queue and the prioirty value should be the f-score
                heapq.heappush(priority_queue, (f_score, neighbour))

                # Allows the get_path function to backtrack later, do not change
                predecessors[neighbour] = current_cell
    return None


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


if __name__ == "__main__":
    maze_map = utils.import_maze("mazes/maze1.txt")     # Change the path as required.
    start = utils.locate(maze_map, 's')
    goal = utils.locate(maze_map, 'g')
    # Print out the path returned by the a_star function (after you have completed it)
    print(a_star(maze_map, start, goal))

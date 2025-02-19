import pathfinding
import utils


def display_map(maze):
    for row in maze:
        for item in row:
            print(item, end=" ")
        print()


def show_path(maze, path):
    for move in path[1:-1]:
        maze[move[1]][move[0]] = '#'
        display_map(maze)
        print("\n")


if __name__ == "__main__":
    maze_map = utils.import_maze("mazes/maze4.txt")
    start = utils.locate(maze_map, 's')
    goal = utils.locate(maze_map, 'g')
    display_map(maze_map)
    show_path(maze_map, pathfinding.a_star(maze_map, start, goal))
    print (pathfinding.a_star(maze_map, start, goal))
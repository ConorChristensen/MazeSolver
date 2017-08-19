#Conor Christensen
#Last edited - 15/ 05/17
from maze import Maze

def read_in_maze():
    file = open('maze_eg_1.txt')
    maze = Maze()
    lines = 0
    for line in file:
        line = line.strip('\n')
        this_line = []
        for character in range(len(line)):
            if line[character] == 'S':
                start = [lines, character]
                maze.set_start(start)
            elif line[character] == 'F':
                finish = [lines, character]
                maze.set_finish(finish)
            this_line.append(line[character])
            maze.width = character+1
        maze.append(this_line)
        lines+=1
    maze.height = lines
    maze.generate_partial_solutions()
    file.close()
    return maze

def walk_through_maze(maze):                        #Initiate the stepping through of the maze.
    start = maze.start
    finish = maze.finish
    step(maze, start, start)
    return maze

def step(maze, position, previous):                 #A recursive function that takes the base case as a completed maze.
    if position == maze.finish:
        maze.state = 'complete'
        return position
    if maze.state == 'complete':
        return
    elif maze.partial_solutions[position[0]][position[1]] != []:
        return maze.partial_solutions[position[0]][position[1]]
    else:
        next_moves = where_next(maze, position, previous)
        if len(next_moves) == 0:
            return position
        for i in range(len(next_moves)):
            maze.partial_solutions[position[0]][position[1]].append(next_moves[i])
            step(maze, next_moves[i], position)



def where_next(maze, position, previous):                   #Function evaluates and returns which moves are next possible
                                                            #from the current position.
    next_moves = []
    if position[0] == maze.height-1:
        if position[1] == maze.width-1:
            if maze[position[0]][position[1]-1] == '.' or maze[position[0]][position[1]-1] == 'F':
                next_moves.append([position[0],position[1]-1])
            if maze[position[0]-1][position[1]] == '.' or maze[position[0]-1][position[1]] == 'F':
                next_moves.append([position[0]-1, position[1]])
        elif position[1] == 0:
            if maze[position[0]][position[1]+1] == '.' or maze[position[0]][position[1]+1] == 'F':
                next_moves.append([position[0],position[1]+1])
            if maze[position[0]-1][position[1]] == '.' or maze[position[0]-1][position[1]] == 'F':
                next_moves.append([position[0]-1, position[1]])
        else:
            if maze[position[0]][position[1]+1] == '.' or maze[position[0]][position[1]+1] == 'F':
                next_moves.append([position[0],position[1]+1])
            if maze[position[0]-1][position[1]] == '.' or maze[position[0]-1][position[1]] == 'F':
                next_moves.append([position[0]-1, position[1]])
            if maze[position[0]][position[1]-1] == '.' or maze[position[0]][position[1]-1] == 'F':
                next_moves.append([position[0],position[1]-1])
    elif position[0] == 0:
        if position[1] == maze.width-1:
            if maze[position[0]][position[1]-1] == '.' or maze[position[0]][position[1]-1] == 'F':
                next_moves.append([position[0],position[1]-1])
            if maze[position[0]+1][position[1]] == '.' or maze[position[0]+1][position[1]] == 'F':
                next_moves.append([position[0]+1, position[1]])
        elif position[1] == 0:
            if maze[position[0]][position[1]+1] == '.' or maze[position[0]][position[1]+1] == 'F':
                next_moves.append([position[0],position[1]+1])
            if maze[position[0]+1][position[1]] == '.' or maze[position[0]+1][position[1]] == 'F':
                next_moves.append([position[0]+1, position[1]])
        else:
            if maze[position[0]][position[1]+1] == '.' or maze[position[0]][position[1]+1] == 'F':
                next_moves.append([position[0],position[1]+1])
            if maze[position[0]+1][position[1]] == '.' or maze[position[0]+1][position[1]] == 'F':
                next_moves.append([position[0]+1, position[1]])
            if maze[position[0]][position[1]-1] == '.' or maze[position[0]][position[1]-1] == 'F':
                next_moves.append([position[0],position[1]-1])
    else:
        if position[1] == maze.width-1:
            if maze[position[0]][position[1]-1] == '.' or maze[position[0]][position[1]-1] == 'F':
                next_moves.append([position[0],position[1]-1])
            if maze[position[0]-1][position[1]] == '.' or maze[position[0]-1][position[1]] == 'F':
                next_moves.append([position[0]-1, position[1]])
            if maze[position[0]+1][position[1]] == '.' or maze[position[0]+1][position[1]] == 'F':
                next_moves.append([position[0]+1, position[1]])
        elif position[1] == 0:
            if maze[position[0]][position[1]+1] == '.' or maze[position[0]][position[1]+1] == 'F':
                next_moves.append([position[0],position[1]+1])
            if maze[position[0]-1][position[1]] == '.' or maze[position[0]-1][position[1]] == 'F':
                next_moves.append([position[0]-1, position[1]])
            if maze[position[0]+1][position[1]] == '.' or maze[position[0]+1][position[1]] == 'F':
                next_moves.append([position[0]+1, position[1]])
        else:
            if maze[position[0]][position[1]+1] == '.' or maze[position[0]][position[1]+1] == 'F':
                next_moves.append([position[0],position[1]+1])
            if maze[position[0]-1][position[1]] == '.' or maze[position[0]-1][position[1]] == 'F':
                next_moves.append([position[0]-1, position[1]])
            if maze[position[0]][position[1]-1] == '.' or maze[position[0]][position[1]-1] == 'F':
                next_moves.append([position[0],position[1]-1])
            if maze[position[0]+1][position[1]] == '.' or maze[position[0]+1][position[1]] == 'F':
                next_moves.append([position[0]+1, position[1]])
    for i in range(len(next_moves)):
        if next_moves[i] == maze.finish:
            maze.state = 'complete'
        if next_moves[i] == previous:
            next_moves.pop(i)
            break
    print(position)
    return next_moves

def find_solution(maze, spot, solution = [], forks = [], potential_bans = [], other_bans = []):
    for g in range(len(maze.partial_solutions[spot[0]][spot[1]])):
        if maze.partial_solutions[spot[0]][spot[1]][g] == maze.finish:
            solution.append(maze.finish)
            maze.state = 'complete'
            return
    else:
        is_fork = False
        i=0
        rewind = False
        if len(maze.partial_solutions[spot[0]][spot[1]]) > 1 or spot in forks:
            if spot not in forks:
                forks.append(spot)
            is_fork = True
        while maze.partial_solutions[maze.partial_solutions[spot[0]][spot[1]][i][0]][maze.partial_solutions[spot[0]][spot[1]][i][1]] == [] or maze.partial_solutions[spot[0]][spot[1]][i] in solution or maze.partial_solutions[spot[0]][spot[1]][i] in other_bans:
            if len(maze.partial_solutions[spot[0]][spot[1]]) == 1:
                rewind = True
                break
            else:
                i += 1
        if is_fork:
            potential_bans.append(maze.partial_solutions[spot[0]][spot[1]][i])
        if not rewind:
            solution.append(maze.partial_solutions[spot[0]][spot[1]][i])
            find_solution(maze, maze.partial_solutions[spot[0]][spot[1]][i], solution, forks, potential_bans)
        else:
            how_many_pops = 0

            for q in range(len(maze.partial_solutions[spot[0]][spot[1]])):
                if maze.partial_solutions[forks[-1][0]][forks[-1][1]][q] == potential_bans[-1]:
                    maze.partial_solutions[forks[-1][0]][forks[-1][1]].pop(q)
                    potential_bans.pop()
            spot = forks[-1]
            j=1
            while len(maze.partial_solutions[spot[0]][spot[1]]) == 0:
                spot = forks[-j]
                j+=1
            for p in range(1, len(solution) - 1):
                if solution[-p] == spot:
                    how_many_pops = p
                    break
            for n in range(how_many_pops-1):
                other_bans.append(solution[-n])
                solution.pop()
            find_solution(maze, spot, solution, forks, potential_bans, other_bans)
    return solution


def write_in_solution(solution):
    file = open('maze_eg_1.txt', 'r')
    lines = []
    current_line = 0
    for line in file:
        lines.append([])
        for characters in range(len(line)):
            if [current_line, characters] in solution or line[characters] == 'S':
                lines[current_line].append('o')
            else:
                lines[current_line].append(line[characters])
        current_line += 1
    file.close()
    file = open('solution.txt', 'w')
    for i in range(len(lines)):
        for p in range(len(lines[i])):
            file.write(str(lines[i][p]))

maze = read_in_maze()
walk_through_maze(maze)
solution = find_solution(maze, maze.start)
write_in_solution(solution)


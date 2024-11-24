from Stack import Stack

def solveMaze(maze, startX, startY):
    stack = Stack()
    stack.push([startX, startY])
    step = 1
    directions = [(-1, 0), (0, -1),(1, 0), (0, 1)]

    while not stack.isEmpty():
        x, y = stack.peek()

        if maze[x][y] == 'G':
            return True
        if maze[x][y] == ' ':
            maze[x][y] = step
            step += 1

        moved = False
        for direction in directions:
            nextX = x + direction[0]
            nextY = y + direction[1]

            if maze[nextX][nextY] == ' ' or maze[nextX][nextY] == 'G':
                stack.push([nextX, nextY])
                moved = True
                break
        if not moved:
            stack.pop()

    return False


def printMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            print("|{:<2}".format(maze[row][col]), sep='',end='')
        print("|")
    print()
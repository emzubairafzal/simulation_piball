def grid_size():
    score, total = 0, 0
    m, n = [int(y) for y in input("Enter values of m and n : ").split()]
    if 2 < m < 51 and 2 < n < 51:
        grid = [[0] * n for _ in range(m)]
        for item in grid:
            print(item)
        bumpers_input(m, n, grid, score)
    else:
        print("Values are not in range please try again ...")
        grid_size()


def bumpers_input(m, n, grid, score):
    wall_cost = int(input("Enter the cost of hitting a wall : "))
    p = int(input("Enter the number of bumpers : "))
    if p >= 0:
        for i in range(p):
            x, y, value, cost = [
                int(i) for i in input("Enter x,y axis value and cost of bumper respectively : ").split()]
            print(i)
            if 0 <= x <= m and 0 <= y <= n:
                grid[x][y] = "B"
                for item in grid:
                    print(item)
            else:
                print("Please enter values of x and y axis in range...")
                bumpers_input(m, n, grid, score)
        balls_input(grid, n, y, m, x, wall_cost, score, value, cost)
    else:
        print("Please enter correct number of bumpers ")
        bumpers_input(m, n, grid, score)


def direction(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost):
    if direc == 0:
        move_right(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
    if direc == 1:
        move_up(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
    if direc == 2:
        move_left(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
    if direc == 3:
        move_down(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)


def move_right(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost):
    for count in reversed(range(lifetime)):
        print("moving right")
        if is_wall_right(direc, by, n):
            score = score + wall_cost
            lifetime = lifetime - wall_cost
            if lifetime > 0:
                direc = 3
                move_down(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
            else:
                print("Game is over ... ")
                break
        elif is_bumper(bx, by, grid, y, x):
            score = score + value
            lifetime = lifetime - cost
            grid[bx][by] = "B"
            grid[bx + 1][by] = 1
            bx += 1
            direc = 3
            for j in grid:
                print(j)
            print("\n")
            move_down(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
        elif lifetime > 0:
            grid[bx][by] = 0
            grid[bx][by + 1] = 1
            lifetime -= 1
            by += 1
            for j in grid:
                print(j)
            print("\n")
        else:
            print("Game is over ... ")
            break
    print("The score of ball is ", score)
    exit()


def move_up(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost):
    for count in reversed(range(lifetime)):
        print("moving up")
        if is_wall_up(direc, bx):
            score = score + wall_cost
            lifetime = lifetime - wall_cost
            if lifetime > 0:
                direc = 0
                move_right(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
            else:
                print("Game is over ... ")
                break
        elif is_bumper( bx, by, grid, y, x):
            score = score + value
            lifetime = lifetime - cost
            grid[bx][by] = "B"
            grid[bx][by + 1] = 1
            by += 1
            direc = 0
            for j in grid:
                print(j)
            print("\n")
            move_right(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
        elif lifetime > 0:
            grid[bx][by] = 0
            grid[bx - 1][by] = 1
            lifetime -= 1
            bx -= 1
            for j in grid:
                print(j)
            print("\n")
        else:
            print("Game is over ... ")
            break
    print("The score of ball is ", score)
    exit()


def move_left(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost):
    for count in reversed(range(lifetime)):
        print("moving left")
        if is_wall_left(direc, by):
            score = score + wall_cost
            lifetime = lifetime - wall_cost
            if lifetime > 0:
                direc = 1
                move_up(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
            else:
                print("Game is over ... ")
                break
        elif is_bumper(bx, by, grid, y, x):
            score = score + value
            lifetime = lifetime - cost
            grid[bx][by] = "B"
            grid[bx - 1][by] = 1
            bx -= 1
            direc = 1
            for j in grid:
                print(j)
            print("\n")
            move_up(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
        elif lifetime > 0:
            grid[bx][by] = 0
            grid[bx][by - 1] = 1
            lifetime -= 1
            by -= 1
            for j in grid:
                print(j)
            print("\n")
        else:
            print("Game is over ... ")
            break
    print("The score of ball is ", score)
    exit()


def move_down(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost):
    for count in reversed(range(lifetime)):
        print("moving down")
        if is_wall_down(direc, bx, m):
            score = score + wall_cost
            lifetime = lifetime - wall_cost
            if lifetime > 0:
                direc = 2
                move_left(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
            else:
                print("Game is over ... ")
                break
        elif is_bumper(bx, by, grid, y, x):
            score = score + value
            lifetime = lifetime - cost
            grid[bx][by] = "B"
            grid[bx][by - 1] = 1
            by -= 1
            direc = 2
            for j in grid:
                print(j)
            print("\n")
            move_left(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)
        elif lifetime > 0:
            grid[bx][by] = 0
            grid[bx + 1][by] = 1
            lifetime -= 1
            bx += 1
            for j in grid:
                print(j)
            print("\n")
        else:
            print("Game is over ... ")
            break
    print("The score of ball is ", score)
    exit()


def is_wall_right(direc, by, n):
    if by == n-1 and direc == 0:
        print("ball hits the wall ... ")
        return True
    else:
        return False


def is_wall_down(direc, bx, m):
    if bx == m-1 and direc == 3:
        print("ball hits the wall ... ")
        return True
    else:
        return False


def is_wall_left(direc, by):
    if by == 0 and direc == 2:
        print("ball hits the wall ... ")
        return True
    else:
        return False


def is_wall_up(direc, bx):
    if bx == 0 and direc == 1:
        print("ball hits the wall ... ")
        return True
    else:
        return False


def is_bumper(bx, by, grid, y, x):
    if grid[bx][by] == grid[x][y]:
        print("ball hits the bumper ... ")
        return True
    else:
        return False


def balls_input(grid, n, y, m, x, wall_cost, score, value, cost):
    bx, by, direc, lifetime = [
        int(x) for x in input("Enter bx,by axis direction and lifetime of balls respectively : ").split()]
    bx = int(bx)
    by = int(by)
    direc = int(direc)
    if lifetime > 0:
        lifetime = int(lifetime)
    else:
        print("Lifetime must be greater than zero ... ")
        balls_input(grid, n, y, m, x, wall_cost, score, value, cost)
    grid[bx][by] = 1
    print("The ball is placed at: ")
    for item in grid:
        print(item)
    print("\n")
    direction(lifetime, bx, by, grid, y, direc, n, m, x, wall_cost, score, value, cost)


grid_size()

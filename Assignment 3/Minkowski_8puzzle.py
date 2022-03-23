import copy


class Node:
    def __init__(self, matrix, parent):
        self.matrix = matrix
        self.parent = parent
        self.heuristic = -1

    # checks if node already exists in closed(visited nodes)
    def not_in(self, closed):
        for i in closed:
            if self.matrix == i.matrix:
                return False
        return True

    @staticmethod
    def coordinates(num, child, goal):
        r_child, c_child, r_goal, c_goal = 0, 0, 0, 0
        for i in range(0, 3):
            for j in range(0, 3):
                # finding num in current node
                if child.matrix[i][j] == num:
                    r_child = i; c_child = j
                if goal[i][j] == num:
                    r_goal = i; c_goal = j
        return r_child, c_child, r_goal, c_goal

    @staticmethod
    def minkowski(child, goal, p):
        heuristic = 0
        for i in range(1, 9):
            r_child, c_child, r_goal, c_goal = Node.coordinates(i, child, goal)
            heuristic += (abs((r_child - r_goal)**p) + abs((r_child - r_goal)**p))**(1/p)
        return heuristic

    # finds zero
    def find_zero(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.matrix[i][j] == 0:
                    return i, j

    # moves zero to the right
    def right(self, zero_r, zero_c):
        child = copy.deepcopy(self)
        # swapping of values
        child.matrix[zero_r][zero_c] = child.matrix[zero_r][zero_c + 1]
        child.matrix[zero_r][zero_c+1] = 0
        return child

    # moves zero to the left
    def left(self, zero_r, zero_c):
        child = copy.deepcopy(self)
        # swapping of values
        child.matrix[zero_r][zero_c] = child.matrix[zero_r][zero_c-1]
        child.matrix[zero_r][zero_c-1] = 0
        return child

    def up(self, zero_r, zero_c):
        child = copy.deepcopy(self)
        child.matrix[zero_r][zero_c] = child.matrix[zero_r-1][zero_c]
        child.matrix[zero_r-1][zero_c] = 0
        return child

    def down(self, zero_r, zero_c):
        child = copy.deepcopy(self)
        child.matrix[zero_r][zero_c] = child.matrix[zero_r+1][zero_c]
        child.matrix[zero_r+1][zero_c] = 0
        return child

    def move_zero(self, open, closed, goal):
        # print(f"matrix = {self.matrix}")
        if self.matrix == goal:
            return len(closed), self

        zero_r, zero_c = self.find_zero()

        # check if right movement is possible
        if zero_c != 2:
            # print(f"right {self.matrix}")
            child_right = self.right(zero_r, zero_c)
            child_right.heuristic = Node.minkowski(child_right, goal, p)
            child_right.parent = self

            if Node.not_in(child_right, closed):
                closed.append(child_right)
                open.append(child_right)

            if child_right.matrix == goal:
                return len(closed), child_right

        # check if left movement is possible
        if zero_c != 0:
            # print(f"left {self.matrix}")
            child_left = self.left(zero_r, zero_c)
            child_left.heuristic = Node.minkowski(child_left, goal, p)
            child_left.parent = self

            if Node.not_in(child_left, closed):
                closed.append(child_left)
                open.append(child_left)

            if child_left.matrix == goal:
                return len(closed), child_left

        # check if up movement is possible
        if zero_r != 0:
            # print(f"up {self.matrix}")
            # print(self.matrix)
            child_up = self.up(zero_r, zero_c)
            child_up.heuristic = Node.minkowski(child_up, goal, p)
            child_up.parent = self

            if Node.not_in(child_up, closed):
                closed.append(child_up)
                open.append(child_up)

            if child_up.matrix == goal:
                return len(closed), child_up

        # checks if down movement is possible
        if zero_r != 2:
            # print(f"down {self.matrix}")
            child_down = self.down(zero_r, zero_c)
            child_down.heuristic = Node.minkowski(child_down, goal, p)
            child_down.parent = self

            if Node.not_in(child_down, closed):
                closed.append(child_down)
                open.append(child_down)

            if child_down.matrix == goal:
                return len(closed), child_down

        open.sort(key=lambda x: x.heuristic)

        if open:
            # print(open)
            # print(f"closed = {closed}")
            return open.pop(0).move_zero(open, closed, goal)
        else:
            return False

    @staticmethod
    def print_matrix(output):
        for i in output:
            for j in i:
                print(j)
            print("-"*10)


if __name__ == "__main__":
    closed = []
    open = []
    initial_state = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
    goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    ans = []
    p = 1  # minkowski distance variable

    print("-" * 25)
    print("Name: Shivam Taneja")
    print("Roll Number: 102003244")
    print("-" * 25)

    start = Node(initial_state, [0])
    open.append(start)
    closed.append(start)

    iterations, nodes = start.move_zero(open, closed, goal)
    if iterations > 0:
        print(f"Number of iterations to reach solution {iterations}")
        print("Nodes visited: ")
        while nodes != [0]:
            ans.append(nodes.matrix)
            nodes = nodes.parent
        ans.reverse()
        start.print_matrix(ans)
    else:
        print("No solution found")


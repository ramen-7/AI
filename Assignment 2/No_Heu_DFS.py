import copy


class Node:
    def __init__(self, matrix, parent):
        self.matrix = matrix
        self.parent = parent

    # checks if node already exists in closed(visited nodes)
    def not_in(self, closed):
        for i in closed:
            if self.matrix == i.matrix:
                return False
        return True

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
            child_right.parent = self

            if Node.not_in(child_right, closed):
                closed.insert(0, child_right)
                open.insert(0, child_right)

            if child_right.matrix == goal:
                return len(closed), child_right

        # check if left movement is possible
        if zero_c != 0:
            # print(f"left {self.matrix}")
            child_left = self.left(zero_r, zero_c)
            child_left.parent = self

            if Node.not_in(child_left, closed):
                closed.insert(0, child_left)
                open.insert(0, child_left)

            if child_left.matrix == goal:
                return len(closed), child_left

        # check if up movement is possible
        if zero_r != 0:
            # print(f"up {self.matrix}")
            # print(self.matrix)
            child_up = self.up(zero_r, zero_c)
            child_up.parent = self

            if Node.not_in(child_up, closed):
                closed.insert(0, child_up)
                open.insert(0, child_up)

            if child_up.matrix == goal:
                return len(closed), child_up

        # checks if down movement is possible
        if zero_r != 2:
            # print(f"down {self.matrix}")
            child_down = self.down(zero_r, zero_c)
            child_down.parent = self

            if Node.not_in(child_down, closed):
                closed.insert(0, child_down)
                open.insert(0, child_down)

            if child_down.matrix == goal:
                return len(closed), child_down

        if open:
            # print(open)
            # print(f"closed = {closed}")
            return open.pop(0).move_zero(open, closed, goal)
        else:
            return False

    def print_matrix(self, output):
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

    print("-" * 25)
    print("Name: Shivam Taneja")
    print("Roll Number: 102003244")
    print("-" * 25)

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


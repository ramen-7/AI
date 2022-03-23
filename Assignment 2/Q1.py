import copy

filled = [4, 3]


# max[0] = input("Input max value of jug 1")
# max[1] = input("Input max value of jug 2")


class Node:
    jugs = []
    parent = []

    def __init__(self, jugs, parent):
        self.jugs = jugs
        self.parent = parent

    # checks if node already exists in closed(visited nodes)
    def not_in(self, closed):
        for node in closed:
            if self.jugs == node.jugs:
                return False
        return True

    def filling_jugs(self, open, closed, goal):
        # returns the no. of visited nodes, and the node where we found the goal state
        if self.jugs == goal:
            return len(closed), self

        # fills the first jug
        if self.jugs[0] != filled[0]:
            # print("Fills jug 1")
            child = copy.deepcopy(self)  # creates a child of current node
            child.jugs[0] = filled[0]
            child.parent = self  # assigns current node as parent to child

            # if node has not been visited before, add it to closed and open
#             # print(f"Check = {Node.not_in(child, closed)}")
            if Node.not_in(child, closed):
                open.append(child)
                closed.append(child)

            # we return the child where we found the goal state
            if child.jugs == goal:
                return len(closed), child

        # fills the second jug
        if self.jugs[1] != filled[1]:
            # print("Fills jug 2")
            child = copy.deepcopy(self)
            child.jugs[1] = filled[1]
            child.parent = self

            # print(f"Check = {Node.not_in(child, closed)}")
            if Node.not_in(child, closed):
                open.append(child)
                closed.append(child)

            if child.jugs == goal:
                return len(closed), child

        # empties first jug
        if self.jugs[0] != 0:
            child = copy.deepcopy(self)  # creates a child of current node
            child.jugs[0] = 0
            child.parent = self  # assigns current node as parent of child

            # if node was not visited before we are adding it to closed and open
            # print(f"Check = {Node.not_in(child, closed)}")
            if Node.not_in(child, closed):
                open.append(child)
                closed.append(child)

            if child.jugs == goal:
                return len(closed), child

        # empties jug 2
        if self.jugs[1] != 0:
            child = copy.deepcopy(self)  # creates a child of current node
            child.jugs[1] = 0
            child.parent = self  # assigns current node as parent of child

            # if node was not visited before we are adding it to closed and open
            # print(f"Check = {Node.not_in(child, closed)}")
            if Node.not_in(child, closed):
                open.append(child)
                closed.append(child)

            if child.jugs == goal:
                return len(closed), child

        # Transfer from jug 1 to 2
        if self.jugs[0] != 0 or self.jugs[1] != filled[1]:
            # print("Transfers from jug 1 to 2")
            #  checks if jug 1 is empty and if jug 2 is filled to the max
            child = copy.deepcopy(self)  # creates a child
            # checks if all of jug 1 can be transferred to jug 2 or not
            child.jugs[0] = max(0, self.jugs[0] - (filled[1] - self.jugs[1]))
            # checks if jug 2 is full or equal to that what was added from jug 1
            child.jugs[1] = min(filled[1], self.jugs[0] + self.jugs[1])
            child.parent = self

            # print(f"Check = {Node.not_in(child, closed)}")
            if Node.not_in(child, closed):
                open.append(child)
                closed.append(child)

            if child.jugs == goal:
                return len(closed), child

        # Transfer from jug 2 to 1
        if self.jugs[1] != 0 or self.jugs[0] != filled[0]:
            # print("Transfers from jug 2 to 1")
            # checks if jug 2 is empty and if jug 1 is filled to the max
            child = copy.deepcopy(self)
            # checks if all of jug 2 can be transferred to jug 1 or not
            child.jugs[1] = max(0, self.jugs[1] - (filled[0] - self.jugs[0]))
            # checks if jug 1 is full or equal to that what was added from jug 2
            child.jugs[0] = min(filled[0], self.jugs[0] + self.jugs[1])
            child.parent = self

            # print(f"Check = {Node.not_in(child, closed)}")
            if Node.not_in(child, closed):
                open.append(child)
                closed.append(child)

            if child.jugs == goal:
                return len(closed), child

        # checks if there is any node in open
        if open:
            return open.pop(0).filling_jugs(open, closed, goal)
        else:
            return False


if __name__ == "__main__":
    closed = []
    open = []
    goal = [2, 0]
    ans = []

    start = Node([0, 0], [-1, -1])

    open.append(start)
    closed.append(start)

    iterations, nodes = start.filling_jugs(open, closed, goal)
    print("Closed: ")
    # for i in closed:
    #     print(i.jugs)

    if iterations > 0:
        print("-" * 25)
        print("Name: Shivam Taneja")
        print("Roll Number: 102003244")
        print("-" * 25)

        print(f"Number of iterations to reach solution {iterations}")
        print("Nodes visited: ")
        while nodes != [-1, -1]:
            ans.append(nodes.jugs)
            nodes = nodes.parent
        ans.reverse()
        for i in ans:
            print(i)
            print("-" * 5)
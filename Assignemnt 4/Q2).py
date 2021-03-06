import copy


class MyBlockProblem:
    def __init__(self, start, goal):
        self.currentState = start
        self.goalState = goal
        self.prevState = None

    def isGoalReached(self):
        for i in range(0, 4):
            if self.currentState[i] == goal:
                return True

        return False

    def displayState(self):
        for i in range(0, 4):
            if self.currentState[i] != []:
                print(f"Stack {i}:")
                print(self.currentState[i])
                print("-" * 10)
        print("*" * 20)

    def _eq_(self, other):
        return self.currentState == other.currentState

    def movefromStackXtoStackY(self, x, y):
        if self.currentState[x] != [] and len(self.currentState[y]) != 4:
            self.prevState = copy.deepcopy(self)
            block = self.currentState[x].pop()
            self.currentState[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self):
        stateList = []
        for i in range(0, 4):
            for j in range(0, 4):
                copy_state = copy.deepcopy(self)
                if i != j and copy_state.movefromStackXtoStackY(i, j):
                    stateList.append(copy_state)


        return stateList

    def heuristic(self):
        value = 0

        for i in range(0, 4):
            goalBlock = self.goalState[i]
            goalBlockIndex = i

            for j in range(0, 4):
                flag = 0
                if self.currentState[j] != []:
                    for k in range(0, len(self.currentState[j])):
                        if self.currentState[j][k] == goalBlock:
                            currentBlockIndexX = j
                            currentBlockIndexY = k
                            flag = 1
                            break

                if flag == 1:
                    flag = 0
                    break

            if currentBlockIndexY != goalBlockIndex:
                value -= currentBlockIndexY
            else:
                value += currentBlockIndexY

        return value


def constructPath(goalState):
    print("Displaying path from start to goal")
    while goalState:
        goalState.displayState()
        goalState = goalState.prevState

    return 1


def HillClimbing(startState):
    open = []
    closed = []

    # Step 1
    open.append(startState)

    # Step 2
    returnVal = 0
    while open:

        #
        thisState = open.pop(0)
        thisState.displayState()

        # Step 4
        if thisState.isGoalReached():
            print("Goal state found.. stopping search")
            returnVal = constructPath(thisState)
            break

        # Step 5
        nextStates = thisState.possibleNextStates()

        # Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                # If next state is better than current state(higher heuristic value is better)
                if eachState.heuristic() > thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)

    if returnVal != 1:
        print("Error: Local Maxima")


if __name__ == "__main__":
    print("-" * 25)
    print("Name: Shivam Taneja")
    print("Roll Number: 102003244")
    print("-"*25)
    start = [[2, 3, 4, 1], [], [], []]
    goal = [1, 2, 3, 4]
    problem = MyBlockProblem(start, goal)
    HillClimbing(problem)
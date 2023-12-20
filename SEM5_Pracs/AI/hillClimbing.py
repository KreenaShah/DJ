import copy
visited_states = []

def heuristic(currentState, goalState):
    goal = goalState[3]
    val = 0
    for i in range(len(currentState)):
        checkValue = currentState[i]
        if len(checkValue) > 0:
            for j in range(len(checkValue)):
                if checkValue[j] != goal[j]:
                    val -= j
                else:
                    val += j
    return val

def generate_next(currentState, heuristicVal, goalState):
    global visited_states
    state = copy.deepcopy(currentState)
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            print("jiss element ke sath kide krne haii",elem)
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                    print(f'this is the new state for test {temp1}')
                    if temp1 not in visited_states:
                        currentH = heuristic(temp1, goalState)
                        if currentH > heuristicVal:
                            child = copy.deepcopy(temp1)
                            print("Returning this state : ",child,"\n")
                            return child
    return 0

def solution(initialState, goalState):
    global visited_states
    if initialState == goalState:
        print('Solution found. Goal State : ',goalState)
        return
    current_state = copy.deepcopy(initialState)
    while True:
        visited_states.append(copy.deepcopy(current_state))
        heuristicVal = heuristic(current_state, goalState)
        print("Current State :",current_state, '||', "Heuristic :",heuristicVal)
        child = generate_next(current_state, heuristicVal, goalState)
        if child == 0:
            print('Final state : ', current_state)
            return
        current_state = copy.deepcopy(child)

def solver():
    initialState = [[], [], [], ['B', 'C', 'D', 'A']]
    goalState = [[], [], [], ['A', 'B', 'C', 'D']]
    print('States : Heuristic Function Value')
    solution(initialState, goalState)           

if __name__ == "__main__":
    solver()
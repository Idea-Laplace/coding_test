def solution(priorities, location):
    tuples = list(enumerate(priorities))
    stack = []
    while tuples:
        if tuples[0][1] == max(tuples, key=lambda x: x[1])[1]:
            stack.append(tuples.pop(0))
        else:
            tuples.append(tuples.pop(0))
    order = [stack[i][0] for i in range(len(stack))]
    return order.index(location) + 1


print(solution([2, 1, 3, 2], 2))

from itertools import permutations as pmt
def solution(numbers):
    per = set()
    for i in range(1, len(numbers)+1):
        per = per|set(map(''.join, pmt(numbers, i)))
    int_form = {int(str) for str in per}
    answer = len(int_form)
    for element in int_form:
        for num in range(2, max(element,3)):
            if element == 2:
                break
            if element % num == 0 or element == 1:
                answer -= 1
                break
    return answer
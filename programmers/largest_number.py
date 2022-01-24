def solution(numbers):
    class StrCompare():
        def __init__(self, item):
            self.data = item

        def __gt__(self, other):
            if self.data + other.data >= other.data + self.data:
                return True
            return False

    answer = ''
    for idx in range(len(numbers)):
        numbers[idx] = StrCompare(str(numbers[idx]))

    numbers.sort()

    for idx in range(len(numbers)):
        answer += numbers[len(numbers) - idx - 1].data
    if answer.startswith('0'):
        return '0'

    return answer


k = solution([2, 10, 81, 542])
print(k)

from itertools import permutations as per
import my_func as rep
# Permutation의 구현, n길이 array의 r개 선택의 경우

def permutation(array: str, r = 1) -> list: #내가 짠 코드
    if r > len(array):
        raise IndexError

    array = list(array)
    step = 1  # Increases until step == r
    memo = {} # For memo
    # Case of r == 1
    ways = []
    for idx in range(len(array)):
        c_arr = array[:]
        ways.append((c_arr.pop(idx), c_arr))
    memo[1] = ways

    # For cases of r > 1
    while step < r:
        ways = []
        for tuple in memo[step]:
            for idx in range(len(tuple[1])):
                c_arr = tuple[1][:]
                ways.append((tuple[0] + c_arr.pop(idx), c_arr))
        step += 1
        memo[step] = ways
    ans = [v[0] for v in memo[r]]

    return ans

def list_per(char: str) -> list:  #itertools 모튤을 사용
    return list(map(''.join, per(char)))


def permute(arr): #github 함수
    result = arr[:] # array 보존
    status = [0] * len(arr)
    i = 0
    while i < len(arr):
        if status[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[status[i]], arr[i] = arr[i], arr[status[i]]
            result.append(arr[:])
            status[i] += 1
            i = 0
        else:
            status[i] = 0
            i += 1
    return list(map(''.join, result))

if __name__ == '__main__':
    num = '123456789ab'
    for i in range(4,6):
        print(f'Level {i}')
        r1 = rep.lead_time(list_per, num[:i])
        r2 = rep.lead_time(permute,list(num[:i]))
        r3 = rep.lead_time(permutation, num[:i], i)
        print()

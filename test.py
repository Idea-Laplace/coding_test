import random as r
import time

tick = int(input(">Number of which you want to loop: "))
loop = 0


def deco(function):
    def nested(phone_book):
        start = time.time()
        function(phone_book)
        end = time.time()
        print(f"lead time: {end - start}sec")

    return nested


@deco
def solution(phone_book):
    ph_len = sorted(list(set([len(phone_book[i]) for i in range(len(phone_book))])))
    for length in ph_len:
        sample = [phone_book[i] for i in range(len(phone_book)) if len(phone_book[i]) == length]
        inspect = [phone_book[i][0:length] for i in range(len(phone_book)) if len(phone_book[i]) > length]
        if set(sample) & set(inspect):
            print("result: False.")
            return False

    print("result: True")
    return True


@deco
def solution2(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            print("result: False.")
            return False
    print("result: True")
    return True


while loop < tick:

    list_phone = []
    rand = r.randrange(1, 1000000)
    while len(list_phone) <= rand:
        list_phone.append(str(r.randrange(10 ** 19)))

    list_phone = list(set(list_phone))

    print("="*40, end="\n\n")
    print(f"Try: {loop + 1}\n")
    print("solution1")
    solution(list_phone)
    print()
    print("solution2")
    solution2(list_phone)
    print()
    loop += 1

input()

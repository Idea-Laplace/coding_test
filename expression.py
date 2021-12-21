import time as t
import os

loop = True
while loop:
    # Input
    N = input(">>insert a material number N: ")
    if not N.isdigit():
        print("Insert \'integers\' of 1 digit")
        continue
    elif int(N) != float(N):
        print("Insert \'integers\' of 1 digit")
        continue
    elif int(N) not in range(1, 10):
        print("Insert integers of \'1 digit\'")
        continue
    else:
        N = int(N)

    while True:
        number = input(">>Insert a number to express by N: ")
        if not number.isdigit():
            print("Insert a \'positive integer\'")
            continue
        elif int(number) != float(number):
            print("Insert an \'integer\'")
            continue
        else:
            number = int(number)
            break


    # Definition
    def solution(N, number):
        ans = 2
        deg = 111
        # int
        all = [[], [N], [11 * N, N + N, N * N, 1, 0]]
        # character
        all_chr = [[], [f"{N}"], [f"{N}" * 2, f"{N}+{N}", f"{N}*{N}", f"{N}/{N}", f"{N}-{N}"]]

        # trivial cases
        if number == N:
            return 1
        if number in all[2]:
            return 2

        while number not in all[ans]:
            ans += 1
            if ans == 8:
                return 0, [f"Cannot be expressed by {N} less than 8 numbers"]
            all.append([])
            all_chr.append([])
            for i in range(1, ans):
                # Actual calculation
                p = [all[i][j] + all[ans - i][k] for j in range(len(all[i])) for k in
                     range(len(all[ans - i]))]
                m = [all[i][j] * all[ans - i][k] for j in range(len(all[i])) for k in
                     range(len(all[ans - i]))]
                mi = [all[i][j] - all[ans - i][k] for j in range(len(all[i])) for k in
                      range(len(all[ans - i]))]
                d = [all[i][j] / all[ans - i][k] for j in range(len(all[i])) for k in
                     range(len(all[ans - i])) if all[ans - i][k] != 0]

                all[ans] = list(set(all[ans] + p + m + mi + d))

                # character part
                p_chr = ["(" + all_chr[i][j] + ")" + "+" + "(" + all_chr[ans - i][k] + ")" for j in
                         range(len(all_chr[i])) for k in range(len(all_chr[ans - i]))]
                m_chr = ["(" + all_chr[i][j] + ")" + "*" + "(" + all_chr[ans - i][k] + ")" for j in
                         range(len(all_chr[i])) for k in range(len(all_chr[ans - i]))]
                mi_chr = ["(" + all_chr[i][j] + ")" + "-" + "(" + all_chr[ans - i][k] + ")" for j in
                          range(len(all_chr[i])) for k in range(len(all_chr[ans - i]))]
                d_chr = ["(" + all_chr[i][j] + ")" + "/" + "(" + all_chr[ans - i][k] + ")" for j in
                         range(len(all_chr[i])) for k in range(len(all_chr[ans - i])) if eval(all_chr[ans - i][k]) != 0]

                all_chr[ans] = list(set(all_chr[ans] + p_chr + m_chr + mi_chr + d_chr))

            all[ans] = all[ans] + [deg * N]
            all_chr[ans] = all_chr[ans] + [str(N) * ans]
            deg = 10 * deg + 1

        expression = [all_chr[ans][i] for i in range(len(all_chr[ans])) if eval(all_chr[ans][i]) == number]
        return ans, expression


    start = t.time()
    print(solution(N, number), end="\n")
    end = t.time()
    print("Lead time:", round(end - start, 3), "sec")

    while True:
        sel = input("> Loop this program? (y/n): ")
        if sel not in ["Y", "y", "N", "n"]:
            print("> input y or n.")
        elif sel.lower() == 'y':
            os.system("cls")
            break
        else:
            input(">>Press any button to terminate this program.")
            loop = False
            break

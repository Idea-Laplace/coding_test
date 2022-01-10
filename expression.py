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
        all = [set(), {N}, {11 * N, N + N, N * N, 1, 0}]
        # character
        all_chr = [set(), {f"{N}"}, {f"{N}" * 2, f"{N}+{N}", f"{N}*{N}", f"{N}/{N}", f"{N}-{N}"}]

        # trivial cases
        if number == N:
            return 1, N
        if number in all[2]:
            expression = [expr for expr in all_chr[2] if eval(expr) == number]
            return 2, expression

        while number not in all[ans]:
            ans += 1
            if ans == 8:
                return 0, f"Cannot be expressed by {N} less than or equal to 7 numbers"
            all.append(set())
            all_chr.append(set())
            for i in range(1, ans):
                # Actual calculation
                p = {l_value + r_value
                     for l_value in all[i]
                     for r_value in all[ans - i]}
                m = {l_value * r_value
                     for l_value in all[i]
                     for r_value in all[ans - i]}
                mi = {l_value - r_value
                     for l_value in all[i]
                     for r_value in all[ans - i]}
                d = {l_value / r_value
                     for l_value in all[i]
                     for r_value in all[ans - i]
                     if r_value  != 0}

                all[ans].update(p | m | mi | d | {deg * N})

                # character part
                p_chr = {f"({l_value})+({r_value})"
                         for l_value in all_chr[i]
                         for r_value in all_chr[ans - i]}
                m_chr = {f"({l_value})*({r_value})"
                         for l_value in all_chr[i]
                         for r_value in all_chr[ans - i]}
                mi_chr = {f"({l_value})-({r_value})"
                         for l_value in all_chr[i]
                         for r_value in all_chr[ans - i]}
                d_chr = {f"({l_value})/({r_value})"
                         for l_value in all_chr[i]
                         for r_value in all_chr[ans - i]
                         if eval(r_value) != 0}

                all_chr[ans].update(p_chr | m_chr | mi_chr | d_chr | {str(N)*ans})

            deg = 10 * deg + 1

        expression = [expr for expr in all_chr[ans] if eval(expr) == number]
        return ans, expression


    start = t.time()
    print(solution(N, number))
    end = t.time()
    print("Lead time:", end - start, "sec")

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
# Modules
import os
import re
import time
import keyboard as k
import postfix as p

# Variables
loop = True
Up = 72
Down = 80
Left = 75
Right = 77
arrow_0 = [' 7 ', ' 8 ', ' 9 ', ' Backspace ', ' CE ']
arrow_1 = [' 4 ', ' 5 ', ' 6 ', ' + ', ' - ']
arrow_2 = [' 1 ', ' 2 ', ' 3 ', ' * ', ' / ']
arrow_3 = [' ( ', ' 0 ', ' ) ', ' . ', ' = ']
arrow = [arrow_0, arrow_1, arrow_2, arrow_3]

#Actual Calculator
def calculator():
    formula = ''
    position = None
    print("\n\n\n")
    print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
    for arrow_list in arrow:
        for value in arrow_list:
            print(value, end=' ')
        print()

    #Key operations
    while loop:
        if k.is_pressed(Up):
            os.system('cls')
            if not position:
                position = [3, 1]
                arrow[position[0]][position[1]] = '{' + arrow[position[0]][position[1]].strip() + '}'
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)
            else:
                arrow[position[0]][position[1]] = re.sub('[{}]', ' ', arrow[position[0]][position[1]])
                position[0] = (position[0] - 1) % 4
                arrow[position[0]][position[1]] = '{' + arrow[position[0]][position[1]].strip() + '}'
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)

        if k.is_pressed(Down):
            os.system('cls')
            if not position:
                position = [0, 1]
                arrow[position[0]][position[1]] = '{' + arrow[position[0]][position[1]].strip() + '}'
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)
            else:
                arrow[position[0]][position[1]] = re.sub('[{}]', ' ', arrow[position[0]][position[1]])
                position[0] = (position[0] + 1) % 4
                arrow[position[0]][position[1]] = '{' + arrow[position[0]][position[1]].strip() + '}'
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)
        if k.is_pressed(Left):
            os.system('cls')
            if not position:
                position = [1, 4]
                arrow[position[0]][position[1]] = '{' + arrow[position[0]][position[1]].strip() + '}'
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)
            else:
                arrow[position[0]][position[1]] = re.sub('[{}]', ' ', arrow[position[0]][position[1]])
                position[1] = (position[1] - 1) % 5
                arrow[position[0]][position[1]] = '{' + arrow[position[0]][position[1]].strip() + '}'
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)
        if k.is_pressed(Right):
            os.system('cls')
            if not position:
                position = [1, 0]
                arrow[position[0]][position[1]] = '{' + arrow[position[0]][position[1]].strip() + '}'
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)
            else:
                arrow[position[0]][position[1]] = re.sub('[{}]', ' ', arrow[position[0]][position[1]])
                position[1] = (position[1] + 1) % 5
                arrow[position[0]][position[1]] = '{' + arrow[position[0]][position[1]].strip() + '}'
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)
        if k.is_pressed('enter'):
            if not position:
                time.sleep(0.1)
            select = re.sub('[{}]', ' ', arrow[position[0]][position[1]]).strip()

            if select == 'CE':
                os.system('cls')
                formula = ''
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)

            elif select == 'Backspace':
                os.system('cls')
                if formula:
                    formula = formula[:-1]
                else:
                    pass
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)

            elif select == '=':
                os.system('cls')
                formula = str(p.solution(formula))
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)

            else:
                os.system('cls')
                formula += select
                print("\n\n\n")
                print('[', ' ' * (30 - len(formula)) + formula, ']', end='\n\n')
                for arrow_list in arrow:
                    for value in arrow_list:
                        print(value, end=' ')
                    print()
                time.sleep(0.2)


calculator()

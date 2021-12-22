def decsion(function)
    def nested()
    loop = True
    while loop:
        reply_list = ['y', 'n']
        formula = input("Make a suitable formula > ")
        print(function(formula))
        while True:
            reply = input("Do you want to calculate other formulas? (y/n) : ")
            if reply.lower() not in reply_list:
                print("Type y or n.")
            elif reply.lower() == 'y':
                os.system('cls')
                break
            else:
                input("Press any key to quit this program.")
                loop = False
                break
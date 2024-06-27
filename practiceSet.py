def want_practice_set_gen():
    check = True
    while check:
        n = input("Wanna create a course or practice_set template (y/n/yes/no): ")
        check = False
        n = n.lower().strip()
        if n not in ['y', 'n', 'yes', 'no']:
            print("Enter a valid input")
            check = True
    if n in ['y', 'yes']:
        return True
    elif n in ['n', 'no']:
        return False
    else:
        return False

def gen_practice_set(num:int):
    a = set()
    check = True
    while check == True:
        check = False
        temp = input(f"Enter file name_template: ")
        temp = temp.strip()
        symbols = ('<', '>', ':', "/", "\\", "|", "?", "*")
        for i in symbols:
            if temp.find(i) != -1:
                print(f"Donot use any of these {symbols}")
                check = True
                break
    for i in range(0, num):
        tem = temp+f"_{i+1}"
        a.add(tem)
    return a
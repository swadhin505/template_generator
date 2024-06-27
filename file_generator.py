import sys, os, practiceSet
import HCJ, C, Cpp, p

def is_platform_windows():
    if (sys.platform.startswith("win32")):
        return True
    elif (sys.platform.startswith("linux")):
        return False
    else:
        sys.exit(0)

def open_file(n):
    if n == 1:
        HCJ.HTML_CSS_JS()
    elif n == 2:
        psg = practiceSet.want_practice_set_gen()
        Cpp.Cpp(psg)
    elif n == 3:
        psg = practiceSet.want_practice_set_gen()
        C.C(psg)
    elif n == 4:
        psg = practiceSet.want_practice_set_gen()
        p.py(psg)
if is_platform_windows() == True:
    print("""What code template you want to create ?
            1. HTML_CSS_Javascript
            2. C++
            3. C
            4. Python
            5. nodejs
    """)
    check = True
    while check:
        try:
            n = int(input("Enter the index: "))
            check = False;
        except Exception as e:
            print(e)
    open_file(n)
    # with open("del.bat", "w") as f:
    #     text = "RMDIR "
elif is_platform_windows() == False:
    pass
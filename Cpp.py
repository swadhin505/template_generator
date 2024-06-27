import os
import subprocess
import sys
import practiceSet

def Cpp(psg):
    t = input("Enter the title of the template: ")
    t = t.strip()
    check = True
    while check:
        try:
            n = int(input("Enter number of C++ files: "))
            check = False;
        except Exception as e:
            print(e)
    if psg == False:
        a = set()
        for i in range(0, n):
            check = True
            while check == True:
                check = False
                temp = input(f"{i+1}. file name: ")
                temp = temp.strip()
                symbols = ('<', '>', ':', "/", "\\", "|", "?", "*")
                for i in symbols:
                    if temp.find(i) != -1:
                        print(f"Donot use any of these {symbols}")
                        check = True
                        break
            a.add(temp)
    elif psg == True:
        a = practiceSet.gen_practice_set(n)
    pwd = os.getcwd()
    with open(f"{pwd}\Batch.bat", 'w') as f:
        text = f"""
@echo off
md "{pwd}\{t}"
cd "{pwd}\{t}"\n
            """
        for i in a:
            text += f"echo hello > \"{pwd}\{t}\{i}.cpp\"\n"
        f.write(text)

    C_text = """// Header files
#include <iostream>

using namespace::std;

// Main function
int main() {
    cout << "Hello World!" << endl;
    return 0;
}
            """
    subprocess.call(f"{pwd}\Batch.bat")
    for i in a:
        with open(f"{pwd}\{t}\{i}.cpp", 'w') as f:
            f.write(C_text)
    os.remove(f"{pwd}\Batch.bat")

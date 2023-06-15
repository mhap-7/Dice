import random
import os
i = ""

print("(: Mhap :)\n\n")

while True:

    rm = random.randint(1 , 6)

    if rm == 1:
        print("   \n 0 \n   ")
    if rm == 2:
        print("  0\n   \n0  ")
    if rm == 3:
        print("  0\n 0 \n0  ")
    if rm == 4:
        print("0 0\n   \n0 0")
    if rm == 5:
        print("0 0\n 0 \n0 0")
    if rm == 6:
        print("000\n   \n000")
    print("=(:==============================================================:)=")

    i = input("Enter<----! : ")
    
    
    print("\n\n")
    if i == "exit" or i == "EXIT" or i == "quit" or i == "QUIT":
        break
    if i == "cls":
        os.system("cls")
    elif i != "":
        print("for next random number click 'Enter<----!' Button.")
    
    

print("\nBy!")

print("programmer : Mhap")
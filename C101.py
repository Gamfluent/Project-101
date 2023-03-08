import random

response = "y"

while response == "y":
    num = random.randint(1, 6)

    if num == 1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")  
    elif num == 2:
        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")
    elif num == 3:
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")   
    elif num == 4:
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    elif num == 5:
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    elif num == 6:
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
    response = input("Roll again: y or n")
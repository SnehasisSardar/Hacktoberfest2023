import random

def game(x,y):
    if x==y:
        print("This is draw!")
    elif x==1 and y==2:
        print("You won!")
    elif x==2 and y==3:
        print("You won!")
    elif x==3 and y==1:
        print("You won!")
    elif x==2 and y==1:
        print("You lost!")
    elif x==3 and y==2:
        print("You lost!")
    elif x==3 and y==1:
        print("You lost!")
    else:
        print("Enter valid input!!")

print("For Snake enter 1")
print("For Water enter 2")
print("For Gun enter 3")
x=int(input("Enter your choice: "))
y=random.randint(1,3)
print(f"You entered: {x}")
print(f"Computer entered: {y}")
game(x,y)

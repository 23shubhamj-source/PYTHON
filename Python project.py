import random
"""1 is a rock,
 0 is a paper and 
    -1 is a scissors"""
comp=random.choice([1,0,-1])
dic={"r":1,"p":0,"s":-1}
user_dict=input("Enter your choice(r=rock,p=paper,s=scissors):").lower()
user=dic[user_dict]
reverse_dict={1:"rock",0:"paper",-1:"scissors"}

print(f"You have chosen {reverse_dict[user]} and computer has chosen {reverse_dict[comp]}.")

if user==comp:
    print("It's a draw.")
else:
    if (user==1 and comp==-1) or (user==0 and comp==1) or (user==-1 and comp==0):
        print("You win!!")
    elif(user==1 and comp==0) or(user==0 and comp==-1)or (user==-1 and comp==1):
        print("Computer wins!!")
    else:
        print("Invalid input. Please enter a valid input.")


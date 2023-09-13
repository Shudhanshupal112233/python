import random
user_action=input("enter any one rock paper scissor:")
computer_action=random.choice(["rock","paper","scissor"])
if user_action==computer_action:
    print("both are same no one wins")
elif user_action=="rock":
        if computer_action=="paper":
            print("papper covers rocks ,you lose")
        else:
            print("rock broke scissor,you win")
elif user_action=="paper":
        if computer_action=="rock":
            print("papper covers rocks ,you win")
        else:
            print(" scissor cuts paper,you loose")
            
elif user_action=="scissor":
        if computer_action=="paper":
            print(" scissor cuts papper ,you win")
        else:
            print("rock broke scissor,you loose")
                        
                        
                
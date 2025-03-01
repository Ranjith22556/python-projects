import random
options=["rock","paper","scissors"]
while True:
    player=None
    alex=random.choice(options)
    print("Options:(rock,paper,scissors)")
    player=input("Your choice   : ").lower()
    if player  not in options:
        player=input("Your choice   : ").lower()
    print(f"Alex's Choice : {alex}")
    if player==alex:
        print("It's a Tie")
    elif player=="rock" and alex=="scissors":
        print("You Win!")
    elif player=="scissors" and alex=="paper":
        print("You Win!")
    elif player=="paper" and alex=="rock":
        print("You Win!")
    else:
        print(f"Alex's Choice : {alex}")
        print("Alex Win's")
    stop=input("'p' TO PLAY,'s' TO STOP :").lower()
    if stop=="p":
        continue
    elif stop=="s":
        break
    else:
        stop=input("'p' TO PLAY,'s' TO STOP :").lower()

#ladders
def ladders(x):
    if x==2: return 25
    elif x==7: return 31
    elif x==20:return 44
    elif x==33:return 76
    elif x==41:return 96
    elif x==53:return 89
    else:return x
    
def turn(player,score): #Turn function
    print()
    print("Its",player,"turn.")
    roll2 = input("Press enter to Roll")
    print()

    if roll2 == "":
        a = randint(1,6) #player dice roll
        print(player,"rolled the dice")
        print(player,"got a",a)
        score += a
        
        if score <= 100:
            lad = ladders(score) #checking for ladders for player
            if lad != score:
                print("There's a ladder!",player,"climbed up.")
                score = lad
            snk = snakes(score)
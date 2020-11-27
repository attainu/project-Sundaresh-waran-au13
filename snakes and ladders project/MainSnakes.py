#snakes
def snakes(x): 
    if x==40:return 5
    elif x==46:return 11
    elif x==99:return 23
    elif x==70:return 27
    elif x==83:return 57
    elif x==92:return 48
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

            if snk != score: #checking for snakes for player
                print(player,"got bitten by a snake!",player,"fall down!")
                score = snk
            print(player,"is now on box",score)
#Creating the random integer
import random
randnum = random.randint(1,100)

#Game set-up
playerguess = 0
guesslist = []
guesslist += str(playerguess)
guesscounter = 0
congratulations_message = "Congratulations, you guessed the number! It took you {guesscounter} tries"

while playerguess != randnum:
    playerguess = int(input("Guess the number: "))
    guesslist.append(playerguess)
    #Invalid value checking
    if ((playerguess > 100) or (playerguess < 1)):
        print("OUT OF BOUNDS")
        guesscounter += 1
        continue
    #Checking for hole in one
    elif (playerguess == randnum):
        guesscounter += 1
        print(fcongratulations_message)
        break
    #If within 10 of the value
    elif (abs(playerguess-randnum)<=10):
        print("WARM!")
        guesscounter += 1
        while playerguess != randnum:
            if playerguess == randnum:
                print(fcongratulations_message)
            #If guessed value is closer than the last
            elif(abs((guesslist[-1]) - randnum) < abs((guesslist[-2]) - randnum)):
                playerguess = int(input("Warmer! \nTry again: "))
                guesslist.append(playerguess)
                guesscounter += 1
                if (playerguess == randnum):
                            print(f"{congratulations_message}")
                            break
                continue
            #If guessed value is further than the last
            elif (abs((guesslist[-1]) - randnum) > abs((guesslist[-2]) - randnum)):
                playerguess = int(input("Colder! \nTry again: "))
                guesslist.append(playerguess)
                guesscounter += 1
                if (playerguess == randnum):
                            print(f"{congratulations_message}")
                            break
                continue
    #If not within 10 of the value
    else:
        print("COLD!")
        guesscounter += 1
        continue

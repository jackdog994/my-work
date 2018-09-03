#Creating the random integer
import random
randnum = random.randint(1,100)

#Game set-up
playerguess = 0
guesslist = []
guesslist += str(playerguess)
guesscounter = 0
def win():
    print(f"Congratulations, you guessed the number! It took you {guesscounter} tries")

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
        win()
        break
    #If within 10 of the value
    elif (abs(playerguess-randnum)<=10):
        print("WARM!")
        guesscounter += 1
        while playerguess != randnum:
            if playerguess == randnum:
                win()
            #If guessed value is closer than the last
            elif(abs(int(guesslist[-1]) - randnum) < abs(int(guesslist[-2]) - randnum)):
                playerguess = int(input("Warmer! \nTry again: "))
                guesslist.append(playerguess)
                guesscounter += 1
                if (playerguess == randnum):
                    win()
                    break
                continue
            #If guessed value is further than the last
            elif (abs(int(guesslist[-1]) - randnum) > abs(int(guesslist[-2]) - randnum)):
                playerguess = int(input("Colder! \nTry again: "))
                guesslist.append(playerguess)
                guesscounter += 1
                if (playerguess == randnum):
                    win()
                    break
                continue
    #If not within 10 of the value
    else:
        print("COLD!")
        guesscounter += 1
        continue

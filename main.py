
# Import the modules
import sys
import random

# ans is a variable that holds the boolean value "True"
ans = True

# while is both a conditial and an iteration.  It is known as a "Conditional Loop"
while ans:
    # question is a variable that stores the users text input
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    # answers is a variable that stores a random number between 1 & 20
    answers = random.randint(1,20)
    #print(answers)
    # the following conditional stops the program when the user inputs no text 
    if question == "":
        sys.exit() 
   
    
    # the following 20 statements are all conditionals that respond only to a specific number between 1 & 20 that is stored in the answers variable
    elif answers == 1:
        print("It is certain")    
    elif answers == 2:
        print("It is decidedly so")    
    elif answers == 3:
        print("Without a doubt")    
    elif answers == 4:
        print("Yes - definitely")    
    elif answers == 5:
        print("You may rely on it")    
    elif answers == 6:
        print("As I see it, yes")    
    elif answers == 7:
        print("Most likely")    
    elif answers == 8:
        print("Outlook good")
    elif answers == 9:
        print("Yes")
    elif answers == 10:
        print("Signs point to yes")
    elif answers == 11:
        print("Don't count on it")
    elif answers == 12:
        print("My reply is no")
    elif answers == 13:
        print("My sources say no")
    elif answers == 14:
        print("Outlook not so good")
    elif answers == 15:
        print("Very doubtful")
    elif answers == 16:
        print("Reply hazy, try again")
    elif answers == 17:
        print("Ask again later")
    elif answers == 18:
        print("Better not tell you now")
    elif answers == 19:
        print("Cannot predict now")
    elif answers == 20:
        print("Concentrate and ask again")

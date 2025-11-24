import random
w=0
n=0
while True :
    n+=1
    word_list = [ "accuracy", "adaptive", "advisor", "alleged", "analyze", "apparent", "assumed", "attitude", "awareness", "behavior", "benefit", "blizzard", "capable", "career", "cautious", "champion", "climate", "collapse", "commerce", "community", "confirm", "conquer", "crisis", "current", "declared", "defense", "deliver", "demand", "destroy", "developer", "digital", "discover", "drastic", "elegant", "emerging", "endeavor", "estimate", "ethical", "except", "executive", "exhibit", "expected", "failure", "fantastic", "feasible", "feature", "formula", "forward", "frequent", "frustrate", "generate", "globally", "graduate", "habitat", "honesty", "identity", "illusion", "impact", "improve", "include", "industry", "inspect", "instinct", "integral", "interact", "involve", "isolate", "judgment", "justify", "kindness", "legendary", "located", "logical", "magnify", "maximum", "merchant", "minister", "momentum", "movement", "multiple", "necessary", "observer", "official", "operate", "origin", "outcome", "overview", "partner", "pattern", "perform", "philosophy", "popular", "predict", "prepare", "previous", "priority", "professor", "proposal", "protect", "publish", "balloon", "banana"]
    word = random.choices(word_list)
    fword = word[0]
    word_len = len(word[0])
    wordl=list(fword)
    guess = [ "_" for i in range(len(fword))]
    print("--------------------WELCOME TO HANGMAN GAME !!--------------------")
    print("the len of the word is : ",word_len)
    print("""
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    """)
    print(guess)
    copyl = wordl.copy()
    total_life = 6
    stages = [  
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    """,
                    
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    """,
                    
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    """,
                    
                    """
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    """,
                    
                    """
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    """,
                    
                    """
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    """,
                    
                    """
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    """
        ]
    while total_life > 0:
        inp = input("Enter letter :" )
        if inp in wordl :
            print("correct guess")
            c=wordl.count(inp)
            for i in range(c):
                l = copyl.index(inp)
                guess[l] = inp
                copyl[l] = "*"
            print(guess) 
        else :
            print("wrong guess")
            total_life -=1
        if total_life == 5 :
            print(stages[1])    
        if total_life == 4 :
            print(stages[2])
        if total_life == 3 :
            print(stages[3])
        if total_life == 2 :
            print(stages[4])
        if total_life == 1 :
            print(stages[5])      
        if total_life == 0 :
            print(stages[6])
            print("YOU LOST !! BETTER LUCK NEXT TIME :( .")
            print(wordl)
            break
        if guess == wordl :
            print("CONGRATULATIONS!! YOU HAVE WON THE GAME :) .")
            w+=1
            break
    ch=input("do you want to play again (yes/no) : ")
    if ch=='no':
        break
print()
print("---------------------SCOREBOARD--------------------")
print()
print("no. of times game played : ",n)
print("win score : ",w)
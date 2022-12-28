'''
Word Puzzle Game

Problem Statement: You have to write a Word Puzzle Game in which the user has to form
the correct word out of a given set of characters. In the game the user has to solve this
puzzle for 3 words, one at a time. Problem words are stored in a list and appear to the user
in random sequence. Give the user score +1 for each correct answer and give -1 for each
wrong answer. At last print the final score. You can store any number of words in the list, but
in each round of the game only 5 words are shown to the user.
Sample output of the game:


Arrange the letters to form a valid word:

RAEHTF
Father
Correct

Arrange the letters to form a valid word:

KABRE
Barke
Wrong

Arrange the letters to form a valid word:

CYROTNU
Cry
Wrong

Arrange the letters to form a valid word:

RENEG
green
Correct

Arrange the letters to form a valid word:

OAERELANP
aeroplane
Correct

Net Score is 3
'''
import random
# ---------------------------------------------------
def Game():
    score=0
    words=['PYTHON','PROGRAMMER','CODER']
    words= random.sample(words,k=len(words))

    for word in words:
        score=puzzlequestion(word,score)

    print("Your Score is =",score)

# -----------------------------------------------------
def puzzlequestion(word,score):
    problemword=shuffleword(word)
    print("\nArrange the letters to form a valid word:")
    print(problemword)
    userinput=input()
    if (userinput.upper()==word):
        print("Well Done! Correct Answer")
        score+=1
    else:
        print("Very Sad for You. You are Wrong")
        score-=1
    return score
# ---------------------------------------------------------

def shuffleword(wrd):
    wd=random.sample(wrd,k=len(wrd))
    return ''.join(wd)

Game()

        
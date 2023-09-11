import random
def give_instructions():
    print("""\n Wordle is a word guessing game,
        You have 5 attempts
        (C) means the letter is in the word and in the right position.
        (W) means the letter is in the word but is not the right position. 
        (X) means the letter is not in the word. 
        """)
words = ["this","five","pink","cool","tree"]
hidden_word = random.choice(words)
def check_word(guess):
        if hidden_word == guess:
            print("Congrats!! You won the game.")
            return True
        else: 
            result = ""
            for i,j in zip(guess,hidden_word):
                if i == j: 
                    result = result + "C"
                elif i in hidden_word: 
                    result = result + "W"
                else:  
                    result = result + "X"
            print(result)
            return False 
def main(): 
    attempt = 5
    give_instructions()
    while attempt>0:
        guess = input ("Enter four letter word: ") 
        if check_word(guess):
            break
        else: 
            attempt -= 1 #attempt = attempt - 1 
            print(f"You have {attempt} attempt left. ")
    else: 
        print("Game over")
main()



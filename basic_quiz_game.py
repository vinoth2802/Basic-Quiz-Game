# This is the source code for the basic quiz game.
# This file is created by Vinothkumar J.

# function for diplaying questions and options, and collecting player's answers
def play():
    print("---------Let's play the quiz----------")
    question_number=0
    guesses = []
    correct_guesses=0


    #loop for printing questions
    for question in questions:
        print(question)

        #loop for printing options
        for key,option in options[question_number].items():
            print(key+") "+option)

        #Get the player's guess
        guess=input("Choose the answer (A/B/C/D):").upper()
        guesses.append(guess)

        #checking whether the guess is right or wrong
        if answers[question_number+1]==guess:
            print("CORRECT! you got it right\U0001F929")
            correct_guesses+=1
        else:
            print("INCORRECT! It's wrong\U0001F614")
            print("The correct answer is " + options[question_number][answers[question_number + 1]])

        print("--------------------------------------")
        question_number += 1

    get_results(guesses,correct_guesses)


# Function for calculating player's score
def get_results(guesses,correct_guesses):
    number_of_questions=len(questions)
    score=0
    print("-------------RESULTS---------------")

    print("your guesses    :",end=" ")
    for i in guesses:
        print(i,end=" ")
    print()

    print("Correct answers :",end=" ")
    for i in answers.values():
        print(i,end=" ")
    print()

    print("You got ",correct_guesses,"/",number_of_questions," questions right!")
    score=int((correct_guesses/number_of_questions)*100)
    print("Your quiz score is",score,"%")
    print("-----------------------------------")


# Function for playing again
def play_again():
    choice=input("Do you want to play again?(yes/no): ").lower()
    if choice=="yes":
        play()
    else:
        print("Thank you for playing! Hope you enjoyed! Bye! ")
        exit(0)


questions=["1.What is the largest ocean in the world?",
           "2.What is the tallest mountain in the world?",
           "3.What is the chemical formula for water?",
           "4.What is the name of the largest planet in the solar system?"]

options=[{"A":"Atlantic","B":"Pacific","C":"Indian","D":"Arctic"},
         {"A":"Mount Fuji","B":"Mount Kilimanjaro","C":"Mount Everest","D":"Kangchenjunga"},
         {"A":"H₂O","B":"CO₂","C":"HCL","D":"CO₃"},
         {"A":"Earth","B":"Neptune","C":"Jupiter","D":"Saturn"}]

answers={1:"B",2:"C",3:"A",4:"C"}

play()
play_again()

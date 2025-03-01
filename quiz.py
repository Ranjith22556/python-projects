questions=["What is the correct syntax to output Hello, World! in Python?",
           "Which of the following is a valid variable name in most programming languages?",
           "What does the following code return: len('Python')?",
           "Which data type is used to store True or False values?",
           "Which keyword is used to create a function in JavaScript?"]
answers=["B","C","B","B","A"]
guess=[]
score=0
options=[
        ["A) echo 'Hello, World!'",
         "B) print('Hello, World!')",
         "C) printf('Hello, World!')",
         "D) cout << 'Hello, World!';"],
        ["A) 1_variable",
         "B) variable-name",
         "C) _variable",
         "D) variable"],
         ["A) 5",
         "B) 6",
         "C) 7",
         "D) Error"],
         ["A) int",
         "B) bool",
         "C) char",
         "D) float"],
         ["A) function",
         "B) fun",
         "C) def",
         "D) create"],
         ]
for x in range(len(questions)):
    print(questions[x])
    for y in range(4):
        print(options[x][y])
    guesses=input("Enter your Answer: ")
    guesses=guesses.upper()
    guess.append(guesses)
    if answers[x]==guess[x]:
        print("Correct!")
    else:
        print(f"Incorrect! The correct Answer is {answers[x]}")
    print("-----------------------------------------------------------")
for x in range(len(questions)):
    if answers[x]==guess[x]:
        score+=1
score=(score/len(questions))*100
print(f"Your Score is {score:2}%")
print("-----------------------------------------------------------")
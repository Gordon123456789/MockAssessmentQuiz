#Version 1
#The following program is a quiz that asks questions to a user for points
#User's score will be shown at the end of quiz

qa = {'What continent is China in?':'Asia', 'What continent is South Africa in?':'Africa', 'What continent is Mexico in?':'North America','What continent is India in?':'Asia','What continent is Fiji in?':'Oceania','What continent is France in?':'Europe','What is the capital of Russia?':'Moscow','What is the capital of Japan?':'Tokyo','What is the capital of Australia?':'Canberra','What is the largest ocean?':'Pacific'}
options = [['Africa','Asia','Europe'],
           ['Oceania','South America','Africa'],
           ['Africa','North America','South America'],
           ['Asia','Europe','Oceania'],
           ['Europe','Oceania','Africa'],
           ['North America','Asia','Europe'],
           ['Moscow','Berlin','Samara'],
           ['Beijing','Tokyo','New York'],
           ['Canberra','Sydney','Wellington'],
           ['Atlantic','Southern','Pacific']      
           ]
instructions = ["Welcome to the quiz", 
                "To answer questions enter option or option number", 
                "Answers are capital sensitive", #telling users answers require correct input of capital letters 
                "Enter a key to continue"]
#Storing questions, answers and options in dictionary and storage variables


def quiz(): #defining function
    num = 0
    opt_num = 0
    score = 0
    name = str()
    age = int()
    #initialising variables

    print("---------------------------------------")
    print(f"{instructions[0]}, \n{instructions[1]}, \n{instructions[2]}, \n{instructions[3]}") #Prints each instruction using sequence
    input("Do you want to continue : ") #Asks user to give an input to continue
    print("---------------------------------------")
    while True: 
        while True:
            name = input("\nEnter your name : ") #Asking user information inputs
            if name == "":
                 print("You must enter a name.")
            else: 
                 break
        while True:
            try:#Trap Errors
                age = int(input("Enter your age (years) : ")) #Asking user information inputs
                break
            except ValueError: #Exception/error has occured
                print("\nYou must enter an integer")
        if age < 13:
            print("You are too young for this quiz")
            break
        elif age > 18:
            print("You are too old for this quiz")
            break
        
        for q, a in qa.items(): #Reads question and answer in qa dictionary to print each
            print("\n---------------------------------------")
            num +=1 #adds a question number for next question being printed
            print(f"\nQuestion {num}:")
            print(q)
            print('Options:')
            for o, option in enumerate(options[opt_num]): #Reads option in options dictionary
                print(f'  {o + 1}. {option}') #enumerate keeps track of option number for each iteration in options
            opt_num += 1 #adds an option number for next option being printed
            try: #Trap Errors
                user_ans = input('Enter your answer : ') #Asking user for answer input
                while True: 
                    if user_ans == a:
                        score += 1 #Adds a point to score if user answer is correct
                        print("Correct!")
                        break
                    elif options[opt_num - 1][int(user_ans) - 1] == a: #Checks if user entered option number as answer
                        score += 1 #Adds a point to score if user answer is correct
                        print('Correct!')
                        break
                    else:
                        print(f"The answer is {a}, not {user_ans!r}") #Tells user answer is wrong and tells user correct answer
                        break
            except ValueError: #Exception/error has occured
                print(f"The answer is {a}, not {user_ans!r}") #Tells user answer is wrong and tells user correct answer
            print("Score : ", score) #Tells user score after each question
        print("\n---------------------------------------")
        print(f'\n{name} your final score is {score} out of {num} questions') #Tells user final score
        break
#Calling function
quiz()

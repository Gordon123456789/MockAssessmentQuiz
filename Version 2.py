"""
Version 2
The following program is a multi-choice quiz
User's score will be shown at the end of quiz
"""

che_qa = {'What is the symbol for Fluorine?':'F', 'What is the symbol for Nitrogen?':'N', 'What is the symbol for Gold?':'Au','What is the symbol for Lead?':'Pb','What is the symbol for Neon?':'Ne','What is the symbol for Oxygen?':'O','What is H2O?':'Water','What revolves around the nucleus of an atom?':'Electron','What state of matter is held together?':'Solid','What is the smallest unit of matter?':'Atom'}
che_options = [['Ne','F','Pb'],
           ['Zn','Au','N'],
           ['Au','Be','Li'],
           ['Pb','U','L'],
           ['Be','Ne','F'],
           ['I','Ox','O'],         
           ['Glass','Water','Sand'],        
           ['Electron','Proton','Neutron'],
           ['Gas','Liquid','Solid'],
           ['Atom','Molecule','Dust']      
           ]

gen_qa = {'What is a group of birds called?':'Flock', 'What is the most spoken language?':'English', 'What is H2O?':'Water','What is the largest ocean?':'Pacific','What planet is closest to the sun?':'Mercury','What is the fastest land mammal?':'Cheetah','What is the largest country in the world?':'Russia','What shape has 4 equal sides and 4 right angles?':'Square','What do you call a group of fish?':'School','What is Football also known as?':'Soccer'}
gen_options = [['Birds','Flock','Group'],
           ['English','French','Sign Language'],
           ['Water','Mud','rock'],
           ['Atlantic','Pacific','Antarctic'],
           ['Mercury','Earth','Neptune'],
           ['Cheetah','Rabbit','Dog'],
           ['Australia','Canada','Russia'],
           ['Rectangle','Square','Triangle'],
           ['School','Fishes','Colony'],
           ['Rugby','Soccer','Basketball']      
           ]

geo_qa = {'What continent is China in?':'Asia', 'What continent is South Africa in?':'Africa', 'What continent is Mexico in?':'North America','What continent is India in?':'Asia','What continent is Fiji in?':'Oceania','What continent is France in?':'Europe','What is the capital of Russia?':'Moscow','What is the capital of Japan?':'Tokyo','What is the capital of Australia?':'Canberra','What is the largest ocean?':'Pacific'}
geo_options = [['Africa','Asia','Europe'],
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
num = 0
opt_num = 0
score = 0
quiz_ins = ["\nIf you would like to play a Chemistry Quiz press '1'",
                    "If you would like to play a General Knowledge Quiz press '2'",
                    "If you would like to play a Geography  Quiz press '3'",]

#Storing questions, answers, option and instructions in dictionary and storage variables

def quiz():
    def user_opt(): #defining function
        #initialising variables
        name = str()
        age = int()
        q_opt = int()
        open('user_det.txt', 'w').close() #deleting all past user data for new user
        q = open("quiz_inf_console.txt", "r")
        inf = q.read()
        print(inf) #Tells user all quiz details
        input("Enter a key to continue : ") #Asks user to give an input to continue
        print("\n---------------------------------------")
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
                exit()
        elif age > 18:
                print("You are too old for this quiz")
                exit()
        print(f"{quiz_ins[0]}, \n{quiz_ins[1]}, \n{quiz_ins[2]}") #Prints each instruction using sequence
        while True:
            try:#Trap Errors
                q_opt = int(input("Enter the number of the quiz you would like to play : ")) #Asking user information inputs
                break
            except ValueError: #Exception/error has occured
                    print("You must enter an integer")
        if q_opt == 1:
            quiz_type = "Chemistry"
            with open("user_det.txt", "a") as user_det_file:
                user_det_file.write(f"Quiz Type : {quiz_type}\n")
                user_det_file.write(f"Name : {name}\n")
                user_det_file.write(f"Age : {age}\n")
            che() #Calling function
        elif q_opt == 2:
            quiz_type = "General Knowledge"
            with open("user_det.txt", "a") as user_det_file:
                user_det_file.write(f"Quiz Type : {quiz_type}\n")
                user_det_file.write(f"Name : {name}\n")
                user_det_file.write(f"Age : {age}\n")
            gen() #Calling function
        elif q_opt == 3:
            quiz_type = "Geography"
            with open("user_det.txt", "a") as user_det_file:
                user_det_file.write(f"Quiz Type : {quiz_type}\n")
                user_det_file.write(f"Name : {name}\n")
                user_det_file.write(f"Age : {age}\n")
            geo() #Calling function
        else: 
            print("You must enter a valid quiz number")

    def che(): #defining function
        global num
        global opt_num
        global score
        print("\n--------------Chemistry Quiz----------------")
        for q, a in che_qa.items(): #Reads question and answer in qa dictionary to print each
                print("\n------------------------------")
                num +=1 #adds a question number for next question being printed
                print(f"\nQuestion {num}:")
                print(q)
                print('Options:')
                for o, option in enumerate(che_options[opt_num]): #Reads option in options dictionary
                    print(f'  {o + 1}. {option}') #enumerate keeps track of option number for each iteration in options
                opt_num += 1 #adds an option number for next option being printed
                try: #Trap Errors
                    user_ans = input('Enter your answer : ') #Asking user for answer input
                    while True: 
                        if user_ans == a:
                                score += 1 #Adds a point to score if user answer is correct
                                print("Correct!")
                                break
                        elif che_options[opt_num - 1][int(user_ans) - 1] == a: #Checks if user entered option number as answer
                                score += 1 #Adds a point to score if user answer is correct
                                print('Correct!')
                                break
                        else:
                                print(f"The answer is {a}, not {user_ans!r}") #Tells user answer is wrong and tells user correct answer
                                print("Score : ", score) #Tells user score after each question   
                                break
                except ValueError: #Exception/error has occured
                    print(f"The answer is {a}, not {user_ans!r}") #Tells user answer is wrong and tells user correct answer
                    print("Score : ", score) #Tells user score after each question 
        with open("user_det.txt", "a") as user_det_file:  
            user_det_file.write(f"Total Score : {score}/{num}\n")
            user_det_file.write(f"--------------------------------\n")
        user_inf()
        
    def gen(): #defining function
        global num
        global opt_num
        global score
        print("\n--------------General Knowledge Quiz----------------")
        for q, a in gen_qa.items(): #Reads question and answer in qa dictionary to print each
                print("\n------------------------------")
                num +=1 #adds a question number for next question being printed
                print(f"\nQuestion {num}:")
                print(q)
                print('Options:')
                for o, option in enumerate(gen_options[opt_num]): #Reads option in options dictionary
                    print(f'  {o + 1}. {option}') #enumerate keeps track of option number for each iteration in options
                opt_num += 1 #adds an option number for next option being printed
                try: #Trap Errors
                    user_ans = input('Enter your answer : ') #Asking user for answer input
                    while True: 
                        if user_ans == a:
                                score += 1 #Adds a point to score if user answer is correct
                                print("Correct!")
                                break
                        elif gen_options[opt_num - 1][int(user_ans) - 1] == a: #Checks if user entered option number as answer
                                score += 1 #Adds a point to score if user answer is correct
                                print('Correct!')
                                break
                        else:
                                print(f"The answer is {a}, not {user_ans!r}") #Tells user answer is wrong and tells user correct answer
                                print("Score : ", score) #Tells user score after each question   
                                break
                except ValueError: #Exception/error has occured
                    print(f"The answer is {a}, not {user_ans!r}") #Tells user answer is wrong and tells user correct answer
                    print("Score : ", score) #Tells user score after each question 
        with open("user_det.txt", "a") as user_det_file:  
            user_det_file.write(f"Total Score : {score}/{num}\n")
            user_det_file.write(f"--------------------------------\n")
        user_inf()

    def geo(): #defining function
        global num
        global opt_num
        global score
        print("\n--------------Geography Quiz----------------")
        for q, a in geo_qa.items(): #Reads question and answer in qa dictionary to print each
                print("\n------------------------------")
                num +=1 #adds a question number for next question being printed
                print(f"\nQuestion {num}:")
                print(q)
                print('Options:')
                for o, option in enumerate(geo_options[opt_num]): #Reads option in options dictionary
                    print(f'  {o + 1}. {option}') #enumerate keeps track of option number for each iteration in options
                opt_num += 1 #adds an option number for next option being printed
                try: #Trap Errors
                    user_ans = input('Enter your answer : ') #Asking user for answer input
                    while True: 
                        if user_ans == a:
                                score += 1 #Adds a point to score if user answer is correct
                                print("Correct!")
                                break                   
                        elif geo_options[opt_num - 1][int(user_ans) - 1] == a: #Checks if user entered option number as answer
                                score += 1 #Adds a point to score if user answer is correct
                                print('Correct!')
                                break
                        else:
                                print(f"The answer is {a}, not {user_ans!r}") #Tells user answer is wrong and tells user correct answer
                                print("Score : ", score) #Tells user score after each question   
                                break
                except ValueError: #Exception/error has occured
                    print(f"The answer is {a}, not {user_ans!r}") #Tells user answer is wrong and tells user correct answer
                    print("Score : ", score) #Tells user score after each question 
        with open("user_det.txt", "a") as user_det_file:  
            user_det_file.write(f"Total Score : {score}/{num}\n")
            user_det_file.write(f"--------------------------------\n")
        user_inf()
        
    def user_inf():
        print("\n\n---------------------------------------")
        f = open("user_det.txt", "r")
        data = f.read()
        print(data) #Tells user all quiz details
        incorrect_score = num-score
        import matplotlib.pyplot as plt

        #change the default size of graphs to 12" by 5"
        plt.rcParams["figure.figsize"] = (12, 5)

        names = ["Correct", "Incorrect"]
        scores = [score, incorrect_score]

        #defines how many rows and columns of graphs 
        plt.subplot(1, 2, 1)

        #Creates a bar graph from a list of labels, and a list of values 
        plt.bar(names, scores)
        #Move to the second graph spot
        plt.subplot(1, 2, 2)
        #Create pie chart of the scores
        plt.pie(scores, labels=names)
        #display the graphs
        plt.show()

    #Calling function
    user_opt()

#Calling function
quiz()
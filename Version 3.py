"""
Version 3
#The following program is a multi-choice quiz that asks questions to a user for points
#User's score will be shown at the end of quiz
#This program is written with EasyGui
"""
from easygui import* 

mat_qa = [
        ('What is 10 x 20?', '200'),
        ('Which is an Integer?', '10'),
        ('What is 110 divided by 10?', '11'),
        ('What is 45 + 45?', '90'),
        ('What symbol is used for addition?', '+'),
        ('If davids age in 2020 is 10, what is his age in 2024?', '14'),
        ('Solve for "X", 5x = 25', '5'),
        ('What is the 2d shape with 3 sides?', 'Triangle'),
        ('What is this equation called? y = ax+b','Linear'),
        ('What is the chance of getting heads if I flip a two sided coin?', '50%')]
mat_options = [['20','200','2000','Skip', 'Exit Quiz'],
           ['10','5.5','0.2','Skip', 'Exit Quiz'],
           ['5.5','100','11','Skip', 'Exit Quiz'],
           ['100','90','80','Skip', 'Exit Quiz'],
           ['+','-','x','Skip', 'Exit Quiz'],
           ['16','15','14','Skip', 'Exit Quiz'],         
           ['5','10','50','Skip', 'Exit Quiz'],        
           ['Triangle','Circle','Square','Skip', 'Exit Quiz'],
           ['Quadratic','Linear','Straight','Skip', 'Exit Quiz'],
           ['25%','50%','100%','Skip', 'Exit Quiz']]

che_qa = [('What is the symbol for Fluorine?', 'F'),
           ('What is the symbol for Nitrogen?', 'N'),
             ('What is the symbol for Gold?', 'Au'),
             ('What is the symbol for Lead?', 'Pb'),
             ('What is the symbol for Neon?', 'Ne'),
             ('What is the symbol for Oxygen?', 'O'),
             ('What is H2O?', 'Water'),
             ('What revolves around the nucleus of an atom?', 'Electron'),
             ('What state of matter is held together?', 'Solid'),
             ('What is the smallest unit of matter?', 'Atom')]
che_options = [['Ne','F','Pb','Skip', 'Exit Quiz'],
           ['Zn','Au','N','Skip', 'Exit Quiz'],
           ['Au','Be','Li','Skip', 'Exit Quiz'],
           ['Pb','U','L','Skip', 'Exit Quiz'],
           ['Be','Ne','F','Skip', 'Exit Quiz'],
           ['I','Ox','O','Skip', 'Exit Quiz'],         
           ['Glass','Water','Sand','Skip', 'Exit Quiz'],        
           ['Electron','Proton','Neutron','Skip', 'Exit Quiz'],
           ['Gas','Liquid','Solid','Skip', 'Exit Quiz'],
           ['Atom','Molecule','Dust','Skip', 'Exit Quiz']]

gen_qa = [('What is a group of birds called?', 'Flock'), 
          ('What is the most spoken language?', 'English'),
            ('How many minutes are in 3 hours?', '180'),
            ('How many letters are in the English alphabet?', '26'),
            ('What planet is closest to the sun?', 'Mercury'),
            ('What is the fastest land mammal?', 'Cheetah'),
            ('What is the largest country in the world?', 'Russia'),
            ('What shape has 4 equal sides and 4 right angles?', 'Square'),
            ('What do you call a group of fish?', 'School'),
            ('What is Football also known as?', 'Soccer')]
gen_options = [['Birds','Flock','Group','Skip', 'Exit Quiz'],
           ['English','French','Sign Language','Skip', 'Exit Quiz'],
           ['180','300','100','Skip', 'Exit Quiz'],
           ['24','25','26','Skip', 'Exit Quiz'],
           ['Mercury','Earth','Neptune','Skip', 'Exit Quiz'],
           ['Cheetah','Rabbit','Dog','Skip', 'Exit Quiz'],
           ['Australia','Canada','Russia','Skip', 'Exit Quiz'],
           ['Rectangle','Square','Triangle','Skip', 'Exit Quiz'],
           ['School','Fishes','Colony','Skip', 'Exit Quiz'],
           ['Rugby','Soccer','Basketball','Skip', 'Exit Quiz']      
           ]

geo_qa = [('What continent is China in?', 'Asia'),
           ('What continent is South Africa in?', 'Africa'),
             ('What continent is Mexico in?', 'North America'),
             ('What continent is India in?', 'Asia'),
             ('What continent is Fiji in?', 'Oceania'),
             ('What continent is France in?', 'Europe'),
             ('What is the capital of Russia?', 'Moscow'),
             ('What is the capital of Japan?', 'Tokyo'),
             ('What is the capital of Australia?', 'Canberra'),
             ('What is the largest ocean?', 'Pacific')]
geo_options = [['Africa','Asia','Europe','Skip', 'Exit Quiz'],
           ['Oceania','South America','Africa','Skip', 'Exit Quiz'],
           ['Africa','North America','South America','Skip', 'Exit Quiz'],
           ['Asia','Europe','Oceania','Skip', 'Exit Quiz'],
           ['Europe','Oceania','Africa','Skip', 'Exit Quiz'],
           ['North America','Asia','Europe','Skip', 'Exit Quiz'],
           ['Moscow','Berlin','Samara','Skip', 'Exit Quiz'],
           ['Beijing','Tokyo','New York','Skip', 'Exit Quiz'],
           ['Canberra','Sydney','Wellington','Skip', 'Exit Quiz'],
           ['Atlantic','Southern','Pacific','Skip', 'Exit Quiz']      
           ]
num = 0
opt_num = 0
score = 0

q_ins = ["\nQuiz Selection",
        "Select the quiz you want to play"]

#Storing questions, answers, option and instructions in dictionary and storage variables

def quiz(): 
    def user_option(): #defining function
        #initialising variables
        name = str()
        age = int()
        q_opt = int()
        open('user_det.txt', 'w').close() #deleting all past user data for new user
        q = open("quiz_inf_easygui.txt", "r")
        inf = q.read()
        msgbox(inf) #Tells user all quiz details
        while True:
            name = enterbox("\nEnter your name : ") #Asking user information inputs
            if name == "":
                 msgbox("You must enter a name.")
            else: 
                 break
        while True:
            try:#Trap Errors
                age = integerbox("Enter your age : ") #Asking user information inputs
                break
            except ValueError: #Exception/error has occured
                msgbox("\nYou must enter an integer")
            if age < 13:
                msgbox("You are too young for this quiz")
                quit()
            elif age > 18:
                msgbox("You are too old for this quiz")
                quit()
        choices = ["Math", "Chemistry", "General Knowledge", "Geography"] #these are the buttonbox options
        q_opt = buttonbox(q_ins[0], q_ins[1], choices)        
        if q_opt == "Math":
            quiz_type = "Math" 
            with open("user_det.txt", "a") as user_det_file: #writing user details in external file
                user_det_file.write(f"--------------------------------\n")
                user_det_file.write(f"Quiz Type : {quiz_type}\n")
                user_det_file.write(f"Name : {name}\n")
                user_det_file.write(f"Age : {age}\n")
            mat() #Calling function
        elif q_opt == "Chemistry":
            quiz_type = "Chemistry"
            with open("user_det.txt", "a") as user_det_file: #writing user details in external file
                user_det_file.write(f"--------------------------------\n")
                user_det_file.write(f"Quiz Type : {quiz_type}\n")
                user_det_file.write(f"Name : {name}\n")
                user_det_file.write(f"Age : {age}\n")
            che() #Calling function
        elif q_opt == "General Knowledge":
            quiz_type = "General Knowledge"
            with open("user_det.txt", "a") as user_det_file: #writing user details in external file
                user_det_file.write(f"--------------------------------\n")
                user_det_file.write(f"Quiz Type : {quiz_type}\n")
                user_det_file.write(f"Name : {name}\n")
                user_det_file.write(f"Age : {age}\n")
            gen() #Calling function
        elif q_opt == "Geography":
            quiz_type = "Geography"
            with open("user_det.txt", "a") as user_det_file: #writing user details in external file
                user_det_file.write(f"--------------------------------\n")
                user_det_file.write(f"Quiz Type : {quiz_type}\n")
                user_det_file.write(f"Name : {name}\n")
                user_det_file.write(f"Age : {age}\n")
            geo() #Calling function

    def mat(): #defining function
        global num
        global opt_num
        global score
        msgbox("➗Math Quiz➗")
        for q, a in mat_qa: #Reads question and answer in qa dictionary to print each
            num+=1 #adds to question number
            user_ans = buttonbox(q, f"Question {num}" , mat_options[opt_num])
            opt_num+=1 #adds to option number
            if user_ans == a:
                score += 1 #adds to score if correct
                msgbox(f"✅Correct!✅\n\nScore : {score}")
            elif user_ans == "Skip":
                msgbox(f"You have skipped the question\n\nThe answer to the question was {a}\n\nScore : {score}")
            elif user_ans == "Exit Quiz":
                msgbox(f"You have ended the quiz and skipped all upcoming questions")
                with open("user_det.txt", "a") as user_det_file:  
                    user_det_file.write(f"Total Score : {score}/{num}\n") #writes user total score to external file
                user_info()
            else:
                msgbox(f"❌Incorrect❌\n\nThe answer is {a}, not {user_ans!r}\n\nScore : {score}") #Tells user answer is wrong and tells user correct answer
        with open("user_det.txt", "a") as user_det_file:  
            user_det_file.write(f"Total Score : {score}/{num}\n")  #writes user total score to external file
        user_info()    
    def che(): #defining function
        global num
        global opt_num
        global score
        msgbox("🧪Chemistry Quiz🧪")
        for q, a in che_qa: #Reads question and answer in qa dictionary to print each
            num+=1 #adds to question number
            user_ans = buttonbox(q, f"Question {num}" , che_options[opt_num])
            opt_num+=1 #adds to option number
            if user_ans == a:
                score += 1 #adds to score if correct
                msgbox(f"✅Correct!✅\n\nScore : {score}")
            elif user_ans == "Skip":
                msgbox(f"You have skipped the question\n\nThe answer to the question was {a}\n\nScore : {score}")
            elif user_ans == "Exit Quiz":
                msgbox(f"You have ended the quiz and skipped all upcoming questions")
                with open("user_det.txt", "a") as user_det_file:  
                    user_det_file.write(f"Total Score : {score}/{num}\n")  #writes user total score to external file
                user_info()
            else:
                msgbox(f"❌Incorrect❌\n\nThe answer is {a}, not {user_ans!r}\n\nScore : {score}") #Tells user answer is wrong and tells user correct answer
        with open("user_det.txt", "a") as user_det_file:  
            user_det_file.write(f"Total Score : {score}/{num}\n")  #writes user total score to external file
        user_info()    
    def gen(): #defining function
        global num
        global opt_num
        global score
        msgbox("🌐General Knowledge🌐")
        for q, a in gen_qa: #Reads question and answer in qa dictionary to print each
            num+=1 #adds to question number 
            user_ans = buttonbox(q, f"Question {num}" , gen_options[opt_num])
            opt_num+=1 #adds to option number
            if user_ans == a:
                score += 1 #adds to score if correct
                msgbox(f"✅Correct!✅\n\nScore : {score}")
            elif user_ans == "Skip":
                msgbox(f"You have skipped the question\n\nThe answer to the question was {a}\n\nScore : {score}")
            elif user_ans == "Exit Quiz":
                msgbox(f"You have ended the quiz and skipped all upcoming questions")
                with open("user_det.txt", "a") as user_det_file:  
                    user_det_file.write(f"Total Score : {score}/{num}\n") #writes user total score to external file
                user_info()
            else:
                msgbox(f"❌Incorrect❌\n\nThe answer is {a}, not {user_ans!r}\n\nScore : {score}") #Tells user answer is wrong and tells user correct answer
        with open("user_det.txt", "a") as user_det_file:  
            user_det_file.write(f"Total Score : {score}/{num}\n") #writes user total score to external file
        user_info()    
    def geo(): #defining function
        global num
        global opt_num
        global score
        msgbox("🌎Geography Quiz🌎")
        for q, a in geo_qa: #Reads question and answer in qa dictionary to print each
            num+=1 #adds to question number
            user_ans = buttonbox(q, f"Question {num}" , geo_options[opt_num])
            opt_num+=1 #adds to option number
            if user_ans == a:
                score += 1 #adds to score if correct
                msgbox(f"✅Correct!✅\n\nScore : {score}")
            elif user_ans == "Skip":
                msgbox(f"You have skipped the question\n\nThe answer to the question was {a}\n\nScore : {score}")
            elif user_ans == "Exit Quiz":
                msgbox(f"You have ended the quiz and skipped all upcoming questions")
                with open("user_det.txt", "a") as user_det_file:  
                    user_det_file.write(f"Total Score : {score}/{num}\n") #writes user total score to external file
                user_info()
            else:
                msgbox(f"❌Incorrect❌\n\nThe answer is {a}, not {user_ans!r}\n\nScore : {score}") #Tells user answer is wrong and tells user correct answer
        with open("user_det.txt", "a") as user_det_file:  
            user_det_file.write(f"Total Score : {score}/{num}\n") #writes user total score to external file
        user_info()    

    def user_info():
        f = open("user_det.txt", "r")
        data = f.read()
        msgbox(data) #Tells user all quiz details
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
        exit()

    #Calling function
    user_option()

#Calling function
quiz()
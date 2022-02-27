from verifiers import *
from cipher import *
from rwaFiles import *
from colors import *
import getpass
passCounter = 0
idCounter = 0
userID = ''

############################################ Start of Register User ############################################
# Register User Function - userid_pswd.csv
def registerUser():
    print("\n\ta) Register User")
    print("\tb) Edit User")
    print("\tc) Delete User")
    print("\td) Retrieve User List")
    print("\te) back to previous")

    adminInput = input("\n\tSelect option: ")
    if adminInput == "a":                                                           # a) Register User
        tOrF = True
        
        while tOrF == True:
            userID = input("\nPlease enter the new user's ID: ")                    # ask for new user's userID
            verifyUserID = checkComma(userID)
            if verifyUserID == True:
                print("Please do not enter a comma in your ID.")
                tOrF = True
            else:
                tOrF = regUsrIDone(verifyUserID)

        tOrF = True
        while tOrF == True:
            userPswd = input("\nPlease enter the new user's Password: ")            # ask for new user's passwd
            tOrF = passcheck(userPswd)                                              # check if the passwd is secure
        
        encryptedPass = encrypt(userPswd)                                           # encrypt passwd with Caesar Cipher

        tOrF = True
        while tOrF == True:
            aOrU = input("Enter (a) for admin account and (u) for user account: ")  # ask if new account is admin or user account
            tOrF = admOrUsr(aOrU)
        
        if aOrU == 'a':                                                             # set total Attempts 
            attempts = 999
        else:
            attempts = qzSettings(3)
        
        tOrF = True
        while tOrF == True:
            scrtQn = input("\nPlease enter a secret recovery question.\n>>> ")      # ask for secret question
            verifyScrtQn = checkComma(scrtQn)
            if verifyScrtQn == True:
                print("Please do not enter a comma in your question.")
                tOrF = True
            else:
                tOrF = False

        tOrF = True
        while tOrF == True:
            scrtAns = input("\nPlease enter your secret question's answer.\n>>> ")  # ask for secret question's answer
            verifyScrtAns = checkComma(scrtAns)
            if verifyScrtAns == True:
                print("Please do not enter a comma in your answer.")
                tOrF = True
            else:
                tOrF = False

        # concatenate userID + userPswd + aOrU + Attempts + secret question + secret question's answer'
        writeIntoFile = (str(userID)+','+str(encryptedPass)+','+str(aOrU)+','+str(attempts) +',' + str(scrtQn)+','+str(scrtAns))

        newUsr(writeIntoFile)                                                       # insert userID and passwd into userid_pswd.csv
        print("\nRegistration Successful!\n")                                       # print successful
        rmvSpaceID()
        registerUser()                                                              # back to menu
        
    elif adminInput == "b":                                                         # b) Edit User Passwd
        tOrF = True
        passchecker = True
        idCounter = 0

        while tOrF == True:
            userID = input("\nPlease enter the existing user's ID: ")               # ask for existing user's userID
            tOrF = regUsrIDtwo(userID,'a') and regUsrIDtwo(userID,'u')
            if tOrF == False:
                print("User exists.")
            idCounter += 1
            if idCounter == 3 and tOrF == True:
                print("You have tried too many times, returning you to previous menu.\n")
                startAdmin()
        
        tOrF = True
        passCounter = 0
        
        while tOrF == True:
            userPswd = input("\nPlease enter the user's Password: ")                # ask for the user's passwd
            encryptedPass = encrypt(userPswd)
            tOrF = usrPswd(userID,encryptedPass)                                    # check if the passwd is correct

            passCounter += 1
            if passCounter == 3 and tOrF == True:                                   # limit password tries
                print("You have tried too many times.")
                tOrF = False
                if tOrF == False:
                    registerUser()                                                  # back to menu
        
        while passchecker == True :
            newUsrPswd = input("\nPlease enter the new password: ")                 # ask for user's new passwd
            passchecker = passcheck(newUsrPswd)                                     # check if the passwd is secure
        
        encryptedPass = encrypt(newUsrPswd)
        editPswd(userID,encryptedPass)                                              # insert passwd into correct line in userid_pswd.csv
        rmvSpaceID()
        print("Password edited successfully.")                                      # print successful
        registerUser()                                                              # back to menu

    elif adminInput == "c":                                                         # c) Delete User
        tOrF = True
        idCounter = 0

        while tOrF == True:
            userID = input("\nPlease enter the existing user's ID: ")               # ask for user's userID to delete
            tOrF = regUsrIDtwo(userID,'a') and regUsrIDtwo(userID,'u') 
            idCounter += 1
            if idCounter == 3 and tOrF == True:
                print("You have tried too many times, returning you to previous menu.\n")
                startAdmin()

        if dblConfirm() == True:                                                    # ask for user's input to double confirm deletion, if not, back to menu
            pass
        else:
            print("You entered (n), returning you to the menu.")
            registerUser()
        
        removeUsr(userID)                                                           # delete respective line in userid_pswd.csv
        rmvSpaceID()
        print("User deleted successfully.")                                         # print successful
        registerUser()                                                              # back to menu

    elif adminInput == "d":                                                         # d) Retrieve User List
        usrList()                                                                   # print list of users from userid_pswd.csv
        registerUser()                                                              # back to menu

    elif adminInput == "e":                                                         # e) back to previous
        startAdmin()

    else:                   
        print("You have not entered a valid option")                                # invalid input
        registerUser()

############################################ Start of Quiz Settings ############################################
# Setup Quiz Function & Modules - quiz_settings.csv & quiz_topics.csv 
def setupQuiz(): #set quiz timer, 
    print("\n\ta) Set Quiz Timer")
    print("\tb) Set Number of Questions Tested")
    print("\tc) Set Total Attempts for Quiz")
    print("\td) Create New Quiz Topic")
    print("\te) Delete Existing Quiz Topic")
    print("\tf) Edit Name of a Topic")
    print("\tg) back to previous")

    adminInput = input("\n\tSelect option: ")
    if adminInput == "a":                                                           # a) Set Quiz Timer
        tOrF = True
        selection = 'Quiz Timer'
        
        while tOrF == True:
            qzTimer = input("Please enter the new quiz timer: ")                    # ask for user's input for quiz timer
            if qzTimer.isnumeric():
                tOrF = intCheck(float(qzTimer))
            else:
                print("Please enter a valid integer.")                              # invalid input
                tOrF = True
        
        quizTimer(qzTimer,selection)                                                # update quiz_settings.csv on quiz timer
        print("Quiz timer updated successfully.")                                   # print successful
        setupQuiz()                                                                 # back to menu

    elif adminInput == "b":                                                         # b) Set Number of Questions Tested
        tOrF = True
        selection = 'No. of Questions'

        while tOrF == True:
            qzNum = input("Please enter the number of questions to be tested: ")    # ask for user's input for number of questions to be tested
            if qzNum.isnumeric():
                tOrF = intCheck(float(qzNum))
            else:
                print("Please enter a valid integer.")                              # invalid input
                tOrF = True
        
        quizTimer(qzNum,selection)                                                  # update quiz_settings.csv on number of questions to be tested
        print("Number of questions updated successfully.")                          # print successful
        setupQuiz()                                                                 # back to menu

    elif adminInput == "c":                                                         # c) Set Total Marks for Quiz
        tOrF = True
        selection = 'Attempts'
        
        while tOrF == True:
            qzAtmpt = input("Please enter the total attempts to be set: ")          # ask for user's input for total attempts set for the quiz
            if qzAtmpt.isnumeric():
                tOrF = intCheck(float(qzAtmpt))
            else:
                print("Please enter a valid integer.")                              # invalid input
                tOrF = True
        
        quizTimer(qzAtmpt,selection)                                                # update quiz_settings.csv on total marks of entire quiz
        print("Number of attempts updated successfully.")                           # print successful
        setupQuiz()                                                                 # back to menu
    
    elif adminInput == "d":                                                         # add new module

        tOrF = True
        while tOrF == True:
            newTopic = input("Enter the new topic name: ")                          # ask for existing module name
            checkModule = checkTopicOne(newTopic)                                   # check if module actually existing 
            if checkModule == False:                                                # if module don't exist, check for comma
                verifyNewTopic = checkComma(newTopic)
                if verifyNewTopic == True or len(newTopic) == 0:                    # if got comma, print error message
                    print("Please do not enter (, or | or &) in your topic name.")  # invalid input
                    tOrF = True                                                         
                else:                                                               # if don't have comma, continue on to 
                    tOrF = False
                    addNewTopic(newTopic)                                           # add new module in 
                    print("\n[SUCCESS] Topic successfully created. Sending you back to the menu.")
                    setupQuiz()                                                     #back to this menu
            else:                                                                   # elif module already exist, print error msg
                print("\n[ERROR] Topic already exists, sending you back to the menu.")
                setupQuiz()                                                         # back to this menu

    elif adminInput == "e":                                                         # delete existing module
        tOrF = False

        while tOrF == False:
            # ask for user's input on question to delete
            moduleToDel = input("\nPlease enter the topic to delete: ")
            tOrF = checkTopicOne(moduleToDel)                                      # check if module exists, if not, print does not exist and ask again
        
        if dblConfirm() == True:                                                    # ask for user's input to double confirm deletion, if not, back to menu
            pass
        else:
            print("You entered (n), returning you to the menu.")
            setupQuiz()
        
        delTopic(moduleToDel)                                                      # delete selected question in question_pool.csv 
        rmvSpaceTopic()

        print("Topic deleted successfully.")                                       # print successful
        setupQuiz()
    elif adminInput == "f":                                                         # edit name of existing module
        tOrF = False

        while tOrF == False:
            # ask for user's input on question to delete
            moduleToEdit = input("\nPlease enter the topic to edit: ")
            tOrF = checkTopicOne(moduleToEdit)                                     # check if module exists, if not, print does not exist and ask again
        
        while tOrF:
            nameToChg = input("What do you want to change the name to? ")           # ask user for change   
            verifyNameToChg = checkComma(nameToChg)
            if verifyNameToChg == True or len(nameToChg) == 0:
                print("Please do not enter (, or | or &) in your topic name.")
                tOrF = True
            else:
                tOrF = False            


        if dblConfirm() == True:                                                    # ask for user's input to double confirm deletion, if not, back to menu
            pass
        else:
            print("You entered (n), returning you to the menu.")
            setupQuiz()

        # if yes, write new name into csv file
        editTopicName(moduleToEdit,nameToChg)
        editQuesPoolTopics(moduleToEdit,nameToChg)
        editQuizzesTopics(moduleToEdit,nameToChg)
        rmvSpaceQn()
        rmvSpaceTopic()
        print("Module updated successfully.")
        setupQuiz()


    elif adminInput == "g":                                                         # d) back to previous
        startAdmin()

    else:                   
        print("You have not entered a valid option")                                # invalid input
        setupQuiz()

############################################ Start of Define Options ############################################
# Define Options Functions - question_pool.csv
def defineOptions():
    print("\n\ta) Add Question")
    print("\tb) Edit Question")
    print("\tc) Delete Question")
    print("\td) Add Quiz")
    print("\te) Delete Quiz")
    print("\tf) Retrieve Question List")
    print("\tg) back to previous")

    adminInput = input("\n\tSelect option: ")
    if adminInput == "a":                                                           # a) Add Question
        
        tOrF = True
        while tOrF == True:
            newQn = input("Enter the new question: ")                               # ask for user's input on new question
            checkQn = regQnone(newQn)                                               # check if question already exist, if exist, print already exist
            if checkQn == False:                                                    # if question doesn't exist, check for comma
                verifyNewQn = checkComma(newQn)
                if verifyNewQn == True:                                             # if got comma, print error message
                    print("Please do not enter a comma in your question.")
                    tOrF = True                                                         
                else:                                                               # if don't have comma, continue on to 
                    tOrF = False
            else:
                tOrF = True

        # ask for question options
        tOrF = True
        while tOrF:
            newQnA = input("Enter the first option a) ")                            # ask for question's first option
            verifyNewQnA = checkComma(newQnA)
            if verifyNewQnA == True:                                                # if got comma, print error message
                print("Please do not enter a comma in your question.")
                tOrF = True                                                         
            else:                                                                   # if don't have comma, continue on to 
                tOrF = False

        tOrF = True
        while tOrF:
            newQnB = input("Enter the second option b) ")                           # ask for question's first option
            verifyNewQnB = checkComma(newQnB)
            if verifyNewQnB == True:                                                # if got comma, print error message
                print("Please do not enter a comma in your question.")
                tOrF = True                                                         
            else:                                                                   # if don't have comma, continue on to 
                tOrF = False
                
        tOrF = True
        while tOrF:
            newQnC = input("Enter the third option c) ")                            # ask for question's first option
            verifyNewQnC = checkComma(newQnC)
            if verifyNewQnC == True:                                                # if got comma, print error message
                print("Please do not enter a comma in your question.")
                tOrF = True                                                         
            else:                                                                   # if don't have comma, continue on to 
                tOrF = False

        tOrF = True
        while tOrF:
            newQnD = input("Enter the fourth option d) ")                           # ask for question's first option
            verifyNewQnD = checkComma(newQnD)
            if verifyNewQnD == True:                                                # if got comma, print error message
                print("Please do not enter a comma in your question.")
                tOrF = True                                                         
            else:                                                                   # if don't have comma, continue on to 
                tOrF = False

        newQnAns = qnAnsOption()                                                    # ask for question answer

        #what topic do you want to add this question to?
        
        questionFormat = (f'{newQn},{newQnA},{newQnB},{newQnC},{newQnD},{newQnAns},{chooseTopic()}')# concatenate question answers and options together
        addQuestion(questionFormat)                                                 # write question,a,b,c,d,ans into question_pool.csv
        print("Question added successfully.")                                       # print successful
        defineOptions()                                                             # back to menu

    elif adminInput == "b":                                                         # b) Edit Question
        tOrF = True
        options = True
        
        while tOrF == True:
            qnToEdit = input("\nPlease enter the question to edit: ")               # ask for user's input on question to edit
            tOrF = regQntwo(qnToEdit)                                               # check if question exists, if not, print does not exist
        
        while options == True:
            qnOpToEdit = input("What do you want to edit (qn|a|b|c|d|ans)? ")       # ask for user's input on whether to change question,a,b,c,d, or ans

            if qnOpToEdit == 'qn':
                tOrF = True
                while tOrF:
                    qnOpChg = input("What do you want to change it to? ")           # ask user for change   
                    verifyQnOpChg = checkComma(qnOpChg)
                    if verifyQnOpChg == True:
                        print("Please do not enter a comma in your question.")
                        tOrF = True
                    else:
                        tOrF = False

                editQn(qnToEdit,qnOpChg,0)                                          # write changes into question_pool.csv
                options = False
                
            elif qnOpToEdit == 'a':
                tOrF = True
                while tOrF:
                    qnOpChg = input("What do you want to change it to? ")           # ask user for change   
                    verifyQnOpChg = checkComma(qnOpChg)
                    if verifyQnOpChg == True:
                        print("Please do not enter a comma in your option.")        # if input has comma, prompt for change again
                        tOrF = True
                    else:
                        tOrF = False                                                
                editQn(qnToEdit,qnOpChg,1)                                          # write changes into question_pool.csv
                options = False

            elif qnOpToEdit == 'b':
                tOrF = True
                while tOrF:
                    qnOpChg = input("What do you want to change it to? ")           # ask user for change   
                    verifyQnOpChg = checkComma(qnOpChg)
                    if verifyQnOpChg == True:
                        print("Please do not enter a comma in your option.")        # if input has comma, prompt for change again
                        tOrF = True
                    else:
                        tOrF = False
                editQn(qnToEdit,qnOpChg,2)                                          # write changes into question_pool.csv
                options = False

            elif qnOpToEdit == 'c':
                tOrF = True
                while tOrF:
                    qnOpChg = input("What do you want to change it to? ")           # ask user for change   
                    verifyQnOpChg = checkComma(qnOpChg)
                    if verifyQnOpChg == True:
                        print("Please do not enter a comma in your option.")        # if input has comma, prompt for change again
                        tOrF = True
                    else:
                        tOrF = False
                editQn(qnToEdit,qnOpChg,3)                                          # write changes into question_pool.csv
                options = False
                
            elif qnOpToEdit == 'd':
                tOrF = True
                while tOrF:
                    qnOpChg = input("What do you want to change it to? ")           # ask user for change   
                    verifyQnOpChg = checkComma(qnOpChg)
                    if verifyQnOpChg == True:
                        print("Please do not enter a comma in your option.")        # if input has comma, prompt for change again
                        tOrF = True
                    else:
                        tOrF = False
                editQn(qnToEdit,qnOpChg,4)                                          # write changes into question_pool.csv
                options = False

            elif qnOpToEdit == 'ans':                                               # ask user for change
                qnOpChg = abcdOption()                                              # verify the input is (a) to (d) only
                editQn(qnToEdit,qnOpChg,5)                                          # write changes into question_pool.csv
                options = False
            else:
                print("Please input a valid options.")                              # invalid input
                options = True
        
        print("Successful!")                                                        # print successful
        rmvSpaceQn()
        defineOptions()                                                             # back to menu
    elif adminInput == "c":                                                         # c) Delete Question
        tOrF = True

        while tOrF == True:
            # ask for user's input on question to delete
            qnToDel = input("\nPlease enter the question to delete: ")
            tOrF = regQntwo(qnToDel)                                                # check if question exists, if not, print does not exist and ask again
        
        if dblConfirm() == True:                                                    # ask for user's input to double confirm deletion, if not, back to menu
            pass
        else:
            print("You entered (n), returning you to the menu.")
            defineOptions()
        
        removeQn(qnToDel)                                                           # delete selected question in question_pool.csv 
        rmvSpaceQn()
        print("Question deleted successfully.")                                     # print successful
        defineOptions()                                                             # back to menu

    elif adminInput == 'd':                                                         # add quiz

        school = {'course':'DISM','module':'Beginner Math'}

        tOrF = True
        while tOrF == True:
            newQn = input("\nEnter the new quiz name: ")                              # ask for user's input on new quiz name
            if len(newQn) == 0 :
                print("Please enter a proper quiz name")
                tOrF = True
            else:
                checkQn = checkQuizOne(newQn)                                         # check if quiz already exist, if exist, print already exist
                if checkQn == False:                                                  # if quiz doesn't exist, check for comma
                    verifyNewQn = checkComma(newQn)
                    if verifyNewQn == True:                                           # if got comma, print error message
                        print("Please do not enter (, or | or &) in your quiz name.")
                        tOrF = True                                                         
                    else:                                                             # if don't have comma, continue on to 
                        tOrF = False
                else:
                    print("Quiz name already exists. Try again.")
                    tOrF = True

        def addNewTopics():
            topics = 0
            vessel = []
            tOrF = True
            print(styleStr('\nInclude minimally 2 different topics in the quiz.',rgb=(255,255,0)))
            while tOrF:
                    # ask for 1st topic to include inside
                print("\nWhich topic do you want to include in the quiz?")
                firstTopic = chooseTopic()

                # ask for how many questions to add, MUST VERIFY IT IS A VALID INPUT
                integer = True
                while integer:
                    noOfQuestions = input("How many questions do you want to add (0-60)? ")
                    integer = intCheck(float(noOfQuestions))

                vessel.append(f"{firstTopic},{noOfQuestions}")    # <--------------------------------------------
                topics += 1
                if topics > 1:
                    # ask to stop or add more topics

                    newLine = ''

                    for a in vessel:
                        aSplit = a.split(sep=',')
                        vessel.remove(a)

                        for b in vessel:
                            bSplit = b.split(sep=',')
                            if bSplit[0] == aSplit[0]:
                                
                                vessel.remove(b)

                                newCount = str(int(bSplit[1]) + int(aSplit[1]))

                                vessel.insert(0,f"{aSplit[0]},{newCount}")
                                
                                break
                        else:
                            vessel.insert(0,a)


                    for i in vessel:
                        iSplit = i.split(sep=',')
                        newLine += f"&&{iSplit[0]},{iSplit[1]}"

                    if len(vessel) == 2:

                        tester = True
                        while tester:
                            moreTopics = input("\nDo you want to add more topics (y|n): ")

                            # if stop:
                            if moreTopics == "n":
                                # could strip and add the list items into a string before returning
                                return newLine

                            # elif add more topics
                            elif moreTopics == "y":
                                tester = False
                                tOrF = True
                            else:
                                print("\nInvalid input, try again.")
                                tester = True
                    
        newTopics = addNewTopics()

        newQuizString = f"{school['course']}|{school['module']}|{newQn}|{newTopics}"
        regNewQuiz(newQuizString)
        print("Registration successful!")
        rmSpaceQuiz()
        defineOptions()

    elif adminInput == "e":                                                         # delete quiz
        
        tOrF = True
        while tOrF == True:
            newQn = input("Enter the quiz name to delete (case-sensitive): ")                              # ask for user's input on new quiz name
            checkQn = checkQuizOne(newQn)                                           # check if quiz already exist, if exist, print already exist
            if checkQn == True: 
                if dblConfirm() == True:                                            # ask for user's input to double confirm deletion, if not, back to menu
                    deleteQuiz(newQn)
                    defineOptions()
                else:
                    print("You entered (n), returning you to the menu.")
                    defineOptions()
                
                                                      # back to menu
            else:
                print("Quiz doesn't exist, sending you back to the menu.")
                tOrF = True
                # send back to menu
                defineOptions()

    elif adminInput == "f":                                                         # d) Retrieve Question List
        qnList()                                                                    # print list of  questions only from question_pool.csv
        defineOptions()                                                             # back to menu

    elif adminInput == "g":                                                         # e) back to previous
        startAdmin()

    else:                                                                           # invalid input
        print("You have not entered a valid option") 
        defineOptions()


############################################ Plus Minus Attempts ############################################
def plusMinusA():
    global userID
    print("\n\ta) Reset All Attempts")
    print("\tb) Plus 1 Attempt to all users")
    print("\tc) Minus 1 Attempt to all users")
    print("\td) Set to unlimited attempts")
    print("\te) back to previous")

    #Filter Input
    adminInput = input("\n\tSelect option: ")
    if adminInput == "a":   # a) Reset All Attempts
        resetAttempt()      
        print("Successfully reset all attempts to users.")
        plusMinusA()

    elif adminInput == "b": # b) Plus 1 Attempt to all users
        plusAttempt()
        print("Successfully add 1 attempt to users.")
        plusMinusA()
        
    elif adminInput == "c": # c) Minus 1 Attempt to all users
        minusAttempt()
        print("Successfully minus 1 attempt to users.")
        plusMinusA()

    elif adminInput == "d": # d) Set to unlimited attempts
        unlimitedAttempt()
        print("Successfully set attempts to unlimited.")
        plusMinusA()
        
    
    elif adminInput == "e": # e) back to previous
        startAdmin()
    else:                   # invalid input
        print("You have not entered a valid option.") 
        plusMinusA()

############################################ Start of Generating Report ############################################
# Generate Report Function - quiz_results.csv
def genReport():
    print("\n\ta) Retrieve Report of Specific Quiz")
    print("\tb) Retrieve Report of All")
    print('\tc) Back to previous menu')

    userInput = input("\n\tSelect Option: ")

    if userInput == "a":
        selectedQuiz = chooseQuiz()

        if selectedQuiz == False:
            print("\nNo existing quiz currently.")
            genReport()

        resultsList = ''
        resultsList = quizResults(selectedQuiz)

        r = 0
        for i in resultsList:
            r += 1
            #resultsList +=str(r)+'. ' + i + '\n'
            print(str(r)+'. ' + i)

        genReport()

    elif userInput == 'b':
        resultList() # get quiz results from quiz_results.csv
        genReport() # return back to menu
    elif userInput == 'c':
        startAdmin()
    else:                                           # invalid input
        print("\n\tInvalid input.")
        genReport() # return back to menu

############################################ Start of Admin Program ##########################################
def startAdmin():
    
    #Provide Options
    print("\na) User Functions")
    print("b) Define various options")
    print("c) Setup the pool of quiz questions")
    print("d) Plus Minus Attempts")
    print("e) Retrieve Results") 
    print("f) Exit")

    #Filter Input
    adminInput = input("\nSelect option: ")
    if adminInput == "a":   # a) Register User
        registerUser()
        
    elif adminInput == "b": # b) Define various options
        
        setupQuiz()
    elif adminInput == "c": # c) Setup the pool of quiz questions
        defineOptions()
        
    elif adminInput == "d": # d) Plus Minus Attempts
        plusMinusA()

    elif adminInput == "e": # e) Retrieve Results
        genReport()
        
    
    elif adminInput == "f": # f) Exit
        exit()
    else:                   # invalid input
        print("You have not entered a valid option.") 
        startAdmin()

############################################ Start of Admin Login ##########################################

def adminLogin():
    global userID
    global idCounter
    global passCounter
    idCount = True
    tOrF = True

    print("<<<Welcome to Admin Login Page>>> ")                                     # print welcome message
    while tOrF == True and idCount == True:
        userID = input("\nPlease enter the admin user's ID: ")                      # check if userID exists, if not, ask again
        tOrF = adminORuser(userID)
        if tOrF == True:
            print("Invalid admin user")
        idCounter += 1
        if idCounter == 3 and tOrF == True:                                         # limit id tries
            print("You have tried too many times.")
            exit()

    tOrF = True
    passCount = True
    while tOrF == True and passCount == True:        
        userPswd = getpass.getpass("\nPlease enter the admin user's Password: ")    # ask for password 
        # encrypt with Caesar cipher and check it against userid_pswd.csv, if it's not a match, ask to re-enter
        encryptedPass = encrypt(userPswd)
        tOrF = usrPswd(userID,encryptedPass)

        passCounter += 1
        if passCounter == 3 and tOrF == True:                                       # limit password tries
            print("You have tried too many times.")
            passCount = False
            exit()
            
    if tOrF == False:
        startAdmin()                                                                # if admin login successful, move onto options

adminLogin()


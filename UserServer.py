import socket
import threading
from verifiers import *
from rwaFiles import *
from cipher import *
import random
from colors import *
from datetime import datetime
HEADER = 4096
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =(SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
MAINMENU = "\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit"
print(f"Server : {SERVER}, Port : {PORT}")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):                              #meant to handle the indiv connection between the client and server so one client and one server
    
                                                
    print(f"[NEW CONNECTION] {addr} connected.")
    userInput = ''
    global connected
    def serverSend(msg):
        conn.send(str(msg).encode(FORMAT))

    connected = True
    while connected:
        userInput = 'Start'
        def serverRecv():
            global connected
            msg = conn.recv(HEADER).decode(FORMAT)
           
            if msg == DISCONNECT_MESSAGE or msg == 'x':
                connected = False
                print(f"[{addr}] {msg}")
                conn.close()
                return False
            else:
                print(f"[{addr}] {msg}")
                return msg

        welcomeMessage = ("\n***Welcome to Quiz Application***"+ MAINMENU)                      
        serverSend(welcomeMessage)
        while userInput == 'Start':                                                             # START OF QUIZ APPLICATION
            
            userInput = serverRecv()

            if userInput:

                userInputList = userInput.split(sep = ',')
                userInput = userInputList[0]
                userID = userInputList[1]
                
                while userInput == 'a':                                                          # Start Quiz Application
                    
                    userPass = userInputList[2]

                    # check ID n Pass
                    tOrF = True
                    while tOrF:
                        #check ID
                        tOrF = regUsrIDtwo(userID,'a') and regUsrIDtwo(userID,'u')

                        if tOrF == True:    # if user does not exist
                            serverSend("User does not exist. Sending you back to main menu."+MAINMENU)
                            tOrF = False
                            userInput = 'Start'

                        elif tOrF == False: # if user exists

                            encryptedPass = encrypt(userPass)
                            tOrF = usrPswd(userID,encryptedPass)

                            if tOrF == True: # if wrong password
                                serverSend("User exists but wrong password. Sending you back to main menu." + MAINMENU)
                                tOrF = False
                                userInput = 'Start'

                            elif tOrF == False: # if correct password, query user next menu

                                attemptsLeft = usrAttempts(userID)                                              # check attempts left

                                if attemptsLeft == True:                                                        # if 0 attempts left, return to menu
                                    userInput = 'Start'
                                    serverSend("User does not have anymore attempts left. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit" or condition == "User exists but wrong password. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit")
                                
                                else:
                                    userInput = "Login successful."
                                    while userInput == "Login successful.":
                                        serverSend(userInput)

                                        print(userInput)
                                        userInput = serverRecv()
                                        
                                        if userInput:
                                            if userInput == 'View Previous Attempts': # view previous attempts and return to main menu
                                                resultMsg = ''
                                                resultList = userResults(userID)

                                                r = 0
                                                for i in resultList:
                                                    r += 1
                                                    resultMsg +=str(r)+'. ' + i + '\n'
                                                serverSend(resultMsg + MAINMENU)
                                                userInput = 'Start'

                                            elif userInput == 'Back to previous menu': # back to previous menu
                                                serverSend(MAINMENU)
                                                userInput = 'Start'

                                            else:                                       # retrieve selected quiz questions

                                                quizLine = retrieveQuiz(userInput)
                                                quizList = quizLine.split(sep='|')

                                                course = quizList[0]
                                                module = quizList[1]
                                                quizName = quizList[2]

                                                topicList = quizList[3].split(sep='&&')

                                                answerList = []
                                                questionVessel = f'{course}|{module}|{quizName}|'
                                                
                                                for i in topicList:
                                                    if i == '':
                                                        pass
                                                    else:
                                                        topicAndNumber = i.split(sep=',')

                                                        topic = topicAndNumber[0]
                                                        number = topicAndNumber[1]

                                                        # retrieve questions from question pool and put into a list

                                                        questionList = retrieveQuestions(topic)
                                                        questionListSplit = questionList.split(sep='&&')
                                                        random.shuffle(questionListSplit)
                                                        r = 0
                                                        
                                                            
                                                        for i in questionListSplit:

                                                            r += 1

                                                            if i == '':
                                                                r -= 1
                                                                pass
                                                            else:
                                                                
                                                                questionAndAnswer = i.split(sep=',')

                                                                question = questionAndAnswer[0]
                                                                optA = questionAndAnswer[1]
                                                                optB = questionAndAnswer[2]
                                                                optC = questionAndAnswer[3]
                                                                optD = questionAndAnswer[4]
                                                                answer = questionAndAnswer[5]

                                                                if r <= int(number):
                                                                    answerList.append(answer)
                                                                    questionVessel += f"&&{question},{optA},{optB},{optC},{optD}"
                                                                else:
                                                                    pass

                                                serverSend(questionVessel)                  # send questions and options over to client
                                                
                                                userAnswers = serverRecv()
                                                if userAnswers:
                                                    userAnswerList = userAnswers.split(sep=',')
                                                    userAnswerList.pop(0)   # pops out ''
                                                    userAnswerList.pop(0)   # pops out '0\n'

                                                    totalMarks = 0

                                                    for f in range(len(answerList)):
                                                        if userAnswerList[f] == answerList[f]:                                      # check if answer is correct
                                                            totalMarks += 2                                                         # for every answer that is correct, add 2 marks
                                                        else:
                                                            pass

                                                    fullMarks = len(answerList)*2
                                                    if totalMarks == 0:
                                                        percentage = 0.0
                                                    else:
                                                        percentage = round(totalMarks / fullMarks * 100,2)                          # calculate percentage

                                                    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                # date & time

                                                    #write results into quiz_results.csv
                                                    resultToWrite = (f"{userID},{str(totalMarks)},{str(percentage)},{current_date_time},{quizName}")
                                                    wResults(resultToWrite)
                                                    rmvSpaceR()

                                                    markAndPercentage = f"{totalMarks},{percentage}"
                                                    serverSend(markAndPercentage)

                                                    tOrF = True
                                                    if tOrF == True:
                                                        tOrF = adminORuser(userID)                                                  # check if user is admin or user
                                                        if tOrF == True:                                                            # if user:
                                                            attemptCount(userID)                                                    # take away 1 attempt count from user

                                                    
                                                    userInput = serverRecv()                                                        # check if user wants to do another quiz

                                                    if userInput == 'y':                                                            # go back to login successful if yes
                                                        userInput = "Login successful."
                                                    
                                                    else:                                                                           # close connection if dont want
                                                        conn.close()
                                                        break



                while userInput == 'b': # Register New User
                    encryptedPass = userInputList[2]
                    scrtQn = userInputList[3]
                    scrtAns = userInputList[4]

                    tOrF = True
                    while tOrF:
                        #check ID
                        tOrF = regUsrIDtwo(userID,'a') and regUsrIDtwo(userID,'u')
                        if tOrF == False:    # if user exist, send error message that new user cannot be created
                            serverSend("\nUser ID is already taken. Sending you back to main menu.\n***Welcome to Quiz Application***\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit")
                            tOrF = False
                            userInput = 'Start'

                        elif tOrF == True: # if user does not exists, send message that new user will be created

                            # create string
                            writeIntoFile = (str(userID)+','+str(encryptedPass)+',u'+','+str(qzSettings(3)) + ',' + str(scrtQn) + ',' + str(scrtAns) )
                            # write in the new user into csv
                            newUsr(writeIntoFile)
                            rmvSpaceID()

                            serverSend("\nUser ID is availabe. New user registered.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit")
                            userInput = 'Start'
                            tOrF = False

                while userInput == 'c': # Reset Password
                    
                    # check if user ID exists
                    tOrF = True
                    while tOrF:
                        #check ID
                        tOrF = regUsrIDtwo(userID,'a') and regUsrIDtwo(userID,'u')

                        # SEND CONDITIONAL text OR secret question
                        if tOrF == True:    # if user does not exist
                            serverSend("User does not exist. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit")
                            tOrF = False
                            userInput = 'Start'

                        elif tOrF == False:   # send scrtQn
                            secretQuestion = secretQ(userID)
                            serverSend(secretQuestion)

                            # receive secret answer
                            userInput = serverRecv()
                            # check if secret answer is correct
                            newtOrF = secretA(userID,userInput)
                            # determine CONDITIONAL text 'YES' or 'NO'
                            if newtOrF == True:
                                condition = 'NO'
                            else:
                                condition = 'Enter new password'

                            # if CONDITIONAL text == 'YES': # means scrt answer is correct
                            if condition == 'Enter new password':
                                # SEND CONDITIONAL text
                                serverSend(condition)
                                # RECEIVE new password from server
                                newPass = serverRecv()
                                # write in the new user info into csv
                                editPswd(userID,newPass)
                                rmvSpaceID()
                                # SEND confirmation message+Main Menu and go back to main menu
                                serverSend("Password successfully updated.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit")
                                userInput = 'Start'
                                #tOrF = False

                            # elif CONDITIONAL text == 'NO':
                            elif condition == 'NO':
                                # SEND CONDITIONAL text+Main Menu and go back to main menu
                                serverSend("Wrong answer. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit")
                                userInput = 'Start'
                                #tOrF = False

def start():
    print(f"Server is listening on {SERVER}")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count()-1}")



print("Starting server....")
start()

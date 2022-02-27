# StudentID:	p2136798
# Name:	        Gan Hanyong
# Class:		DISM/FT/1B/02   
# Assessment:	CA2
# 
# Script name:	UserClient.py
# 
# Purpose:  	Creation, editing, and deletion of users, questions, and quiz settings. To generate results report too.
#
# Usage syntax:	F5
# 
# References: https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/
#
# Python ver:	Python 3.9.7

import socket
import time
import threading
from rwaFiles import *
from verifiers import *
from cipher import *
from colors import *
import getpass
HEADER = 4096
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =(SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
print(f"Server : {SERVER}, Port : {PORT}")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

timer = qzSettings(1)
stop_threads = False
############################################ Start of Countdown ############################################
def countdown():
    global timer
    global stop_threads
    timer *=  60                                                                    # TIMER in minutes * 60 seconds
    for i in range(timer):
        timer-=1
        time.sleep(1)
        if stop_threads:
            break

cdthread = threading.Thread(target = countdown)                             # threading target countdown TIMER function

def recv():
    
    return client.recv(4096).decode(FORMAT)

def send_msg(msg):
    message = msg.encode(FORMAT)

    client.send(message)
    

print(recv())
condition = 'Start'
while condition == 'Start':

    tOrF = True
    while tOrF:
        condition = input("Enter (a) to (c) to continue, (x) to exit: ")
        # validate input
        if condition == 'a' or condition =='b' or condition =='c' or condition =='x':
            
            tOrF = False
        else:
            print("Please enter a proper value.")

    while condition == 'a': #Start Quiz Application
        
        tOrF = True
        while tOrF:
            print("\nEnter your user ID")
            userID = input('\n>>> ')
            commaVerifier = checkComma(userID)
            if commaVerifier == True:
                tOrF = True
            else:
                tOrF = False

        tOrF = True
        while tOrF:
            print("\nEnter your user Password")
            userPass = getpass.getpass('\n>>> ')
            commaVerifier = checkComma(userPass)
            if commaVerifier == True: 
                tOrF = True
            else:
                tOrF = False

        login = f"{condition},{userID},{userPass}"
        send_msg(login)

        condition = 'attempt'
        while condition == 'attempt':

            condition = recv()
            if condition == "User does not exist. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit" or condition == "User exists but wrong password. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit":
                print(condition)
                condition = 'Start'

            elif condition == "User does not have anymore attempts left. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit" or condition == "User exists but wrong password. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit":
                print(condition)
                condition = 'Start'

            elif condition == "Login successful.":
                print(condition)
                userInput = chooseQuizForUser()

                if userInput == "View Previous Attempts":
                    send_msg(userInput)
                    print(recv())
                    condition = 'Start'

                elif userInput == "Back to previous menu":
                    send_msg(userInput)
                    print(recv())
                    condition = 'Start'

                elif userInput == "Exit":
                    send_msg(DISCONNECT_MESSAGE)
                    break
                
                else:
                    send_msg(userInput)

                    

                    quizInformation = recv()
                    sections = quizInformation.split(sep='|')
                    course = sections[0]
                    module = sections[1]
                    quizName = sections[2]
                    questions = sections[3]

                    individualQuestion = questions.split(sep='&&')

                    print(f"Course Name: {course}\nModule Name: {module}\nAssessment Component: {quizName}")

                    cdthread.start()                                                            # initiate threading function

                    print(styleStr((f"Time allowed: {qzSettings(1)} minute(s)."),rgb=(255,200,100)))# get timer from quiz setting

                    noOfQns = (len(individualQuestion))
                    answerList = ["0\n"] * noOfQns # IMPT

                    condition = 'startQuiz'
                    while condition == 'startQuiz':                    
                        qnNum = 0
                        
                        while qnNum < noOfQns-1: #maybe put a -1 to noofqns
                            qnNum += 1
                            if individualQuestion[qnNum] == '':
                                pass
                            else:
                                qnPool = individualQuestion[qnNum].split(sep=',')
                                print(f'\n\tQuestion {qnNum}: '+qnPool[0]+'\n')
                                print(f'\ta) {qnPool[1]}\n\tb) {qnPool[2]}\n\tc) {qnPool[3]}\n\td) {qnPool[4]}\n')

                                usrAns = quizOption(qnNum,noOfQns-1)

                                if qnNum < noOfQns:
                                    if usrAns == 'N':
                                        qnNum += 0
                                    elif usrAns == 'P':
                                        if qnNum <=0:
                                            pass
                                        else:
                                            qnNum -= 2
                                    else:
                                        answerList[qnNum] = usrAns

                                elif qnNum >= noOfQns:
                                    print()

                            if timer == 0:                                                          # if TIMER reaches 0, auto submit quiz
                                print("You have ran out of time. Voiding this attempt.")
                                print("DISCONNECTING...")
                                time.sleep(3)
                                send_msg(DISCONNECT_MESSAGE)
                                exit()
                                
                                

                        qnNumber = 0
                        while qnNumber < noOfQns-1:
                            qnNumber += 1
                            qnPool = individualQuestion[qnNumber].split(sep=',')
                            print(f'\n\tQuestion {qnNumber}: '+qnPool[0]+'\n')
                            print(f'\ta) {qnPool[1]}\n\tb) {qnPool[2]}\n\tc) {qnPool[3]}\n\td) {qnPool[4]}\n\t(Your Answer) >>> {answerList[qnNumber]}')
                            condition = 'endQuiz'
                        
                    
                        while condition == 'endQuiz':
                            tOrF = True
                            while tOrF == True:
                                submission = input(styleStr(("\nEnter 0 to submit or 1 to make changes: "),rgb=(255,200,100)))            # ask user to confirm submission or to change answer
                                if submission == "0":
                                    tOrF = False
                                    condition = 'printResults'

                                    answerString = ''
                                    for i in answerList:
                                        answerString += f',{i}'
                                    send_msg(answerString)

                                elif submission == "1":
                                    tOrF = False
                                    condition = 'startQuiz'
                                else:
                                    print("Please enter a valid input.")
                                    tOrF = True

                        while condition == 'printResults':
                            markAndPercentage = recv()                  # RECEIVE MESSAGE HERE
                            mApList = markAndPercentage.split(sep=',')  # mApList stands for markAndPercentage's List
                            
                            totalMarks = mApList[0]
                            percentage = float(mApList[1])

                            print(f'\nTotal Marks: {totalMarks}')  
                            print(f"\nYou've scored {percentage}%.")

                            if percentage >= 50 and percentage < 60:                                        # print out grade
                                print(styleStr(("That's a D grade. You can do better!"),rgb=(255,48,48)))
                            elif percentage >= 60 and percentage < 70:
                                print(styleStr(("That's a C grade. Keep it up!"),rgb=(48,249,255)))
                            elif percentage >= 70 and percentage < 80:
                                print(styleStr(("That's a B grade. Almost there!"),rgb=(235,255,48)))
                            elif percentage >= 80 and percentage <= 100:
                                print(styleStr(("That's an A grade. Good job!"),rgb=(55,255,48)))
                            else:
                                print("You have failed the test. Study harder!")

                            condition = 'askToTryAgain'
                        
                        while condition == 'askToTryAgain':
                            tOrF = True
                            while tOrF:
                                userInput = input("Do you want to try again (y|n)? ")
                                tOrF = yOrN(userInput)
                            if userInput == 'y':
                                send_msg(userInput)
                                condition = "attempt"
                                # start new quiz

                            else:
                                stop_threads = True
                                cdthread.join()
                                send_msg(DISCONNECT_MESSAGE)
                                
                                break


    while condition == 'b': #Register User Account
        # ask for username 
        tOrF = True
        while tOrF:
            print("\nEnter your desired user ID")
            userID = input('\n>>> ')
            commaVerifier = checkComma(userID)
            if commaVerifier == True:
                tOrF = True
            else:
                tOrF = False

        # ask for Password
        tOrF = True
        while tOrF:
            print("\nEnter your user Password")
            userPass = input('\n>>> ')
            tOrF = passcheck(userPass)    

        encryptedPass = encrypt(userPass)
        
        tOrF = True
        while tOrF == True:
            scrtQn = input("\nPlease enter a secret recovery question.\n>>> ")              # ask for secret question
            verifyScrtQn = checkComma(scrtQn)
            if verifyScrtQn == True:
                print("Please do not enter a comma in your question.")
                tOrF = True
            else:
                tOrF = False

        tOrF = True
        while tOrF == True:
            scrtAns = input("\nPlease enter your secret question's answer.\n>>> ")          # ask for secret question's answer
            verifyScrtAns = checkComma(scrtAns)
            if verifyScrtAns == True:
                print("Please do not enter a comma in your answer.")
                tOrF = True
            else:
                tOrF = False

        # add the items together 
        newUser = f"{condition},{userID},{encryptedPass},{scrtQn},{scrtAns}"
        #send to Server
        send_msg(newUser)

        condition = recv()
        if condition == "\nUser ID is already taken. Sending you back to main menu.\n***Welcome to Quiz Application***\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit":
            print(condition)
            condition = 'Start'
        else:
            print(condition)
            condition = 'Start'

    while condition == 'c': #Reset Password
        # ask for user ID
        tOrF = True
        while tOrF:
            print("\nEnter your user ID")
            userID = input('\n>>> ')
            commaVerifier = checkComma(userID)
            if commaVerifier == True:
                tOrF = True
            else:
                tOrF = False

        # SEND user ID to server
        resetPass = f"{condition},{userID}"
        send_msg(resetPass)
        # RECEIVE CONDITIONAL text from Server
        condition = recv()
        # if CONDITIONAL text == "User does not exist. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit":
        if condition == "User does not exist. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit":
            print(condition)
            condition = 'Start'

        # else:
        else:
            # print secret question
            print('\n'+condition)
            # ask for secret answer
            secretAnswer = input("\n>>> ")
            # SEND secret answer to Server
            send_msg(secretAnswer)
            # RECEIVE CONDITIONAL text from server
            condition = recv()
            # if CONDITIONAL text == 'NO':
            if condition == 'Wrong answer. Sending you back to main menu.\n[Main Menu]\na) Start Quiz Application\nb) Register User Account\nc) Reset Password\nx) Exit"':
                # print CONDITIONAL text; basically send back to main Menu
                print(condition)
            # else:
            else:
                # ask for new Password
                print('\n'+condition)

                tOrF = True
                while tOrF:
                    userPass = input("\n>>> ")
                    # verify password strength if not ask for password agai
                    tOrF = passcheck(userPass)

                # encrypt Password
                encryptedPass = encrypt(userPass)

                # SEND new encrypted password to server
                send_msg(encryptedPass)
                # RECEIVE confirmation text back from Server
                confirmation = recv()
                print(confirmation)
                # go to main Menu
                condition = 'Start'
            

    while condition == 'x':    # go back to main menu
        send_msg('x')
        break

#send_msg(DISCONNECT_MESSAGE)
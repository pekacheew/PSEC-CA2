# StudentID:	p2136798
# Name:	        Gan Hanyong
# Class:		DISM/FT/1B/02   
# Assessment:	CA2
# 
# Script name:	rwaFiles.py
# 
# Purpose:  	Reusable read, write, append Functions
#
# Usage syntax:	F5
# 
# Input file:	Specify full path, 'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\userid_pswd.csv'
#                                  'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\quiz_settings.csv'
#                                  'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\question_pool.csv'
#                                  'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\quiz_results.csv'
#                                  'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\quizes.csv'
#                                  'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\quiz_topics.csv'
#
# Output file:	Specify full path, 'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\userid_pswd.csv'
#                                  'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\quiz_settings.csv'
#                                  'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\question_pool.csv'
#                                  'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\quiz_results.csv'
#                                  'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\quizes.csv'
#                                  'D:\SP School\Y1 SEM2\PSEC\1B02-GanHanyong\csv\quiz_topics.csv'
# 
# Python ver:	Python 3.9.7

########################## userid_pswd.csv #######################
# Remove spacing in list function
def rmvSpaceID():
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            if i == '\n':
                csvFileR.remove(i)
        csvFile.seek(0)
        csvFile.truncate()
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()

# Check if User already Exist 
def regUsrIDone(userID):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            for i in csvFileR:
                exUserID = i.split(sep=',')
                if userID == exUserID[0]:
                    print("User already exists.")
                    csvFile.close()
                    return True

            else:
                csvFile.close()
                return False

# Check if User Exist 
def regUsrIDtwo(userID,aOrU):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            for i in csvFileR:
                exUserID = i.split(sep=',')
                stripUserID = exUserID[2].strip('\n')
                if userID == exUserID[0]:
                    #check if user is admin or user account
                    if aOrU == stripUserID:
                        
                        csvFile.close()
                        return False
            else:
                csvFile.close()
                return True
                
# check if user is admin or user account
def adminORuser(userID):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            for i in csvFileR:
                exUserID = i.split(sep=',')
                stripExUserID = exUserID[2].strip('\n')
                if userID == exUserID[0]:
                    #check if user is admin or user account
                    if stripExUserID == 'a':
                        csvFile.close()
                        return False
                    elif stripExUserID == 'u':
                        csvFile.close()
                        return True
            else:
                csvFile.close()
                return True

# write New User into userid_pswd.csv
def newUsr(writeIntoFile):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        csvFileR.append(f'\n{writeIntoFile}')
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()

# check if password is correct
def usrPswd(userID,userPswd):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            
            for i in csvFileR:
                attempts = i.split(sep=',')
                stripAttempts = attempts[1].strip('\n')
                
                if userID == attempts[0] and userPswd == stripAttempts:
                    print("Correct Password")
                    csvFile.close()
                    return False
                elif userID == attempts[0] and userPswd != stripAttempts:
                    print("Wrong password")
                    csvFile.close()
                    return True
            else:
                pass

# update new password of existing user
def editPswd(userID,newuserPswd):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in range(len(csvFileR)):
            attempts = csvFileR[i].split(sep=',')

            if userID == attempts[0]:
                toAppend = userID + ',' + newuserPswd + ',' + attempts[2] +',' + attempts[3] +',' +attempts[4] +',' + attempts[5]+'\n'
                csvFileR[i] = toAppend
                
    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'w') as csvFile:
        for n in csvFileR:
            
            csvFile.write(n)

        csvFile.close()
    

# remove User
def removeUsr(userID):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
    
        for i in csvFileR:
            userIDsplit = i.split(sep=',')
            if userID == userIDsplit[0]:
                csvFileR.remove(i)
        csvFile.close()
    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()

# retrieve user list
def usrList():
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
        r = 0

        for i in csvFileR:
            r += 1
            userIDsplit = i.split(sep=',')
            print(str(r)+'. '+userIDsplit[0])

        csvFile.close()

# check attempts
def usrAttempts(userID):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        
        for i in csvFileR:
            attempts = i.split(sep=',')
            stripAttempts = attempts[3].strip('\n')
            
            if userID == attempts[0] and stripAttempts == '999':
                print("\nUnlimited attempts.\n")
                csvFile.close()
                return False
            elif userID == attempts[0] and stripAttempts == '0':
                print("\n0 Attempts Remaining, returning to main menu.\n")
                csvFile.close()
                return True
            elif userID == attempts[0]:
                print(f"\n{stripAttempts} Attempts Remaining")
                csvFile.close()
                return False

        else:
            pass

# update attempt count
def attemptCount(userID):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        

        for i in range(len(csvFileR)):
            attempts = csvFileR[i].split(sep=',')
            if userID == attempts[0] and attempts[3] == '999':
                pass
            else:
                newAttempt = int(attempts[3]) - 1 
                if userID == attempts[0]:
                    toAppend = attempts[0] + ',' + attempts[1] + ',' + attempts[2] +',' + str(newAttempt)+',' + attempts[4] + ',' + attempts[5] 
                    csvFileR[i] = toAppend
                
    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'w') as csvFile:
        for n in csvFileR:
            
            csvFile.write(n)

        csvFile.close()

# Reset all Attempts
def resetAttempt():
    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in range(len(csvFileR)):
            userIdSplit = csvFileR[i].split(sep=',')

            if adminORuser(userIdSplit[0]) == True:
                toAppend = userIdSplit[0] + ',' + userIdSplit[1] + ',' + userIdSplit[2] +',' + str(qzSettings(3)) +',' +userIdSplit[4] +',' +userIdSplit[5]
                csvFileR[i] = toAppend

    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()


# Plus 1 Attempt to all users
def plusAttempt():
    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in range(len(csvFileR)):
            userIdSplit = csvFileR[i].split(sep=',')
            if adminORuser(userIdSplit[0]) == True:
                toAppend = userIdSplit[0] + ',' + userIdSplit[1] + ',' + userIdSplit[2] +',' + str(int(userIdSplit[3])+int(1)) + ',' +userIdSplit[4] +',' +userIdSplit[5]
                csvFileR[i] = toAppend
    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'w') as csvFile:
            for n in csvFileR:
                csvFile.write(n)
            csvFile.close()

# Minus 1 Attempt to all user
def minusAttempt():
    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in range(len(csvFileR)):
            userIdSplit = csvFileR[i].split(sep=',')
            if adminORuser(userIdSplit[0]) == True:
                toAppend = userIdSplit[0] + ',' + userIdSplit[1] + ',' + userIdSplit[2] +',' + str(int(userIdSplit[3])-int(1)) +',' +userIdSplit[4] +',' +userIdSplit[5]
                csvFileR[i] = toAppend
    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'w') as csvFile:
            for n in csvFileR:
                csvFile.write(n)
            csvFile.close()

# Set to unlimited attempts
def unlimitedAttempt():
    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in range(len(csvFileR)):
            userIdSplit = csvFileR[i].split(sep=',')
            if adminORuser(userIdSplit[0]) == True:
                toAppend = userIdSplit[0] + ',' + userIdSplit[1] + ',' + userIdSplit[2] +',' + str(999) +',' +userIdSplit[4] +',' +userIdSplit[5]
                csvFileR[i] = toAppend
    with open('./1B02-GanHanyong/csv/userid_pswd.csv', 'w') as csvFile:
            for n in csvFileR:
                csvFile.write(n)
            csvFile.close()

# Check User Input against Secret Answer
def secretA(userID,secretAns):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:
                csvFileR = csvFile.readlines()
                for i in csvFileR:
                    attempts = i.split(sep=',')
                    stripAttempts = attempts[5].strip('\n')
                    
                    if userID == attempts[0] and secretAns == stripAttempts:
                        print("Correct")
                        csvFile.close()
                        return False
                    elif userID == attempts[0] and secretAns != stripAttempts:
                        print("Wrong")
                        csvFile.close()
                        return True
                else:
                    pass

# retrieve user's secret question
def secretQ(userID):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()

        for i in csvFileR:
            userIDsplit = i.split(sep=',')
            if userID == userIDsplit[0]:
                return userIDsplit[4]

        csvFile.close()

# retrieve user's secret question's Answer
def secretAns(userID):
    with open('./1B02-GanHanyong/csv/userid_pswd.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()

        for i in csvFileR:
            userIDsplit = i.split(sep=',')
            if userID == userIDsplit[0]:
                return userIDsplit[5]

        csvFile.close()        
########################## quiz_settings.csv #######################
# quiz timer
def quizTimer(newTime,selection):
    with open('./1B02-GanHanyong/csv/quiz_settings.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()

            for i in range(len(csvFileR)):
                qzSet = csvFileR[i].split(sep=',')
                if qzSet[0] == selection:
                    toAppend = str(selection) + ', ' + str(newTime) + '\n'
                    csvFileR[i] = toAppend
                
    with open('./1B02-GanHanyong/csv/quiz_settings.csv', 'w') as csvFile:
        for n in csvFileR:
            
            csvFile.write(n)

        csvFile.close()

# get quiz settings data
def qzSettings(input):
    with open('./1B02-GanHanyong/csv/quiz_settings.csv','r+') as csvFile:
        qzSettingsVessel = []                      
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            
            qzSettingsVessel.append(i.split(',')[1])

        if input == 1:                              #timer
            variable = int(qzSettingsVessel[0]) 
            return variable
        elif input == 2:                           #num of questions
            variable = int(qzSettingsVessel[1]) 
            return variable
        elif input == 3:                          #attempts
            variable = int(qzSettingsVessel[2]) 
            return variable

########################## question_pool.csv #######################
# remove space in question_pool
def rmvSpaceQn():
    with open('./1B02-GanHanyong/csv/question_pool.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            if i == '\n':
                csvFileR.remove(i)
        csvFile.seek(0)
        csvFile.truncate()
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()

# check if question already exists
def regQnone(qn):
    with open('./1B02-GanHanyong/csv/question_pool.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            for i in csvFileR:
                qnPool = i.split(sep=',')
                if qn == qnPool[0]:
                    print("Question already exists.")
                    csvFile.close()
                    return True

            else:
                csvFile.close()
                return False

# check if question exists to be edited.
def regQntwo(qnToDel):
    with open('./1B02-GanHanyong/csv/question_pool.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            for i in csvFileR:
                qnPool = i.split(sep=',')
                if qnToDel == qnPool[0]:
                    print("Question exists.")
                    csvFile.close()
                    return False

            else:
                print("Question does not exist.")
                csvFile.close()
                return True

# add new line of question in
def addQuestion(newQuestion):
    with open('./1B02-GanHanyong/csv/question_pool.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        csvFileR.append(f'\n{newQuestion}')
    with open('./1B02-GanHanyong/csv/question_pool.csv','w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()
    rmvSpaceQn()
            
# remove question
def removeQn(qnDel):
    with open('./1B02-GanHanyong/csv/question_pool.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
    
        for i in csvFileR:
            qnSplit = i.split(sep=',')
            if qnDel == qnSplit[0]:
                csvFileR.remove(i)
        csvFile.close()
    with open('./1B02-GanHanyong/csv/question_pool.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()

# retrieve Question list
def qnList():
    with open('./1B02-GanHanyong/csv/question_pool.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
        r = 0

        for i in csvFileR:
            r += 1
            qnSplit = i.split(sep=',')
            print('\n\t'+str(r)+'. '+qnSplit[0])
            print(f"\ta) {qnSplit[1]}")
            print(f"\tb) {qnSplit[2]}")
            print(f"\tc) {qnSplit[3]}")
            print(f"\td) {qnSplit[4]}")
            print(f"\t(ANS): {qnSplit[5]}")

        csvFile.close()

# edit question into question_pool.csv
def editQn(qn,newChg,index):
    with open('./1B02-GanHanyong/csv/question_pool.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        rmvSpaceQn()
        for i in range(len(csvFileR)):
            qnPool = csvFileR[i].split(sep=',')

            if qn == qnPool[0]:
                if index == 0:
                    toAppend = f'{newChg},{qnPool[1]},{qnPool[2]},{qnPool[3]},{qnPool[4]},{qnPool[5]},{qnPool[6]}\n'
                    csvFileR[i] = toAppend
                elif index == 1:
                    toAppend = f'{qnPool[0]},{newChg},{qnPool[2]},{qnPool[3]},{qnPool[4]},{qnPool[5]},{qnPool[6]}\n'
                    csvFileR[i] = toAppend
                elif index == 2:
                    toAppend = f'{qnPool[0]},{qnPool[1]},{newChg},{qnPool[3]},{qnPool[4]},{qnPool[5]},{qnPool[6]}\n'
                    csvFileR[i] = toAppend
                elif index == 3:
                    toAppend = f'{qnPool[0]},{qnPool[1]},{qnPool[2]},{newChg},{qnPool[4]},{qnPool[5]},{qnPool[6]}\n'
                    csvFileR[i] = toAppend
                elif index == 4:
                    toAppend = f'{qnPool[0]},{qnPool[1]},{qnPool[2]},{qnPool[3]},{newChg},{qnPool[5]},{qnPool[6]}\n'
                    csvFileR[i] = toAppend
                elif index == 5:
                    toAppend = f'{qnPool[0]},{qnPool[1]},{qnPool[2]},{qnPool[3]},{qnPool[4]},{newChg},{qnPool[6]}\n'
                    csvFileR[i] = toAppend

        rmvSpaceQn()

    with open('./1B02-GanHanyong/csv/question_pool.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()

def retrieveQuestions(topic):
    questionList = ''
    with open('./1B02-GanHanyong/csv/question_pool.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in csvFileR:
            question = i.split(sep=',')
            qnTopic = question[6].strip('\n')
            if topic == qnTopic:
                insertQuestion = f'&&{question[0]},{question[1]},{question[2]},{question[3]},{question[4]},{question[5]}'
                questionList += insertQuestion

        csvFile.close()
        return questionList

def editQuesPoolTopics(moduleToEdit,nameToChg):
    with open('./1B02-GanHanyong/csv/question_pool.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in range(len(csvFileR)):
            iSplit = csvFileR[i].split(sep=',')
            topicName = iSplit[6].strip('\n')
            if topicName == moduleToEdit:
                csvFileR[i] = f'{iSplit[0]},{iSplit[1]},{iSplit[2]},{iSplit[3]},{iSplit[4]},{iSplit[5]},{nameToChg}\n'
    with open('./1B02-GanHanyong/csv/question_pool.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()


########################## quiz_results.csv #######################
# write into quiz results
def wResults(resultToWrite):
    with open('./1B02-GanHanyong/csv/quiz_results.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        csvFileR.append(f'\n{resultToWrite}')
    with open('./1B02-GanHanyong/csv/quiz_results.csv','w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()

# remove space for quiz_results.csv
def rmvSpaceR():
    with open('./1B02-GanHanyong/csv/quiz_results.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            if i == '\n':
                csvFileR.remove(i)
        csvFile.seek(0)
        csvFile.truncate()
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()

# retrieve entire quiz results
def resultList():
    with open('./1B02-GanHanyong/csv/quiz_results.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
        r = 0

        for i in csvFileR:
            r += 1
            resultPool = i.split(sep=',')
            stripResultPool = resultPool[4].strip('\n')
            print(f"{str(r)}. {resultPool[0]} scored {resultPool[1]} marks. {resultPool[2]}%. Timestamp: {resultPool[3]} Topic: {stripResultPool}")

        csvFile.close()

# retrieve results for specific quiz
def quizResults(quizName):
    with open('./1B02-GanHanyong/csv/quiz_results.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
        resultList = []
        for i in csvFileR:
            qResults = i.split(sep=',')
            stripQuizResults = qResults[4].strip('\n')

            if quizName == stripQuizResults:
                resultList.append(f"{qResults[0]} scored {qResults[1]} marks. {qResults[2]}%. Timestamp: {qResults[3]} Quiz: {stripQuizResults}")

            csvFile.close()
        return resultList

# retrieve quiz results for specific user
def userResults(userID):
    with open('./1B02-GanHanyong/csv/quiz_results.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
        #r = 0
        resultList = []
        for i in csvFileR:
            #r += 1
            userResults = i.split(sep=',')
            if userID == userResults[0]:
                stripUserResults = userResults[4].strip('\n')
                # resultList.append(f"{str(r)}. {userResults[0]} scored {userResults[1]} marks. {userResults[2]}%. Timestamp: {stripUserResults}")
                resultList.append(f"{userResults[0]} scored {userResults[1]} marks. {userResults[2]}%. Timestamp: {userResults[3]} Topic: {stripUserResults}")

            csvFile.close()
        return resultList

            


########################## quiz_topics.csv #######################

def chooseTopic():
    with open('./1B02-GanHanyong/csv/quiz_topics.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        r = 0
        topicNameList = []
        listIndex = []
        for i in csvFileR:
            if i == '\n':
                pass
            else:
                r += 1
                topicName = i.strip('\n')
                topicNameList.append(f"{str(r)}. {topicName}")
        
        for i in topicNameList:
            print(i)

        for i in range(len(topicNameList)):
            nameListIndex = topicNameList[i].split(sep='.')
            listIndex.append(int(nameListIndex[0]))

    if listIndex == []:
        exit()
    else:

        tOrF = True
        while tOrF:
            userInput = input(f"\nPlease choose the topic you want ({min(listIndex)}) - ({max(listIndex)}): ")
            for i in range(len(listIndex)):
                if userInput == str(listIndex[i]):
                    selectedModule = topicNameList[i].split(sep='. ')
                    #print(selectedModule[1])
                    return selectedModule[1]
                    tOrF = False
            if tOrF:
                print("Please enter a valid input.")
                tOrF = True

def checkTopicOne(moduleName):
    with open('./1B02-GanHanyong/csv/quiz_topics.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            mNames = i.strip('\n')
            if moduleName == mNames:
                #print("Module already exists.")
                csvFile.close()
                return True

        else:
            csvFile.close()
            return False


# add new quiz modules
def addNewTopic(moduleName):
    with open('./1B02-GanHanyong/csv/quiz_topics.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        csvFileR.append(f'\n{moduleName}')
    with open('./1B02-GanHanyong/csv/quiz_topics.csv','w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()
    rmvSpaceTopic()
        
# delete existing quiz modules
def delTopic(moduleName):
    with open('./1B02-GanHanyong/csv/quiz_topics.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()
    
        for i in csvFileR:
            moduleStriped = i.strip('\n')
            if moduleName == moduleStriped:
                csvFileR.remove(i)
        csvFile.close()
    with open('./1B02-GanHanyong/csv/quiz_topics.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()



def editTopicName(moduleName,newModuleName):
    with open('./1B02-GanHanyong/csv/quiz_topics.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        # strip every line of '\n'
        for i in range(len(csvFileR)):
            moduleStriped = csvFileR[i].strip('\n')
            # change the line that is equal to moduleName to newModuleName
            if moduleStriped == moduleName:
                csvFileR[i] = f"{newModuleName}\n"
        
    with open('./1B02-GanHanyong/csv/quiz_topics.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()

        
def rmvSpaceTopic():
    with open('./1B02-GanHanyong/csv/quiz_topics.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            if i == '\n':
                csvFileR.remove(i)
        csvFile.seek(0)
        csvFile.truncate()
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()

########################## quizes.csv #######################

def checkQuizOne(qName):
    with open('./1B02-GanHanyong/csv/quizes.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            quizPool = i.split(sep='|')
            if qName == quizPool[2]:
                csvFile.close()
                return True

        else:
            csvFile.close()
            return False        

# write New Quiz into quizes.csv
def regNewQuiz(writeIntoFile):
    with open('./1B02-GanHanyong/csv/quizes.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        csvFileR.append(f'\n{writeIntoFile}')
    with open('./1B02-GanHanyong/csv/quizes.csv','w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()



def deleteQuiz(qName):
    with open('./1B02-GanHanyong/csv/quizes.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
    
        for i in csvFileR:
            qnSplit = i.split(sep='|')
            if qName == qnSplit[2]:
                csvFileR.remove(i)
        csvFile.close()
    with open('./1B02-GanHanyong/csv/quizes.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()



def rmSpaceQuiz():
    with open('./1B02-GanHanyong/csv/quizes.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            if i == '\n':
                csvFileR.remove(i)
        csvFile.seek(0)
        csvFile.truncate()
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()

def chooseQuiz():
    with open('./1B02-GanHanyong/csv/quizes.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        r = 0
        topicNameList = []
        listIndex = []
        for i in csvFileR:
            if i == '\n':
                pass
            else:
                r += 1
                i.strip('\n')
                topicName = i.split(sep='|')
                topicNameList.append(f"{str(r)}. {topicName[2]}")
        
        for i in topicNameList:
            print(i)



        for i in range(len(topicNameList)):
            nameListIndex = topicNameList[i].split(sep='.')
            listIndex.append(int(nameListIndex[0]))

    if listIndex == []:
        # print("No existing quiz currently.")
        return False
          # probably should fix this
    else:

        tOrF = True
        while tOrF:
            userInput = input(f"\nPlease choose the quiz you want ({min(listIndex)}) - ({max(listIndex)}): ")
            for i in range(len(listIndex)):
                if userInput == str(listIndex[i]):
                    selectedModule = topicNameList[i].split(sep='. ')
                    #print(selectedModule[1])
                    return selectedModule[1]
                    tOrF = False
            if tOrF:
                print("Please enter a valid input.")
                tOrF = True

def chooseQuizForUser():
    with open('./1B02-GanHanyong/csv/quizes.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        r = 0
        topicNameList = []
        listIndex = []
        for i in csvFileR:
            if i == '\n':
                pass
            else:
                r += 1
                i.strip('\n')
                topicName = i.split(sep='|')
                topicNameList.append(f"{str(r)}. {topicName[2]}")
        
        # maybe can append "view results" and "back to menu" here
        topicNameList.append(f"{str(r+1)}. View Previous Attempts")
        topicNameList.append(f"{str(r+2)}. Back to previous menu")
        topicNameList.append(f"{str(r+3)}. Exit")
        for i in topicNameList:
            print(i)

        for i in range(len(topicNameList)):
            nameListIndex = topicNameList[i].split(sep='.')
            listIndex.append(int(nameListIndex[0]))


    tOrF = True
    while tOrF:
        userInput = input(f"\nPlease select an option ({min(listIndex)}) - ({max(listIndex)}): ")
        for i in range(len(listIndex)):
            if userInput == str(listIndex[i]):
                selectedModule = topicNameList[i].split(sep='. ')
                # print(selectedModule[1])
                return selectedModule[1]
                tOrF = False
        if tOrF:
            print("Please enter a valid input.")
            tOrF = True

# chooseQuizForUser()
def retrieveQuiz(selectedQuiz):
    with open('./1B02-GanHanyong/csv/quizes.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            quiz = i.strip('\n')
            quizList = quiz.split(sep='|')

            courseName = quizList[0]
            moduleName = quizList[1]
            quizName = quizList[2]

            if selectedQuiz == quizName:
                csvFile.close()
                return quiz

                
def editQuizzesTopics(moduleToEdit,nameToChg):
    with open('./1B02-GanHanyong/csv/quizes.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        newline = ''
        for i in range(len(csvFileR)):
            iSplit = csvFileR[i].split(sep='|')
            topics = iSplit[3].split(sep='&&')
            topics.pop(0)

            newline = f'{iSplit[0]}|{iSplit[1]}|{iSplit[2]}|'
            for n in topics:
                topicAndNum = n.split(sep=',')

                

                if topicAndNum[0] == moduleToEdit:
                    newline += f'&&{nameToChg},{topicAndNum[1]}'
                    

                else:
                    newline += f'&&{topicAndNum[0]},{topicAndNum[1]}'

            csvFileR[i] = newline
    with open('./1B02-GanHanyong/csv/quizes.csv','w') as csvFile:

        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()
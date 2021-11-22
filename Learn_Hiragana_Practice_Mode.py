from Classes import*
from Learn_Hiragana_Learning_Mode import*
from Populate_Values import*

def practice_appStarted(app):
    pass
practiceHiraganaAndVocab = list(overall_dict.keys())
toBePracticed = copy.deepcopy(overall_dict)
###############################################################################

#Getting Things

###############################################################################
def getRandomPracticeKey(app):
    if app.prevFlashCard != dict():
        previousKeys = list()
        for prevKey in app.prevFlashCard:
            previousKeys.append(prevKey)
        randomizedPrev = random.shuffle(previousKeys)
        randomKey = random.choice(randomizedPrev)
        return randomKey
    else:
        randomKey = random.choice(modifyListOfKeys)
        return randomKey

def getQuestionType():
    randomQuestionType = random.randint(1,4)
    testingType = 1
    return testingType

def getAnswerChoices():
    #Question Type 1
    characterChoices = list(character_dict.values())
    characterPronunciations = list()
    for row in range(len(characterChoices)):
        for col in range(len(characterChoices[0])):
            romanji = characterChoices[row][col]
            if len(romanji) == 1:
                characterPronunciations.append(romanji)
    return random.sample(characterPronunciations, k=3)

#Once practice Mode is finished/ on Transition screen, 
# user will seen what they got wrong and what they got right in the end
def getSummary():
    return toBeReview, knowledgeable, correctAnswers, incorrectAnswers


################################################################

#Determining Correctness

###############################################################
correctAnswers = dict()
isCorrectKey = list()
incorrectAnswers = dict()
def isCorrect(app,targetAnswer, questionType, timeDifference):
    correctMessages = ["That's Correct!", "You're the best!", 
                            "You're a Hiragana Expert!"]
    incorrectMessages = ["Sorry, that's incorrect","Better luck next time!"]
    #may need to be changed for other question types
    answerChoice = app.userAnswer
    if answerChoice == targetAnswer and app.finishedQuestion == True:
        storeCorrectIncorrect(targetAnswer, True, questionType, timeDifference,
                                app)
        praise = random.choice(correctMessages)
        app.showMessage(praise)
    elif answerChoice != targetAnswer and app.finishedQuestion == True:
        #defaulQuestionTime - time user takes to answer a question
        storeCorrectIncorrect(targetAnswer,answerChoice, False, questionType, 
                            timeDifference,app)
        notPraise = random.choice(incorrectMessages)
        app.showMessage(notPraise)

alreadyPracticed = dict()
#will form basis for review mode
toBeReview = dict()
knowledgeable = dict()
def storeCorrectIncorrect(targetAnswer, questionCorrect, questionType, 
                            timeDifference, app):
    #Question Type 1
    answerChoice = app.userAnswer
    if questionType == 1:
        if questionCorrect == True:
        #targetAnswer will be hiragana/key 
        #Want each answer to have a counter 
            if targetAnswer not in correctAnswers:
                correctAnswers[targetAnswer] = answerChoice
            elif (targetAnswer not in correctAnswers and 
                targetAnswer in incorrectAnswers):
                #For now a clean slate
                del incorrectAnswers[targetAnswer]
                correctAnswers[targetAnswer] = answerChoice
            elif targetAnswer in correctAnswers:
                app.characterLevel += 1
                knowledgeable[targetAnswer] = answerChoice
        elif questionCorrect == False:
            #User hasn't done question before or gotten it wrong before
            if targetAnswer not in incorrectAnswers:
                incorrectAnswers[targetAnswer] = answerChoice
            #Needs to be reviewed
            elif targetAnswer in incorrectAnswers:
                toBeReview[targetAnswer] =  answerChoice
#Storing
def getPracticeHiraganaOrVocab(app, randomKey):
    hiraganaOrVocab = randomKey
    if hiraganaOrVocab in hiraganaList:
        hiraganaValue = overall_dict[hiraganaOrVocab]
        app.prevFlashCard[hiraganaOrVocab] = hiraganaValue 
        seenHiraganaFlashCards[hiraganaOrVocab] = hiraganaValue 
        seenFlashCards[hiraganaOrVocab] = hiraganaValue 
        del toBePracticed[hiraganaOrVocab]      
    elif hiraganaOrVocab in vocabList:
        vocabValue = overall_dict[hiraganaOrVocab]
        app.prevFlashCard[hiraganaOrVocab] = vocabValue
        seenVocabFlashCards[hiraganaOrVocab] = vocabValue
        seenFlashCards[hiraganaOrVocab] = vocabValue
        del toBePracticed[hiraganaOrVocab] 
######################################################################

#The question in question

#######################################################################
def questionCard(app,canvas,questionType):
    questionFlashCard = FlashCard(app.newKey,toBePracticed[app.newKey])
    if questionType == 1:
        currQuestion = questionFlashCard.drawTimedFlashCard1(canvas, app)
        return currQuestion
    elif questionType == 2: pass
    elif questionType == 4: pass
    elif questionType == 4: pass
    else:app.showMessage('There as been an error')

def answerQuestion(app,canvas):
    startTime = time.time()
    defaultTimeLimit = app.baseProblemTime
    questionType = getQuestionType()
    if questionType == 1: #hiragana to romanji
        questionFlashCard = FlashCard(app.newKey,toBePracticed[app.newKey])
        if (defaultTimeLimit != 0 and questionFlashCard.frontText 
            in hiraganaList):
                targetAnswer = questionFlashCard.frontText
                questionFlashCard.drawTimedFlashCard1(canvas, app)
                print(targetAnswer)
                app.showMessage('Press e to Input Your Answer!')
                if app.wantInput == True:
                    answer = app.getUserInput('Please Type in Best Answer')
                    if answer == None:
                        app.wantInput = False
                    else:
                        modifiedIsCorrect(targetAnswer,answer)
                else:
                    #Seleting an answer choice
                    listOfPossibleChoices =(random.sample(
                        practiceHiraganaAndVocab, k=4))
                    if targetAnswer in listOfPossibleChoices:
                        drawAnswerChoices(app,canvas)
                        #if clicked, that is answerChoice number
                        userAnswer  = app.answerChoice
                        modifiedIsCorrect(targetAnswer,userAnswer)

        elif defaultTimeLimit <= 0:
            app.showMessage("Time's Up!")
            app.showMessage('Please Press Right or Click Next to Continue')
    elif questionType == 2: #vocab to romanji
        pass
    elif questionType == 3: #romanji to vocab
        pass
    
    elif questionType == 4: #romanji to hiragana
        pass

    else:
        app.showMessage("There has been an error")


def drawAnswerChoices(app,canvas):
    targetAnswer = app.practiceFlashCard.frontText
    #Option 1
    randomChoice1 = app.listOfPossibleChoices[0]
    print(randomChoice1)
    randomChoice2 = app.listOfPossibleChoices[1]
    randomChoice3 = app.listOfPossibleChoices[2]
    randomChoice4 = app.listOfPossibleChoices[3]
    # if (randomChoice1 == app.practiceFlashCard.frontText or 
    #     randomChoice2 == app.practiceFlashCard.frontText
    #     or randomChoice3 == app.practiceFlashCard.frontText 
    #     or randomChoice4 == app.practiceFlashCard.frontText):
    if app.lightMode == True:
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.3,
                                app.cx//2,
                                app.cy*1.4, 
                                fill = 'light goldenrod')
        canvas.create_text(app.cx,app.cy*1.35,text = f'1 {randomChoice1}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy,0,0, fill = 'navajo white')
        #Option 2
        
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.4,
                                app.cx//2,
                                app.cy*1.5, 
                                fill = 'plum')
        canvas.create_text(app.cx,app.cy*1.45,text = f'2 {randomChoice2}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy//2,0,0, fill = 'navajo white')
        #Option 3
    
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.5,
                                app.cx//2,
                                app.cy*1.6,
                                fill = 'lemon chiffon')
        canvas.create_text(app.cx,app.cy*1.55, text = f'3 {randomChoice3}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy//4,0,0, fill = 'navajo white')
        #Option 4
        
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.6,
                                app.cx//2,
                                app.cy*1.7,
                                fill = 'honeydew2')
        canvas.create_text(app.cx,app.cy*1.65, text = f'4 {randomChoice4}', 
        fill ='black')
        #canvas.create_oval(app.cx,app.cy//6,0,0, fill = 'navajo white')
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.7,
                                app.cx//2,
                                app.cy*1.8,
                                fill = 'snow')
        canvas.create_text(app.cx,app.cy*1.75,
                            text = 'Press e to Input Your Answer', 
                            fill ='black')
        #canvas.create_oval(app.cx,app.cy//6,0,0, fill = 'navajo white')
    elif app.darkMode == True:
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.3,
                                app.cx//2,
                                app.cy*1.4, 
                                fill = 'pale violet red')
        canvas.create_text(app.cx,app.cy//12,text = f'{randomChoice1}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy,0,0, fill = 'navajo white')
        #Option 2
        
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.4,
                                app.cx//2,
                                app.cy*1.5, 
                                fill = 'dark orange')
        canvas.create_text(app.cx//2,app.cy//12,text = f'{randomChoice2}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy//2,0,0, fill = 'navajo white')
        #Option 3
    
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.5,
                                app.cx//2,
                                app.cy*1.6,
                                fill = 'maroon')
        canvas.create_text(app.cx//2,app.cy//12,text = f'{randomChoice3}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy//4,0,0, fill = 'navajo white')
        #Option 4
        
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.6,
                                app.cx//2,
                                app.cy*1.7,
                                fill = 'dark goldenrod')
        canvas.create_text(app.cx//2,app.cy//12, text = f'{randomChoice4}', 
        fill ='black')
        #canvas.create_oval(app.cx,app.cy//6,0,0, fill = 'navajo white')
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.7,
                                app.cx//2,
                                app.cy*1.8,
                                fill = 'rosy brown')
        canvas.create_text(app.cx,app.cy*1.75,
                            text = 'Press e to Input Your Answer', 
                            fill ='black')
#keep randomizing list until targetAnswer in list of possible answers
###########################################################################

#Pressed

###########################################################################
def practiceMode_keyPressed(app,event):
    if (event.key == 'p'):
        app.paused = not app.paused
    elif event.key == 'q':
        app.showMessage("All your progress will be lost!")
        app.phase = 'start'
    elif event.key == 'Right':
        getRandomPracticeKey(app)
        app.listOfPossibleChoices = getAnswerChoices()  
        app.listOfPossibleChoices.append(app.practiceFlashCard.frontText)
        app.makeFlashCard = True
        app.startQuestion = True
        app.finishedQuestion = False
        app.isContinueKeyPressed = True
        if app.cardsToDo != 0:
            app.cardsToDo -= 1
    if event.key == 's':
        getRandomPracticeKey(app)
        app.listOfPossibleChoices = getAnswerChoices()  
        app.makeFlashCard = True
        app.startQuestion = True
        app.finishedQuestion = False
    elif event.key == 'w':
        app.listOfPossibleChoices = getAnswerChoices()  
    elif event.key == 'd':
        app.startQuestion = False
        app.finishedQuestion = True
    elif event.key == 'e':
        app.userAnswer = app.getUserInput('Please Type in Best Answer')
        app.wantInput = True
    #Answer Selections
    if event.key == '1':
        app.option1Chosen = True
        app.finishedQuestion = True
    elif event.key == '2':
        app.option2Chosen = True
        app.finishedQuestion = True
    elif event.key == '3':
        app.option3Chosen = True
        app.finishedQuestion = True
    elif event.key == '4':
        app.option4Chosen = True
        app.finishedQuestion = True
def practice_mousePressed(app,event):
    if (app.width//4 <= event.x and event.x >= app.width//6 and 
        app.height//10 <= event.y and event.y >= app.height//5):
        app.showMessage('Clicked')
        app.option1Chosen = True
        app.finishedQuestion = True
    # app.finishedQuestion = True
    # # elif 
    # #     app.option2Chosen = True
    #         app.finishedQuestion = True
    # # elif 
    # #     app.option3Chosen = True
    # app.finishedQuestion = True
    # # elif 
    # #     app.option4Chosen = True
    # app.finishedQuestion = True
##############################################################################

#"Modified" Functions (For MVP Testing)

##############################################################################
def modifiedIsCorrect(targetAnswer, app, diff):
    correctMessages = ["That's Correct!", "You're the best!", 
                            "You're a Hiragana Expert!"]
    incorrectMessages = ["Sorry, that's incorrect","Better luck next time!"]
    #may need to be changed for other question types
    answerChoice = app.userAnswer
    if (answerChoice == character_dict[targetAnswer] and app.finishedQuestion == True):
        storeCorrectIncorrect(targetAnswer, True, diff, app)
        praise = random.choice(correctMessages)
        app.showMessage(praise)
    elif( answerChoice != character_dict[targetAnswer] and
         app.finishedQuestion == True):
        #defaulQuestionTime - time user takes to answer a question
        storeCorrectIncorrect(targetAnswer,answerChoice, diff, False,app)
        notPraise = random.choice(incorrectMessages)
        app.showMessage(notPraise)

def modifiedAnswerQuestion(app, targetAnswer):
    startTime = time.time()
    defaultTimeLimit = app.baseProblemTime
    #timeDifference = defaultTimeLimit = timeTaken
     #hiragana to romanji
    if defaultTimeLimit > 0:
            print(targetAnswer)
            if app.wantInput == True:
                if app.userAnswer == None:
                    app.wantInput = False
                else:
                    endTime = time.time()
                    diff = endTime = startTime
                    modifiedIsCorrect(targetAnswer, app, diff)
            else:
                #Seleting an answer choice
                if targetAnswer in app.listOfPossibleChoices:
                    if app.option1Chosen == True:
                        endTime = time.time()
                        diff = endTime - startTime
                        userAnswer  = app.listOfPossibleChoices[0]
                        modifiedIsCorrect(targetAnswer,userAnswer, app, diff)
                    elif app.option2Chosen == True:
                        endTime = time.time()
                        diff = endTime - startTime
                        userAnswer = app.listOfPossibleChoices[1]
                        modifiedIsCorrect(targetAnswer,userAnswer, app, diff)
                    elif app.option3Chosen == True:
                        endTime = time.time()
                        diff = endTime - startTime
                        userAnswer = app.listOfPossibleChoices[2]
                        modifiedIsCorrect(targetAnswer,userAnswer, app, diff)
                    elif app.option4Chosen == True:
                        endTime = time.time()
                        diff = endTime - startTime
                        userAnswer = app.listOfPossibleChoices[3]
                        modifiedIsCorrect(targetAnswer,userAnswer, app, diff)
    elif defaultTimeLimit == 0:
        app.showMessage('Please Press Right or Click Next to Continue')
        

#Automatically move on to next flashcard card, Doing stage
def practice_timerFired(app):
    if app.paused == False:
        #app.listOfPossibleChoices = getAnswerChoices()  
        app.baseProblemTime -= 1
        app.timeTaken += 1
        if app.baseProblemTime == 0 and app.isContinueKeyPressed == False:
            app.finishedQuestion = True

            app.baseProblemTime = 30
            app.timeTaken = 0
        if app.makeFlashCard == True:
            app.currQuestionType = getQuestionType()

#############################################################################

#Extras

################################################################################
answerStreak = list()
def hasStreak(answerStreak):
    for i in range(len(answerStreak)):
        for j in range (i+1,len(answerStreak)):
            if answerStreak[i][j] == 1:
                return True
###########################################################################

#Drawings

###########################################################################

def drawAnswerChoices(app,canvas):
    targetAnswer = app.practiceFlashCard.frontText
    #Option 1
    randomChoice1 = app.listOfPossibleChoices[0]
    print(randomChoice1)
    randomChoice2 = app.listOfPossibleChoices[1]
    randomChoice3 = app.listOfPossibleChoices[2]
    randomChoice4 = app.listOfPossibleChoices[3]
    # if (randomChoice1 == app.practiceFlashCard.frontText or 
    #     randomChoice2 == app.practiceFlashCard.frontText
    #     or randomChoice3 == app.practiceFlashCard.frontText 
    #     or randomChoice4 == app.practiceFlashCard.frontText):
    if app.lightMode == True:
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.3,
                                app.cx//2,
                                app.cy*1.4, 
                                fill = 'light goldenrod')
        canvas.create_text(app.cx,app.cy*1.35,text = f'1 {randomChoice1}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy,0,0, fill = 'navajo white')
        #Option 2
        
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.4,
                                app.cx//2,
                                app.cy*1.5, 
                                fill = 'plum')
        canvas.create_text(app.cx,app.cy*1.45,text = f'2 {randomChoice2}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy//2,0,0, fill = 'navajo white')
        #Option 3
    
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.5,
                                app.cx//2,
                                app.cy*1.6,
                                fill = 'lemon chiffon')
        canvas.create_text(app.cx,app.cy*1.55, text = f'3 {randomChoice3}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy//4,0,0, fill = 'navajo white')
        #Option 4
        
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.6,
                                app.cx//2,
                                app.cy*1.7,
                                fill = 'honeydew2')
        canvas.create_text(app.cx,app.cy*1.65, text = f'4 {randomChoice4}', 
        fill ='black')
        #canvas.create_oval(app.cx,app.cy//6,0,0, fill = 'navajo white')
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.7,
                                app.cx//2,
                                app.cy*1.8,
                                fill = 'snow')
        canvas.create_text(app.cx,app.cy*1.75,
                            text = 'Press e to Input Your Answer', 
                            fill ='black')
        #canvas.create_oval(app.cx,app.cy//6,0,0, fill = 'navajo white')
    elif app.darkMode == True:
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.3,
                                app.cx//2,
                                app.cy*1.4, 
                                fill = 'pale violet red')
        canvas.create_text(app.cx,app.cy//12,text = f'{randomChoice1}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy,0,0, fill = 'navajo white')
        #Option 2
        
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.4,
                                app.cx//2,
                                app.cy*1.5, 
                                fill = 'dark orange')
        canvas.create_text(app.cx//2,app.cy//12,text = f'{randomChoice2}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy//2,0,0, fill = 'navajo white')
        #Option 3
    
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.5,
                                app.cx//2,
                                app.cy*1.6,
                                fill = 'maroon')
        canvas.create_text(app.cx//2,app.cy//12,text = f'{randomChoice3}', 
        fill ='black' )
        #canvas.create_oval(app.cx,app.cy//4,0,0, fill = 'navajo white')
        #Option 4
        
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.6,
                                app.cx//2,
                                app.cy*1.7,
                                fill = 'dark goldenrod')
        canvas.create_text(app.cx//2,app.cy//12, text = f'{randomChoice4}', 
        fill ='black')
        #canvas.create_oval(app.cx,app.cy//6,0,0, fill = 'navajo white')
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.7,
                                app.cx//2,
                                app.cy*1.8,
                                fill = 'rosy brown')
        canvas.create_text(app.cx,app.cy*1.75,
                            text = 'Press e to Input Your Answer', 
                            fill ='black')
def drawNextButton(app,canvas):
    canvas.create_rectangle(app.cx*3,
                            app.cy*1.2,
                            app.cx,
                            app.cy*1.1, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.15,
                        font = 'Arial',  text = "Next", fill = 'black')
def practiceModeRedrawAll(app,canvas):
    canvas.create_text(app.cx,app.cy, font = 'Arial 20',
                        text = 'Press s to Start!')
    #still true
    if app.makeFlashCard == True:
        app.practiceFlashCard.drawTimedFlashCard1(canvas, app)  
        canvas.create_text(app.cx, app.cy*1.2, font = 'Arial 20', 
    text ="Please Select/Input the Best Answer", fill = 'black')
        targetAnswer = app.practiceFlashCard.frontText
        drawAnswerChoices(app,canvas)  
        modifiedAnswerQuestion(app,targetAnswer)
    elif app.baseProblemTime == 0 or app.cardsToDo == 0:
        drawNextButton(app,canvas)   
    #if app.makeFlashCard == False and app.cardsToDo == 5:
        
        
    # # elif app.makeFlashCard == True and app.cardsToDo >= 0:
    # #     app.flashCard.drawFlashCard(canvas,app)
    # elif app.makeFlashCard == True and app.cardsToDo >= 0:
    #     app.newKey = getRandomKey()
    #     drawNewCard(app,canvas)  

    #if answer is correct and in a certain range

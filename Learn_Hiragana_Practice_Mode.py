from Classes import*
from Learn_Hiragana_Learning_Mode import*

practiceHiraganaAndVocab = list(overall_dict.keys())
toBePracticed = copy.deepcopy(overall_dict)
alreadyPracticed = dict()
#will form basis for review mode
toBeReview = dict()
knowledgeable = dict()

#Extras
answerStreak = list()
def hasStreak(answerStreak):
    for i in range(len(answerStreak)):
        for j in range (i+1,len(answerStreak)):
            if answerStreak[i][j] == 1:
                return True
def getRandomPracticeKey(app):
    for randomKey in random.shuffle(app.prevFlashCard):
        return randomKey
def getPracticeHiraganaOrVocab(app):
    hiraganaOrVocab = getRandomKey()
    #Base: Can store in practice
    #Inner: Store whether correct/incorrect
    if hiraganaOrVocab in hiraganaList:
        hiraganaValue = toBeLearned[hiraganaOrVocab]
        app.prevFlashCard[hiraganaOrVocab] = hiraganaValue 
        seenHiraganaFlashCards[hiraganaOrVocab] = hiraganaValue 
        seenFlashCards[hiraganaOrVocab] = hiraganaValue 
        del toBePracticed[hiraganaOrVocab]      
    elif hiraganaOrVocab in vocabList:
        vocabValue = toBeLearned[hiraganaOrVocab]
        app.prevFlashCard[hiraganaOrVocab] = vocabValue
        seenVocabFlashCards[hiraganaOrVocab] = vocabValue
        seenFlashCards[hiraganaOrVocab] = vocabValue
        del toBePracticed[hiraganaOrVocab] 
    return hiraganaOrVocab 

correctAnswers = dict()
isCorrectKey = list()
incorrectAnswers = dict()
def isCorrect(app,targetAnswer,answerChoice, questionType, timeDifference):
    correctMessages = ["That's Correct!", "You're the best!", 
                            "You're a Hiragana Expert!"]
    incorrectMessages = ["Sorry, that's incorrect","Better luck next time!"]
    #may need to be changed for other question types
    if answerChoice == targetAnswer and app.finsihedQuestion == True:
        storeCorrectIncorrect(targetAnswer,answerChoice, True, questionType, 
                                timeDifference,app)
        praise = random.choice(correctMessages)
        app.showMessage(praise)
    elif answerChoice != targetAnswer and app.finsihedQuestion == True:
        #defaulQuestionTime - time user takes to answer a question
        storeCorrectIncorrect(targetAnswer,answerChoice, False, questionType, 
                            timeDifference,app)
        notPraise = random.choice(incorrectMessages)
        app.showMessage(notPraise)

def storeCorrectIncorrect(targetAnswer, answerChoice, questionCorrect, 
                        questionType, timeDifference, app):
    #Question Type 1
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

#Once practice Mode is finished/ on Transition screen, 
# user will seen what they got wrong and what they got right in the end
def getSummary():
    return toBeReview, knowledgeable, correctAnswers, incorrectAnswers

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
                        drawAnswerChoices(app,canvas,listOfPossibleChoices)
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

def getQuestionType():
    randomQuestionType = random.randint(1,4)
    testingType = 1
    return testingType

def drawAnswerChoices(app,canvas,listOfChoices):
    #Option 1
    randomChoice1 = listOfChoices[0][0]
    randomChoice2 = listOfChoices[1][0]
    randomChoice3 = listOfChoices[2][0]
    randomChoice4 = listOfChoices[3][0]
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
def practiceMode_keyPressed(app,event):
    if (event.key == 'p'):
        app.paused = not app.paused
    elif event.key == 'q':
        app.showMessage("All your progress will be lost!")
        app.phase = 'start'
    elif event.key == 'Right':
        getRandomPracticeKey(app)
        app.makeFlashCard = True
        if app.cardsToDo != 0:
            app.cardsToDo -= 1
    if event.key == 's':
        app.startQuestion = True
        app.finishedQuestion = False
    elif event.key == 'd':
        app.startQuestion = False
        app.finishedQuestion = True
    elif event.key == 'e':
        app.wantInput = True

def practice_mousePressed(app,event):
    if (app.width//4 <= event.x and event.x >= app.width//6 and 
        app.height//10 <= event.y and event.y >= app.height//5):
        app.showMessage('Clicked')
        app.option1Chosen = True
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
    

def modifiedIsCorrect(targetAnswer,answerChoice, app, diff):
    correctMessages = ["That's Correct!", "You're the best!", 
                            "You're a Hiragana Expert!"]
    incorrectMessages = ["Sorry, that's incorrect","Better luck next time!"]
    #may need to be changed for other question types
    if (answerChoice == character_dict[targetAnswer] and 
        app.finishedQuestion == True):
        storeCorrectIncorrect(targetAnswer,answerChoice, True, diff, app)
        praise = random.choice(correctMessages)
        app.showMessage(praise)
    elif( answerChoice != character_dict[targetAnswer] and
         app.finishedQuestion == True):
        #defaulQuestionTime - time user takes to answer a question
        storeCorrectIncorrect(targetAnswer,answerChoice, diff, False,app)
        notPraise = random.choice(incorrectMessages)
        app.showMessage(notPraise)

def modifiedAnswerQuestion(app, targetAnswer, listOfPossibleChoices):
    startTime = time.time()
    defaultTimeLimit = app.baseProblemTime
    #timeDifference = defaultTimeLimit = timeTaken
     #hiragana to romanji
    if defaultTimeLimit > 0:
            print(targetAnswer)
            #app.showMessage('Press e to Input Your Answer!')
            if app.wantInput == 'Yes':
                answer = app.getUserInput('Please Type in Best Answer')
                if answer == None:
                    app.wantInput == 'No'
                else:
                    endTime = time.time()
                    diff = endTime = startTime
                    modifiedIsCorrect(targetAnswer,answer, app, diff)
            else:
                #Seleting an answer choice
                if targetAnswer in listOfPossibleChoices:
                    if app.option1Chosen == True:
                        endTime = time.time()
                        diff = endTime - startTime
                        userAnswer  = listOfPossibleChoices[0]
                        modifiedIsCorrect(targetAnswer,userAnswer, app, diff)
                    elif app.option2Chosen == True:
                        endTime = time.time()
                        diff = endTime - startTime
                        userAnswer = listOfPossibleChoices[1]
                        modifiedIsCorrect(targetAnswer,userAnswer, app, diff)
                    elif app.option3Chosen == True:
                        endTime = time.time()
                        diff = endTime - startTime
                        userAnswer = listOfPossibleChoices[2]
                        modifiedIsCorrect(targetAnswer,userAnswer, app, diff)
                    elif app.option4Chosen == True:
                        endTime = time.time()
                        diff = endTime - startTime
                        userAnswer = listOfPossibleChoices[3]
                        modifiedIsCorrect(targetAnswer,userAnswer, app, diff)
    elif defaultTimeLimit == 0:
        app.showMessage('Please Press Right or Click Next to Continue')
        

#Automatically move on to next flashcard card, Doing stage
def practice_timerFired(app):
    if app.paused == False:
        app.baseProblemTime -= 1
        app.timeTaken += 1
        if app.baseProblemTime == 0 and app.makeFlashCard == True:
            app.baseProblemTime = 30
            app.timeTaken = 0

def drawNextButton(app,canvas):
    canvas.create_rectangle(app.cx*3,
                            app.cy*1.2,
                            app.cx,
                            app.cy*1.1, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.15,
                        font = 'Arial',  text = "Next", fill = 'black')

def practiceModeRedrawAll(app,canvas):
    canvas.create_text(app.cx,app.cy, text = 'Press Right to Start!,')
    #still true
    if app.makeFlashCard == True:
        characterChoices = list(character_dict.values())
        listOfPossibleChoices = random.sample(characterChoices, k=4)
        app.practiceFlashCard.drawTimedFlashCard1(canvas, app)  
        canvas.create_text(app.cx, app.cy*1.2, font = 'Arial', 
    text ="Please Select/Input the Best Answer", fill = 'black')
        targetAnswer = app.practiceFlashCard.frontText
        drawAnswerChoices(app,canvas,listOfPossibleChoices)  
        modifiedAnswerQuestion(app,targetAnswer,listOfPossibleChoices)
             
    elif app.baseProblemTime == 0 or app.cardsToDo == 0:
        drawNextButton(app,canvas)   
    #if app.makeFlashCard == False and app.cardsToDo == 5:
        
        
    # # elif app.makeFlashCard == True and app.cardsToDo >= 0:
    # #     app.flashCard.drawFlashCard(canvas,app)
    # elif app.makeFlashCard == True and app.cardsToDo >= 0:
    #     app.newKey = getRandomKey()
    #     drawNewCard(app,canvas)  

    #if answer is correct and in a certain range

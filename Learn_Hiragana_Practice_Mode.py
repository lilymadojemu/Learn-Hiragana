from Classes import*
from Learn_Hiragana_Learning_Mode import*

correctAnswers = dict()
isCorrectKey = list()
incorrectAnswers = dict()
practiceHiraganaAndVocab = list(overall_dict.keys())
print(practiceHiraganaAndVocab)
toBePracticed = copy.deepcopy(overall_dict)
alreadyPracticed = dict()
#will form basis for review mode
toBeReview = dict()
knowledgeable = dict()


def getPracticeHiraganaOrVocab():
    hiraganaOrVocab = getRandomKey()
    #Base: Can store in practice
    #Inner: Store whether correct/incorrect
    if hiraganaOrVocab in hiraganaList:
        hiraganaValue = toBeLearned[hiraganaOrVocab]
        prevFlashCard[hiraganaOrVocab] = hiraganaValue 
        seenHiraganaFlashCards[hiraganaOrVocab] = hiraganaValue 
        seenFlashCards[hiraganaOrVocab] = hiraganaValue 
        del toBePracticed[hiraganaOrVocab]      
    elif hiraganaOrVocab in vocabList:
        vocabValue = toBeLearned[hiraganaOrVocab]
        prevFlashCard[hiraganaOrVocab] = vocabValue
        seenVocabFlashCards[hiraganaOrVocab] = vocabValue
        seenFlashCards[hiraganaOrVocab] = vocabValue
        del toBePracticed[hiraganaOrVocab] 
    return hiraganaOrVocab 



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
    #timeDifference = defaultTimeLimit = timeTaken
    questionType = getQuestionType()
    if questionType == 1: #hiragana to romanji
        questionFlashCard = FlashCard(app.newKey,toBePracticed[app.newKey])
        if (defaultTimeLimit != 0 and questionFlashCard.frontText 
            in hiraganaList):
                targetAnswer = questionFlashCard.frontText
                questionFlashCard.drawTimedFlashCard1(canvas, app)
                print(targetAnswer)
                app.showMessage('Press e to Input Your Answer!')
                if app.wantInput == 'Yes':
                    answer = app.getUserInput('Please Type in Best Answer')
                    if answer == None:
                        app.wantInput == 'No'
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
    return randomQuestionType

def drawAnswerChoices(app,canvas,listOfChoices):
    #Option 1
    randomChoice1 = listOfChoices[0]
    canvas.create_rectangle(app.cx//2,app.cy//12,app.cx*1.5,app.cy//6, 
    text =f'{randomChoice1}',  fill = 'plum')
    #Baby Button
    canvas.create_oval(app.cx,app.cy,0,0, fill = 'white')
    #Option 2
    randomChoice2 = listOfChoices[1]
    canvas.create_rectangle(app.cx//2,app.cy//12,app.cx*1.5,app.cy//6, 
    text = f'{randomChoice2}', fill = 'plum')
    canvas.create_oval(app.cx,app.cy//2,0,0, text =f'',
                    fill = 'white')
    #Option 3
    randomChoice3 = listOfChoices[2]
    canvas.create_rectangle(app.cx//2,app.cy//12,app.cx*1.5,app.cy//6,
    text = f'{randomChoice3}', fill = 'plum')

    canvas.create_oval(app.cx,app.cy//4,0,0, fill = 'white')
    #Option 4
    randomChoice4 = listOfChoices[3]
    canvas.create_rectangle(app.cx//2,app.cy//12,app.cx*1.5,app.cy//6, 
    text = f'{randomChoice4}', fill = 'plum')
    canvas.create_oval(app.cx,app.cy//6,0,0, fill = 'white')

#keep randomizing list until targetAnswer in list of possible answers
def practiceMode_keyPressed(app,event):
    #Pausing, unpausing in Practice Mode Only
    if (event.key == 'p'):
        app.paused = not app.paused
    if event.key == 'q':
        app.showMessage("All your progress will be lost!")
        app.phase = 'start'
    if event.key == 'Right':
        app.makeFlashCard = True
        app.cardsToDo -= 1
    if event.key == 's':
        app.startQuestion = True
        app.finishedQuestion = False
    elif event.key == 'd':
        app.startQuestion = False
        app.finishedQuestion = True
    elif event.key == 'e':
        app.wantInput = 'Yes'

def practice_mousePressed(app,event):
    if event.key == 'Up':
        app.showMessage("Went up!")

def modifiedIsCorrect(targetAnswer,answerChoice, app):
    correctMessages = ["That's Correct!", "You're the best!", 
                            "You're a Hiragana Expert!"]
    incorrectMessages = ["Sorry, that's incorrect","Better luck next time!"]
    #may need to be changed for other question types
    if answerChoice == targetAnswer and app.finishedQuestion == True:
        storeCorrectIncorrect(targetAnswer,answerChoice, True, app)
        praise = random.choice(correctMessages)
        app.showMessage(praise)
    elif answerChoice != targetAnswer and app.finishedQuestion == True:
        #defaulQuestionTime - time user takes to answer a question
        storeCorrectIncorrect(targetAnswer,answerChoice, False,app)
        notPraise = random.choice(incorrectMessages)
        app.showMessage(notPraise)

def modifiedAnswerQuestion(app,canvas):
    startTime = time.time()
    defaultTimeLimit = app.baseProblemTime
    #timeDifference = defaultTimeLimit = timeTaken
     #hiragana to romanji
    if defaultTimeLimit != 0:
            targetAnswer = app.flashCard.frontText
            print(targetAnswer)
            #app.showMessage('Press e to Input Your Answer!')
            if app.wantInput == 'Yes':
                answer = app.getUserInput('Please Type in Best Answer')
                if answer == None:
                    app.wantInput == 'No'
                else:
                    app.finishedQuestion = True
                    modifiedIsCorrect(targetAnswer,answer, app)
            else:
                #Seleting an answer choice
                listOfPossibleChoices =(random.sample(practiceHiraganaAndVocab, 
                                        k=4))
                if targetAnswer in listOfPossibleChoices:
                    #drawAnswerChoices(app,canvas,listOfPossibleChoices)
                    #if clicked, that is answerChoice number
                    userAnswer  = app.answerChoice
                    app.finishedQuestion = True
                    modifiedIsCorrect(targetAnswer,userAnswer, app)
    elif defaultTimeLimit <= 0:
        app.showMessage("Time's Up!")
        app.showMessage('Please Press Right or Click Next to Continue')

#Automatically move on to next flashcard card, Doing stage
def timerFired(app):
    if app.paused == False:
        if app.startQuestion == True:
            app.baseProblemTime -= 1
            app.timeTaken += 1
        
def practiceModeRedrawAll(app,canvas):
    if app.makeFlashCard == False and app.cardsToDo == 5:
        app.practiceFlashCard.drawTimedFlashCard1(canvas, app)
        #modifiedAnswerQuestion(app,canvas) 
        #drawAnswerChoices(app,canvas,listOfPossibleChoices)
    # # elif app.makeFlashCard == True and app.cardsToDo >= 0:
    # #     app.flashCard.drawFlashCard(canvas,app)
    # elif app.makeFlashCard == True and app.cardsToDo >= 0:
    #     app.newKey = getRandomKey()
    #     drawNewCard(app,canvas)  
    canvas.create_text(app.cx, app.cy*1.2, font = 'Arial', 
    text ="Please Select/Input\nthe Best Answer", fill = 'black')
    if (app.cardsToLearn == 0):
        app.phase = 'transition'
   
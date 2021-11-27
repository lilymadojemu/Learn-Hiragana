from Classes import*
from Learn_Hiragana_Learning_Mode import*
from Populate_Values import*
from random import randrange
def practice_appStarted(app):
    pass
practiceHiraganaAndVocab = list(overall_dict.keys())
toBePracticed = copy.deepcopy(overall_dict)
###############################################################################
# Leitner system,3 box set up
#ima, questioned right after
#middle, comes up after 2 questions of other types (1 immediate & 1 adv, etc.)
#adv, comes up after 4 questions 
#Practice is unlimitied (BUT!) Transition screen will come up every few cards
#to give users opporunity to end session and see progress
###############################################################################
#Getting Things
###############################################################################
seenBox1Keys = []
def getBox1Key(app):
    box1Keys = list(app.ima.keys())
    for currBox1Key in box1Keys:
        if currBox1Key != app.practiceKey and currBox1Key not in seenBox1Keys:
            seenBox1Keys.append(currBox1Key)
            return currBox1Key
seenBox2Keys = []
def getBox2Key(app):
    box2Keys =list(app.mama.keys())
    for currBox2Key in box2Keys:
        if currBox2Key != app.practiceKey and currBox2Key not in seenBox2Keys:
            seenBox2Keys.append(currBox2Key)
            return currBox2Key

seenBox3Keys = []
def getBox3Key(app):
    box3Keys = list(app.jyozu.keys())
    for currBox3Key in box3Keys:
        seenBox3Keys.append(currBox3Key)
        return currBox3Key

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
def getSummary(app):
    return app.ima, app.mama, app.jyozu
################################################################
#Determining Correctness
###############################################################

def storeCorrectIncorrect(questionCorrect,app):
    #Question Type 1
    answerChoice = app.userAnswer
    print(answerChoice)
    questionType = app.currQuestionType
    if questionType == 1:
        if questionCorrect == True:
            
            #No correct answers in box 1
            #Criteria to get to box 2 from box 1
            if (app.practiceKey in app.ima and 
                app.practiceKey not in app.mama and 
                app.practiceKey not in app.jyozu):
                #print(app.prevFlashCard)
                #Initial FlashCard
                #if app.cardsToDo == 5:
                app.mama.add(app.practiceKey)
                app.ima.remove(app.practiceKey)
                print(app.mama)
                #Other FlashCards
                # else:
                #     lookingFor = overall_dict[app.practiceKey]
                #     answer = lookingFor[0]
                #     app.mama[answer] = answerChoice
            #Criteria to get to box 3 from box 2
            elif (app.practiceKey not in app.ima and 
                    app.practiceKey in app.mama and 
                    app.practiceKey not in app.jyozu):
                    #if app.cardsToDo == 5:
                    app.jyozu.add(app.practiceKey)
                    app.mama.remove(app.practiceKey)
                    print(app.jyozu)
                    # else:
                    #     lookingFor = overall_dict[app.practiceKey]
                    #     answer = lookingFor[0]
                    #     app.jyozu[answer] = answerChoice
            elif (app.practiceKey not in app.ima and 
                    app.practiceKey not in app.mama
                    and app.practiceKey in app.jyozu):
                    if app.practiceKey in hiraganaList:
                        app.characterLevel += 1
                    elif app.practiceKey in vocabList:
                        app.vocabLevel += 1
            else:
                print(app.mama)
                app.showMessage('Question Correct storing error')
        #Currently not removing anything
        elif questionCorrect == False:
            #Get into box 2 from box 3
            if (app.practiceKey not in app.ima and 
                app.practiceKey not in app.mama
                and app.practiceKey in app.jyozu):
                #Currently not removing anything
                # if app.cardsToDo == 5:
                app.mama.add(app.practiceKey)
                app.jyozu.remove(app.practiceKey)
                # else:
                #     lookingFor = overall_dict[app.practiceKey]
                #     answer = lookingFor[0]
                #     app.mama[answer] = answerChoice
            #Get into box 1 from box 2
            elif (app.practiceKey not in app.ima and 
                app.practiceKey in app.mama and 
                app.practiceKey not in app.jyozu):
                #if app.cardsToDo == 5:
                    app.ima.add(app.practiceKey)
                    app.mama.remove(app.practiceKey)
                # else:
                #     lookingFor = overall_dict[app.practiceKey]
                #     answer = lookingFor[0]
                #     app.ima[answer] = answerChoice
            #Lower Character & vocab levels
            elif (app.practiceKey in app.ima and 
                app.practiceKey not in app.mama and 
                app.practiceKey  not in app.jyozu):
                if app.practiceKey in hiraganaList:
                    app.characterLevel -= 1
                elif app.practiceKey in vocabList:
                    app.vocabLevel -= 1
            else:
                app.showMessage('Question Incorrect storing error')
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
def drawAnswerChoices(app,canvas):
    randomChoice1 = app.listOfPossibleChoices[0]
    randomChoice2 = app.listOfPossibleChoices[1]
    randomChoice3 = app.listOfPossibleChoices[2]
    randomChoice4 = app.listOfPossibleChoices[3]
    if app.lightMode == True:
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.3,
                                app.cx//2,
                                app.cy*1.4, 
                                fill = 'light goldenrod')
        canvas.create_text(app.cx,app.cy*1.35,text = f'1 {randomChoice1}', 
        fill ='black' )

        #Option 2
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.4,
                                app.cx//2,
                                app.cy*1.5, 
                                fill = 'plum')
        canvas.create_text(app.cx,app.cy*1.45,text = f'2 {randomChoice2}', 
        fill ='black' )

        #Option 3
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.5,
                                app.cx//2,
                                app.cy*1.6,
                                fill = 'lemon chiffon')
        canvas.create_text(app.cx,app.cy*1.55, text = f'3 {randomChoice3}', 
        fill ='black' )
        
        #Option 4
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.6,
                                app.cx//2,
                                app.cy*1.7,
                                fill = 'honeydew2')
        canvas.create_text(app.cx,app.cy*1.65, text = f'4 {randomChoice4}', 
        fill ='black')
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.7,
                                app.cx//2,
                                app.cy*1.8,
                                fill = 'snow')
        canvas.create_text(app.cx,app.cy*1.75,
                            text = 'Press e to Input Your Answer', 
                            fill ='black')
    elif app.darkMode == True:
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.3,
                                app.cx//2,
                                app.cy*1.4, 
                                fill = 'pale violet red')
        canvas.create_text(app.cx,app.cy//12,text = f'{randomChoice1}', 
        fill ='black' )

        #Option 2
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.4,
                                app.cx//2,
                                app.cy*1.5, 
                                fill = 'dark orange')
        canvas.create_text(app.cx//2,app.cy//12,text = f'{randomChoice2}', 
        fill ='black' )

        #Option 3
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.5,
                                app.cx//2,
                                app.cy*1.6,
                                fill = 'maroon')
        canvas.create_text(app.cx//2,app.cy//12,text = f'{randomChoice3}', 
        fill ='black' )

        #Option 4
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.6,
                                app.cx//2,
                                app.cy*1.7,
                                fill = 'dark goldenrod')
        canvas.create_text(app.cx//2,app.cy//12, text = f'{randomChoice4}', 
        fill ='black')
        #Input Answer Option
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.7,
                                app.cx//2,
                                app.cy*1.8,
                                fill = 'rosy brown')
        canvas.create_text(app.cx,app.cy*1.75,
                            text = 'Press e to Input Your Answer', 
                            fill ='black')
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
        app.currQuestionType = getQuestionType()  
        if app.ima == app.prevFlashCard or app.cardsToDo != 0:
            app.practiceKey = getPreviousKey(app)
        else: #THESE TIMES MAY CHANGE
            if (app.ima != set() and app.timeTaken <= 3 or app.mama == set() and
                app.jyozu == set()): #Box1
                app.practiceKey = getBox1Key(app)
            elif (app.mama != set() and app.timeTaken >=6 or 
                app.ima == set() and app.jyozu == set()):
                app.practiceKey = getBox2Key(app)
            elif (app.jyozu != set() and app.timeTaken >= 8 or 
                app.mama == set() and app.ima == set()):
                app.practiceKey = getBox3Key(app)
            elif app.ima == set() and app.mama == set() and app.jyozu == set():
                app.finishedQuestion = True
                app.cardsToDo = 0
            else:
                app.finishedQuestion = True
                app.cardsToDo = 0

        app.option1Chosen = False
        app.option2Chosen = False
        app.option3Chosen = False
        app.option4Chosen = False
        app.listOfPossibleChoices = getAnswerChoices()
        if app.practiceKey != None:
            realTarget = overall_dict[app.practiceKey]
        #from https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
            app.listOfPossibleChoices.insert(randrange(
                                    len(app.listOfPossibleChoices)+1),realTarget[0]) 
            app.baseProblemTime = 30
            app.timeTaken = 0
            app.makeFlashCard = True
            app.startQuestion = True
            app.finishedQuestion = False
            app.isContinueKeyPressed = True
            if app.cardsToDo != 0:
                app.cardsToDo -= 1
    if event.key == 's': 
        app.currQuestionType = getQuestionType()  
        app.practiceKey = getPreviousKey(app)
        app.listOfPossibleChoices = getAnswerChoices()
        print(app.practiceKey)
        realTarget = overall_dict[app.practiceKey]
        #from https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
        app.listOfPossibleChoices.insert(randrange(
                                len(app.listOfPossibleChoices)+1),realTarget[0])  
        app.baseProblemTime = 30
        app.timeTaken = 0
        app.makeFlashCard = True
        app.startQuestion = True
        app.finishedQuestion = False
    elif event.key == 'w':
        app.listOfPossibleChoices = getAnswerChoices()  
    elif event.key == 'e':
        app.userAnswer = app.getUserInput('Please Type in Best Answer')
        app.wantInput = True
    #Answer Selections
    if event.key == '1':
        app.option1Chosen = True
    elif event.key == '2':
        app.option2Chosen = True
    elif event.key == '3':
        app.option3Chosen = True
    elif event.key == '4':
        app.option4Chosen = True
def practice_mousePressed(app,event):
    if app.width//4 <= event.x:
        if event.y: #option1
            app.showMessage('Clicked1')
            app.option1Chosen = True
        elif event.y: #option2
            app.showMessage('Clicked2')
            app.option2Chosen = True
        elif event.y: #option3
            app.showMessage('Clicked3')
            app.option3Chosen = True
        elif event.y: #option4
            app.showMessage('Clicked4')
            app.option4Chosen = True
        elif event.y: #Input
            app.showMessage('ClickedI')
            app.wantInput = True
            app.userAnswer = app.getUserInput('Please Type in Best Answer')
        elif event.y: #Click Next/Finished
            app.currQuestionType = getQuestionType()  
            getPreviousKey(app)
            app.listOfPossibleChoices = getAnswerChoices()
            realTarget = app.practiceFlashCard.backText
            #from https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
            app.listOfPossibleChoices.insert(randrange(
                                    len(app.listOfPossibleChoices)+1),realTarget[0])  
            app.baseProblemTime = 30
            app.timeTaken = 0
            app.makeFlashCard = True
            app.startQuestion = True
            app.finishedQuestion = False
##############################################################################
def modifiedIsCorrect(targetAnswer, answerChoice, app):
    correctMessages = ["That's Correct!", "You're the best!", 
                            "You're a Hiragana Expert!"]
    incorrectMessages = ["Sorry, that's incorrect",
                "Better luck next time! Click Next/Press Right to Continue."]
    if answerChoice == targetAnswer and app.finishedQuestion == False:
        app.userAnswer = answerChoice
        storeCorrectIncorrect(True, app)
        praise = random.choice(correctMessages)
        app.showMessage(praise)
        app.startQuestion = False
        app.finishedQuestion = True
    elif answerChoice != targetAnswer and app.finishedQuestion == False:
        app.userAnswer = answerChoice
        storeCorrectIncorrect(False,app)
        notPraise = random.choice(incorrectMessages)
        app.showMessage(notPraise)  
        app.startQuestion = False
        app.finishedQuestion = True

def modifiedAnswerQuestion(app):
    defaultTimeLimit = app.baseProblemTime
    #hiragana to romanji
    if (app.currQuestionType == 1 and app.startQuestion == True and 
        app.finishedQuestion == False):
        values = overall_dict[app.practiceKey]
        answerValue = values[0]
        print(answerValue)
        if defaultTimeLimit > 0:
                if app.wantInput == True:
                    if app.userAnswer == None:
                        app.wantInput = False
                    else:
                        userAnswer = app.userAnswer
                        modifiedIsCorrect(answerValue, userAnswer, app)
                else:
                    if answerValue in app.listOfPossibleChoices:
                        if app.option1Chosen == True:
                            userAnswer  = app.listOfPossibleChoices[0]
                            modifiedIsCorrect(answerValue,userAnswer,app)
                        elif app.option2Chosen == True:
                            userAnswer = app.listOfPossibleChoices[1]
                            modifiedIsCorrect(answerValue,userAnswer,app)
                        elif app.option3Chosen == True:
                            userAnswer = app.listOfPossibleChoices[2]
                            modifiedIsCorrect(answerValue,userAnswer,app)
                        elif app.option4Chosen == True:
                            userAnswer = app.listOfPossibleChoices[3]
                            modifiedIsCorrect(answerValue,userAnswer,app)
        elif defaultTimeLimit == 0:
            app.showMessage("Time's Up! Please Press Right to Continue")
        # else:
        #     if defaultTimeLimit > 0:
        #             if app.wantInput == True:
        #                 if app.userAnswer == None:
        #                     app.wantInput = False
        #                 else:
        #                     userAnswer = app.userAnswer
        #                     modifiedIsCorrect(answer, userAnswer, app)
        #     else:
        #         if answer in app.listOfPossibleChoices:
        #             if app.option1Chosen == True:
        #                 userAnswer  = app.listOfPossibleChoices[0]
        #                 modifiedIsCorrect(answer,userAnswer,app)
        #             elif app.option2Chosen == True:
        #                 userAnswer = app.listOfPossibleChoices[1]
        #                 modifiedIsCorrect(answer,userAnswer,app)
        #             elif app.option3Chosen == True:
        #                 userAnswer = app.listOfPossibleChoices[2]
        #                 modifiedIsCorrect(answer,userAnswer,app)
        #             elif app.option4Chosen == True:
        #                 userAnswer = app.listOfPossibleChoices[3]
        #                 modifiedIsCorrect(answer,userAnswer,app)
        #         elif defaultTimeLimit == 0:
        #             app.showMessage("Time's Up! Please Press Right to Continue")
    elif app.currQuestionType == 2: #vocab to romanji
        pass
    elif app.currQuestionType == 3: #romanji to vocab
        pass
    
    elif app.currQuestionType == 4: #romanji to hiragana
        pass
    else:
        app.showMessage("Sorry, There has been an error")
            
#Automatically move on to next flashcard card, Doing stage
def practice_timerFired(app):
    if app.paused == False:
        if (app.startQuestion == True and app.finishedQuestion == False and 
                app.currQuestionType == 1 and app.makeFlashCard == True):
                startTime = time.time()
                modifiedAnswerQuestion(app)
                app.baseProblemTime -= 1
                endTime = time.time()
                app.timeTaken = endTime - startTime
                print(app.timeTaken)
                if app.baseProblemTime == 0:
                    app.startQuestion = False
                    app.finishedQuestion = True
        if  (app.finishedQuestion == True and app.cardsToDo == 0):
            app.phase = 'transition'

###########################################################################
#Drawings
###########################################################################
def drawAnswerChoices(app,canvas):
    randomChoice1 = app.listOfPossibleChoices[0]
    randomChoice2 = app.listOfPossibleChoices[1]
    randomChoice3 = app.listOfPossibleChoices[2]
    randomChoice4 = app.listOfPossibleChoices[3]
    if app.lightMode == True:
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.3,
                                app.cx//2,
                                app.cy*1.4, 
                                fill = 'light goldenrod')
        canvas.create_text(app.cx,app.cy*1.35,text = f'1 {randomChoice1}', 
        fill ='black' )
        #Option 2
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.4,
                                app.cx//2,
                                app.cy*1.5, 
                                fill = 'plum')
        canvas.create_text(app.cx,app.cy*1.45,text = f'2 {randomChoice2}', 
        fill ='black' )
        #Option 3
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.5,
                                app.cx//2,
                                app.cy*1.6,
                                fill = 'lemon chiffon')
        canvas.create_text(app.cx,app.cy*1.55, text = f'3 {randomChoice3}', 
        fill ='black' )
        #Option 4
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.6,
                                app.cx//2,
                                app.cy*1.7,
                                fill = 'honeydew2')
        canvas.create_text(app.cx,app.cy*1.65, text = f'4 {randomChoice4}', 
        fill ='black')
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.7,
                                app.cx//2,
                                app.cy*1.8,
                                fill = 'snow')
        canvas.create_text(app.cx,app.cy*1.75,
                            text = 'Press e to Input Your Answer', 
                            fill ='black')
    elif app.darkMode == True:
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.3,
                                app.cx//2,
                                app.cy*1.4, 
                                fill = 'pale violet red')
        canvas.create_text(app.cx,app.cy//12,text = f'{randomChoice1}', 
        fill ='black' )
       
        #Option 2
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.4,
                                app.cx//2,
                                app.cy*1.5, 
                                fill = 'dark orange')
        canvas.create_text(app.cx//2,app.cy//12,text = f'{randomChoice2}', 
        fill ='black' )

        #Option 3  
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.5,
                                app.cx//2,
                                app.cy*1.6,
                                fill = 'maroon')
        canvas.create_text(app.cx//2,app.cy//12,text = f'{randomChoice3}', 
        fill ='black' )
        
        #Option 4
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.6,
                                app.cx//2,
                                app.cy*1.7,
                                fill = 'dark goldenrod')
        canvas.create_text(app.cx//2,app.cy//12, text = f'{randomChoice4}', 
        fill ='black')
        
        canvas.create_rectangle(app.cx*1.5,
                                app.cy*1.7,
                                app.cx//2,
                                app.cy*1.8,
                                fill = 'rosy brown')
        canvas.create_text(app.cx,app.cy*1.75,
                            text = 'Press e to Input Your Answer', 
                            fill ='black')

def drawNextButton(app,canvas):
    canvas.create_rectangle(app.cx//1.2,
                            app.cy//2.5,
                            app.cx*1.2,
                            app.cy//1.8, 
                            fill = 'honeydew2')
    canvas.create_text(app.cx,app.cy//2, font = 'Arial', text = "Next", 
                        fill = 'DeepSkyBlue2')

def drawFinishButton(app,canvas):
    canvas.create_rectangle(app.cx//1.2,
                            app.cy*1.2,
                            app.cx*1.2,
                            app.cy//3, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx,app.cy//5, font = 'Arial', text = "Finish", 
                        fill = 'azure4')
def drawPracticeCard(app,canvas):
    #FlashCard info.
    practiceFlashCard = FlashCard(app.practiceKey, overall_dict[app.practiceKey])
    practiceFlashCard.drawTimedFlashCard1(canvas, app)
    canvas.create_text(app.cx, app.cy*1.2, font = 'Arial 15', 
    text ="Please Select/Input the Best Answer", fill = 'black')

def practiceModeRedrawAll(app,canvas):
    canvas.create_text(app.cx,app.cy, font = 'Arial 20',
                        text = 'Press s to Start!')
    if (app.makeFlashCard == True and app.cardsToDo > 0 and 
        app.practiceKey != None):
        drawPracticeCard(app,canvas) 
        drawAnswerChoices(app,canvas)  
    if app.finishedQuestion == True and app.cardsToDo > 0:
        drawNextButton(app,canvas)  
    if app.finishedQuestion == True and app.cardsToDo == 0:
        drawFinishButton(app,canvas)
    #If time difference is in some range, draw that card from box 2 or 3
    #Box 1, First five from learning mode that is the first time seeing and 
    # anything wrong from box 2
    #if app.ima != dict() and 30 <= app.timeTaken >= 40:
        #drawPracticeCard (Where will app.practice key come from?)
    #elif

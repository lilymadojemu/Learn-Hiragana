#Review Mode

from Classes import*
from Learn_Hiragana_Learning_Mode import*
from Populate_Values import*
from random import randrange

practiceHiraganaAndVocab = list(overall_dict.keys())
toBePracticed = copy.deepcopy(overall_dict)
'''
Getting Things
'''
#Determines if len(app.jyozu) is a factor of 5 and adjusts number of cards in
#learn mode accordingly
def isFactor(app): pass

def getBox1Key(app):
    for currBox1Key in app.reviewBox1:
        # if currBox1Key != app.practiceKey:
        #     #app.seenBox1Keys.append(currBox1Key)
            return currBox1Key

def getBox2Key(app):
    for currBox2Key in app.reviewBox2:
            return currBox2Key
def getBox3Key(app):
    box3Keys = app.reviewBox3
    for currBox3Key in box3Keys:
        if app.reviewKey  != currBox3Key and currBox3Key not in app.justSeen:
            app.justSeen.add(currBox3Key)
            return currBox3Key
        elif( currBox3Key in app.justSeen and 
            len(app.justSeen) == len(app.currSession.keys())):
            app.justSeen = set()

def getQuestionType():
    randomQuestionType = random.randint(1,4)
    testingType = 1
    return testingType

def getAnswerChoices(app):
    #Question Type 1
    characterChoices = list(character_dict.values())
    characterPronunciations = list()
    vocabChoices = list(vocabulary_dict.values())
    vocabPronunciations = list()
    for row in range(len(characterChoices)):
        for col in range(len(characterChoices[0])):
            romanji = characterChoices[row][col]
            if len(romanji) == 1:
                characterPronunciations.append(romanji)
    for vocabRow in range(len(vocabChoices)):
        for vocabCol in range(len(vocabChoices[0])):
            vocab = vocabChoices[vocabRow][vocabCol]
            if len(vocab) == 1:
                vocabPronunciations.append(vocab)
    overallPronunciations = characterPronunciations +  vocabPronunciations
    if app.reviewKey not in overallPronunciations:
        return random.sample(overallPronunciations, k=3)

'''
Determining Correctness
'''
def storeCorrectIncorrect(questionCorrect,app):
    #Question Type 1
    answerChoice = app.userAnswer
    print(answerChoice)
    questionType = app.currQuestionType
    if questionType == 1:
        if questionCorrect == True:
            #No correct answers in box 1
            #Criteria to get to box 2 from box 1
            if (app.reviewKey  in app.reviewBox1 and 
                app.reviewKey not in app.reviewBox2 and 
                app.reviewKey  not in app.reviewBox3):
                app.reviewBox2.add(app.reviewKey )
                app.reviewBox1.remove(app.reviewKey )
                print(f' True box 1 to box 2 {app.reviewBox2}')
                print(f'Box 2 {app.reviewBox2}')
                print(f"Box 1 {app.reviewBox1}")
            #Criteria to get to box 3 from box 2
            elif (app.reviewKey not in app.reviewBox1 and 
                    app.reviewKey  in app.reviewBox2 and 
                    app.reviewKey  not in app.reviewBox3):
                    app.reviewBox3.add(app.reviewKey )
                    app.reviewBox2.remove(app.reviewKey )
                    print(f' True box 2 to box 3 {app.reviewBox3}')
                    print(f"Box 3 {app.reviewBox3}")
            else:
                app.showMessage('Question Correct storing error')
        elif questionCorrect == False:
            #Get into box 2 from box 3
            if (app.reviewKey not in app.reviewBox1 and 
               app.reviewKey  not in app.reviewBox2
                and app.reviewKey  in app.reviewBox3):
                app.reviewBox2.add(app.reviewKey )
                app.reviewBox3.remove(app.reviewKey )
                print(f' False Box 2 to 3 {app.reviewBox2}')
            #Get into box 1 from box 2
            elif (app.reviewKey not in app.reviewBox1 and 
                app.reviewKey  in app.reviewBox2 and 
                app.reviewKey  not in app.reviewBox3):
                # if len(app.seenBox1Keys) == 5:
                #     app.seenBox1Keys = list()
                app.reviewBox1 .add(app.reviewKey)
                app.reviewBox2.remove(app.reviewKey )
                print(f' False Box 1 to 2 {app.reviewBox1}')
            else:
                app.showMessage('Question Incorrect storing error')
'''
Pressed
'''
def reviewMode_keyPressed(app,event):
    if event.key == 'p':
        app.paused = not app.paused
    elif event.key == 'Right':
        if app.wantInput == True:
            app.wantInput = False
        app.currQuestionType = getQuestionType()
        app.option1Chosen = False
        app.option2Chosen = False
        app.option3Chosen = False
        app.option4Chosen = False  
        if app.reviewBox1 != set():#Box 1
            app.reviewKey  = getBox1Key(app)
            print(f'From app.reviewBox1 {app.reviewKey }')
        if app.reviewBox1 == set(): 
                if app.reviewBox2 != set():#Box 2 preference
                    app.reviewKey  = getBox2Key(app)
                    print(f'From app.reviewBox2 {app.reviewKey }')
                elif (app.reviewBox2 == set() and app.reviewBox3 != set()):
                    app.reviewKey  = getBox3Key(app)
                    print(f'From app.reviewBox3 {app.reviewKey }')
                elif app.reviewBox3 != set():#Box 3 preference
                    app.reviewKey  = getBox3Key(app)
                    print(f'From app.reviewBox3 {app.reviewKey }')
                elif app.reviewBox2 != set() and app.reviewBox3 == set(): #Box 2 preference
                    app.reviewKey  = getBox2Key(app)
                    print(f'From app.reviewBox2 {app.reviewKey }')  
                else:
                    app.finishedQuestion = True         
        app.listOfPossibleChoices = getAnswerChoices(app)        
        if app.reviewKey  != None:
            realTarget = overall_dict[app.reviewKey]
        #from https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
            app.listOfPossibleChoices.insert(randrange(
                                len(app.listOfPossibleChoices)+1),realTarget[0]) 
            app.baseProblemTime = 15
            app.makeFlashCard = True
            app.startQuestion = True
            app.finishedQuestion = False
            app.isContinueKeyPressed = True
            # if app.cardsToDo != 0:
            #     app.cardsToDo -= 1
        # else:
        #     app.finishedQuestion = True
        #     app.cardsToDo = 0

    if event.key == 's': 
        app.currQuestionType = getQuestionType()  
        if app.reviewBox1 != None:
            app.reviewKey  = getBox1Key(app)
            app.listOfPossibleChoices = getAnswerChoices(app)
            if app.reviewKey  != None:
                realTarget = overall_dict[app.reviewKey]
                #from https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
                app.listOfPossibleChoices.insert(randrange(
                                len(app.listOfPossibleChoices)+1),realTarget[0])  
                app.baseProblemTime = 15
                app.makeFlashCard = True
                app.startQuestion = True
                app.finishedQuestion = False
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

def review_mousePressed(app,event):
    if app.cx//2 <= event.x <= app.cx*1.5:
        if app.cy*1.3 <= event.y <= app.cy*1.4:
            app.showMessage('Clicked1')
            app.option1Chosen = True
        elif app.cy*1.4 <= event.y <= app.cy*1.5: 
            app.showMessage('Clicked2')
            app.option2Chosen = True
        elif app.cy*1.5 <= event.y <= app.cy*1.6: 
            app.showMessage('Clicked3')
            app.option3Chosen = True
        elif app.cy*1.6 <= event.y <= app.cy*1.7: 
            app.showMessage('Clicked4')
            app.option4Chosen = True
        elif app.cy*1.7 <= event.y <= app.cy*1.8: 
            app.showMessage('ClickedI')
            app.wantInput = True
            app.userAnswer = app.getUserInput('Please Type in Best Answer')
    elif app.cx//1.2 < event.x < app.cx*1.2:
        if app.cy//2.5 <= event.y <= app.cy//1.8:
            print('Next is clicked')
             #Click Next/Finished
            app.currQuestionType = getQuestionType()  
        if app.reviewBox1 != set():#Box 1
            app.reviewKey  = getBox1Key(app)
            print(f'From app.reviewBox1 {app.reviewKey }')
        elif app.reviewBox1 == set(): 
                if app.reviewBox2 != set():#Box 2 preference
                    app.reviewKey  = getBox2Key(app)
                    print(f'From app.reviewBox2 {app.reviewKey }')
                elif (app.reviewBox2 == set() and app.reviewBox3 != set()):
                    app.reviewKey  = getBox3Key(app)
                    print(f'From app.reviewBox3 {app.reviewKey }')
                elif app.reviewBox3 != set():#Box 3 preference
                    app.reviewKey  = getBox3Key(app)
                    print(f'From app.reviewBox3 {app.reviewKey }')
                elif app.reviewBox2 != set() and app.reviewBox3 == set(): #Box 2 preference
                    app.reviewKey  = getBox2Key(app)
                    print(f'From app.reviewBox2 {app.reviewKey }')  
                else:
                    app.finishedQuestion = True    
        app.listOfPossibleChoices = getAnswerChoices(app)        
        app.option1Chosen = False
        app.option2Chosen = False
        app.option3Chosen = False
        app.option4Chosen = False
        if app.reviewKey  != None:
            realTarget = overall_dict[app.reviewKey]
        #from https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
            app.listOfPossibleChoices.insert(randrange(
                            len(app.listOfPossibleChoices)+1),realTarget[0]) 
            app.baseProblemTime = 30
            app.timeTaken = 0
            app.makeFlashCard = True
            app.startQuestion = True
            app.finishedQuestion = False
            # app.isContinueKeyPressed = True
            # if app.cardsToDo != 0:
            #     app.cardsToDo -= 1

def modifiedIsCorrect(targetAnswer, answerChoice, app):
    correctMessages = ["That's Correct!", "You're the best!", 
                            "You're a Hiragana Expert!"]
    incorrectMessages = ["Sorry, that's incorrect. Click Next/Press Right to Continue.",
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
        values = overall_dict[app.reviewKey]
        answerValue = values[0]
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
    elif app.currQuestionType == 2: #vocab to romanji
        pass
    elif app.currQuestionType == 3: #romanji to vocab
        pass
    
    elif app.currQuestionType == 4: #romanji to hiragana
        pass
    else:
        app.showMessage("Sorry, There has been an error")

def review_timerFired(app):
    if app.paused == False:
        if (app.startQuestion == True and app.finishedQuestion == False and 
                app.currQuestionType == 1 and app.makeFlashCard == True):
                startTime = time.time()
                modifiedAnswerQuestion(app)
                app.baseProblemTime -= 1
                if app.baseProblemTime == 0:
                    app.startQuestion = False
                    app.finishedQuestion = True
                if app.finishedQuestion == True:
                    endTime = time.time()
                    app.timeTaken = endTime - startTime
                    print(app.timeTaken)
        # if (len(app.jyozu) is a factor of five, and 
        #     app.characterLevel >= len(app.jyozu) and
        #     app.vocabLevel >= len(app.jyozu)):
        #     app.cardsToLearn = app.cardsToLearn*5

'''
Drawings
'''
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
        #Input
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

def drawReviewCard(app,canvas):
    practiceFlashCard = FlashCard(app.reviewKey , overall_dict[app.reviewKey])
    practiceFlashCard.drawTimedFlashCard1(canvas, app)
    canvas.create_text(app.cx, app.cy*1.2, font = 'Arial 15', 
    text ="Please Select/Input the Best Answer", fill = 'black')

def reviewModeRedrawAll(app,canvas):
    canvas.create_text(app.cx,app.cy//1.1, font = 'Arial 15',
                        text = "Press t at any time to see your progress!")
    if app.startQuestion == False:
        canvas.create_text(app.cx,app.cy, font = 'Arial 20',
                            text = 'Press s to Start!')
    if (app.makeFlashCard == True and app.reviewKey != None):
        drawReviewCard(app,canvas)
        drawAnswerChoices(app,canvas)  
    if app.finishedQuestion == True:
        drawNextButton(app,canvas)  
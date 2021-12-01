from Classes import*
from Learn_Hiragana_Learning_Mode import*
from Populate_Values import*
from random import randrange

#Practice is unlimitied (BUT!) Transition screen can be triggered at anytime
#to give users opporunity to end session and see progress
practiceHiraganaAndVocab = list(overall_dict.keys())
toBePracticed = copy.deepcopy(overall_dict)
'''
Getting Things
'''
#Determines if len(app.jyozu) is a factor of 5 and adjusts number of cards in
#learn mode accordingly
def isFactor(app): 
    if len(app.jyozu) % 5 == 0:
        return True
    return False

def getBox1Key(app):
    for currBox1Key in app.ima:
            return currBox1Key

def getBox2Key(app):
    for currBox2Key in app.mama:
            return currBox2Key

def getBox3Key(app):
    box3Keys = app.jyozu
    for currBox3Key in box3Keys:
        if app.practiceKey != currBox3Key and currBox3Key not in app.justSeen:
            app.justSeen.add(currBox3Key)
            return currBox3Key
        elif( currBox3Key in app.justSeen and 
            len(app.justSeen) == len(app.currSession.keys())):
            app.justSeen = set()

def getQuestionType():
    randomQuestionType = random.randint(1,4)
    baseType = 1
    return baseType

def getAnswerChoices(app):
    #Question Type 1
    characterChoices = list(character_dict.values())
    print(characterChoices)
    characterPronunciations = list()
    vocabChoices = list(vocabulary_dict.values())
    print(vocabChoices)
    vocabPronunciations = list()
    for row in range(len(characterChoices)):
        for col in range(len(characterChoices[0])):
            romanji = characterChoices[row][col]
            if len(romanji) == 1:
                characterPronunciations.append(romanji)
    for vocabRow in range(len(vocabChoices)):
        for vocabCol in range(len(vocabChoices[0])):
            vocab = vocabChoices[vocabRow][vocabCol]
            if len(vocab) >= 2:
                vocabPronunciations.append(vocab)
            elif len(vocab) == 1 and vocab in vocabList:
                vocabPronunciations.append(vocab)
    overallPronunciations = characterPronunciations + vocabPronunciations
    print(overallPronunciations)
    randomPronunications = random.sample(overallPronunciations, k=3)
    print(randomPronunications)
    if app.practiceKey not in randomPronunications:
        return randomPronunications

'''
Determining Correctness
'''
def storeCorrectIncorrect(questionCorrect,app):
    #Question Type 1
    answerChoice = app.userAnswer
    questionType = app.currQuestionType
    if questionType == 1:
        if questionCorrect == True:
            #No correct answers in box 1
            #Criteria to get to box 2 from box 1
            if (app.practiceKey in app.ima and 
                app.practiceKey not in app.mama and 
                app.practiceKey not in app.jyozu):
                app.mama.add(app.practiceKey)
                app.ima.remove(app.practiceKey)
                print(f' True box 1 to box 2 {app.mama}')
                print(f'Box 2 {app.mama}')
                print(f"Box 1 {app.ima}")
            #Criteria to get to box 3 from box 2
            elif (app.practiceKey not in app.ima and 
                    app.practiceKey in app.mama and 
                    app.practiceKey not in app.jyozu):
                    app.jyozu.add(app.practiceKey)
                    app.mama.remove(app.practiceKey)
                    print(f' True box 2 to box 3 {app.jyozu}')
                    print(f"Box 3 {app.jyozu}")
            elif (app.practiceKey not in app.ima and 
                    app.practiceKey not in app.mama
                    and app.practiceKey in app.jyozu):
                    print(f'True Increase {app.jyozu}')
                    if app.practiceKey in hiraganaList:
                        app.characterLevel += 1
                    elif app.practiceKey in vocabList:
                        app.vocabLevel += 1
            else:
                app.showMessage('Question Correct storing error')
        #Currently not removing anything
        elif questionCorrect == False:
            #Get into box 2 from box 3
            if (app.practiceKey not in app.ima and 
                app.practiceKey not in app.mama
                and app.practiceKey in app.jyozu):
                app.mama.add(app.practiceKey)
                app.jyozu.remove(app.practiceKey)
                print(f' False Box 2 to 3 {app.mama}')
            #Get into box 1 from box 2
            elif (app.practiceKey not in app.ima and 
                app.practiceKey in app.mama and 
                app.practiceKey not in app.jyozu):
                app.ima.add(app.practiceKey)
                app.mama.remove(app.practiceKey)
                print(f' False Box 1 to 2 {app.ima}')
            #Lower Character & vocab levels
            elif (app.practiceKey in app.ima and 
                app.practiceKey not in app.mama and 
                app.practiceKey  not in app.jyozu):
                print(f' False decrease {app.jyozu}')
                if app.practiceKey in hiraganaList and app.characterLevel > 0:
                    app.characterLevel -= 1
                elif app.practiceKey in vocabList and app.vocabLevel > 0:
                    app.vocabLevel -= 1
            else:
                app.showMessage('Question Incorrect storing error')

'''
Pressed
'''
def practiceMode_keyPressed(app,event):
    if (event.key == 'p'):
        app.paused = not app.paused
    elif event.key == 'q':
        app.phase = 'start'

    elif event.key == 'Right':
        if app.wantInput == True:
            app.wantInput = False
        app.currQuestionType = getQuestionType()
        app.option1Chosen = False
        app.option2Chosen = False
        app.option3Chosen = False
        app.option4Chosen = False  
        if app.ima != set():#Box 1
            app.practiceKey = getBox1Key(app)
            print(f'From app.ima {app.practiceKey}')
        if app.ima == set(): 
                if app.mama != set():#Box 2 preference
                    app.practiceKey = getBox2Key(app)
                    print(f'From app.mama {app.practiceKey}')
                elif (app.mama == set() and app.jyozu != set()):
                    app.practiceKey = getBox3Key(app)
                    print(f'From app.jyozu {app.practiceKey}')
                elif app.jyozu != set():#Box 3 preference
                    app.practiceKey = getBox3Key(app)
                    print(f'From app.jyozu {app.practiceKey}')
                elif app.mama != set() and app.jyozu == set(): #Box 2 preference
                    app.practiceKey = getBox2Key(app)
                    print(f'From app.mama {app.practiceKey}')  
                else:
                    app.finishedQuestion = True         
        app.listOfPossibleChoices = getAnswerChoices(app)        
        if app.practiceKey != None:
            realTarget = overall_dict[app.practiceKey]
        #from https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
            app.listOfPossibleChoices.insert(randrange(
                                len(app.listOfPossibleChoices)+1),realTarget[0]) 
            app.baseProblemTime = 15
            app.makeFlashCard = True
            app.startQuestion = True
            app.finishedQuestion = False
            app.isContinueKeyPressed = True

    if event.key == 's': 
        app.currQuestionType = getQuestionType()  
        if app.ima != None:
            app.practiceKey = getBox1Key(app)
            app.listOfPossibleChoices = getAnswerChoices(app)
            if app.practiceKey != None:
                realTarget = overall_dict[app.practiceKey]
                #from https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
                app.listOfPossibleChoices.insert(randrange(
                                len(app.listOfPossibleChoices)+1),realTarget[0])  
                app.baseProblemTime = 15
                app.makeFlashCard = True
                app.startQuestion = True
                app.finishedQuestion = False
    elif event.key == 't':
        app.phase = 'transition'
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
    if app.cx//2 <= event.x <= app.cx*1.5:
        if app.cy*1.3 <= event.y <= app.cy*1.4:
            app.option1Chosen = True
        elif app.cy*1.4 <= event.y <= app.cy*1.5: 
            app.option2Chosen = True
        elif app.cy*1.5 <= event.y <= app.cy*1.6: 
            app.option3Chosen = True
        elif app.cy*1.6 <= event.y <= app.cy*1.7: 
            app.option4Chosen = True
        elif app.cy*1.7 <= event.y <= app.cy*1.8: 
            app.showMessage('ClickedI')
            app.wantInput = True
            app.userAnswer = app.getUserInput('Please Type in Best Answer')
    elif app.cx*1.3 < event.x < app.cx*1.7:
        if app.cy*1.45 <= event.y <= app.cy*1.6:
            if app.wantInput == True:
                app.wantInput = False
            app.currQuestionType = getQuestionType()
            app.option1Chosen = False
            app.option2Chosen = False
            app.option3Chosen = False
            app.option4Chosen = False  
            if app.ima != set():#Box 1
                app.practiceKey = getBox1Key(app)
                print(f'From app.ima {app.practiceKey}')
            if app.ima == set(): 
                    if app.mama != set():#Box 2 preference
                        app.practiceKey = getBox2Key(app)
                        print(f'From app.mama {app.practiceKey}')
                    elif (app.mama == set() and app.jyozu != set()):
                        app.practiceKey = getBox3Key(app)
                        print(f'From app.jyozu {app.practiceKey}')
                    elif app.jyozu != set():#Box 3 preference
                        app.practiceKey = getBox3Key(app)
                        print(f'From app.jyozu {app.practiceKey}')
                    elif app.mama != set() and app.jyozu == set(): #Box 2 preference
                        app.practiceKey = getBox2Key(app)
                        print(f'From app.mama {app.practiceKey}')  
                    else:
                        app.finishedQuestion = True         
            app.listOfPossibleChoices = getAnswerChoices(app)        
            if app.practiceKey != None:
                realTarget = overall_dict[app.practiceKey]
            #from https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
                app.listOfPossibleChoices.insert(randrange(
                                    len(app.listOfPossibleChoices)+1),realTarget[0]) 
                app.baseProblemTime = 15
                app.makeFlashCard = True
                app.startQuestion = True
                app.finishedQuestion = False
                app.isContinueKeyPressed = True

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
        values = overall_dict[app.practiceKey]
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

def practice_timerFired(app):
    if app.paused == False:
        if (app.startQuestion == True and app.finishedQuestion == False and 
                app.currQuestionType == 1 and app.makeFlashCard == True):
                modifiedAnswerQuestion(app)
                app.baseProblemTime -= 1
                if app.baseProblemTime == 0:
                    app.startQuestion = False
                    app.finishedQuestion = True
        if (isFactor(app) == True and len(app.jyozu) >= 5 and
            app.characterLevel >= len(app.jyozu) 
            and app.vocabLevel >= len(app.jyozu) 
            and app.cardsToLearn <= len(overall_dict)):
            print(app.cardsToLearn)
            app.cardsToLearn = app.learnNum + 5

'''
Drawings
'''
def drawAnswerChoices(app,canvas):
    randomChoice1 = app.listOfPossibleChoices[0]
    randomChoice2 = app.listOfPossibleChoices[1]
    randomChoice3 = app.listOfPossibleChoices[2]
    randomChoice4 = app.listOfPossibleChoices[3]
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

def drawPracticeCard(app,canvas):
    practiceFlashCard = FlashCard(app.practiceKey, overall_dict[app.practiceKey])
    practiceFlashCard.drawTimedFlashCard1(canvas, app)
    canvas.create_text(app.cx, app.cy*1.2, font = 'Arial 15', 
    text ="Please Select/Input the Best Answer", fill = 'black')

def practiceModeRedrawAll(app,canvas):
    canvas.create_text(app.cx,app.cy//1.1, font = 'Arial 15',
                        text = "Press t at any time to see your progress!",
                        fill = 'ghost white')
    if app.startQuestion == False:
        canvas.create_text(app.cx,app.cy, font = 'Arial 20',
                            text = 'Press s to Start!', fill = 'ghost white')
    if (app.makeFlashCard == True and app.practiceKey != None):
        drawPracticeCard(app,canvas) 
        drawAnswerChoices(app,canvas)  
    if app.finishedQuestion == True:
        canvas.create_text(app.cx,app.cy//1.5, font = 'Arial 20',
                            text = 'Press Right Arrow Key to Continue!', 
                            fill = 'ghost white')  
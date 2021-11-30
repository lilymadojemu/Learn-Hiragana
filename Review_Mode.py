#Review Mode

from Classes import*
from Learn_Hiragana_Learning_Mode import*
from Learn_Hiragana_Practice_Mode import*
from Populate_Values import*
from random import randrange
'''
Getting Things
'''
def getReviewBox1Key(app):
    for currBox1Key in app.reviewBox1:
            return currBox1Key

def getReviewBox2Key(app):
    for currBox2Key in app.reviewBox2:
            return currBox2Key

def getReviewBox3Key(app):
    box3Keys = app.reviewBox3
    for currBox3Key in box3Keys:
        if( app.reviewKey != currBox3Key and 
            currBox3Key not in app.justSeenReview):
            app.justSeenReview.add(currBox3Key)
            return currBox3Key
        elif(currBox3Key in app.justSeen and 
            len(app.justSeenReview) == len(app.toBeReviewed.keys())):
            app.justSeenReview = set()

'''
Determining Correctness
'''
def storeReviewCorrectIncorrect(questionCorrect,app):
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
    elif event.key == 'u':
        del app.toBeReviewed[app.reviewKey]
    elif event.key == 'Right':
        if app.wantInput == True:
            app.wantInput = False
        app.currQuestionType = getQuestionType()
        app.option1Chosen = False
        app.option2Chosen = False
        app.option3Chosen = False
        app.option4Chosen = False  
        if app.reviewBox1 != set():#Box 1
            app.reviewKey  = getReviewBox1Key(app)
            print(f'From app.reviewBox1 {app.reviewKey }')
        elif app.reviewBox1 == set(): 
                #Box 2 preference
                if app.reviewBox2 != set():
                    app.reviewKey  = getReviewBox2Key(app)
                    print(f'From app.reviewBox2 {app.reviewKey }')
                elif (app.reviewBox2 == set() and app.reviewBox3 != set()):
                    app.reviewKey  = getReviewBox3Key(app)
                    print(f'From app.reviewBox3 {app.reviewKey }')
                elif app.reviewBox3 != set():#Box 3 preference
                    app.reviewKey  = getReviewBox3Key(app)
                    print(f'From app.reviewBox3 {app.reviewKey }')
                #Box 2 preference   
                elif app.reviewBox2 != set() and app.reviewBox3 == set(): 
                    app.reviewKey  = getReviewBox2Key(app)
                    print(f'From app.reviewBox2 {app.reviewKey }')  
                else:
                    app.finishedQuestion = True         
        app.listOfPossibleChoices = getAnswerChoices(app)        
        if app.reviewKey != None:
            realTarget = overall_dict[app.reviewKey]
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
        if app.reviewBox1 != None:
            app.reviewKey  = getReviewBox1Key(app)
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
            app.reviewKey  = getReviewBox1Key(app)
            print(f'From app.reviewBox1 {app.reviewKey }')
        elif app.reviewBox1 == set(): 
                if app.reviewBox2 != set():#Box 2 preference
                    app.reviewKey  = getReviewBox2Key(app)
                    print(f'From app.reviewBox2 {app.reviewKey }')
                elif (app.reviewBox2 == set() and app.reviewBox3 != set()):
                    app.reviewKey  = getReviewBox3Key(app)
                    print(f'From app.reviewBox3 {app.reviewKey }')
                elif app.reviewBox3 != set():#Box 3 preference
                    app.reviewKey  = getReviewBox3Key(app)
                    print(f'From app.reviewBox3 {app.reviewKey }')
                elif app.reviewBox2 != set() and app.reviewBox3 == set(): #Box 2 preference
                    app.reviewKey  = getReviewBox2Key(app)
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
            app.baseProblemTime = 15
            app.makeFlashCard = True
            app.startQuestion = True
            app.finishedQuestion = False

def modifiedIsCorrect(targetAnswer, answerChoice, app):
    correctMessages = ["That's Correct!", "You're the best!", 
                            "You're a Hiragana Expert!"]
    incorrectMessages = ["Sorry, that's incorrect. Click Next/Press Right to Continue.",
                "Better luck next time! Click Next/Press Right to Continue."]
    if answerChoice == targetAnswer and app.finishedQuestion == False:
        app.userAnswer = answerChoice
        storeReviewCorrectIncorrect(True, app)
        praise = random.choice(correctMessages)
        app.showMessage(praise)
        app.startQuestion = False
        app.finishedQuestion = True
    elif answerChoice != targetAnswer and app.finishedQuestion == False:
        app.userAnswer = answerChoice
        storeReviewCorrectIncorrect(False,app)
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
'''
Delete from box once unfavorited
'''
def review_timerFired(app):
    if app.paused == False:
        if (app.startQuestion == True and app.finishedQuestion == False and 
                app.currQuestionType == 1 and app.makeFlashCard == True):
                modifiedAnswerQuestion(app)
                app.baseProblemTime -= 1
                if app.baseProblemTime == 0:
                    app.startQuestion = False
                    app.finishedQuestion = True

'''
Drawings
'''
def drawReviewCard(app,canvas):
    practiceFlashCard = FlashCard(app.reviewKey , overall_dict[app.reviewKey])
    practiceFlashCard.drawTimedFlashCard1(canvas, app)
    canvas.create_text(app.cx, app.cy*1.2, font = 'Arial 15', 
    text ="Please Select/Input the Best Answer", fill = 'black')

def reviewModeRedrawAll(app,canvas):
    if app.toBeReviewed != dict():
        canvas.create_text(app.cx,app.cy//1.1, font = 'Arial 15',
                        text = "Press u to unfavorite a word")
        if app.startQuestion == False:
            canvas.create_text(app.cx,app.cy, font = 'Arial 20',
                                text = 'Press s to Start!')
        if (app.makeFlashCard == True and app.reviewKey != None):
            drawReviewCard(app,canvas)
            drawAnswerChoices(app,canvas)  
        if app.finishedQuestion == True:
            drawNextButton(app,canvas)  
    else:
        canvas.create_text(app.cx,app.cy, font = ('Arial, 20, bold'),
                        text = "There are No Words to Review!")
        canvas.create_text(app.cx,app.cy*1.5, font = ('Arial, 20, bold'),
                        text = "Press q to return to start menu")

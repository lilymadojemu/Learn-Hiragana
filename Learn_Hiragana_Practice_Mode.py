from Classes import*

#sensei = SenseiBot("Sensei",app.baseProblemTime)

incorrectProblems = dict()
correctProblems = dict()
practiceHiraganaAndVocab = list(overall_dict.keys())
toBePracticed = copy.deepcopy(overall_dict)



def questionCard(app,canvas):
    questionFlashCard = FlashCard(practiceKey,toBePracticed[practiceKey])
    questionFlashCard.drawTimedFlashCard()
    pass

def answerQuestion(app):
    questionType = getQuestionType()
    #Kind or Strict
    sensei = SenseiBot('kind', problemTime,targetAnswer)
    sensei.isCorrect(userInput)
    app.showMessage('Please Select/Input the Best Answer!')
    if questionType == 1:
        sensei.isCorrect(userInput)
        pass
    elif questionType == 2:
        pass
    elif questionType == 3:
        pass
    
    elif questionType == 4:
        pass
    else:
        app.showMessage("There has been an error")

def getQuestionType():
    randomQuestionType = random.randint(1,4)
    return randomQuestionType


def practiceMode_keyPressed(app,event):
    #Pausing, unpausing in Practice Mode Only
    if (event.key == 'p'):
        app.paused = not app.paused
    if event.key == 'q':
        app.showMessage("All your progress will be lost!")
        app.phase = 'start'

def practice_mousePressed(app,event):
    if event.key == 'Up':
        app.showMessage("Went up!")

def drawAnswerChoices(app, canvas):
    pass

#manually underline text? loop over given word, if target letter in word, underline               
    #canvas.create_text(  f'{app.characterLevel}, {app.vocabLevel}')    
    #Back, romanji
    #function from another file
    # if isCorrect == False:
    #     #don't show back of card
    #     pass
# def practiceCards(selectedWord):
#     if currCard.getMeaning(selectedWord) == currCard.getMeaning(correctAnswer):
#         user.isCorrect(selectedWord) 
#     else:
#         not user.isCorrect(selectedWord)
#Automatically move on to next flashcard card, Doing stage
def timerFired(app):
    pass


def practiceModeRedrawAll(app,canvas):
    if app.makeFlashCard == False:
        app.startingFlashcard.drawFlashcard(canvas,app)
    elif app.makeFlashCard == True:
        app.newFlashCard.drawFlashcard(canvas,app)
    canvas.create_text(app.cx, app.cy, font = 'Arial', 
    text ="Please Select/Input\nthe Best Answer", fill = 'black')
    drawAnswerChoices(app,canvas)    
    if (app.cardsToLearn == 0):
        app.phase = 'transition'
   
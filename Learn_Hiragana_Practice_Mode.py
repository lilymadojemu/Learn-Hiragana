from Classes import*
from Learn_Hiragana_Learning_Mode import*

#sensei = SenseiBot("Sensei",app.baseProblemTime)

incorrectProblems = dict()
correctProblems = dict()
practiceHiraganaAndVocab = list(overall_dict.keys())
toBePracticed = copy.deepcopy(overall_dict)
alreadyPracticed = dict()



def getPracticeHiraganaOrVocab():
    hiraganaOrVocab = getRandomKey()
    #Base: Can store in practice
    #Inner: Store whether correct/incorrect
    if hiraganaOrVocab in hiraganaList:
        hiraganaValue = toBeLearned[hiraganaOrVocab]
        prevFlashCard[hiraganaOrVocab] = hiraganaValue 
        seenHiraganaFlashCards[hiraganaOrVocab] = hiraganaValue 
        seenFlashCards[hiraganaOrVocab] = hiraganaValue 
        #del toBeLearned[hiraganaOrVocab]      
    elif hiraganaOrVocab in vocabList:
        vocabValue = toBeLearned[hiraganaOrVocab]
        prevFlashCard[hiraganaOrVocab] = vocabValue
        seenVocabFlashCards[hiraganaOrVocab] = vocabValue
        seenFlashCards[hiraganaOrVocab] = vocabValue
        #del toBeLearned[hiraganaOrVocab] 
    return hiraganaOrVocab 

practiceKey = getHiraganaOrVocab()





def questionCard():
    questionFlashCard = FlashCard(practiceKey,toBePracticed[practiceKey])
    currQuestion = questionFlashCard.drawTimedFlashCard()
    return currQuestion


def answerQuestion(app,canvas):
    questionType = getQuestionType()
    #Kind or Strict
    sensei = SenseiBot('kind', problemTime,targetAnswer)
    app.showMessage('Please Select/Input the Best Answer!')
    if questionType == 1: #hiragana to romanji
        currCard = questionCard()
        targetAnswer = currCard.getFrontText()
        app.message('Press e to Input Your Answer!')
        if app.wantInput == 'Yes':
            pass
        else:
             #Seleting an answer choice
            listOfPossibleChoices = random.sample(practiceHiraganaAndVocab, k=4) 
            if targetAnswer in listOfPossibleChoices:
                drawAnswerChoices(app,canvas,listOfPossibleChoices)
                pass
                sensei.isCorrect(1,userInput, targetAnswer)
        '''click here if you want to input your answer!, wantInput'''
        pass
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
    canvas.create_rectangle()
    #Option 2
    canvas.create_rectangle()
    #Option 3
    canvas.create_rectangle()
    #Option 4
    canvas.create_rectangle()

#keep randomizing list until targetAnswer in list of possible answers
def practiceMode_keyPressed(app,event):
    #Pausing, unpausing in Practice Mode Only
    if (event.key == 'p'):
        app.paused = not app.paused
    if event.key == 'q':
        app.showMessage("All your progress will be lost!")
        app.phase = 'start'

    elif event.key == 'e':
        app.wantInput = 'Yes'

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
   
from Classes import*
from Populate_Values import*
modifyListOfKeys = list(overall_dict.keys())
toBeLearned = copy.deepcopy(overall_dict)
#Track what flashcards have been seen overall
seenFlashCards = dict()
seenHiraganaFlashCards = dict()
seenVocabFlashCards = dict()
def learning_appStarted(app):
    pass
def getRandomKey():
    randomKey = random.choice(modifyListOfKeys)
    return randomKey

def getHiraganaOrVocab(app,randomKey):
    hiraganaOrVocab = randomKey
    if hiraganaOrVocab in hiraganaList:
        hiraganaValue = overall_dict[hiraganaOrVocab]
        app.prevFlashCard[hiraganaOrVocab] = hiraganaValue
        seenHiraganaFlashCards[hiraganaOrVocab] = hiraganaValue
        seenFlashCards[hiraganaOrVocab] = hiraganaValue
        if (hiraganaOrVocab in modifyListOfKeys and 
            hiraganaOrVocab in toBeLearned):
            modifyListOfKeys.remove(hiraganaOrVocab)
            del toBeLearned[hiraganaOrVocab]      
    elif hiraganaOrVocab in vocabList:
        vocabValue = overall_dict[hiraganaOrVocab]
        app.prevFlashCard[hiraganaOrVocab] = vocabValue
        seenVocabFlashCards[hiraganaOrVocab] = vocabValue
        seenFlashCards[hiraganaOrVocab] = vocabValue
        print(seenFlashCards)
        if (hiraganaOrVocab in modifyListOfKeys and 
            hiraganaOrVocab in toBeLearned):
            modifyListOfKeys.remove(hiraganaOrVocab)
            del toBeLearned[hiraganaOrVocab] 


def drawNewCard(app,canvas):
    #FlashCard info.
    currFlashCard = FlashCard(app.newKey, overall_dict[app.newKey])
    currFlashCard.drawFlashCard(canvas,app)

def drawPrevCard(app,canvas):
    previousFlashCard = FlashCard(app.prevCard, overall_dict[app.prevCard])  
    print(overall_dict[app.prevCard])                 
    previousFlashCard.drawFlashCard(canvas,app)



#What is a flip, like a blink/flash, will need another background for back
#Understanding from https://www.youtube.com/watch?v=kvd6i1mXec8
#from https://coderedirect.com/questions/124487/simple-animation-using-tkinter
def learningMode_keyPressed(app,event):
    #flips front of flash card to back
    #flips back to front 
    if event.key == 'q':
        app.showMessage("All your progress will be lost!")
        app.phase = 'start'
    if event.key == 'Up' or event.key == 'Down':
        app.isFlipped = not app.isFlipped
    #Move to new card, populate next card
    elif event.key == 'Right':
        app.newKey = getRandomKey()
        app.isContinueKeyPressed = True
        app.makeFlashCard = True
        app.cardsLearned += 1
        if app.cardsToLearn != 0:
            app.cardsToLearn -= 1
    #Move to previous card
    elif event.key == 'Left':
        app.prevCard = getPreviousKey(app)
        app.isBackKeyPressed = True
        app.makeOldFlashCard = True
        if app.cardsToLearn != 0:
            app.cardsToLearn += 1

    elif event.key == 'r':
        app.phase = 'review'
    elif event.key == 'l':
        app.phase = 'practice'

def getPreviousKey(app):
    prevKeyList = list(app.prevFlashCard.keys())
    randomKey = random.choice(prevKeyList)
    if randomKey != app.newKey:
        return randomKey
    newKey = random.choice(prevKeyList)
    return newKey


def learningMode_mousePressed(app,event):
    #Determines whether a card needs to be flip
    if app.width >= event.x and event.y >= app.height:
            app.showMessage("Clicked!")
            app.isFlipped = not app.isFlipped
    #Fix parameters
    if (app.cardsToLearn > 0 and app.width//4 <= event.x and 
        event.x >= app.width//6 and app.height//10 <= event.y and 
        event.y >= app.height//6):
        app.makeNewCard = True
        app.cardsLearned += 1
        if app.cardsToLearn != 0:
            app.cardsToLearn -= 1
    elif (app.cardsToLearn == 0 and app.width//4 <= event.x and 
        event.x >= app.width//6 and app.height//10 <= event.y and 
        event.y >= app.height//5):
        app.showMessage('Are you ready to practice?\n Press l to Continue!')
        
def drawBackButton(app,canvas):
    canvas.create_rectangle(app.cx//1.5,
                            app.cy*1.45,
                            app.cx//-2,
                            app.cy*1.6, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx//1.5,app.cy*1.5,
                        font = 'Arial',  text = "Back", fill = 'black')
def drawNextButton(app,canvas):
    canvas.create_rectangle(app.cx*2.5,
                            app.cy*1.45,
                            app.cx,
                            app.cy*1.6, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.5,
                        font = 'Arial',  text = "Next", fill = 'black')
#Initiate Practice Mode
def drawLetsTryitButton(app,canvas):
    canvas.create_rectangle(app.cx*2.5,
                            app.cy*1.45,
                            app.cx,
                            app.cy*1.6, 
                            fill = 'cadet blue')
    canvas.create_text(app.cx*1.5,app.cy*1.5,
                        font = 'Arial',  text = "Let's Try it!", fill = 'black')
                        
def decreasingFrontCard(app):
    app.isShrinking = True 
    if app.isShrinking == True:
        if app.frontcx == app.width//2 and app.frontcy == app.height//2:
            app.frontcx -= 100
            app.frontcy -= 100
        elif app.frontcx == app.width//6 and app.frontcy == app.height//6:
            app.isShrinking = False
            app.isGrowing = True

def increasingBackCard(app):
    if app.isGrowing == True and app.isShrinking == False:
        if app.frontcx != app.width//2 and app.frontcy !=app.height//2:
            app.backcx += 100
            app.backcy += 100
        elif app.frontcx == app.width//2 and app.frontcy == app.height//2:
            app.isGrowing = False

def learning_timerFired(app):
    #"flipping flashCard"
    if app.isFlipped == True:
        '''
        Things look smaller and text/icons look zoomed out
        goes slow but there is then a "jump" to make the card look
        squeezed in horizontally
        Once it gets to that point of looking squeezed, there is a change of 
        what text is on the card and its size and it grows bigger

        Split up flash card (front and back)
        The front card needs to decrease to a certain point (but not completely)
        the back card will then be created and overlay whateva went on with 
        front card

        More of an illusion than actual flipping
        Only need to decrease once and increase once
        '''
        decreasingFrontCard(app)
        increasingBackCard(app)
    elif app.isContinueKeyPressed == True:
        getHiraganaOrVocab(app,app.newKey)
    elif (app.cardsToLearn == 5):
        getHiraganaOrVocab(app,app.firstKey)
    elif app.isBackKeyPressed == True:
        app.prevCard = getPreviousKey(app)


def learningModeRedrawAll(app,canvas):

    drawNextButton(app,canvas)
    # if toBeLearned == dict():
    #     app.showMessage("You have learned everything!")
    #     userYesOrNo = app.getUserInput("Want to Review")
    #     if userYesOrNo == 'Yes' or userYesOrNo == 'yes':
    #         app.showMessage("Press r to Review!")
    #     elif userYesOrNo == 'No' or userYesOrNo == 'no':
    #         app.showMessage("Press q to Quit!")
    #Learning Cards
    if  app.isContinueKeyPressed == False and app.cardsToLearn == 5:
        app.flashCard.drawFlashCard(canvas,app)
    if app.isContinueKeyPressed == True and toBeLearned != dict():
        drawNewCard(app,canvas)             
    if app.isBackKeyPressed == True and toBeLearned != dict():
        drawPrevCard(app,canvas)

    if app.cardsToLearn == 0:
        drawBackButton(app,canvas)
        drawLetsTryitButton(app,canvas)
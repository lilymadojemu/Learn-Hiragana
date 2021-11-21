from Classes import*

from Populate_Values import*
'''
Overall Purpose: It is up to the user to read what is on the front and back of 
the flashcards
'''
'''
flipping cards
be at a base position, want that base position to change when flipped
Get base position and center and ending base position & center
'''
modifyListOfKeys = list(overall_dict.keys())
toBeLearned = copy.deepcopy(overall_dict)
#not completely off base
prevFlashCard = dict()
#Track what flashcards have been seen overall
seenFlashCards = dict()
seenHiraganaFlashCards = dict()
seenVocabFlashCards = dict()

def getRandomKey():
    randomKey = random.choice(modifyListOfKeys)
    return randomKey

def getHiraganaOrVocab(randomKey):
    hiraganaOrVocab = randomKey
    if hiraganaOrVocab in hiraganaList:

        hiraganaValue = overall_dict[hiraganaOrVocab]
        
        prevFlashCard[hiraganaOrVocab] = hiraganaValue
        seenHiraganaFlashCards[hiraganaOrVocab] = hiraganaValue
        seenFlashCards[hiraganaOrVocab] = hiraganaValue
        if (hiraganaOrVocab in modifyListOfKeys and 
            hiraganaOrVocab in toBeLearned):

            modifyListOfKeys.remove(hiraganaOrVocab)
            del toBeLearned[hiraganaOrVocab]      
    elif hiraganaOrVocab in vocabList:
        vocabValue = overall_dict[hiraganaOrVocab]
        prevFlashCard[hiraganaOrVocab] = vocabValue
        seenVocabFlashCards[hiraganaOrVocab] = vocabValue
        seenFlashCards[hiraganaOrVocab] = vocabValue
        if (hiraganaOrVocab in modifyListOfKeys and 
            hiraganaOrVocab in toBeLearned):
            modifyListOfKeys.remove(hiraganaOrVocab)
            del toBeLearned[hiraganaOrVocab] 


def drawNewCard(app,canvas):
    #FlashCard info.
    currFlashCard = FlashCard(app.newKey, overall_dict[app.newKey])
    currFlashCard.drawFlashCard(canvas,app)

def makePrevCard(app,canvas):
    #FlashCard info.
    for oldKey in prevFlashCard:
        previousFlashCard = FlashCard(oldKey, prevFlashCard[oldKey])                   
        previousFlashCard.drawFlashCard(canvas, app)


#What is a flip, like a blink/flash, will need another background for back
#Understanding from https://www.youtube.com/watch?v=kvd6i1mXec8
#from https://coderedirect.com/questions/124487/simple-animation-using-tkinter
def blinkSmallerLearning(app):
    #Make app.cx and app.cy smaller until it reaches the center
    # app.cx = app.width//2
    # app.cy = app.height//2
    if app.cardcx < app.width//4 and app.cardcy < app.height//4:
        app.cardcx -= 100
        app.cardcy -= 100
    elif app.cx == app.width//4 and app.cy == app.height//4:
        blinkDefaultLearning(app)
def blinkDefaultLearning(app):
    if app.cardcx != app.width//2 and app.cardcy != app.height//2:
        app.cardx += 100
        app.cardcy += 100

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
        app.isContinueKeyPressed = True
        app.makeFlashCard = True
        app.cardsLearned += 1
        if app.cardsToLearn != 0:
            app.cardsToLearn -= 1
    #Move to previous card
    elif event.key == 'Left':
        app.isBackKeyPressed = True
        app.makeOldFlashCard = True
    elif event.key == 'r':
        app.phase = 'review'
    elif event.key == 'l':
        app.phase = 'practice'




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
    canvas.create_rectangle(app.cx//2,
                            app.cy*1.45,
                            app.cx//-2,
                            app.cy*1.6, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx//1.5,app.cy*1.5,
                        font = 'Arial',  text = "Back", fill = 'black')
def drawNextButton(app,canvas):
    canvas.create_rectangle(app.cx*3,
                            app.cy*1.45,
                            app.cx,
                            app.cy*1.6, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.5,
                        font = 'Arial',  text = "Next", fill = 'black')
#Initiate Practice Mode
def drawLetsTryitButton(app,canvas):
    canvas.create_rectangle(app.cx*3,
                            app.cy*1.45,
                            app.cx,
                            app.cy*1.6, 
                            fill = 'cadet blue')
    canvas.create_text(app.cx*1.5,app.cy*1.15,
                        font = 'Arial',  text = "Let's Try it!", fill = 'black')
                        
def decreasingFrontCard(app): pass
def increasingBackCard(app): pass
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
    if (app.makeFlashCard == True and toBeLearned != dict()):
        app.newKey = getRandomKey()
        getHiraganaOrVocab(app.newKey)
    if (app.isContinueKeyPressed == False and app.cardsToLearn == 5):
        getHiraganaOrVocab(app.firstKey)
        

def learningModeRedrawAll(app,canvas):
    drawNextButton(app,canvas)
    if toBeLearned == dict():
        app.showMessage("You have learned everything!")
        userYesOrNo = app.getUserInput("Want to Review")
        if userYesOrNo == 'Yes' or userYesOrNo == 'yes':
            app.showMessage("Press r to Review!")
        elif userYesOrNo == 'No' or userYesOrNo == 'no':
            app.showMessage("Press q to Quit!")
    #Learning Cards
    if (app.isContinueKeyPressed == False and app.cardsToLearn == 5):
        app.flashCard.drawFlashCard(canvas,app)
    elif (app.isContinueKeyPressed == True and toBeLearned != dict()):
        drawNewCard(app,canvas)             
    elif app.isContinueKeyPressed == False and app.isBackKeyPressed == True:
        makePrevCard(app,canvas)
    if app.cardsLearned >= 1 and app.phase == 'learning':
        drawBackButton(app,canvas)
    if app.cardsToLearn == 0 and app.phase == 'learning':
        drawLetsTryitButton(app,canvas)

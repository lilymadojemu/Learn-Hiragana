from Classes import*
from Populate_Values import*
import random
from random import randrange, sample

modifyListOfKeys = list(overall_dict.keys())
toBeLearned = copy.deepcopy(overall_dict)
#Track what flashcards have been seen overall
seenFlashCards = dict()
seenHiraganaFlashCards = dict()
seenVocabFlashCards = dict()
'''
Getting things
'''
#Gets a random key from the overall dictionary to be shown in current session
def getRandomKey():
    randomKey = random.choice(modifyListOfKeys)
    return randomKey

#Gets Each Previous Key in the dictionary for the current session
def getPreviousKey(app):
    prevCurrKeyList = list(app.currSession.keys())
    reversedList = prevCurrKeyList
    for prevKey in range(len(reversedList)):
        if app.prevCard == None and app.prevSet == set():
            app.prevCard = app.newKey
        elif app.prevCard != None and reversedList[prevKey] != None:
            currPreviousIndex = reversedList.index(app.prevCard)
            if reversedList[currPreviousIndex - 1] != None:
                if reversedList[currPreviousIndex - 1] not in app.prevSet:
                    app.prevSet.add(reversedList[currPreviousIndex - 1])
                return reversedList[currPreviousIndex - 1]

def getNextKeyFromPrevious(app):
    currListKeys = list(app.currSession.keys())
    for redrawCard in range(len(currListKeys)):
        if app.prevCard != None and currListKeys[redrawCard] != None:
            currPreviousIndex = currListKeys.index(app.prevCard)
            if len(currListKeys) <= 5 and currPreviousIndex + 1 < 5:
                if currListKeys[currPreviousIndex + 1] != None:
                    if currListKeys[currPreviousIndex + 1] in app.prevSet:
                        app.prevSet.remove(currListKeys[currPreviousIndex + 1])
                    return currListKeys[currPreviousIndex + 1]
#Stores the Hiragana Characters or Vocabulary words into dictionaries
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
        if (hiraganaOrVocab in modifyListOfKeys and 
            hiraganaOrVocab in toBeLearned):
            modifyListOfKeys.remove(hiraganaOrVocab)
            del toBeLearned[hiraganaOrVocab] 
'''
Pressed
'''
def learningMode_keyPressed(app,event):   
    if event.key == 'Up' or event.key == 'Down':
        app.isFlipped = not app.isFlipped
    elif event.key == 'Right':#Move to new card
        app.isFavorite = False
        if app.cardsLearned < app.learnNum and app.cardsToLearn >= 0:
            app.newKey = getRandomKey()
            if app.newKey != None:
                getHiraganaOrVocab(app,app.newKey)
                app.currSession[app.newKey] = overall_dict[app.newKey]
                app.isContinueKeyPressed = True
                app.makeOldFlashCard = False
                app.makeFlashCard = True
                app.cardsLearned += 1
                if app.cardsToLearn >= 0:
                    app.cardsToLearn -= 1
        elif app.cardsLearned == app.learnNum and app.cardsToLearn == 0:
            #Don't go out of bounds!
            app.isFavorite = False
            if len(app.prevSet) <= app.learnNum:
                app.newKey = getNextKeyFromPrevious(app)
                app.isContinueKeyPressed = True
                app.isBackKeyPressed = False
                app.makeOldFlashCard = False
                app.makeFlashCard = True
                app.prevCard = app.newKey
    elif event.key == 'Left':#Move to previous card
        if app.cardsLearned == app.learnNum:
            if app.prevFlashCard != dict() and len(app.prevSet) != app.learnNum:        
                app.prevCard = getPreviousKey(app)
                if app.prevCard != None and app.newKey != app.prevCard:
                    app.isBackKeyPressed = True
                    app.makeOldFlashCard = True
    elif event.key == 'l':
        for seen in app.prevFlashCard:
            if (seen not in app.ima and seen not in app.mama and 
                seen not in app.jyozu):
                app.ima.add(seen)
        app.phase = 'practice'
        app.makeFlashCard = False
    elif event.key == 'f':
        if (app.newKey != None and app.newKey not in app.toBeReviewed
            and app.cardsToLearn != 0): 
            app.isFavorite = True
            app.toBeReviewed[app.newKey] = overall_dict[app.newKey]
        if(app.prevCard != None and app.prevCard not in app.toBeReviewed
            and app.cardsLearned == app.learnNum):
            app.isFavorite = True
            app.toBeReviewed[app.prevCard] = overall_dict[app.prevCard]

def learningMode_mousePressed(app,event):
    if (app.cardsToLearn == 0 and app.width//4 <= event.x and 
        event.x >= app.width//6 and app.height//10 <= event.y and 
        event.y >= app.height//5):
        app.showMessage('Are you ready to practice?\n Press l to Continue!')
'''
Drawings
'''
#Draws a new Card
def drawNewCard(app,canvas):
    currFlashCard = FlashCard(app.newKey, overall_dict[app.newKey])
    currFlashCard.drawFlashCard(canvas,app)

#Draws a previously Shown card
def drawPrevCard(app,canvas):
    previousFlashCard = FlashCard(app.prevCard, overall_dict[app.prevCard])               
    previousFlashCard.drawFlashCard(canvas,app)

def drawBackButton(app,canvas):
    canvas.create_rectangle(app.cx//2,
                            app.cy*1.45,
                            app.cx//1.1,
                            app.cy*1.6, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx//1.5,app.cy*1.5,
                        font = 'Arial',  text = "Back", fill = 'black')
def drawNextButton(app,canvas):
    canvas.create_rectangle(app.cx*1.7,
                            app.cy*1.45,
                            app.cx*1.3,
                            app.cy*1.6, 
                            fill = 'violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.5,
                        font = 'Arial',  text = "Next", fill = 'black')
#Initiate Practice Mode
def drawLetsTryitButton(app,canvas):
    if app.lightMode == True:
        canvas.create_rectangle(app.cx*1.7,
                                app.cy*1.45,
                                app.cx*1.3,
                                app.cy*1.6, 
                                fill = 'cadet blue')
    elif app.darkMode == True:
        canvas.create_rectangle(app.cx*1.7,
                                app.cy*1.45,
                                app.cx*1.3,
                                app.cy*1.6, 
                                fill = 'SlateGray4')
    canvas.create_text(app.cx*1.5,app.cy*1.5,
                        font = 'Arial',  text = "Let's Try it!", fill = 'black')

def learningModeRedrawAll(app,canvas):

    if app.cardsLearned == 0:
            canvas.create_text(app.cx,app.cy, font =('Helvetica','20','bold'), 
            text = "Press the Right Arrow Key to Begin!", fill = "ghost white")
    elif app.cardsLearned >= 1:
        canvas.create_text(app.cx, app.cy//3, font =('Arial','15','bold'), 
                    text = "Use Up/Down Arrow Keys to Flip Card!",
                    fill = "ghost white")
        canvas.create_text(app.cx, app.cy//2.4, font =('Arial','15','bold'), 
                text = "Press the Right Arrow Key to Move Forward!",
                fill = "ghost white")  
        canvas.create_text(app.cx, app.cy//2, font =('Arial','15','bold'), 
                text = "Press f to favorite a card!", fill = "ghost white") 

    if app.toBeReviewed != dict():
        if(app.isFavorite == True and app.cardsToLearn > 0 and
            app.newKey != None and app.newKey in app.toBeReviewed):
            canvas.create_text(app.cx,app.cy*1.4, font =('Arial','15','bold'),
                            text = f"{app.newKey} has been favorited",
                            fill = "ghost white")     
        elif(app.isFavorite == True and app.cardsToLearn == 0): 
            canvas.create_text(app.cx,app.cy*1.4, font =('Arial','15','bold'),
                            text = f"{app.prevCard} has been favorited",
                            fill = "ghost white")       
    if toBeLearned == dict():
        canvas.create_text(app.cx,app.cy, font = ('Arial','20','bold'),
        text = "Congrats! You have learned Everything! Press l to Practice!", 
        fill = "ghost white")                                     

    else: #Learning Cards
        if app.cardsToLearn < app.learnNum:
            drawNextButton(app,canvas)
            if (app.isContinueKeyPressed == True and app.newKey != None and 
                toBeLearned != dict()):
                drawNewCard(app,canvas)             
            if (app.isBackKeyPressed == True and app.prevCard != None):
                drawPrevCard(app,canvas)
            if (app.cardsToLearn == 0 and app.prevFlashCard != dict()):
                canvas.create_text(app.cx, app.cy//1.7, font =('Arial','15','bold'), 
                        text = "Press the Left Arrow Key to Move Back!",
                        fill = "ghost white")
                drawBackButton(app,canvas)
            if (app.cardsToLearn == 0 and app.cardsLearned == app.learnNum and
                app.newKey != None):
                drawLetsTryitButton(app,canvas)
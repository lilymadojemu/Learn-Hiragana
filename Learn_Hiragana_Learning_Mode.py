from Classes import*
from Populate_Values import*
import random, time
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
def learning_appStarted(app):
    pass

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
        # if (reversedList[prevKey] != app.prevCard and 
        #     reversedList[prevKey] not in app.prevSet):
        #     print(app.prevSet)
        #     app.prevSet.add(reversedList[prevKey])
        #     if reversedList[prevKey] in app.seenDrawn:
        #             app.seenDrawn.remove(reversedList[prevKey])
        #     print(f'The card coming from {app.prevCard}')
        #     print(f'The Next Card I should see {reversedList[prevKey]}')
        #     return reversedList[prevKey]
        
            

        #For when in prevSet and I need it
        # elif (reversedList[prevKey] != app.prevCard and 
        #     app.prevCard in app.prevSet and
        #     reversedList[prevKey] in app.prevSet):
        #     print(app.prevSet)
        #     app.prevSet.remove(app.prevCard)
        #     app.prevSet.remove(reversedList[prevKey])
        #     return reversedList[prevKey]

def getNextKeyFromPrevious(app):
    currListKeys = list(app.currSession.keys())
    futurePreviousSession = currListKeys[::-1]
    print(f'Cards That have been seen curr:{currListKeys}')
    print(f'Cards That have been seen curr reversed:{futurePreviousSession}')
    for redrawCard in range(len(currListKeys)):
        if app.prevCard != None and currListKeys[redrawCard] != None:
            currPreviousIndex = currListKeys.index(app.prevCard)
            # if (currListKeys[redrawCard] == currListKeys[currPreviousIndex + 1] 
            #     and currListKeys[redrawCard] != app.prevCard):
            #     if currListKeys[redrawCard] in app.prevSet:
            #         app.prevSet.remove(currListKeys[redrawCard])
            #     #removing and appending directly from list
            #     print(f'Next {app.prevSet}')
            #     app.seenDrawn.add(currListKeys[redrawCard])
            if currListKeys[currPreviousIndex + 1] != None:
                if currListKeys[currPreviousIndex + 1] in app.prevSet:
                    app.prevSet.remove(currListKeys[currPreviousIndex + 1])
                return currListKeys[currPreviousIndex + 1]

#During intermediate times slightly off information is saved

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
    #flips front of flash card to back
    #flips back to front    
    if event.key == 'Up' or event.key == 'Down':
        app.isFlipped = not app.isFlipped
    elif event.key == 'Right':#Move to new card
        if app.cardsLearned < 5:
            app.newKey = getRandomKey()
            getHiraganaOrVocab(app,app.newKey)
            print(f'New Key {app.newKey}')
            app.currSession[app.newKey] = overall_dict[app.newKey]
            app.isContinueKeyPressed = True
            app.makeOldFlashCard = False
            app.makeFlashCard = True
            app.cardsLearned += 1
            app.cardsToLearn -= 1
        else:
            #Don't go out of bounds!
            if len(app.prevSet) <= 5:
                app.newKey = getNextKeyFromPrevious(app)
                print(f'I made it to redraw {app.newKey}')
                print(f'The previous {app.prevCard}')
                app.isContinueKeyPressed = True
                app.isBackKeyPressed = False
                app.makeOldFlashCard = False
                app.makeFlashCard = True
                app.prevCard = app.newKey
    elif event.key == 'Left':#Move to previous card
        if app.cardsLearned == 5:
            print(f'Current Session Normal {list(app.currSession.keys())}')
            currSession = list(app.currSession.keys())
            print(f'Current Session reversed {currSession[::-1]}')
            #Skip first thing when revesed
            print(f'current previous card {app.prevCard}')
            if app.prevFlashCard != dict() and len(app.prevSet) != 5:        
                #current and new current should not be the same 
                app.prevCard = getPreviousKey(app)
                print(f'New current previous card {app.prevCard}')
                if app.prevCard != None and app.newKey != app.prevCard:
                    print(f'Pressed Left for {app.prevCard}')
                    print(app.prevFlashCard)
                    app.isBackKeyPressed = True
                    app.makeOldFlashCard = True
    elif event.key == 'l':
        for seen in app.prevFlashCard:
            app.ima.add(seen)
        print(f"current seen for box 1 {app.ima}")
        app.phase = 'practice'
        app.makeFlashCard = False
    elif event.key == 'f':
        if app.newKey != None and app.newKey not in app.toBeReviewed: 
            app.toBeReviewed[app.newKey] = overall_dict[app.newKey]
            print(app.toBeReviewed)
        
def learningMode_mousePressed(app,event):
    if app.cx//1.1 <= event.x >= app.cx//2.2:
        if app.cx*1.45 <= event.y >= app.cy*1.6:
            if app.prevFlashCard != dict():
                app.prevCard = getPreviousKey(app)
                print(app.prevCard)
                print(app.prevFlashCard)
                app.isBackKeyPressed = True
                app.makeOldFlashCard = True
    #Fix parameters
    if app.cardsToLearn > 0 and app.cx*1.3 <= event.x >= 1.7:
        if app.cx*1.45 <= event.y >= app.cy*1.6:
            app.makeNewCard = True
            app.cardsLearned += 1
            if app.cardsToLearn != 0:
                app.cardsToLearn -= 1
    elif (app.cardsToLearn == 0 and app.width//4 <= event.x and 
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
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.5,
                        font = 'Arial',  text = "Next", fill = 'black')
#Initiate Practice Mode
def drawLetsTryitButton(app,canvas):
    canvas.create_rectangle(app.cx*1.7,
                            app.cy*1.45,
                            app.cx*1.3,
                            app.cy*1.6, 
                            fill = 'cadet blue')
    canvas.create_text(app.cx*1.5,app.cy*1.5,
                        font = 'Arial',  text = "Let's Try it!", fill = 'black')

def learningModeRedrawAll(app,canvas):
    if app.cardsLearned == 0:
            canvas.create_text(app.cx,app.cy, font = 'Arial 20', 
            text = "Press the Right Arrow Key to Begin!")
    elif app.cardsLearned >= 1:
        canvas.create_text(app.cx, app.cy//3, font = 'Arial 15', 
                    text = "Use Up/Down Arrow Keys to Flip Card!")
        canvas.create_text(app.cx, app.cy//2.4, font = 'Arial 15', 
                text = "Click Next/Press the Right Arrow Key to Move Forward!")  
        canvas.create_text(app.cx, app.cy//2, font = 'Arial 15', 
                text = "Press f to favorite a card!", fill = 'black')                       
    if toBeLearned == dict():
        canvas.create_text(app.cx,app.cy, font = 'Arial 20',
        text = "Congrats! You have learned Everything! Press l to Practice!", 
        fill = 'black')
    else: #Learning Cards
        drawNextButton(app,canvas)
        if app.isContinueKeyPressed == True and toBeLearned != dict():
            drawNewCard(app,canvas)             
        if (app.isBackKeyPressed == True and toBeLearned != dict() and 
            app.prevCard != None):
            drawPrevCard(app,canvas)
        if app.cardsLearned == 5 and app.prevFlashCard != dict():
            canvas.create_text(app.cx, app.cy//1.7, font = 'Arial 15', 
                    text = "Click Back/Press the Left Arrow Key to Move Back!")
            drawBackButton(app,canvas)
        if app.cardsToLearn == 0:
            drawLetsTryitButton(app,canvas)
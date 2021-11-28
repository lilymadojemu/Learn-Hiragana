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
    prevKeyList = list(app.prevFlashCard.keys())
    for prevKey in reversed(prevKeyList):
        if prevKey != app.prevCard and prevKey != app.newKey:
            if prevKey not in app.seenPreviousCardKeys:
                app.seenPreviousCardKeys.append(prevKey)
                return prevKey

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
    if event.key == 'q':
        app.showMessage("All your progress will be lost!")
        app.phase = 'start'
    #flips front of flash card to back
    #flips back to front    
    elif event.key == 'Up' or event.key == 'Down':
        app.isFlipped = not app.isFlipped
    #Move to new card, populate next card
    elif event.key == 'Right':
        if (app.cardsToLearn <= 5 and app.cardsToLearn != 0 and 
            app.cardsToLearn > 0):
             if app.cardsToLearn <= 5:
                if app.firstKey not in app.currSession:
                    app.currSession[app.firstKey] = overall_dict[app.firstKey]
                app.newKey = getRandomKey()
                print(f'a {app.newKey}')
                app.currSession[app.newKey] = overall_dict[app.newKey]
                app.isContinueKeyPressed = True
                app.makeOldFlashCard = False
                app.makeFlashCard = True
                app.cardsLearned += 1
                app.cardsToLearn -= 1
        #Based on seencards
        else:
            print(f'curr:{app.currSession}')
            print(f'prev {app.prevFlashCard}')
            if len(app.currSession.keys()) == len(app.prevFlashCard.keys()):
                for key in range(len(app.seenPreviousCardKeys)):
                    goingThrough = app.seenPreviousCardKeys[::-1]
                    if app.prevCard == None:
                        previousIndex = 0
                    else:
                        previousIndex = goingThrough.index(app.prevCard)
                        nextKey = goingThrough[previousIndex + 1]
                        print(app.prevCard)
                        print(nextKey)
                        if nextKey != app.prevCard:
                            app.newKey = nextKey
                            print(app.newKey)
                            app.isContinueKeyPressed = True
                            app.isBackKeyPressed = False
                            app.makeOldFlashCard = False
                            app.makeFlashCard = True
                                # app.notSeenPreviousCardKeys.append(nextKey)
                                # app.seenPreviousCardKeys.remove(nextKey)
    #Move to previous card
    elif event.key == 'Left':
        if app.prevFlashCard != dict():
            app.prevCard = getPreviousKey(app)
            print(app.prevCard)
            print(app.prevFlashCard)
            app.isBackKeyPressed = True
            app.makeOldFlashCard = True
    elif event.key == 'l':
        for seen in app.prevFlashCard:
            app.ima.add(seen)
        app.phase = 'practice'
        app.makeFlashCard = False

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
Flipping
'''     
#What is a flip, like a blink/flash, will need another background for back
#Understanding from https://www.youtube.com/watch?v=kvd6i1mXec8
#Idea from https://coderedirect.com/questions/124487/simple-animation-using-tkinter
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
        pass
        # decreasingFrontCard(app)
        # increasingBackCard(app)
    if app.isContinueKeyPressed == False and app.cardsLearned == 0:
        getHiraganaOrVocab(app,app.firstKey)
    if app.isContinueKeyPressed == True:
        if app.newKey not in app.prevFlashCard:
            app.prevFlashCard[app.newKey] = overall_dict[app.newKey]
        getHiraganaOrVocab(app,app.newKey)
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
    canvas.create_text(app.cx, app.cy//2, font = 'Arial 15', 
                text = "Use Up/Down Arrow Keys to Flip Card!")
    canvas.create_text(app.cx, app.cy//1.7, font = 'Arial 15', 
                text = "Click Next/Press the Right Arrow Key to Move Forward!")             
    if toBeLearned == dict():
        canvas.create_text(app.cx,app.cy, font = 'Arial 20',
        text = "Congrats! You have learned Everything! Press l to Practice!", 
        fill = 'black')
    else: #Learning Cards
        drawNextButton(app,canvas)
        if  app.isContinueKeyPressed == False and app.cardsToLearn == 4:
            app.flashCard.drawFlashCard(canvas,app)
        if app.isContinueKeyPressed == True and toBeLearned != dict():
            drawNewCard(app,canvas)             
        if (app.isBackKeyPressed == True and toBeLearned != dict() and 
            app.prevCard != None):
            drawPrevCard(app,canvas)
        if app.cardsLearned >= 1 and app.prevFlashCard != dict():
            canvas.create_text(app.cx, app.cy//1.5, font = 'Arial 15', 
                text = "Click Back/Press the Left Arrow Key to Move Forward!")
            drawBackButton(app,canvas)
        if app.cardsToLearn == 0:
            drawLetsTryitButton(app,canvas)
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

# '''
#                 #     #Finished with everything
#                 #     if modifiedCharacter_dict == {}:
#                 #         app.showMessage("Empty!")
#                 #         #Once this happens, user will only look at incorrect 
#                 #         #correct characters/words from what they went 
#                 #         # through
#  '''                   
#         #For Vocab Cards, 2 is vocabulary
#         modifiedVocabList = copy.deepcopy(vocabList)
#         modifiedVocab_dict = copy.deepcopy(vocabulary_dict)
#         if app.hiraganaOrVocab == 2:
#             #Keeps track of flashcards I have already been through, 
#             #will play big role in keeping track of users' progress
#             # through flashcards
#             #Currently getting everything instead of one at a time
#             for word in modifiedVocabList:
#                 #while key in modifiedHiraganaList:
#                     self.frontText = word
#                     self.backText = modifiedVocab_dict[word]
#                     #Front of card
#                     if app.isFlipped == False:
#                         #Exact Placement to be changed
#                         #The Vocabulary Word
#                         canvas.create_text(app.cx,app.cy//2,
#                                         font = 'Arial',
#                                         text = f"{self.frontText}", 
#                                         fill = 'thistle')
#                     #Back of card
#                     elif app.isFlipped == True:
#                         #The Pronunciation of Vocabulary
#                         canvas.create_text(app.cx, app.cy//2,font = 'Arial',
#                                         text = f"{self.backText}", 
#                                         fill = 'medium aquamarine')
#                 # #Has user gone to the next card
#                 # elif(app.isContinueKeyPressed == True and
#                 #      app.cardsToLearn >= 0):
#                 #     app.seenVocabularyFlashCards[self.frontText] = (
#                 #                 self.backText)
#                 #     del modifiedVocab_dict[self.frontText]
#                 #     #Finished with everything
#                 #     if modifiedVocab_dict == {}:
#                 #         app.showMessage("Empty!")
#                 #         #Once this happens, user will only look at incorrect 
#                 #         #correct characters/words from what they went 
#                 #         # through
                        
# '''
bigDictionary = copy.copy(overall_dict)
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
        hiraganaValue = toBeLearned[hiraganaOrVocab]
        prevFlashCard[hiraganaOrVocab] = hiraganaValue 
        seenHiraganaFlashCards[hiraganaOrVocab] = hiraganaValue 
        seenFlashCards[hiraganaOrVocab] = hiraganaValue 
        modifyListOfKeys.remove(hiraganaOrVocab)
        del toBeLearned[hiraganaOrVocab]      
    elif hiraganaOrVocab in vocabList:
        vocabValue = toBeLearned[hiraganaOrVocab]
        prevFlashCard[hiraganaOrVocab] = vocabValue
        seenVocabFlashCards[hiraganaOrVocab] = vocabValue
        seenFlashCards[hiraganaOrVocab] = vocabValue
        modifyListOfKeys.remove(hiraganaOrVocab)
        del toBeLearned[hiraganaOrVocab] 


def drawNewCard(app,canvas):
    #FlashCard info.
    currFlashCard = FlashCard(app.newKey, toBeLearned[app.newKey])
    currFlashCard.drawFlashCard(canvas,app)
    if app.isFlipped == True:
        currFlashCard.blinkSmallerLearning(app)

def makePrevCard(app,canvas):
    #FlashCard info.
    if app.isBackKeyPressed == True:
        for oldKey in prevFlashCard:
            currFlashCard = FlashCard(oldKey, prevFlashCard[oldKey])                   
            currFlashCard.drawFlashCard(canvas, app)
            if app.isFlipped == True:
                currFlashCard.blinkSmallerLearning(app)

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
        app.makeNewCard = True
        app.cardsLearned += 1
        if app.cardsToLearn != 0:
            app.cardsToLearn -= 1
        #app.makeFlashCard = True
        #app.hiraganaOrVocab = random.randint(1,2)
    #Move to previous card
    elif event.key == 'Left':
        app.isBackKeyPressed = True
        app.makeOldFlashCard = True
    elif event.key == 'r':
        app.phase = 'review'
    elif event.key == 'l':
        app.phase = 'practice'


def learning_keyReleased(app, event): 
    if event.key == 'Right':
        app.isContinueKeyPressed = False
        app.makeFlashCard = False
    elif event.key == 'Left':
        app.makeOldFlashCard = False

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
        


#Allows users to go back to the previous flashcard
def drawBackButton(app,canvas):
    canvas.create_rectangle(app.cx//2,
                            app.cy*1.2,
                            app.cx//-2,
                            app.cy*1.1, 
                            fill = 'pale violet red')

    canvas.create_text(app.cx/6,app.cy*1.15,
                        font = 'Arial',  text = "Back", fill = 'black')
def drawNextButton(app,canvas):
    canvas.create_rectangle(app.cx*3,
                            app.cy*1.2,
                            app.cx,
                            app.cy*1.1, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.15,
                        font = 'Arial',  text = "Next", fill = 'black')
#Initiate Practice Mode
def drawLetsTryitButton(app,canvas):
    canvas.create_rectangle(app.cx*3,
                            app.cy*1.2,
                            app.cx,
                            app.cy*1.1, 
                            fill = 'cadet blue')
    canvas.create_text(app.cx*1.5,app.cy*1.15,
                        font = 'Arial',  text = "Let's Try it!", fill = 'black')

#create a new key before redraw all and use that new key in drawNewCard
def timerFired(app):
    #"flipping flashCard"
    # if app.isFlipped == True:
    #     #reducing
    #     app.cx -=1
    #     app.cy -=1
    #     if( app.cx == app.width//2 and app.cy == app.height//2):
    #         app.cx += 1
    #         app.cy += 1
    #         app.isFlipped = False
    if (app.makeNewCard == True and toBeLearned != dict()):
        app.newKey = getRandomKey()
        getHiraganaOrVocab(app.newKey)
        

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
    elif (app.makeNewCard == True and toBeLearned != dict()):
        drawNewCard(app,canvas)             
    elif app.isBackKeyPressed == True:
        makePrevCard(app,canvas)
    if app.cardsLearned >= 1:
        drawBackButton(app,canvas)
    if (app.cardsToLearn == 0):
        drawLetsTryitButton(app,canvas)

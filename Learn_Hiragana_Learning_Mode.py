from Classes import*
'''
Overall Purpose: It is up to the user to read what is on the front and back of 
the flashcards
'''
'''
flipping cards
be at a base position, want that base position to change when flipped
Get base position and center and ending base position & center

'''

def letsLearn(app,canvas):
    #FlashCard info.
    while app.phase == 'learning':
        seenFlashCards = dict()
        prevFlashCard = None
        #Determines if flashcard will be a vocab or character card
        luckyChance = random.randint(1,2)
        if luckyChance == 1:
            for cKey in characterDictionary:
                currFlashCard = FlashCard(cKey, characterDictionary[cKey])
                currFlashCard.drawFlashCard()
                if app.isFlipped == True:
                    currFlashCard.flip()
                if app.isContinueKeyPressed == True:
                    currFlashCard = prevFlashCard
                    prevFlashCard.append(seenFlashCards)
                elif app.isBackKeyPressed == True:
                    prevFlashCard.drawFlashCard()
            luckyChance = random.randint(1,2)
        elif luckyChance == 2:
            for vKey in vocabularyDictionary:
                currFlashCard = FlashCard(vKey, vocabularyDictionary[vKey])
                currFlashCard.drawFlashCard()
                if app.isFlipped == True:
                    currFlashCard.flip()
                if app.isContinueKeyPressed == True:
                    currFlashCard = prevFlashCard
                    #Add prevFlashCard key-value to seen flashcard
                    seenFlashCards[prevFlashCard.frontText] =(
                                                 prevFlashCard.backText )
                elif app.isBackKeyPressed == True:
                    prevFlashCard.drawFlashCard()
                luckyChance = random.randint(1,2)
                    
def learningMode_keyPressed(app,event):
    #flips front of flash card to back
    #flips back to front 
    if event.key == 'Up' or event.key == 'Down':
        app.isFlipped = not app.isFlipped
    #Move to new card
    if event.key == 'Right':
        app.cardsToLearn -= 1
        app.isContinueKeyPressed = True
    #Move to previous card
    elif event.key == 'Left':
        app.isBackKeyPressed = True


def learningMode_mousePressed(app,event):
    #Determines whether a card needs to be flip
    if (app.width//2 <= event.x and event.x >= app.width//4 and app.height//4 
        <= event.y and  event.y >= app.height):
            app.isFlipped = not app.isFlipped
    #Click the Lets Try it Button to go onto Practice Mode
    #Need to fix
    if (app.cardsToLearn == 0 and app.width//4 <= event.x and 
        event.x >= app.width//6 and app.height//10 <= event.y and 
        event.y >= app.height//5):
        app.showMessage('Are you ready to practice?')
        app.phase ='practice'

# def drawFlashcard(app,canvas):
#     canvas.create_rectangle(app.cx*1.5,
#                             app.cy//4,
#                             app.cx//4,
#                             app.cy, 
#                             fill = 'bisque')
#     canvas.create_text(app.cx//1.5,app.cy//3,font = 'Arial', 
#     text = f"Kana Level:{app.characterLevel},Vocab Level:{app.vocabLevel}", 
#                         fill = 'medium aquamarine')

#Initiate Practice Mode
#Appears after all learning cards have been done (won't appear before then)
def drawLetsTryitButton(app,canvas):
    canvas.create_rectangle(app.cx*2,
                            app.cy*1.5,
                            app.cx,
                            app.cy*1.3, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.4,
                        font = 'Arial',  text = "Let's Try it!", fill = 'black')

def learningModeRedrawAll(app,canvas):
    letsLearn(app,canvas)
    #drawFlashcard(app,canvas)
    if (app.cardsToLearn == 0):
        drawLetsTryitButton(app,canvas)
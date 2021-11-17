'''Need to call on classes in learning mode functions'''
from Classes import*

'''
Overall Purpose: It is up to the user to read what is on the front and back of 
the flashcards

Important Note: User should be able to flip between the front & back of the card
an unlimited number of times

'''
'''
flipping cards
be at a base position, want that base position to change when flipped
Get base position and center and ending base position & center

'''
def learningMode_keyPressed(app,event):
    #Flipping cards
    #flips front of flash card to back
    if event.key == 'Up':
        pass

    if event.key == 'Down':
        #flip card animation
        pass
    #flip card animation
    #Move to next card
    if event.key == 'Right':
        pass
    #Move to previous card
    elif event.key == 'Left':
        pass
    
def learningMode_mousePressed(app,event):
    #Be able to click within the flashcard to flip
    #Flashcard will always be in the same spot
    #Firgure out parameters for flashcard
    #if event.x ya know
        #flip card animation
    if (app.width//2 <= event.x and event.x >= app.width//4 and app.height//4 
        <= event.y and  event.y >= app.height:
        isFlipped = not isFlipped

    #Click the Lets Try it Button to go onto Practice Mode
    #Need to fix
    for lastCard in range(app.cardsToLearn):
        if (lastCard == 0 and app.width//4 <= event.x and 
            event.x >= app.width//6 and app.height//10 <= event.y and 
            event.y >= app.height//5):
            #app.showMessage('Are you ready to practice?')
            #app.phase ='practice'
            pass


def drawFlashcard(app,canvas):
    canvas.create_rectangle(app.cx*1.5,
                            app.cy//4,
                            app.cx//4,
                            app.cy, 
                            fill = 'bisque')
    canvas.create_text(app.cx//1.5,app.cy//3,font = 'Arial', 
    text = f"Kana Level:{app.characterLevel},Vocab Level:{app.vocabLevel}", 
                        fill = 'medium aquamarine')

def drawContent(app,canvas):
    pass

def flashcard_redrawAll(app, canvas):
    #call method
   drawFlashcard(app,canvas)

#Initiate Practice Mode
#Appears after all learning cards have been done (won't appear before then)
#Will be located at bottom right of the back of the last flashcard
def drawLetsTryitButton(app,canvas):
    canvas.create_rectangle(app.cx*2,
                            app.cy*1.5,
                            app.cx,
                            app.cy*1.3, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.4,
                        font = 'Arial',  text = "Let's Try it!", fill = 'black')

#After "learning" a card, -1 from app.cardsToLearn
def learningModeRedrawAll(app,canvas):
    drawFlashcard(app,canvas)
    for lastCard in range(app.cardsToLearn):
        if lastCard == 0:
            drawLetsTryitButton(app,canvas)
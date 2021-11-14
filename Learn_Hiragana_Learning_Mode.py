'''Need to call on classes in learning mode functions'''
from Classes import*

'''
Overall Purpose: It is up to the user to read what is on the front and back of 
the flashcards

Important Note: User should be able to flip between the front & back of the card
an unlimited number of times

'''

def learningMode_keyPressed(app,event):
    #Flipping cards
    #flips front of flash card to back
    if event.key == 'Right':
        #flip card animation
        pass
    #back of flashcard to front
    elif event.key == 'Left':
        #flip card animation
        pass
    
def learningMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    #Be able to click within the flashcard to flip
    #Flashcard will always be in the same spot
    #Firgure out parameters for flashcard
    #if event.x ya know
        #flip card animation
    #Click the Lets Try it Button to go onto Practice Mode
    #Determine parameters of where button will be
    #if ya know...
        #app.phase ='practice'


def drawFlashcard(app,canvas):
    canvas.create_rectangle(app.width-100,app.height//4, app.width-20,
                                app.height//4+35, fill = 'white')
    #canvas.create_text(f'{app.characterLevel}, {app.vocabLevel}')  
def drawContent(app,canvas):
    pass

def flashcard_redrawAll(self, app, canvas):
    drawFlashcard(app,canvas)


#Initiate Practice Mode
#Appears after all learning cards have been done (won't appear before then)
#Will be located at bottom right of the back of the last flashcard
def drawLetsTryitButton(app,canvas):
    canvas.create_rectangle(app.cx//2,app.cy//2,
                            app.cx//2,app.cy//2, fill = 'teal')
    canvas.create_text(app.cx//2-100,app.cy//2+200,
                        font = 'Arial',  text = "Let's Try it!", fill = 'Red')

def learningModeRedrawAll(app,canvas):
    drawLetsTryitButton(app,canvas)
''' imports '''
from cmu_112_graphics import *
from Populate_Values import *
from Classes import *
from Start_Screen import *
from User_Profile_Select_Screen import *
from Learn_Hiragana_Learning_Mode import *
from Learn_Hiragana_Practice_Mode import *

'''

Can call classes (like in class notes within functions)
'''
def appStarted(app):
    app.phase = "start"
    app.cx = app.width//2
    app.cy = app.height//2
    #Level of vocab/ Character knowledge
    app.characterLevel = 0
    app.vocabLevel = 0
    #During Learning stage, refers to time limit user is given to select answer
    app.paused = False
    #Number of flashcards that will appear in learning stage
    app.cardsToLearn = 5
    #Number of flashcards that will appear in doing stage
    app.cardsToDo = 5
    app.userProfiles = dict()

def drawUserProfileButton(app,canvas):
    canvas.create_rectangle(app.cx,app.cy,app.cx//2,app.cy//2, fill = 'purple')
    canvas.create_text(app.cx//2,app.cy//2,
                        font = 'Arial',  text = "newUser", fill = 'Red')
    #if clicked
def userProfileRedrawAll(app,canvas):
    drawUserProfileButton(app,canvas)
 ########################################################################       

#Begin Doing Stage
def drawLetsDoButton(app,canvas):
    canvas.create_rectangle(app.cx,app.cy,app.cx//2,app.cy//2, fill = 'purple')
    canvas.create_text(app.cx//2,app.cy//2,
                        font = 'Arial',  text = "Let's Try it!", fill = 'Red')




def keyPressed(app,event):
    #Pausing, unpausing in Practice Mode Only
    if (event.key == 'p'):
        app.paused = not app.paused
    #Flipping cards
    #front  of flash card to back
    if event.key == 'Right':
        #flip card animation
        pass
    #back of flashcard to front
    elif event.key == 'Left':
        #flip card animation
        pass
    

def mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    '''flip card Animation, be able to flip unlimited number 
        of times to go to the front or the back'''

    pass

#Learning Stage Specific 




#Doing Stage Specific

###############################################
#My flashcards
def drawLearningFlashcard(app,canvas):
    #front
    canvas.create_rectangle(app.width-100,app.height//4, app.width-20,
                                    app.height//4+35, fill = 'white')
    #canvas.create_text(  f'{app.characterLevel}, {app.vocabLevel}')    \
    # Back 

#manually underline text? loop over given word, if target letter in word, underline               
def drawDoingHiraganaFlashcard(app,canvas):
    #front, hiragana
    canvas.create_rectangle(app.width-100,app.height//4, app.width-20,
                                    app.height//4+35, fill = 'white')
    #canvas.create_text(  f'{app.characterLevel}, {app.vocabLevel}')    
    #Back, romanji
    #function from another file
    # if isCorrect == False:
    #     #don't show back of card
    #     pass

def drawDoingVocabFlashcard(app,canvas):
    #front
    canvas.create_rectangle(app.width-100,app.height//4, app.width-20,
                                    app.height//4+35, fill = 'white')
    #canvas.create_text(  f'{app.characterLevel}, {app.vocabLevel}')    
    #Back
def drawCharacter(app,canvas):
    pass




######################################################################
#Automatically move on to next flashcard card, Doing stage
def timerFired(app):
    pass
    
def redrawAll(app,canvas):
    introScreenRedrawall(app,canvas)
    #Set up user profile
    userProfileRedrawAll(app,canvas)



runApp(width = 600, height = 700)
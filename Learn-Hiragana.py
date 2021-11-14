''' imports '''
from cmu_112_graphics import *
from Populate_Values import *
from Classes import *
from Start_Screen import *
from User_Profile_Select_Screen import *
from Learn_Hiragana_Learning_Mode import *
from Learn_Hiragana_Practice_Mode import *
from Transition_Screen import *

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

def userSelect_mousePressed(app,event):
    #Parameters for learning button to be pressed
    #if event.y ya know...
    #app.phase = 'learning'
    pass

#The redrawAll's of different Screens
def redrawAll(app,canvas):
    startScreenRedrawall(app,canvas)
    #Set up user profile
    # userProfileRedrawAll(app,canvas)
    # #Go to Learning Mode
    # learningModeRedrawAll(app,canvas)
    #Go to Practice Mode
    #practiceModeRedrawAll(app,canvas)
    #Transition
    #transitionScreenRedrawAll(app,canvas)

runApp(width = 600, height = 700)
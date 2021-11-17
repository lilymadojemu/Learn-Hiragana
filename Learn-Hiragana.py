''' imports '''
from cmu_112_graphics import *
from Populate_Values import *
from Classes import *
from Start_Screen import *
from User_Profile_Select_Screen import *
from Learn_Hiragana_Learning_Mode import *
from Learn_Hiragana_Practice_Mode import *
from Transition_Screen import *
import time


'''
Can call classes (like in class notes within functions)
'''
sensei = SenseiBot("Sensei")
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
    
#mousePressed of different phases
def mousePressed(app,event):
    if app.phase == 'start':
        intro_mousePressed(app,event)
    elif app.phase == 'learning':
        learningMode_mousePressed(app,event)
    elif app.phase == 'practice':
        practice_keyPressed(app,event)
    elif app.phase == 'profileselect':
        userSelect_mousePressed(app,event)
    elif app.phase == 'settings':
        ''' After MVP'''
        pass



#The redrawAll's of different phases
def redrawAll(app,canvas):
    if app.phase == 'start':
        startScreenRedrawall(app,canvas)
    elif app.phase == 'learning':
            # #Go to Learning Mode
        learningModeRedrawAll(app,canvas)
    elif app.phase == 'practice':
        #Go to Practice Mode
        practiceModeRedrawAll(app,canvas)
    elif app.phase == 'profileselect':
        #Set up user profile, if clicked! I want to trigger
        userProfileRedrawAll(app,canvas)
    elif app.phase == 'settings':
        pass
    #Transition
    #transitionScreenRedrawAll(app,canvas)

runApp(width = 800, height = 800)
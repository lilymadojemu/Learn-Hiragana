'''

Name: Lily Madojemu
andrewid: lmadojem

'''
''' imports '''
from cmu_112_graphics import *
from Populate_Values import *
from Classes import *
from Start_Screen import *
from User_Profile_Select_Screen import *
from Learn_Hiragana_Learning_Mode import *
from Learn_Hiragana_Practice_Mode import *
from Transition_Screen import *
import time, random
def appStarted(app):
    #Initial phase 
    app.phase = "start"
    app.cx = app.width//2
    app.cy = app.height//2
    #Level of vocab/ Character knowledge
    app.characterLevel = 0
    app.vocabLevel = 0
    #During Practice stage, refers to time limit user is given to select answer
    app.paused = False
    #Number of flashcards that will appear in learning stage
    app.cardsToLearn = 5
    #Number of flashcards that will appear in practice phase
    app.cardsToDo = 5
    #time alloted to answer each question during practice phase
    app.baseProblemTime = 700
    #Checks/Determines if a card has been flipped or not
    app.isFlipped = False
    #Checks if a "continue key" right) has been pressed to
    # move on to next Flashcard
    app.isContinueKeyPressed = False
    #Checks if "back key" (left) has been pressed to go to a previous card
    app.isBackKeyPressed = False
    app.userProfiles = dict()
    #Determines if a new flash card will be shown/made
    app.makeFlashCard = False
    #defaul flash card
    app.startingFlashcard= FlashCard("Hi", "Bye")
    #Decides whether a flashcard appearing will be a 
    # hiragana card or a vocab card
    app.hiraganaOrVocab = random.randint(1,2)
    sensei = SenseiBot("Sensei",app.baseProblemTime)
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

#Houses the key presses of all phases
def keyPressed(app,event):
    if app.phase == 'learning':
        learningMode_keyPressed(app,event)
    elif app.phase == 'practice':
        practiceMode_keyPressed(app,event)

#The redrawAll's of different phases
def redrawAll(app,canvas):
    if app.phase == 'start':
        startScreenRedrawall(app,canvas)
    elif app.phase == 'learning':
            #Go to Learning Mode
        learningModeRedrawAll(app,canvas)
    elif app.phase == 'practice':
        #Go to Practice Mode
        practiceModeRedrawAll(app,canvas)
    elif app.phase == 'profileselect':
        #Set up user profile
        userProfileRedrawAll(app,canvas)
    elif app.phase == 'settings':
        pass
    #Transition
    #transitionScreenRedrawAll(app,canvas)

runApp(width = 800, height = 800)
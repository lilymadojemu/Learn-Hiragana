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
from Settings_Screen import*
import time, random

def appStarted(app):
    listOfKeys = list(overall_dict.keys())
    possibleKey = random.choice(listOfKeys)
    listofHiragana = list(character_dict.keys())
    charaKey = random.choice(listofHiragana)
    #Initial phase 
    app.phase = "start"
    app.cx = app.width//2
    app.cy = app.height//2
    app.frontcx = app.width//2
    app.frontcy = app.height//2
    app.backcx = app.width//2
    app.backcy = app.height//2
    app.textcx = app.width//2
    app.textcy = app.height//2
    #Important/Good to have
    #Overall dictionary with hiragana and vocab 
    app.bigDictionary = overall_dict
    #Stagnant list of all hiragana characters
    app.hiraganaList = hiraganaList
    #Overall vocabulary Dictionary
    app.vocabularyDictionary = vocabulary_dict    
    #Overall character dictionary
    app.characterDictionary = character_dict
    #Takes in all of the flashcards a user has seen Overall
    app.seenFlashCards = dict()
    #Overall hiragana flashcards user has seen
    app.seenHiraganaFlashCards = dict()
    # #Overall vocabulary flashcards user has seen
    app.seenVocabFlashCards = dict()
    app.prevFlashCard= dict()
    #Learning Phase    
    #Checks if a "continue key" right) has been pressed to
    # move on to next Flashcard
    app.isContinueKeyPressed = False
    #Checks if "back key" (left) has been pressed to go to a previous card
    app.isBackKeyPressed = False
    app.image1 = app.loadImage('flashcard.jpg')
    app.image2 = app.loadImage('flashcardBack.jpg')
    app.makeOldFlashCard = False 
    app.makeFlashCard = False
    app.firstKey = getRandomKey()   
    app.flashCard = FlashCard(app.firstKey,overall_dict[app.firstKey])
    app.newKey = getRandomKey()  
    app.prevCard = app.firstKey
    app.alreadyOn = None
    #Checks/Determines if a card has been flipped or not
    app.isFlipped = False
    #Number of flashcards that will appear in learning stage
    app.cardsToLearn = 5
    app.cardsLearned = 0
    app.isGrowing = False
    app.isShrinking = False
    app.isFrontShown = True
    app.isBackShown = False
    #Practice Phase      
    #Leitner System
    #Japanese words for now, middle/fine, and good
    app.ima = app.prevFlashCard #Box 1
    app.mama = dict() #Box 2
    app.jyozu = dict() #Box 3
    #Level of vocab/ Character knowledge
    app.characterLevel = 0
    app.vocabLevel = 0  
    #Number of flashcards that will appear in practice phase
    app.cardsToDo = 10   
    app.cardsPracticed = 0
    app.practiceFlashCard = FlashCard(charaKey, character_dict[charaKey])
    app.practiceKey = getPreviousKey(app)
    app.practiceValue = None
    #time alloted to answer each question during practice phase
    app.baseProblemTime = 30
    app.timeTaken = 0    
    #During Practice stage, refers to time limit user is given to select answer
    app.currQuestionType = 0
    app.paused = False
    app.wantInput = False
    app.startQuestion = False
    app.finishedQuestion = False
    #answer Choices
    app.option1Chosen = False
    app.option2Chosen = False
    app.option3Chosen = False
    app.option4Chosen = False
    app.listOfPossibleChoices = list()
    app.userAnswer = None
    #Users
    app.userProfiles = dict()
    #Extras 
    app.streak = False
    app.startBackground = app.loadImage('background.jpg')
    app.lightMode = True
    app.lightPracticeBackground = app.loadImage('day.jpg')
    app.darkMode = False
    app.darkPracticeBackground = app.loadImage('night.jpg')
    app.transitionBackground = app.loadImage('confetti.jpg')
    app.darkTransitionBackground = app.loadImage('darkConfetti.jpg')
    app.lightSettingsBackground = app.loadImage('lightSettings.jpg')
    app.darkSettingsBackground = app.loadImage('darkSettings.gif')
    app.lightLearningBackground = app.loadImage('lightLearn.jpg')
    app.darkLearningBackground = app.loadImage('darkLearn.gif')
    #Testing
    app.messages = ['appStarted']


#mousePressed of different phases
def mousePressed(app,event):
    if app.phase == 'start':
        intro_mousePressed(app,event)
    elif app.phase == 'learning':
        learningMode_mousePressed(app,event)
    elif app.phase == 'practice':
        practice_mousePressed(app,event)
    elif app.phase == 'transition':
        transition_mousePressed(app,event)
    elif app.phase == 'profileselect':
        userSelect_mousePressed(app,event)
    elif app.phase == 'settings':
        ''' After MVP'''
        pass

#Houses the key presses of all phases
def keyPressed(app,event):
    if event.key == 'Enter':
        app.phase = 'learning'
    elif app.phase == 'practice':
        practiceMode_keyPressed(app,event)
    elif app.phase == 'learning':
        learningMode_keyPressed(app,event)

#The redrawAll's of different phases
def redrawAll(app,canvas):
    if app.phase == 'start':
        canvas.create_image(800, 800, 
                            image=ImageTk.PhotoImage(app.startBackground))
        startScreenRedrawall(app,canvas)
    elif app.phase == 'learning':
        if app.lightMode == True:
            canvas.create_image(800, 800, 
                            image=ImageTk.PhotoImage(app.lightLearningBackground))
            learningModeRedrawAll(app,canvas)
        elif app.darkMode == True:
            canvas.create_image(800, 800, 
                        image=ImageTk.PhotoImage(app.darkLearningBackground))
            learningModeRedrawAll(app,canvas)
    elif app.phase == 'practice':
        if app.lightMode == True:
            canvas.create_image(800, 800, 
                        image=ImageTk.PhotoImage(app.lightPracticeBackground))
            practiceModeRedrawAll(app,canvas)
        elif app.darkMode == True:
            canvas.create_image(800, 800, 
                        image=ImageTk.PhotoImage(app.darkPracticeBackground))
            practiceModeRedrawAll(app,canvas)
    elif app.phase == 'transition':
        if app.lightMode == True:
            canvas.create_image(800, 800, 
                        image=ImageTk.PhotoImage(app.transitionBackground))
            transitionScreenRedrawAll(app,canvas)
        elif app.darkMode == True:
            canvas.create_image(800, 800, 
                        image=ImageTk.PhotoImage(app.darkTransitionBackground))
            transitionScreenRedrawAll(app,canvas)
    elif app.phase == 'profileselect':
        userProfileRedrawAll(app,canvas)
    elif app.phase == 'settings':
        if app.lightMode == True:
            canvas.create_image(800, 800, 
                            image=ImageTk.PhotoImage(app.startBackground))
            settings_redrawAll(app,canvas)
        elif app.darkMode == True:
            canvas.create_image(800, 800, 
                            image=ImageTk.PhotoImage(app.startBackground))
            settings_redrawAll(app,canvas)


def mouseMoved(app, event):
    app.messages.append(f'mouseMoved at {(event.x, event.y)}')

def timerFired(app): 
    if app.phase == 'learning':
         learning_timerFired(app)
    elif app.phase == 'practice':
        practice_timerFired(app)

def letsLearnHiragana():
    runApp(width = 800, height = 800)

def main():
    letsLearnHiragana()

if __name__ == '__main__':
    main()
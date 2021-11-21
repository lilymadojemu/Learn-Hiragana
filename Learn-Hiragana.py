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

listOfKeys = list(overall_dict.keys())
possibleKey = random.choice(listOfKeys)
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
    app.cardsLearned = 0
    app.cardsPracticed = 0
    #time alloted to answer each question during practice phase
    app.baseProblemTime = 700
    #Checks/Determines if a card has been flipped or not
    app.isFlipped = False
    #Checks if a "continue key" right) has been pressed to
    # move on to next Flashcard
    app.isContinueKeyPressed = False
    #Checks if "back key" (left) has been pressed to go to a previous card
    app.isBackKeyPressed = False
    #Determines if a new flash card will be shown/made

    app.makeOldFlashCard = False

    #default flash card, key value
    app.flashCard = FlashCard(possibleKey,overall_dict[possibleKey])

    #Overall hiragana flashcards user has seen
    # app.seenHiraganaFlashCards = dict()
    # #Overall vocabulary flashcards user has seen
    # app.seenVocabFlashCards = dict()
    # #Takes in all of the flashcards a user has seen
    # app.seenFlashCards = dict()
    #Decides whether a flashcard appearing will be a 
    # hiragana card or a vocab card
    app.hiraganaOrVocab = random.randint(1,2)
    #Overall character dictionary
    # app.characterDictionary = character_dict
    # #Overall vocabulary Dictionary
    # app.vocabularyDictionary = vocabulary_dict
    # #Overall dictionary with hiragana and vocab 
    # app.bigDictionary = overall_dict
    #Stagnant list of all hiragana characters
    app.hiraganaList = hiraganaList
    #Information of each user
    app.userProfiles = dict()
    app.wantInput = 'No'
    app.image1 = app.loadImage('flashcard.jpg')
    #Determines if user has gotten answers correct from
    app.streak = False
    app.startQuestion = False
    app.finishedQuestion = False


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
    if app.phase == 'learning':
        learningMode_keyPressed(app,event)
    elif app.phase == 'practice':
        practiceMode_keyPressed(app,event)
def keyRelease(app,event):
    if app.phase == 'learning':
        learning_keyReleased(app, event)
#The redrawAll's of different phases
def redrawAll(app,canvas):
    if app.phase == 'start':
        startScreenRedrawall(app,canvas)
    elif app.phase == 'learning':
        learningModeRedrawAll(app,canvas)
    elif app.phase == 'practice':
        practiceModeRedrawAll(app,canvas)
    elif app.phase == 'transition':
        transitionScreenRedrawAll(app,canvas)
    elif app.phase == 'profileselect':
        userProfileRedrawAll(app,canvas)
    elif app.phase == 'settings':
        pass

def letsLearnHiragana():
    runApp(width = 800, height = 800)

def main():
    letsLearnHiragana()

if __name__ == '__main__':
    main()
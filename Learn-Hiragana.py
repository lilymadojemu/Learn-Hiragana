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
    listOfKeys = list(overall_dict.keys())
    possibleKey = random.choice(listOfKeys)
    listofHiragana = list(character_dict.keys())
    charaKey = random.choice(listofHiragana)
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
    app.baseProblemTime = 30
    #Checks/Determines if a card has been flipped or not
    app.isFlipped = False
    #Checks if a "continue key" right) has been pressed to
    # move on to next Flashcard
    app.isContinueKeyPressed = False
    #Checks if "back key" (left) has been pressed to go to a previous card
    app.isBackKeyPressed = False
    #Determines if a new flash card will be shown/made
    app.makeFlashCard = False
    app.makeOldFlashCard = False

    #default flash card, key value
    getHiraganaOrVocab(possibleKey)
    app.flashCard = FlashCard(possibleKey,overall_dict[possibleKey])
    app.practiceFlashCard = FlashCard(charaKey, character_dict[charaKey])

    #Overall hiragana flashcards user has seen
    # app.seenHiraganaFlashCards = dict()
    # #Overall vocabulary flashcards user has seen
    # app.seenVocabFlashCards = dict()
    # #Takes in all of the flashcards a user has seen
    # app.seenFlashCards = dict()
    #Decides whether a flashcard appearing will be a 
    # hiragana card or a vocab card
    app.hiraganaOrVocab = random.randint(1,2)
    app.newKey = getRandomKey()
    #Overall character dictionary
    app.characterDictionary = character_dict
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
    app.option1Chosen = False
    app.option2Chosen = False
    app.option3Chosen = False
    app.option4Chosen = False
    app.timeTaken = 0
    #Extras
    app.startBackground = app.loadImage('background.jpg')
    app.lightMode = True
    app.lightPracticeBackground = app.loadImage('day.jpg')
    app.darkMode = False
    app.darkPracticeBackground = app.loadImage('night.jpg')
    app.transitionBackground = app.loadImage('confetti.jpg')
    app.darkTransitionBackground = app.loadImage('darkConfetti.jpg')
    app.lightSettingsBackground = app.loadImage('lightSettings.jpg')
    app.darkSettingsBackground = app.loadImage('darkSettings.gif')
    


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
    if event.key == 'l':
        app.phase = 'practice'
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
        canvas.create_image(800, 800, 
                            image=ImageTk.PhotoImage(app.startBackground))
        startScreenRedrawall(app,canvas)
    elif app.phase == 'learning':
        learningModeRedrawAll(app,canvas)
        #I think this continuous state is why answers keep appearing
    elif app.phase == 'practice':
        if app.lightMode == True:
            canvas.create_image(800, 800, 
                        image=ImageTk.PhotoImage(app.lightPracticeBackground))
            if app.cardsToDo == 5:
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
        elif app.darkMode == True:
            canvas.create_image(800, 800, 
                            image=ImageTk.PhotoImage(app.startBackground))
        pass

def letsLearnHiragana():
    runApp(width = 800, height = 800)

def main():
    letsLearnHiragana()

if __name__ == '__main__':
    main()
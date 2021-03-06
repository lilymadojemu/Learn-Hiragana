'''
Name: Lily Madojemu
andrewid: lmadojem
'''
''' imports '''
from cmu_112_graphics import *
from Populate_Values import *
from Classes import *
from Start_Screen import *
from Review_Mode import *
from Learn_Hiragana_Learning_Mode import *
from Learn_Hiragana_Practice_Mode import *
from Transition_Screen import *
from Settings_Screen import*


def appStarted(app):
    app.phase = "start"
    #measurements
    app.cx = app.width//2
    app.cy = app.height//2
    #Important
    app.seenFlashCards = dict()
    app.seenHiraganaFlashCards = dict()#Overall hiragana flashcards user has seen
    app.seenVocabFlashCards = dict()#Overall vocabulary flashcards user has seen
    app.prevFlashCard= dict()
    app.currSession = dict()
    app.currSessionKeys = list(app.currSession.keys())

    #Learning Phase    
    #Checks if a "continue key" has been pressed to move on to next Flashcard
    app.isContinueKeyPressed = False
    #Checks if "back key" (left) has been pressed to go to a previous card
    app.isBackKeyPressed = False
    app.image1 = app.loadImage('flashcard.jpg')
    app.image2 = app.loadImage('flashcardBack.jpg')
    app.makeOldFlashCard = False 
    app.makeFlashCard = False
    app.newKey = getRandomKey()  
    app.prevCard = None
    app.learnNum = 5 #New number for app.cardsToLearn when increased
    app.isFlipped = False 
    #Number of flashcards that will appear in learning stage
    app.cardsToLearn = app.learnNum 
    app.cardsLearned = 0
    app.isFavorite = False
    app.unFavorite = False
    #Practice       
    #Leitner System
    #Japanese words for now, middle/fine, and good
    app.ima = set() #Box 1
    app.mama = set() #Box 2, set contains what the "target answer"
    app.jyozu = set() #Box 3
    app.prevSet = set()
    app.justSeen = set()
    app.justSeenReview = set()
    #Level of vocab/ Character knowledge
    app.characterLevel = 0
    app.vocabLevel = 0  
    app.cardsPracticed = 0
    app.practiceKey = None
    app.baseProblemTime = 15 #time alloted to answer each question during practice phase  
    app.currQuestionType = 0
    app.paused = False
    app.wantInput = False
    app.startQuestion = False
    app.finishedQuestion = False
    app.seenBox1Keys = list()
    app.seenBox2Keys = list()
    app.seenBox3Keys = list()
     
    #answer Choices
    app.option1Chosen = False
    app.option2Chosen = False
    app.option3Chosen = False
    app.option4Chosen = False
    app.listOfPossibleChoices = list()
    app.userAnswer = None

    #Review Mode
    app.reviewKey = None
    app.reviewBox1 = set()
    app.reviewBox2 = set()
    app.reviewBox3 = set()
    app.toBeReviewed = dict()

    #Extras 
    app.lightMode = True
    app.darkMode = False
    #All images free to use from unsplash
    app.startBackground = app.loadImage('background.jpg')
    app.lightPracticeBackground = app.loadImage('day.jpg')
    app.darkPracticeBackground = app.loadImage('nightNew.jpg')
    app.transitionBackground = app.loadImage('transition.jpg')
    app.darkTransitionBackground = app.loadImage('darkTransition.jpg')
    app.lightSettingsBackground = app.loadImage('lightSettings.jpg')
    app.darkSettingsBackground = app.loadImage('darkSettings.jpg')
    app.lightLearningBackground = app.loadImage('lightLearn.jpg')
    app.darkLearningBackground = app.loadImage('darkLearn.jpg')
    app.lightReviewBackground = app.loadImage('reviewLight.jpg')
    app.darkReviewBackground = app.loadImage('reviewDarkNew.jpg')
    app.timerDelay = 1000
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
    elif app.phase == 'review':
        review_mousePressed(app,event)
    elif app.phase == 'settings':
        settings_mousePressed(app,event)

#Houses the key presses of all phases
def keyPressed(app,event):
    if event.key == 'Enter':
        if app.phase == 'start':
            if (isFactor(app) == True and len(app.jyozu) >= app.learnNum and
            (app.characterLevel >= len(app.jyozu) or 
            app.vocabLevel >= len(app.jyozu)) 
            and app.cardsToLearn <= len(overall_dict) and 
            app.cardsToLearn != app.learnNum):
                app.learnNum += 5
            app.phase = 'learning'
    elif event.key == 'q':
        if app.wantInput == True:
            app.wantInput = False
        app.option1Chosen = False
        app.option2Chosen = False
        app.option3Chosen = False
        app.option4Chosen = False
        app.currSession = dict()
        app.currSessionKeys = list(app.currSession.keys())
        app.unfavorite = False
        app.isFavorite = False
        app.makeOldFlashCard = False 
        app.makeFlashCard = False
        app.newKey = getRandomKey()  
        app.prevCard = None
        app.isFlipped = False
        app.isContinueKeyPressed = False
        app.cardsLearned = 0
        app.cardsToLearn = app.learnNum 
        app.finishedQuestion = False
        if app.toBeReviewed != dict():
            if app.reviewBox1 != set():
                app.ima.union(app.reviewBox1)
            elif app.reviewBox2 != set():
                app.mama.union(app.reviewBox2)
            elif app.reviewBox3 != set():
                app.jyozu.union(app.reviewBox3)
        app.phase = 'start'        
    elif event.key == 't':
        app.startQuestion == False
        app.phase = 'transition'
    elif event.key == 'c':
        if app.wantInput == True:
            app.wantInput = False
        app.option1Chosen = False
        app.option2Chosen = False
        app.option3Chosen = False
        app.option4Chosen = False 
        app.phase = 'settings'    
    elif app.phase == 'practice':
        practiceMode_keyPressed(app,event)
    elif app.phase == 'learning':
        learningMode_keyPressed(app,event)
    elif app.phase == 'review':
        reviewMode_keyPressed(app,event)


#The redrawAll's of different phases
def redrawAll(app,canvas):
    if app.phase == 'start':
        canvas.create_image(app.width//2, app.height//2, 
                            image=ImageTk.PhotoImage(app.startBackground))
        startScreenRedrawall(app,canvas)
    elif app.phase == 'learning':
        if app.lightMode == True:
            canvas.create_image(app.width//4, app.height//2, 
                            image=ImageTk.PhotoImage(app.lightLearningBackground))
            learningModeRedrawAll(app,canvas)
        elif app.darkMode == True:
            canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.darkLearningBackground))
            learningModeRedrawAll(app,canvas)
    elif app.phase == 'practice':
        if app.lightMode == True:
            canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.lightPracticeBackground))
            practiceModeRedrawAll(app,canvas)
        elif app.darkMode == True:
            canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.darkPracticeBackground))
            practiceModeRedrawAll(app,canvas)
    elif app.phase == 'transition':
        if app.lightMode == True:
            canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.transitionBackground))
            transitionScreenRedrawAll(app,canvas)
        elif app.darkMode == True:
            canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.darkTransitionBackground))
            transitionScreenRedrawAll(app,canvas)
    elif app.phase == 'review':
        if app.lightMode == True:
            canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.lightReviewBackground))
            reviewModeRedrawAll(app,canvas)
        elif app.darkMode == True:
            canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.darkReviewBackground))
            reviewModeRedrawAll(app,canvas)
    elif app.phase == 'settings':
        if app.lightMode == True:
            canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.lightSettingsBackground))
            settings_redrawAll(app,canvas)
        elif app.darkMode == True:
            canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.darkSettingsBackground))
            settings_redrawAll(app,canvas)


def timerFired(app): 
    if app.phase == 'practice':
        practice_timerFired(app)
    elif app.phase == 'review':
        review_timerFired(app)

def letsLearnHiragana():
    runApp(width = 800, height = 800)

def main():
    letsLearnHiragana()

if __name__ == '__main__':
    main()
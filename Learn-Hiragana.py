#Learn-Hiragana
from cmu_112_graphics import *
#from Populate_Values import *
from Classes import *

def appStarted(app):
    app.cy = app.width//2
    app.cx = app.height//2
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

#Introduction/Start Stage



def introScreenRedrawall(app,canvas):
    canvas.create_text(app.cx,app.cy,
                    font = 'Arial',  text = "Let's Learn Hiragana!", 
                            fill = 'Red')
    #Create a new user profile

def drawUserProfileButton(app,canvas):
    canvas.create_rectangle(app.cx,app.cy,app.cx//2,app.cy//2, fill = 'purple')
    canvas.create_text(app.cx//2,app.cy//2,
                        font = 'Arial',  text = "newUser", fill = 'Red')


########################################################################
#Dictionary that will contain all of the users' login information
#Login and store in dictionary, if no text input, will not use
#Result of drawUserProfileButton
def userProfile(app,canvas):
    enteredUser = input
    canvas.create_text(app.cx//2,app.cy//2,
    font = 'Arial', 
    text = "Please enter Username and Password",
    fill = 'Red')
    for user in app.userProfiles:
        if enteredUser not in userProfile:
            username = input("Please create your username:")
            password = input("Please create your password:")
            app.userProfiles[username] = password
            canvas.create_text(app.cx//2,app.cy//2,
                font = 'Arial', 
                text = "User Profile has been created, please log in again",
                fill = 'Red')
        elif app.userProfiles[user] == app.userProfiles[enteredUser]:
                canvas.create_text(app.cx//2,app.cy//2,
                font = 'Arial', 
                text = f"Welcome {enteredUser}!, Click",
                fill = 'Red')

def userProfileRedrawAll(app,canvas):
    drawUserProfileButton(app,canvas)
    userProfile(app,canvas)
    pass
 ########################################################################       
#Begin Learning Stage
def drawLetsLearnButton(app,canvas):
    canvas.create_rectangle(app.cx,app.cy,app.cx//2,app.cy//2, fill = 'purple')
    canvas.create_text(app.cx//2,app.cy//2,
                        font = 'Arial',  text = "Let's learn!", fill = 'Red')
#Begin Doing Stage
def drawLetsDoButton(app,canvas):
    canvas.create_rectangle(app.cx,app.cy,app.cx//2,app.cy//2, fill = 'purple')
    canvas.create_text(app.cx//2,app.cy//2,
                        font = 'Arial',  text = "Let's Try it!", fill = 'Red')




def keyPressed(app,event):
    if (event.key == 'p'):
        app.paused = not app.paused
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
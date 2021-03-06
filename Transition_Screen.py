'''
At end of practice mode, allows the user to go back to the menu and leave, or
review of difficult cards
'''
from Learn_Hiragana_Practice_Mode import*

def transition_mousePressed(app,event):
    if app.cx//1.25 <= event.x and app.cx*1.25:
        if app.cy//1.01 <= event.y <= app.cy*1.1:
            if (isFactor(app) == True and len(app.jyozu) >= app.learnNum and
            (app.characterLevel >= len(app.jyozu) or app.vocabLevel >= len(app.jyozu)) 
            and app.cardsToLearn <= len(overall_dict) and 
            app.cardsToLearn != app.learnNum):
                app.learnNum += 5
            app.phase = 'learning'
            if app.wantInput == True:
                app.wantInput = False
            app.currQuestionType = getQuestionType()
            app.option1Chosen = False
            app.option2Chosen = False
            app.option3Chosen = False
            app.option4Chosen = False
            app.finishedQuestion = False
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
            app.startQuestion = False
            app.cardsLearned = 0
            app.cardsToLearn = app.learnNum
        elif app.cy*1.1 <= event.y <= app.cy*1.2:
            for seen in app.toBeReviewed:
                app.reviewBox1.add(seen)
            app.phase = 'review'
            app.currQuestionType = 0
            app.paused = False
            app.baseProblemTime = 15
            app.finishedQuestion = False
            app.startQuestion = False 
            app.makeFlashCard = False
            app.wantInput = False
            app.currQuestionType = getQuestionType()
            app.option1Chosen = False
            app.option2Chosen = False
            app.option3Chosen = False
            app.option4Chosen = False  
        elif app.cy*1.1 <= event.y <= app.cy*1.3:
            app.phase = 'start'


def drawExitButton(app,canvas):
    canvas.create_rectangle(app.cx//1.25,
                            app.cy*1.3,
                            app.cx*1.25,
                            app.cy*1.1, 
                            fill = 'light slate gray')
    canvas.create_text(app.cx,app.cy*1.25,
                        font = 'Arial 20', text = "Exit", fill = 'black')

def drawReviewButton(app,canvas):
    canvas.create_rectangle(app.cx//1.25,
                            app.cy*1.2,
                            app.cx*1.25,
                            app.cy*1.1, 
                            fill = 'LemonChiffon4')
    canvas.create_text(app.cx,app.cy*1.15,font = 'Arial 20', 
                        text = "Review", fill = 'black')

def drawLearningButton(app,canvas):
    canvas.create_rectangle(app.cx//1.25,
                            app.cy//1.01,
                            app.cx*1.25,
                            app.cy*1.1, 
                            fill = 'MistyRose2')
    canvas.create_text(app.cx,app.cy*1.05,font = 'Arial 20', 
                        text = "Learn", fill = 'black')

def getSummary(app,canvas):
    if app.lightMode == True:
        canvas.create_text(app.cx, app.cy//1.3, font = 'Arial 15', 
                            text =f"Novice: {app.ima}", 
                            fill = 'dark slate blue')
        canvas.create_text(app.cx, app.cy//1.5, font = 'Arial 15', 
                        text =f"Intermediate: {app.mama}", 
                        fill = 'dark slate blue')
        canvas.create_text(app.cx, app.cy//1.75, font = 'Arial 15', 
                        text =f"Master: {app.jyozu}", fill = 'dark slate blue')
    elif app.darkMode == True:
        canvas.create_text(app.cx, app.cy//1.3, font = 'Arial 15', 
                            text =f"Novice: {app.ima}", 
                            fill = 'light goldenrod')
        canvas.create_text(app.cx, app.cy//1.5, font = 'Arial 15', 
                        text =f"Intermediate: {app.mama}",
                        fill = 'light goldenrod')
        canvas.create_text(app.cx, app.cy//1.75, font = 'Arial 15', 
                        text =f"Master: {app.jyozu}", 
                        fill = 'light goldenrod')

def transitionScreenRedrawAll(app,canvas):
    if app.lightMode == True:
        canvas.create_text(app.cx, app.cy//4, font = 'Arial 20', 
                        text = "Great Job!")
        canvas.create_text(app.cx, app.cy//3, font = 'Arial 20', 
                        text = "Here's Your Progress So Far:")
    elif app.darkMode == True:
        canvas.create_text(app.cx, app.cy//4, font = 'Arial 20', 
                        text = "Great Job!", fill = "ghost white")
        canvas.create_text(app.cx, app.cy//3, font = 'Arial 20', 
                        text = "Here's Your Progress So Far:", 
                        fill = "ghost white")
    getSummary(app,canvas)
    drawLearningButton(app,canvas)
    drawExitButton(app,canvas)
    drawReviewButton(app,canvas)


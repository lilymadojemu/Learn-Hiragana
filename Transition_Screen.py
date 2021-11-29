'''
At end of practice mode, allows the user to go back to the menu and leave, or
continue practicing
'''
from Learn_Hiragana_Practice_Mode import*

def transition_mousePressed(app,event):
    if app.cx//1.25 <= event.x and app.cx*1.25:
        if app.cy*1.1 <= event.y <= app.cy*1.2:
            app.phase = 'practice'
            app.baseProblemTime = 15
            app.finishedQuestion = False
            app.startQuestion = False 
            app.cardsToDo = 10
            app.makeFlashCard = False
        elif app.cy*1.1 <= event.y <= app.cy*1.3:
            app.phase = 'start'

def transition_keyPressed(app,event):
    if event.key == 'o':
        getSummary()
    elif event.key == 'right':
        app.phase = 'practice'
    elif event.key == 'left':
        app.phase = 'start'

def drawExitButton(app,canvas):
    canvas.create_rectangle(app.cx//1.25,
                            app.cy*1.3,
                            app.cx*1.25,
                            app.cy*1.1, 
                            fill = 'light slate gray')
    canvas.create_text(app.cx,app.cy*1.25,
                        font = 'Arial 20', text = "Exit", fill = 'black')

def drawContinueButton(app,canvas):
    canvas.create_rectangle(app.cx//1.25,
                            app.cy*1.2,
                            app.cx*1.25,
                            app.cy*1.1, 
                            fill = 'LemonChiffon4')
    canvas.create_text(app.cx,app.cy*1.15,font = 'Arial 20', 
                        text = "Continue", fill = 'black')
def getSummary(app,canvas):
    canvas.create_text(app.cx, app.cy//1.3, font = 'Arial 15', 
                        text =f"Novice: {app.ima}", fill = 'dark slate blue')
    canvas.create_text(app.cx, app.cy//1.5, font = 'Arial 15', 
                    text =f"Intermediate: {app.mama}", fill = 'dark slate blue')
    canvas.create_text(app.cx, app.cy//1.75, font = 'Arial 15', 
                    text =f"Master: {app.jyozu}", fill = 'dark slate blue')

def transitionScreenRedrawAll(app,canvas):
    canvas.create_text(app.cx, app.cy//4, font = 'Arial 20', 
                    text = "Great Job!")
    canvas.create_text(app.cx, app.cy//3, font = 'Arial 20', 
                    text = "Here's Your Progress So Far:")
    getSummary(app,canvas)
    drawExitButton(app,canvas)
    drawContinueButton(app,canvas)

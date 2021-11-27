#Transition_Screen
#At end of practice mode, allows the user to go back to the menu and leave,
# #  or begin the learning mode again (with new material)
from Learn_Hiragana_Practice_Mode import*

def transition_mousePressed(app,event):
    pass
def transition_keyPressed(app,event):
    if event.key == 'o':
        getSummary()
    elif event.key == 'right':
        app.phase = 'practice'
    elif event.key == 'left':
        app.phase = 'start'

def drawExitButton(app,canvas):
    canvas.create_rectangle(app.cx*3,
                            app.cy*1.2,
                            app.cx,
                            app.cy*1.1, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.15,
                        font = 'Arial',  text = "Exit", fill = 'black')

def drawContinueButton(app,canvas):
    canvas.create_rectangle(app.cx//2,
                            app.cy*1.2,
                            app.cx//-2,
                            app.cy*1.1, 
                            fill = 'pale violet red')

    canvas.create_text(app.cx/6,app.cy*1.15,font = 'Arial 20', 
                        text = "Continue", fill = 'black')

def transitionScreenRedrawAll(app,canvas):
    canvas.create_text(app.cx,app.cy, text = f'{getSummary(app)}', 
                        fill = 'black')
    drawExitButton(app,canvas)
    drawContinueButton(app,canvas)

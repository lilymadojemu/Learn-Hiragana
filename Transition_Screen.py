#Transition_Screen
#At end of practice mode, allows the user to go back to the menu and leave,
# #  or begin the learning mode again (with new material)
from Learn_Hiragana_Practice_Mode import*

def transition_mousePressed(app,event):
    pass
def transition_keyPressed(app,event):
    # if event.key == 'o':
    #     getSummary()
    pass

def drawExitButton(app,canvas):
    pass
def drawContinueButton(app,canvas):
    pass
def transitionScreenRedrawAll(app,canvas):
    app.Message('Press o for Summary!')
    drawExitButton(app,canvas)
    drawContinueButton(app,canvas)

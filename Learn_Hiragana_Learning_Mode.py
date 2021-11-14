'''Need to call on classes in learning mode functions'''
from Classes import*





def learningMode_keyPressed(app,event):
    pass


def learningMode_mouserPressed(app,event):
    pass







#Initiate Practice Mode
def drawLetsTryitButton(app,canvas):
    canvas.create_rectangle(app.cx,app.cy,app.cx//2,app.cy//2, fill = 'purple')
    canvas.create_text(app.cx//2,app.cy//2,
                        font = 'Arial',  text = "Let's Try it!", fill = 'Red')
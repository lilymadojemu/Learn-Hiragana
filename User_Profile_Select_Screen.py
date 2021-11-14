def userSelect_mousePressed(app,event):
    #Parameters for learning button to be pressed
    #if event.y ya know...
        #app.phase = 'learning'

#Initates Learning Mode
def drawLetsLearnButton(app,canvas):
    canvas.create_rectangle(app.cx//4,app.cy//4,app.cx//2,app.cy//2, 
                            fill = 'red')
    canvas.create_text(app.cx//6,app.cy//6,
                        font = 'Arial',  text = "Let's learn!", fill = 'black')

def userProfileRedrawAll(app,canvas):
    #will house anything drawn for the user Profile
    drawLetsLearnButton(app,canvas)

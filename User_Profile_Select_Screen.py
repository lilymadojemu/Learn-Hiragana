def userSelect_mousePressed(app,event):
    #Parameters for learning button to be pressed
    #if event.y ya know...
        app.phase = 'learning'

#Initates Learning Mode
def drawLetsLearnButton(app,canvas):
    canvas.create_rectangle(app.cx,app.cy,app.cx//2,app.cy//2, fill = 'purple')
    canvas.create_text(app.cx//2,app.cy//2,
                        font = 'Arial',  text = "Let's learn!", fill = 'Red')

def userProfileRedrawAll(app,canvas):
    #will house anything drawn for the user Profile
    drawLetsLearnButton(app,canvas)

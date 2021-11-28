#Settings
#Overall history of what got wrong, write, etc.
#Where user can change default values

def settings_mousePressed(app,event):
    pass
def settings_keyPressed(app,event):
    if event.key == 'Right' or event.key == 'Left':
        app.lightMode = not app.lightMode
        app.darkMode = not app.darkMode
    elif event.key == 'q':
        app.phase = 'start'

def drawLightModeButton(app,canvas):
    canvas.create_rectangle(app.cx*2,
                            app.cy*1.2,
                            app.cx,
                            app.cy*1.1, 
                            fill = 'peach puff')
    canvas.create_text(app.cx*1.5,app.cy*1.15,
                        font = 'Arial 20',  text = "Light Mode", 
                        fill = 'deep sky blue')

def drawDarkModeButton(app,canvas):
    canvas.create_rectangle(app.cx//2,
                            app.cy*1.2,
                            app.cx//-1.5,
                            app.cy*1.1, 
                            fill = 'blue violet')
    canvas.create_text(app.cx//4,app.cy*1.15,font = 'Arial 20', 
                        text = "Dark Mode", fill = 'black')

def settings_redrawAll(app,canvas):
    if app.lightMode == True:
        canvas.create_text(app.cx,app.cy//3, font = 'Arial 25', 
                            text = "Welcome to Settings!")
    else:
        canvas.create_text(app.cx,app.cy//3, font = 'Arial 25', 
                            text = "Welcome to Settings!", fill = 'papaya whip')
    drawLightModeButton(app,canvas)
    drawDarkModeButton(app,canvas)
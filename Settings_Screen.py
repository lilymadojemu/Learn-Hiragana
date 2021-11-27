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
    canvas.create_rectangle(app.cx*3,
                            app.cy*1.2,
                            app.cx,
                            app.cy*1.1, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.15,
                        font = 'Arial',  text = "Light Mode", fill = 'black')

def drawDarkModeButton(app,canvas):
    canvas.create_rectangle(app.cx//2,
                            app.cy*1.2,
                            app.cx//-2,
                            app.cy*1.1, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx/6,app.cy*1.15,font = 'Arial 20', 
                        text = "Dark Mode", fill = 'black')

def settings_redrawAll(app,canvas):
    canvas.create_text(app.cx,app.cy, font = 'Arial 25', 
                        text = "Welcome to Settings!")
    drawLightModeButton(app,canvas)
    drawDarkModeButton(app,canvas)
def settings_mousePressed(app,event):
    if app.cx//1.25 <= event.x and app.cx*1.25:
        if app.cy*1.1 <= event.y <= app.cy//1.01:
            app.lightMode = not app.lightMode
            app.darkMode = not app.darkMode
        elif app.cy*1.1 <= event.y <= app.cy*1.2:
            app.lightMode = not app.lightMode
            app.darkMode = not app.darkMode
        elif app.cy*1.1 <= event.y <= app.cy*1.3:
            app.cardsToLearn = app.getUserInput('Type number of cards for Learning Mode (between 1 - 20)')



def drawLightModeButton(app,canvas):
    canvas.create_rectangle(app.cx//1.25,
                            app.cy//1.01,
                            app.cx*1.25,
                            app.cy*1.1,   
                            fill = 'peach puff')
    canvas.create_text(app.cx,app.cy*1.05,
                        font = 'Arial 15',  text = "Light Mode", 
                        fill = 'deep sky blue')

def drawDarkModeButton(app,canvas):
    canvas.create_rectangle(app.cx//1.25,
                            app.cy*1.2,
                            app.cx*1.25,
                            app.cy*1.1,  
                            fill = 'blue violet')
    canvas.create_text(app.cx,app.cy*1.15,font = 'Arial 15', 
                        text = "Dark Mode", fill = 'black')

def drawChangeDefaultLearningButton(app,canvas):
    canvas.create_rectangle(app.cx//1.25,
                            app.cy*1.3,
                            app.cx*1.25,
                            app.cy*1.1, 
                            fill = 'blue violet')
    canvas.create_text(app.cx, app.cy*1.25,font = 'Arial 15', 
                        text = "Change Default Learning Cards", fill = 'black')

def settings_redrawAll(app,canvas):
    if app.lightMode == True:
        canvas.create_text(app.cx,app.cy//3, font = 'Arial 25', 
                            text = "Welcome to Settings!")
    else:
        canvas.create_text(app.cx,app.cy//3, font = 'Arial 25', 
                            text = "Welcome to Settings!", fill = 'papaya whip')
    drawLightModeButton(app,canvas)
    drawDarkModeButton(app,canvas)
    drawChangeDefaultLearningButton(app,canvas)

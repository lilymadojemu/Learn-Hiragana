#Start Screen
'''
Potential colors: ['medium aquamarine','olive drab','tomato','sandy brown',
        'pale violet red','medium slate blue','cadet blue','hot pink',
        'thistle','khaki','navajo white','cyan','bisque','plum','tan']
'''
def intro_mousePressed(app,event):
    #Go to learning mdoe 
    if (app.width//2 <= event.x and event.x >= app.width//4 
            and app.height//16 >= event.y):
        app.showMessage('Learning')
        #app.phase = 'learning'
    elif (app.width//2 <= event.x and event.x >= app.width//4 and 
            app.height//14 >= event.y):
            app.showMessage('Profiles')
            #app.phase = 'profileselect'
    elif (app.width//2 <= event.x and event.x >= app.width//4 and 
        app.height//6 >= event.y):
            app.showMessage('Settings')
            #app.phase = 'settings'
    # else:
    #     app.showMessage("Please click on one of the options.")

#Initiate Learning Mode
def drawLetsLearnButton(app,canvas):
    canvas.create_rectangle(app.cx//2,app.cy//12,app.cx*1.5,app.cy//6, 
                                fill = 'plum')
    canvas.create_text(app.cx,app.cy//9,font = 'Arial', 
                        text = "Let's learn!", fill = 'black')

#End will be a button that goes to profile select
#Will be dealt with later
def drawProfileSelectButton(app,canvas):
    canvas.create_rectangle(app.cx//2,app.cy//4, app.cx*1.5, app.cy//6, 
                            fill = 'bisque')
    canvas.create_text(app.cx,app.cy//5,
                        font = 'Arial',  text = "newUser",
                            fill = 'plum')

#Directly Under the Profile Select Button
#Where user will be able to edit things, like default number of cards, etc. 
def drawSettingsButton(app,canvas):
    canvas.create_rectangle(app.cx//2,
                            app.cy//2.5,
                            app.cx*1.5,
                            app.cy//4, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx,app.cy//3,
                        font = 'Arial',  text = "Settings", fill = 'grey')
    
def startScreenRedrawall(app,canvas):
    canvas.create_text(app.cx, 5, font = 'Arial',  
                        text = "Let's Learn Hiragana!", fill = 'Red')
    drawLetsLearnButton(app,canvas)
    drawProfileSelectButton(app,canvas)
    drawSettingsButton(app,canvas)
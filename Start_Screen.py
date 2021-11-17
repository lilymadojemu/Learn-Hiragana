#Start Screen
'''
Potential colors: ['medium aquamarine','olive drab','tomato','sandy brown',
        'pale violet red','medium slate blue','cadet blue','hot pink',
        'thistle','khaki','navajo white','cyan','bisque','plum','tan']
'''
# def intro_mousePressed(app,event):
#     #Clicking on the Profile Selct button 
#     app.cx = event.x
#     app.cy = event.y
#     #Figure out placement of buttons then determine where clicks will be
#     #Go to learning mdoe 
#     if app.width//4 
#     #app.phase = 'learning'
#     #Go to Profile Select Screen
#     #app.phase = "profileselect"
#     #Go to Settings Screen
#     #app.phase = 'settings'
def intro_mousePressed(app,event):
    #Clicking on the Profile Selct button 
    #Figure out placement of buttons then determine where clicks will be
    #Go to learning mdoe 
    if app.width//4 <= event.x:
        if app.width//4 <= event.y:
            app.showMessage('correct Click')
            app.phase = 'learning'
    else:
        app.showMessage("Please click on one of the options.")
        #Clicking on the Profile Selct button 
    #Figure out placement of buttons then determine where clicks will be
    #Go to learning mdoe 
    # if app.width//4 <= event.x:
    #     if app.width//4 <= event.y:
    #         app.showMessage('correct Click')
    #         app.phase = 'learning'
    # else:
    #     app.showMessage("Please click on one of the options.")

    #Go to Profile Select Screen
    #app.phase = "profileselect"
    #Go to Settings Screen
    #app.phase = 'settings'

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
                            fill = 'blue')
    canvas.create_text(app.cx,app.cy//5,
                        font = 'Arial',  text = "newUser *Coming Soon*",
                            fill = 'tan')

#Directly Under the Profile Select Button
#Where user will be able to edit things, like default number of cards, etc. 
def drawSettingsButton(app,canvas):
    canvas.create_rectangle(app.cx//2,
                            app.cy//2.5,
                            app.cx*1.5,
                            app.cy//4, 
                            fill = 'green')
    canvas.create_text(app.cx,app.cy//3,
                        font = 'Arial',  text = "Settings", fill = 'grey')
    
def startScreenRedrawall(app,canvas):
    canvas.create_text(app.cx, 5, font = 'Arial',  
                        text = "Let's Learn Hiragana!", fill = 'Red')
    drawLetsLearnButton(app,canvas)
    drawProfileSelectButton(app,canvas)
    drawSettingsButton(app,canvas)
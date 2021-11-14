#Start Screen

def introMousePressed(app,event):
    #Clicking on the Profile Selct button 
    app.cx = event.x
    app.cy = event.y
    #Figure out placement of buttons then determine where clicks will be
    #Go to Profile Select Screen
    #app.stage = "profileselect"
    #Go to Settings Screen
    #app.stage = 'settings'



#End will be a button that goes to profile select
def drawProfileSelectButton(app,canvas):
    canvas.create_rectangle(app.cx//6,app.cy//2,
                            app.cx//2,app.cy//2, fill = 'blue')
    canvas.create_text(app.cx//2,app.cy//2,
                        font = 'Arial',  text = "newUser", fill = 'brown')



#Directly Under the Profile Select Button
#Where user will be able to edit things, like default number of cards, etc. 
def drawSettingsButton(app,canvas):
    canvas.create_rectangle(app.cx//2,app.cy//2,
                            app.cx//2,app.cy//2, fill = 'green')
    canvas.create_text(app.cx//2,app.cy//2,
                        font = 'Arial',  text = "Settings", fill = 'grey')
    
def startScreenRedrawall(app,canvas):
    canvas.create_text(app.cx, 0, font = 'Arial',  
                        text = "Let's Learn Hiragana!", fill = 'Red')
    drawProfileSelectButton(app,canvas)
    drawSettingsButton(app,canvas)
    #Create a new user profile
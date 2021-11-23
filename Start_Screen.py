
'''
Potential colors: ['medium aquamarine','olive drab','tomato','sandy brown',
        'pale violet red','medium slate blue','cadet blue','hot pink',
        'thistle','khaki','navajo white','cyan','bisque','plum','tan']
'''
def intro_mousePressed(app,event):
    #Placements still need some work
    #Go to learning mode
    if (app.width//2 <= event.x and event.x >= app.width//4 
            and app.height//16 >= event.y):
        app.showMessage('Lets Learn Something New Today! ≧◠‿◠≦✌')
        app.phase = 'learning'
    elif (app.width//2 <= event.x and event.x >= app.width//4 and 
            app.height//14 >= event.y):
            app.showMessage('Profiles 👋≧◉ᴥ◉≦')
            #app.phase = 'profileselect'
    elif (app.width//2 <= event.x and event.x >= app.width//4 and 
            app.height//6 >= event.y):
            app.showMessage('Settings ʕ•́ᴥ•̀ʔっ')
            #app.phase = 'settings'

#Initiate Learning Mode
def drawLetsLearnButton(app,canvas):
    canvas.create_rectangle(app.cx//2,app.cy//12,app.cx*1.5,app.cy//6, 
                                fill = 'plum')
    canvas.create_text(app.cx,app.cy//9,font = 'Arial', 
                        text = "Let's Learn!", 
                        fill = 'medium aquamarine')

#End will be a button that goes to profile select
#Will be dealt with later
def drawProfileSelectButton(app,canvas):
    canvas.create_rectangle(app.cx//2,app.cy//4, app.cx*1.5, app.cy//6, 
                            fill = 'bisque')
    canvas.create_text(app.cx,app.cy//5,
                        font = 'Arial',  text = "New User",
                            fill = 'plum')

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
    canvas.create_text(app.cx, app.cy, font = 'Arial 24',  
                        text = "Let's Learn Hiragana!", 
                        fill = 'navajo white')
    drawLetsLearnButton(app,canvas)
    drawProfileSelectButton(app,canvas)
    drawSettingsButton(app,canvas)
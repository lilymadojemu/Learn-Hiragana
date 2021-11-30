def intro_mousePressed(app,event):
    if app.cx//4 <= event.x <= app.cx//2:
        if app.cy//12 <= event.y <= app.cy//6:
            app.showMessage('Lets Learn Something New Today! ≧◠‿◠≦✌')
            app.phase = 'learning'
        elif app.cy//6 <= event.y <= app.cy//4:
            if app.toBeReviewed != dict():
                app.phase = 'review'
            else:
                app.showMessage("There's Nothing To Review!")
        elif app.cy//4 <= event.y <= app.cy//2.5:
            app.showMessage('Settings ʕ•́ᴥ•̀ʔっ')
            app.phase = 'settings'

def drawLetsLearnButton(app,canvas):
    canvas.create_rectangle(app.cx//2,app.cy//12,app.cx*1.5,app.cy//6, 
                                fill = 'RoyalBlue3')
    canvas.create_text(app.cx,app.cy//9,font = 'Arial 15', 
                        text = "Let's Learn!", 
                        fill = 'MistyRose2')

def drawReviewButton(app,canvas):
    canvas.create_rectangle(app.cx//2,app.cy//4, app.cx*1.5, app.cy//6, 
                            fill = 'papaya whip')
    canvas.create_text(app.cx,app.cy//5,
                        font = 'Arial 15',  
                        text = "Review",
                        fill = 'plum')

def drawSettingsButton(app,canvas):
    canvas.create_rectangle(app.cx//2,
                            app.cy//2.5,
                            app.cx*1.5,
                            app.cy//4, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx,app.cy//3,
                        font = 'Arial 15', 
                    text = "Settings", fill = 'PeachPuff3')
                        
def startScreenRedrawall(app,canvas):
    canvas.create_text(app.cx, app.cy, font = 'Arial 24',  
                        text = "Let's Learn Hiragana!", 
                        fill = 'navajo white')
    drawLetsLearnButton(app,canvas)
    drawReviewButton(app,canvas)
    drawSettingsButton(app,canvas)
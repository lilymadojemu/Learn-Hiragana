from Populate_Values import*
from Learn_Hiragana_Practice_Mode import*

def intro_mousePressed(app,event):
    if app.cx//2 <= event.x <= app.cx*1.5:
        if app.cy//12 <= event.y <= app.cy//6:
            app.showMessage('Lets Learn Something New Today! ≧◠‿◠≦✌')
            if (isFactor(app) == True and len(app.jyozu) >= app.learnNum and
                (app.characterLevel >= len(app.jyozu) or 
                app.vocabLevel >= len(app.jyozu)) 
                and app.cardsToLearn <= len(overall_dict) and 
                app.cardsToLearn != app.learnNum):
                    app.learnNum += 5
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
    canvas.create_text(app.cx, app.cy*1.2, font = ('Arial', '24', 'bold'),  
                        text = "✍(◔◡◔)", 
                        fill = 'navajo white')
    drawLetsLearnButton(app,canvas)
    drawReviewButton(app,canvas)
    drawSettingsButton(app,canvas)
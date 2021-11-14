def practice_keyPressed(app,event):
    #Pausing, unpausing in Practice Mode Only
    if (event.key == 'p'):
        app.paused = not app.paused


#manually underline text? loop over given word, if target letter in word, underline               
def drawDoingHiraganaFlashcard(app,canvas):
    #front, hiragana
    canvas.create_rectangle(app.width-100,app.height//4, app.width-20,
                                    app.height//4+35, fill = 'white')
    #canvas.create_text(  f'{app.characterLevel}, {app.vocabLevel}')    
    #Back, romanji
    #function from another file
    # if isCorrect == False:
    #     #don't show back of card
    #     pass

#Automatically move on to next flashcard card, Doing stage
def timerFired(app):
    pass

# def practiceModeRedrawAll(app,canvas):
#     pass
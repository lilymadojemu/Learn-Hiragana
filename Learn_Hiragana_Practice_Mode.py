def practiceMode_keyPressed(app,event):
    #Pausing, unpausing in Practice Mode Only
    if (event.key == 'p'):
        app.paused = not app.paused
    if event.key == 'q':
        app.showMessage("All your progress will be lost!")
        app.phase = 'start'

def practice_mousePressed(app,event):
    if event.key == 'Up':
        app.showMessage("Went up!")


#manually underline text? loop over given word, if target letter in word, underline               
    #canvas.create_text(  f'{app.characterLevel}, {app.vocabLevel}')    
    #Back, romanji
    #function from another file
    # if isCorrect == False:
    #     #don't show back of card
    #     pass
# def practiceCards(selectedWord):
#     if currCard.getMeaning(selectedWord) == currCard.getMeaning(correctAnswer):
#         user.isCorrect(selectedWord) 
#     else:
#         not user.isCorrect(selectedWord)
#Automatically move on to next flashcard card, Doing stage
def timerFired(app):
    pass

def practiceModeRedrawAll(app,canvas):
   pass
from Classes import*

from Populate_Values import*
'''
Overall Purpose: It is up to the user to read what is on the front and back of 
the flashcards
'''
'''
flipping cards
be at a base position, want that base position to change when flipped
Get base position and center and ending base position & center

'''
'''Goes Somewhere'''
'''Goes Somewhere

#For Hiragana Cards, 1 is Hiragana
        modifiedHiraganaList = copy.deepcopy(hiraganaList)
        modifiedCharacter_dict = copy.deepcopy(character_dict)
        if app.hiraganaOrVocab == 1:
            #Currently getting everything instead of one at a time
            for kana in modifiedHiraganaList:
                if (kana not in app.seenHiraganaFlashCards and kana not in 
                    app.seenFlashCards):
                    kana = self.frontText
                    modifiedCharacter_dict[kana] = self.backText 
                    #Front of card
                    if app.isFlipped == False:
                        #Exact Placement to be changed
                        #The Hiragana Character
                        canvas.create_text(app.cx,app.cy//2,
                                        font = 'Arial',
                                        text = f"{kana}", 
                                        fill = 'thistle')
                    #Back of card
                    elif app.isFlipped == True:
                        #The Pronunciation of Hiragana Character
                        canvas.create_text(app.cx, app.cy//2,font = 'Arial',
                                    text = f"{modifiedCharacter_dict[kana]}", 
                                        fill = 'medium aquamarine')
                # #User gone to the next card
                # if(app.isContinueKeyPressed == True and
                #      app.cardsToLearn >= 0):
                #     #puts current card in already seen flashcards
                #     #I want to take that key value pair out of characterdict
                #     app.seenHiraganaFlashCards[kana] = (
                #                                modifiedCharacter_dict[kana])
                #     #modifiedHiraganaList.remove(kana)                                        
                #     del modifiedCharacter_dict[kana]
                #     print(modifiedCharacter_dict)

                #     #Finished with everything
                #     if modifiedCharacter_dict == {}:
                #         app.showMessage("Empty!")
                #         #Once this happens, user will only look at incorrect 
                #         #correct characters/words from what they went 
                #         # through
                    
        #For Vocab Cards, 2 is vocabulary
        modifiedVocabList = copy.deepcopy(vocabList)
        modifiedVocab_dict = copy.deepcopy(vocabulary_dict)
        if app.hiraganaOrVocab == 2:
            #Keeps track of flashcards I have already been through, 
            #will play big role in keeping track of users' progress
            # through flashcards
            #Currently getting everything instead of one at a time
            for word in modifiedVocabList:
                #while key in modifiedHiraganaList:
                    self.frontText = word
                    self.backText = modifiedVocab_dict[word]
                    #Front of card
                    if app.isFlipped == False:
                        #Exact Placement to be changed
                        #The Vocabulary Word
                        canvas.create_text(app.cx,app.cy//2,
                                        font = 'Arial',
                                        text = f"{self.frontText}", 
                                        fill = 'thistle')
                    #Back of card
                    elif app.isFlipped == True:
                        #The Pronunciation of Vocabulary
                        canvas.create_text(app.cx, app.cy//2,font = 'Arial',
                                        text = f"{self.backText}", 
                                        fill = 'medium aquamarine')
                # #Has user gone to the next card
                # elif(app.isContinueKeyPressed == True and
                #      app.cardsToLearn >= 0):
                #     app.seenVocabularyFlashCards[self.frontText] = (
                #                 self.backText)
                #     del modifiedVocab_dict[self.frontText]
                #     #Finished with everything
                #     if modifiedVocab_dict == {}:
                #         app.showMessage("Empty!")
                #         #Once this happens, user will only look at incorrect 
                #         #correct characters/words from what they went 
                #         # through
                        
'''

modifyListOfKeys = list(overall_dict.keys())
modifiedOverall_dict = copy.deepcopy(overall_dict)
#not completely off base
def letsLearn(app,canvas):
    #FlashCard info.
    while app.phase == 'learning':
        prevFlashCard = dict()
        possibleKey = random.choice(modifyListOfKeys)
        #Hiragana, for tracking sake
        if possibleKey in hiraganaList and app.hiraganaOrVocab == 1:
                app.flashCard = FlashCard(possibleKey,
                                modifiedOverall_dict[possibleKey])
                currFlashCard = app.flashCard
                currFlashCard.drawFlashCard(canvas,app)

                # if app.isFlipped == True:
                #     currFlashCard.flip()
                if app.isContinueKeyPressed == True:
                    characterKey = currFlashCard.frontText
                    characterValue = currFlashCard.backText
                    prevFlashCard[characterKey] = characterValue
                    del modifiedOverall_dict[characterKey]
                    continue
                elif app.isBackKeyPressed == True:
                    prevFlashCard.drawFlashCard(canvas,app)
        #vocab
        elif possibleKey in vocabList and app.hiraganaOrVocab == 2:
            app.flashCard = FlashCard(possibleKey,
                                    modifiedOverall_dict[possibleKey])
            currFlashCard = app.flashCard
            currFlashCard.drawFlashCard(canvas,app)

            # if app.isFlipped == True:
            #     currFlashCard.flip()
            if app.isContinueKeyPressed == True:
                currFlashCard = prevFlashCard
                #Add prevFlashCard key-value to seen flashcard
                app.seenFlashCards[prevFlashCard.frontText] =(
                                                prevFlashCard.backText )
            elif app.isBackKeyPressed == True:
                prevFlashCard.drawFlashCard()
        # #Check if able to make more flash cards
        # if app.makeFlashCard == True and app.cardsToLearn > 0:
        #     #add exisiting flashcard to seen
        #     app.cardsToLearn -= 1
        #     app.newFlashCard = FlashCard("Me", "Three")
        #     if app.hiraganaOrVocab == 1:
        #         oldFlashCard = currFlashCard
        #         app.seenHiraganaFlashCard[currFlashCard]
        #         currFlashCard = app.newFlashCard
        #     elif app.hiraganaOrVocab == 2:
        #         oldFlashCard = currFlashCard
        #         app.seenVocabularyFlashCard[currFlashCard]
        #         currFlashCard = app.newFlashCard
        # elif app.cardsToLearn < 0:
        #     app.showMessage("You're Done!")
        # elif app.makeOldFlashCard == True:
        #     #Draw flash card based on app.seen (in order)
        #     app.newFlashCard.drawFlashcard(canvas,app)


''' call method on current flashcard'''           
def learningMode_keyPressed(app,event):
    #flips front of flash card to back
    #flips back to front 
    if event.key == 'q':
        app.showMessage("All your progress will be lost!")
        app.phase = 'start'
    if event.key == 'Up' or event.key == 'Down':
        app.isFlipped = not app.isFlipped
    #Move to new card, populate next card
    if event.key == 'Right':
        app.isContinueKeyPressed = True
        app.cardsToLearn -= 1
        app.makeFlashCard = True
        app.hiraganaOrVocab =  random.randint(1,2)
    #Move to previous card
    elif event.key == 'Left':
        app.isBackKeyPressed = True
        app.makeOldFlashCard = True

def learning_keyReleased(app, event): 
    #Once right key is release it defaults
    pass


def learningMode_mousePressed(app,event):
    #Determines whether a card needs to be flip
    if (app.width//2 <= event.x and event.x >= app.width//4 and app.height//4 
        <= event.y and event.y >= app.height):
            app.isFlipped = not app.isFlipped
    #Need to fix
    if (app.cardsToLearn == 0 and app.width//4 <= event.x and 
        event.x >= app.width//6 and app.height//10 <= event.y and 
        event.y >= app.height//5):
        app.showMessage('Are you ready to practice?')
        app.phase ='practice'

#Initiate Practice Mode
def drawLetsTryitButton(app,canvas):
    canvas.create_rectangle(app.cx*2,
                            app.cy*1.5,
                            app.cx,
                            app.cy*1.3, 
                            fill = 'pale violet red')
    canvas.create_text(app.cx*1.5,app.cy*1.4,
                        font = 'Arial',  text = "Let's Try it!", fill = 'black')

def learningModeRedrawAll(app,canvas):
    if app.makeFlashCard == False:
        app.flashCard.drawFlashCard(canvas,app)
    if app.makeFlashCard == True:
        letsLearn(app,canvas)
        app.flashCard.drawFlashCard(canvas,app)
    if (app.cardsToLearn == 0):
        drawLetsTryitButton(app,canvas)

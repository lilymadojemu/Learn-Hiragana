'''
Contains all classes that will be used
'''
from Populate_Values import*
import os, random, time, copy
class correctWord(object):
    def __init__(self, correctWord):
        self.correctWord = correctWord
    def isCorrectAnswer(self, possibleAnswer):
        if self.frontText == possibleAnswer:
            return True
        else:
            return False  

''' In Learning Phase'''
'''
Will use for Flashcard background
From: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
def appStarted(app):
    url = 'https://tinyurl.com/great-pitch-gif'
    app.image1 = app.loadImage(url)
    app.image2 = app.image1.transpose(Image.FLIP_LEFT_RIGHT)

def redrawAll(app, canvas):
    canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))
    canvas.create_image(500, 300, image=ImageTk.PhotoImage(app.image2))
'''

class FlashCard(object):
    def __init__(self, frontText, backText):
        #Before Flipping
        self.frontText = frontText
        self.backText = backText
        #After Flipping
        self.newFront = backText
        self.newBack = frontText

    def drawFlashcard(self,canvas, app):
        canvas.create_rectangle(app.cx*1.5,
                                app.cy//4,
                                app.cx//4,
                                app.cy, 
                                fill = 'bisque')
        canvas.create_text(app.cx//1.5, app.cy//3,font = 'Arial',
    text = f"KanaLevel:{app.characterLevel},{app.vocabLevel}", 
                            fill = 'medium aquamarine')
                            
        if app.phase == 'learning':
            canvas.create_text(app.cx//1.5, app.cy,font = 'Arial',
        text = f"Cards Left:{app.cardsToLearn}", fill = 'medium aquamarine')

        elif app.phase == 'practice':
            canvas.create_text(app.cx//1.5, app.cy,font = 'Arial',
        text = f"Cards Left:{app.cardsToDo}", fill = 'medium aquamarine')



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
                        
                

    # def getMeaning(self, word):
    #     if word in characterDictionary:
    #         return characterDictionary[word]
    #     elif word in vocabularyDictionary:
    #         return vocabularyDictionary[word]
    #     else:
    #         self.app.showMessage('Sorry, that word is invalid:(')
    def flip(self):
        if self.app.isFlipped == True:
            self.frontText = self.newFront
            self.backText = self.newBack

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
#Problemtime - currTime 
#bot that will hold all the inner processes for learner
class SenseiBot(object):
    def __init__(self,botName, currTime):
        self.botName = botName
        # self.possibleChoices = possibleChoices
        # self.targetAnswer = targetAnswer
        # self.app = app
        self.currTime = currTime
        pass
    #Information regarding the choices a user will be able to 
    # select for each prob.
    #Mainy applies in Practice Phase
    def answerChoices(self):
        self.possibleChoices = Merge(self.characterDictionary, 
                                    self.vocabularyDictionary)
        random.random(self.possibleChoices)
        pass
    #Determines whether or not an answer is correct or not,
    #If correct, bot will say "correct!"
    #otherwise, bot will say "incorrect!"
    #Might become its own function
    #Practice Phase
    def isCorrect(self, answerChoice):
        correctMessages = ["That's Correct!", "You're the best!"]
        incorrectMessages = ["Sorry, that's incorrect","Better luck next time!"]
        if answerChoice == self.possibleChoice[self.targetAnswer]:
            self.app.showMessage(random.random(correctMessages))
        else:
            self.app.showMessage(random.random(incorrectMessages))
    #How long user has to select/input answer
    #Should time vary depending on if already known or not
    #If varies, need to be based on Assigned time
    #Practice Phase
    def InternalProblemTimer(self,app,time):
        if self.app.baseProblemTime - self.curr.time:
            pass
'''
Each key-value pair, once answered will be assigned an initial time and a time
where they should go back into circulation based on whether correct or not and
how many times it is deemed correct or not

I will ultimately need to create a formula that will determine the timings for
each card/question
'''

# #Base: what to do with values that are correct
# #Practice Phase
# class AssignedTime(object):
#     def __init__(self):
#         pass
# #What to do with vocab & characters that are incorrect
# class IncorrectAssignedTime(AssignedTime):
#     pass

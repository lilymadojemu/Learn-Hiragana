'''
Contains all classes that will be used
'''
from Populate_Values import*
from cmu_112_graphics import*
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
        #Key its based on
       

    def drawFlashCard(self, canvas, app):
        canvas.create_rectangle(app.cx*1.5,
                                app.cy//4,
                                app.cx//4,
                                app.cy, 
                                fill = 'bisque')
        # canvas.create_image(app.cx, app.cy, 
        #                     image=ImageTk.PhotoImage(app.image1))
        canvas.create_text(app.cx//2, app.cy//5,font = 'Arial',
    text = f"Kana Level:{app.characterLevel},\nVocab Level:{app.vocabLevel}", 
                            fill = 'black')

        if app.phase == 'learning':
            canvas.create_text(app.cx, app.cy,font = 'Arial',
            text = f"Cards Left:{app.cardsToLearn}", fill = 'black')

        elif app.phase == 'practice':
            canvas.create_text(app.cx//1.5, app.cy,font = 'Arial',
                                text = f"Cards Left:{app.cardsToDo}", 
                                fill = 'medium aquamarine')
        #Hiragana
        # if len(self.frontText) == 1:

        #     print(self.frontText)
        #     if app.isFlipped == False:
        #         #Exact Placement to be changed
        #         #The Hiragana Character
        #         canvas.create_text(app.cx,app.cy//2,
        #                         font = 'Arial',
        #                         text = f"{self.frontText}", 
        #                         fill = 'hot pink')
        #     #Back of card
        #     elif app.isFlipped == True:
        #         romanji = self.backText[0]
        #         pronunciation = self.backText[1]
        #         canvas.create_rectangle(app.cx*1.5,
        #                     app.cy//4,
        #                     app.cx//4,
        #                     app.cy, 
        #                     fill = 'olive drab')
        #         #The Pronunciation of Hiragana Character
        #         canvas.create_text(app.cx, app.cy//2,font = 'Arial',
        #                     text = f"{romanji}\n{pronunciation}", 
        #                         fill = 'medium aquamarine')
        # #Vocabulary
        # elif len(self.frontText) != 1:
        #         if app.isFlipped == False:
        #             #Exact Placement to be changed
        #             canvas.create_text(app.cx,app.cy//2,
        #                             font = 'Arial',
        #                             text = f"{self.frontText}", 
        #                             fill = 'thistle')
        #         #Back of card
        #         elif app.isFlipped == True:
        #             if len(self.backText) == 3:
        #                 currRomanji = list(self.backText[0])
        #                 translation1= self.backText[1]
        #                 translation2=self.backText[2]
        #                 currRomanji.insert(7," ")
        #                 currRomanji.insert(10," ")
        #                 threeWordRomanji = ""
        #                 for c in range(len(currRomanji)):
        #                     threeWordRomanji += currRomanji[c]

        #                 canvas.create_rectangle(app.cx*1.5,
        #                         app.cy//4,
        #                         app.cx//4,
        #                         app.cy, 
        #                         fill = 'olive drab')
        #                 canvas.create_text(app.cx, app.cy//2,font = 'Arial',
        #             text = f"{threeWordRomanji}\n{translation1}{translation2}", 
        #                             fill = 'medium aquamarine')
        #             else:
        #                 wordRomanji = self.backText[0]
        #                 translation= self.backText[1]
        #                 canvas.create_rectangle(app.cx*1.5,
        #                             app.cy//4,
        #                             app.cx//4,
        #                             app.cy, 
        #                             fill = 'olive drab')
        #                 canvas.create_text(app.cx, app.cy//2,font = 'Arial',
        #                             text = f"{wordRomanji}\n{translation}", 
        #                                 fill = 'medium aquamarine')
    # def drawTimedFlashCard(self, canvas, app):
    #             canvas.create_rectangle(app.cx*1.5,
    #                             app.cy//4,
    #                             app.cx//4,
    #                             app.cy, 
    #                             fill = 'bisque')

    #             canvas.create_text(app.cx//2, app.cy//5,font = 'Arial',
    # text = f"Kana Level:{app.characterLevel},\nVocab Level:{app.vocabLevel}", 
    #                         fill = 'black')
    #     if app.phase == 'learning':
    #         canvas.create_text(app.cx, app.cy,font = 'Arial',
    #     text = f"Cards Left:{app.cardsToLearn}", fill = 'black')

    #     elif app.phase == 'practice':
    #         canvas.create_text(app.cx//1.5, app.cy,font = 'Arial',
    #                             text = f"Cards Left:{app.cardsToDo}", 
    #                             fill = 'medium aquamarine')
    #     #Hiragana
    #     if app.hiraganaOrVocab == 1:
    #             if app.isFlipped == False:
    #                 #Exact Placement to be changed
    #                 #The Hiragana Character
    #                 canvas.create_text(app.cx,app.cy//2,
    #                                 font = 'Arial',
    #                                 text = f"{self.frontText}", 
    #                                 fill = 'hot pink')
    #             #Back of card
    #             elif app.isFlipped == True:
    #                 romanji = self.backText[0]
    #                 pronunciation = self.backText[1]
    #                 canvas.create_rectangle(app.cx*1.5,
    #                             app.cy//4,
    #                             app.cx//4,
    #                             app.cy, 
    #                             fill = 'olive drab')
    #                 #The Pronunciation of Hiragana Character
    #                 canvas.create_text(app.cx, app.cy//2,font = 'Arial',
    #                             text = f"{romanji}\n{pronunciation}", 
    #                                 fill = 'medium aquamarine')
    #     #Vocabulary
    #     elif app.hiraganaOrVocab == 2:
    #             if app.isFlipped == False:
    #                 #Exact Placement to be changed
    #                 canvas.create_text(app.cx,app.cy//2,
    #                                 font = 'Arial',
    #                                 text = f"{self.frontText}", 
    #                                 fill = 'thistle')
    #             #Back of card
    #             elif app.isFlipped == True:
    #                 if len(self.backText) == 3:
    #                     currRomanji = list(self.backText[0])
    #                     translation1= self.backText[1]
    #                     translation2=self.backText[2]
    #                     currRomanji.insert(7," ")
    #                     currRomanji.insert(10," ")
    #                     threeWordRomanji = ""
    #                     for c in range(len(currRomanji)):
    #                         threeWordRomanji += currRomanji[c]

    #                     canvas.create_rectangle(app.cx*1.5,
    #                             app.cy//4,
    #                             app.cx//4,
    #                             app.cy, 
    #                             fill = 'olive drab')
    #                     canvas.create_text(app.cx, app.cy//2,font = 'Arial',
    #                 text = f"{threeWordRomanji}\n{translation1}{translation2}", 
    #                                 fill = 'medium aquamarine')
    #                 else:
    #                     wordRomanji = self.backText[0]
    #                     translation= self.backText[1]
    #                     canvas.create_rectangle(app.cx*1.5,
    #                                 app.cy//4,
    #                                 app.cx//4,
    #                                 app.cy, 
    #                                 fill = 'olive drab')
    #                     canvas.create_text(app.cx, app.cy//2,font = 'Arial',
    #                                 text = f"{wordRomanji}\n{translation}", 
    #                                     fill = 'medium aquamarine')



    # def getMeaning(self, word):
    #     if word in characterDictionary:
    #         return characterDictionary[word]
    #     elif word in vocabularyDictionary:
    #         return vocabularyDictionary[word]
    #     else:
    #         self.app.showMessage('Sorry, that word is invalid:(')

    #A flip animation
    # def flip(self, app):
    #     if app.isFlipped == True:
    #         self.frontText = self.newFront
    #         self.backText = self.newBack

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
#Problemtime - currTime 
#bot that will hold all the inner processes for learner
class SenseiBot(object):
    def __init__(self,botName, currTime, mood, questionType, targetAnswer):
        self.botName = botName
        self.mood = mood
        self.targetAnswer = targetAnswer
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

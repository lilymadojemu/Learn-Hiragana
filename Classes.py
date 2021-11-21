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
        # canvas.create_image(app.cx*1.5, app.cy, 
        #                     image=ImageTk.PhotoImage(app.image1))
                            
        canvas.create_text(app.cx//3, app.cy//5.5,font = 'Arial',
    text =f"Hiragana Level:{app.characterLevel}\nVocab Level:{app.vocabLevel}", 
                            fill = 'black')
        canvas.create_text(app.cx*1.3, app.cy//6,font = 'Arial',
        text = f"Cards Left:{app.cardsToLearn}", fill = 'black')
        #Hiragana
        if len(self.frontText) == 1:

            print(self.frontText)
            if app.isFlipped == False:
                #Exact Placement to be changed
                #The Hiragana Character
                canvas.create_text(app.cx,app.cy//2,
                                font = 'Arial',
                                text = f"{self.frontText}", 
                                fill = 'hot pink')
            #Back of card
            elif app.isFlipped == True:
                romanji = self.backText[0]
                pronunciation = self.backText[1]
                canvas.create_rectangle(app.cx*1.5,
                            app.cy//4,
                            app.cx//4,
                            app.cy, 
                            fill = 'olive drab')
                #The Pronunciation of Hiragana Character
                canvas.create_text(app.cx, app.cy//2,font = 'Arial',
                            text = f"{romanji}\n{pronunciation}", 
                                fill = 'medium aquamarine')
        #Vocabulary
        elif len(self.frontText) != 1:
                if app.isFlipped == False:
                    #Exact Placement to be changed
                    canvas.create_text(app.cx,app.cy//2,
                                    font = 'Arial',
                                    text = f"{self.frontText}", 
                                    fill = 'thistle')
                #Back of card
                elif app.isFlipped == True:
                    if len(self.backText) == 3:
                        currRomanji = list(self.backText[0])
                        translation1= self.backText[1]
                        translation2=self.backText[2]
                        currRomanji.insert(7," ")
                        currRomanji.insert(10," ")
                        threeWordRomanji = ""
                        for c in range(len(currRomanji)):
                            threeWordRomanji += currRomanji[c]

                        canvas.create_rectangle(app.cx*1.5,
                                app.cy//4,
                                app.cx//4,
                                app.cy, 
                                fill = 'olive drab')
                        canvas.create_text(app.cx, app.cy//2,font = 'Arial',
                    text = f"{threeWordRomanji}\n{translation1}{translation2}", 
                                    fill = 'medium aquamarine')
                    else:
                        wordRomanji = self.backText[0]
                        translation= self.backText[1]
                        canvas.create_rectangle(app.cx*1.5,
                                    app.cy//4,
                                    app.cx//4,
                                    app.cy, 
                                    fill = 'olive drab')
                        canvas.create_text(app.cx, app.cy//2,font = 'Arial',
                                    text = f"{wordRomanji}\n{translation}", 
                                        fill = 'medium aquamarine')

    '''Question1 specific'''
    def drawTimedFlashCard1(self, canvas, app):
        # canvas.create_rectangle(app.cx*1.5,
        #                         app.cy//4,
        #                         app.cx//4,
        #                         app.cy, 
        #                         fill = 'bisque')
        canvas.create_image(app.cx, app.cy, 
                            image=ImageTk.PhotoImage(app.image1))               
        canvas.create_text(app.cx//3.3, app.cy//2,font = 'Arial 15',
    text =f"Hiragana Level:{app.characterLevel}\nVocab Level:{app.vocabLevel}", 
                            fill = 'black')
        canvas.create_text(app.cx*1.5, app.cy//2,font = 'Arial',
                            text = f"Cards Left:{app.cardsToDo}", 
                            fill = 'medium aquamarine')
        canvas.create_text(app.cx//1.5, app.cy*2,font = 'Arial',
                            text = f"Time Limit:{app.baseProblemTime}", 
                            fill = 'sandy brown')
        canvas.create_text(app.cx,app.cy,
                        font = 'Arial',
                        text = f"{self.frontText}", 
                        fill = 'hot pink')

    # def getMeaning(self, word, app):
    #     if word in characterDictionary:
    #         return characterDictionary[word]
    #     elif word in vocabularyDictionary:
    #         return vocabularyDictionary[word]
    #     else:
    #         app.showMessage('Sorry, we don't have that word')

    #A flip animation
    # def flip(self, app):
    #     if app.isFlipped == True:
    #         self.frontText = self.newFront
    #         self.backText = self.newBack
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

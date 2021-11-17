#Classes

'''
Contains all classes that will be used

'''
from Populate_Values import*
import os, random, time
class correctWord(object):
    def __init__(self, correctWord):
        self.correctWord = correctWord

#may not need another class
class incorrectWord(object):
    def __init__(self, incorrectWord):
        self.incorrectWord = incorrectWord

kanaCard = Flashcard(characterDictionary,characterDictionary[key])
vocabCard = Flashcard(vocabularyDictionary, vocabularyDictionary[key])

class FlashCard(object):
    def __init__(self, frontText, backText characterCardCount, vocabCardCount, 
                    app, canvas,):
        self.characterCardCount = characterCardCount
        self.vocabCardCount = vocabCardCount


        self.newFront = backText
        self.newBack = frontText
        self.app = app
        self.canvas = canvas
        self.frontText = frontText
        self.backText = backText
    def drawFlashcard(self):
        self.canvas.create_rectangle(self.app.cx*1.5,
                                self.app.cy//4,
                                self.app.cx//4,
                                self.app.cy, 
                                fill = 'bisque')
        self.canvas.create_text(self.app.cx//1.5,self.app.cy//3,font = 'Arial',
    text = f"KanaLevel:{self.app.characterLevel},{self.app.vocabLevel}", 
                            fill = 'medium aquamarine')
        for key in characterDictionary:
            self.frontText = key
            self.backText = characterDictionary[key]
            self.canvas.create_text(self.app.cx//1.5,self.app.cy//3,
                            font = 'Arial',
                            text = f"{self.frontText}", 
                            fill = 'medium aquamarine')
            self.canvas.create_text(self.app.cx,self.app.cy//3,font = 'Arial',
                            text = f"{self.backText}", 
                            fill = 'medium aquamarine')

    def getMeaning(self, word):
        if word in characterDictionary:
            return characterDictionary[word]
        elif word in vocabularyDictionary:
            return vocabularyDictionary[word]
        else:
            self.app.showMessage('Sorry, that word is invalid:(')
    def flip(self):
        if self.app.isFlipped == True:
            self.frontText = self.newFront
            self.backText = self.newBack




#Character class(base hiragana characters)


# English character class(english equicalents of hiragana)
#Vocabulary Class(base JAPN)


#English Vocabulary subclass

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


Problemtime - currTime 
#bot that will hold all the inner processes for learner
class SenseiBot(object):
    def __init__(self,botName, possibleChoices, targetAnswer, app, currTime):
        self.botName = botName
        self.possibleChoices = possibleChoices
        self.targetAnswer = targetAnswer
        self.app = app
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
        self.app = app
        self.problemTime = 
        pass
'''
Each key-value pair, once answered will be assigned an initial time and a time
where they should go back into circulation based on whether correct or not and
how many times it is deemed correct or not

I will ultimately need to create a formula that will determine the timings for
each card/question
'''

#Base: what to do with values that are correct
#Practice Phase
class AssignedTime(object):
    def __init__(self):
        pass
#What to do with vocab & characters that are incorrect
class IncorrectAssignedTime(AssignedTime):
    pass

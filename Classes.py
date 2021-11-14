#Classes

'''
Contains all classes that will be used

'''
import os, random

class FlashCard(object):
    def __init__(self, app, canvas):
        pass
    # def drawFlashcard(self,app,canvas):
    #     canvas.create_rectangle(app.width-100,app.height//4, app.width-20,
    #                                 app.height//4+35, fill = 'white')
    #     #canvas.create_text(f'{app.characterLevel}, {app.vocabLevel}')  
    
    # def flashcard_redrawAll(self, app, canvas):
    #     drawFlashcard(self,app,canvas)

#Information regarding the choices a user will be able to select for each prob.
class answerChoices(object):
    #Possible choices is either a dictionary or a list, most likely a dictionary
    def __init__(self,possibleChoices):
        pass
    def vocabChoices(self,selectedWord):
        pass
    def characterChoices(self,selectedWord):
        pass
    pass
#Character class(base hiragana characters)


# English character class(english equicalents of hiragana)
#Vocabulary Class(base JAPN)


#English Vocabulary subclass


#bot that will hold all the inner processes for learner
class SenseiBot(object):
    def __init__(self,botName):
        pass

    #Determines whether or not an answer is correct or not,
    #If correct, bot will say "correct!"
    #otherwise, bot will say "incorrect!"
    #Might become its own function
    def isCorrect(self):
        pass

    #How long user has to select/input answer
    #Should time vary depending on if already known or not
    #If varies, need to be based on Assigned time
    def InternalProblemTimer(self,time):
        pass

#Each key-value pair, once answered will be assigned an initial time and a time
#where they should go back into circulation based on whether correct or not and
#how many times it is deemed correct or not

#Base: what to do with values that are correct
class AssignedTime(object):
    def __init__(self):
        pass
#What to do with vocab & characters that are incorrect
class IncorrectAssignedTime(AssignedTime):
    pass

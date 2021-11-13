#Classes

'''
Contains all classes that will be used

Thoughts:
can create a dictionary from textfile, using a very large dict though :(
No direcr try again feature, the incorrecr word will just be added to some bank
keeping track of what words were right and wrong and will output them later 
according to that
No separate review phase (for now)


'''
import os, random

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

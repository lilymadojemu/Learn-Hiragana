#Populate Values

'''
Where I will dynamically populate word and character values
Special case with を
'''
import os, re
#https://www.cs.cmu.edu/~112/notes/notes-strings.html
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

strings = []
with open("Hiragana, romanji, Phonetic Equivalent text file.txt", "r", 
encoding = "utf8") as f:
    for line in f:
        print(line)
        strings.append(line)



# characterRead = 
# #readFile("Hiragana, romanji, Phonetic Equivalent text file.txt")
# vocabRead = readFile("Hiragana Vocabulary, Romanji, Translation.txt")
# def getCharacterDictionary(characterRead):
#     characterDictionary = dict(characterRead)
#     vocabDictionary = dict(vocabRead)

# print(characterRead)
# #Getting Hiragana & romanji

# vocabualryDictionary = dict()
#Getting JAPN Vocab & Romanji
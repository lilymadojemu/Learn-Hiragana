#Populate Values

'''
Where I will dynamically populate word and character values
Special case with を
'''
import os

characterDictionary = dict()
vocabularyDictionary = dict()
#from https://www.cs.cmu.edu/~112/notes/notes-strings.html
def readFile(path):
    with open(path, "rt") as f:
        return f.read()
hiraganaList = []
#Adapted from: https://www.youtube.com/watch?v=oEbNWXhS_mk
#Opens the text file pertaining to Hiragana characters
with open("Hiragana, romanji, Phonetic Equivalent text file.txt", "r", 
encoding = "utf8") as f:
    characterInfo = set()
    for line in f:
        characterLines = line
        strippedCharacters = characterLines.strip('\n')
        hiraganaList.append(strippedCharacters[0])
        for character in hiraganaList:
            #Duplicate values in characterInfo
            look = strippedCharacters[2:]
            characterInfo.add(look)
    characterInformation = list(characterInfo)
    print(characterInformation)
character_dict = dict(zip(hiraganaList, characterInfo))
print(character_dict)


#Opens text file pertaining to Vocabulary
# with open("Hiragana Vocabulary, Romanji, Translation.txt", "r", 
# encoding = "utf8") as f:
#     romanjiTransList = []
#     for line in f:
#         vocabLines = line
#         print(vocabLines)
        



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
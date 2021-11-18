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
    kanaInfo = []
    for line in f:
        characterLines = line
        strippedCharacters = characterLines.strip('\n')
        hiraganaList.append(strippedCharacters[0])
        for kana in hiraganaList:
            #Romanji and Pronunciation
            romaPronun = strippedCharacters[2:]
            if romaPronun not in kanaInfo:
                kanaInfo.append(romaPronun)
character_dict = dict(zip(hiraganaList, kanaInfo))

#Need to Fix
vocabList = []
#Opens text file pertaining to Vocabulary
with open("Hiragana Vocabulary, Romanji, Translation.txt", "r", 
encoding = "utf8") as f:
    vocabInfo = []
    for line in f:
        vocabLines = line
        strippedVocab = vocabLines.strip('\n')
        stripList = list(strippedVocab)
        for i in range(len(stripList)):
            print(i)
            character = strippedVocab[i] 
            print(character)
            if character in hiraganaList:
                vocabList.append(character)
                print(vocabList)
            elif character not in hiraganaList:
                  vocabInfo.append(character)

            #Romanji and Pronunciation
vocabulary_dict = dict(zip(vocabList, vocabInfo))
print(vocabulary_dict)


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
'''
Where I will dynamically populate word and character values
Special case with を

#When showing on card, need to look out for this
print(vocabulary_dict['せんたくをする'])

Finished
'''
#Opens the text file pertaining to Hiragana characters
hiraganaList = []
#Adapted from: https://www.youtube.com/watch?v=oEbNWXhS_mk
with open("Hiragana, romanji, Phonetic Equivalent text file.txt", "r", 
encoding = "utf8") as f:
    kanaInfo = []
    for line in f:
        characterLines = line
        strippedCharacters = characterLines.strip('\n')
        spacedCharacters = strippedCharacters.split()
        hiraganaList.append(strippedCharacters[0])
        for kana in hiraganaList:
            #Romanji and Pronunciation
            romaPronun = spacedCharacters[1:]
            if romaPronun not in kanaInfo:
                kanaInfo.append(romaPronun)
character_dict = dict(zip(hiraganaList, kanaInfo))

#Opens text file pertaining to Vocabulary
vocabList = []
with open("Hiragana Vocabulary, Romanji, Translation.txt", "r", 
encoding = "utf8") as f:
    vocabInfo = []
    for line in f:
        vocabLines = line
        strippedVocab = vocabLines.strip('\n')
        spacedVocab = strippedVocab.split()
        vocabList.append(spacedVocab[0])
        for word in vocabList:
            vocabPronun = spacedVocab[1:]
            if vocabPronun not in vocabInfo:
                vocabInfo.append(vocabPronun)
vocabulary_dict = dict(zip(vocabList, vocabInfo))

overall_dict= character_dict|vocabulary_dict
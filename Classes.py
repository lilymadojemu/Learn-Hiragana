'''
Contains FlashCard Class To Draw A Flashcard
'''
from Populate_Values import*
from cmu_112_graphics import*

class FlashCard(object):
    def __init__(self, frontText, backText):
        self.frontText = frontText
        self.backText = backText

    def drawFlashCard(self, canvas, app):
        canvas.create_text(app.cx//3, app.cy//5.5,font =('Arial','15','bold'),
    text =f"Hiragana Level:{app.characterLevel}\nVocab Level:{app.vocabLevel}", 
                            fill = "ghost white")
        canvas.create_text(app.cx*1.3, app.cy//6, font =('Arial','15','bold'),
        text = f"Cards Left:{app.cardsToLearn}", fill = "ghost white")
        #Hiragana
        if self.frontText in hiraganaList:
            if app.isFlipped == False:
                canvas.create_image(app.cx, app.cy, 
                            image=ImageTk.PhotoImage(app.image1))   
                #The Hiragana Character
                canvas.create_text(app.cx,app.cy,
                                font = 'Arial 20',
                                text = f"{self.frontText}", 
                                fill = 'dark orchid')
            #Back of card
            elif app.isFlipped == True:
                canvas.create_image(app.cx, app.cy, 
                            image=ImageTk.PhotoImage(app.image2))       
                romanji = self.backText[0]
                pronunciation = self.backText[1]    
                canvas.create_text(app.cx,app.cy,
                                        font =('Helvetica','20','bold')
                    , text = f"{romanji}\n as in {pronunciation}", 
                    fill = 'medium aquamarine')
        #Vocabulary
        elif self.frontText in vocabList:
                if app.isFlipped == False:
                    canvas.create_image(app.cx, app.cy, 
                            image=ImageTk.PhotoImage(app.image1))
                    canvas.create_text(app.cx,app.cy,
                                font = 'Arial 20',
                                text = f"{self.frontText}", 
                                fill = 'dark orchid')
                #Back of card
                elif app.isFlipped == True:
                    canvas.create_image(app.cx, app.cy, 
                            image=ImageTk.PhotoImage(app.image2)) 
                    if len(self.backText) == 3:
                        currRomanji = list(self.backText[0])
                        translation1= self.backText[1]
                        translation2=self.backText[2]
                        currRomanji.insert(7," ")
                        currRomanji.insert(10," ")
                        threeWordRomanji = ""
                        for c in range(len(currRomanji)):
                            threeWordRomanji += currRomanji[c]
                        canvas.create_text(app.cx,app.cy,
                            font = 'Arial',
                    text = f"{threeWordRomanji}\n{translation1}{translation2}", 
                                        fill = 'medium aquamarine')
                    else:
                        wordRomanji = self.backText[0]
                        translation= self.backText[1]
                        canvas.create_text(app.cx,app.cy,
                            font = 'Arial',
                                    text = f"{wordRomanji}\n{translation}", 
                                            fill = 'medium aquamarine')

    '''Question Type 1 specific'''
    def drawTimedFlashCard1(self, canvas, app):
        canvas.create_image(app.cx, app.cy, 
                            image=ImageTk.PhotoImage(app.image1))  
        if app.phase == 'practice' and app.lightMode == True:             
            canvas.create_text(app.cx//3.3, app.cy//2,font =('Arial','15','bold'),
        text =f"Hiragana Level:{app.characterLevel}\nVocab Level:{app.vocabLevel}", 
                                fill = 'dark slate blue')
            canvas.create_text(app.cx*1.5, app.cy//2,font =('Arial','15','bold'),
                            text = f"Time Limit:{app.baseProblemTime}", 
                            fill = 'dark slate blue')
        elif app.phase == 'practice' and app.darkMode == True:             
            canvas.create_text(app.cx//3.3, app.cy//2,font =('Arial','15','bold'),
        text =f"Hiragana Level:{app.characterLevel}\nVocab Level:{app.vocabLevel}", 
                                fill = 'firebrick4')
            canvas.create_text(app.cx*1.5, app.cy//2,font =('Arial','15','bold'),
                            text = f"Time Limit:{app.baseProblemTime}", 
                            fill = 'firebrick4')
        elif app.phase == 'review' and app.lightMode == True:
            canvas.create_text(app.cx, app.cy//2,font =('Arial','15','bold'),
                            text = f"Time Limit:{app.baseProblemTime}", 
                            fill = 'dark slate blue')
        elif app.phase == 'review' and app.darkMode == True:
            canvas.create_text(app.cx, app.cy//2,font =('Arial','15','bold'),
                            text = f"Time Limit:{app.baseProblemTime}", 
                            fill = 'ghost white')
        canvas.create_text(app.cx,app.cy,
                        font = 'Arial 20',
                        text = f"{self.frontText}", 
                        fill = 'dark orchid')
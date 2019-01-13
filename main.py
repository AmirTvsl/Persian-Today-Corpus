# This is cross-platform corpus analysis application
'''
Courtesy of Persian Today Corpus by Amir H. Tavassolinia
more information and issues : amirtvsl@outlook.com
'''
import kivy
import re

from collections import Counter

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# my app
class MyApp(App):
# layout
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text="Analyze",pos=(200, 200),size_hint = (.1
                                                                 ,.2))
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)

        btn2 = Button(text="Collocation",pos=(200, 200),size_hint = (.1
                                                                 ,.2))
        btn2.bind(on_press=self.buttonClicked2)
        layout.add_widget(btn2)




        
        self.lbl1 = Label(text="This is Corpus Analysis Tool Developed by Amir H. Tavassolinia \n \n   #### BETA VERSION FOR TESTING PURPOSES ONLY #### \n \n \n                    Paste your corpus below & hit Analyze \n to use collocation, type the desired word first and then paste the text")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=True)
        matn = self.txt1.text
        kalame = matn.split()
        layout.add_widget(self.txt1)
        return layout

# button click function
    def buttonClicked2(self,btn2):
        matn = self.txt1.text
        colist = matn.split()
        tedad = int(len(colist))
        
        collocation = []
        show = []
        for i in range(tedad):
    
            word = colist[i]
            avalin = colist[0]
            
            if word == avalin:
                collocation.append(i)
                
            else:
                pass
 

        for w in collocation:
            if w >= 1:
                try:
                    show.append(str(colist[w-1]) + ' ' + str(avalin) + ' ' + str(colist[w+1]))
                except:
                    pass
            
        
        self.lbl1.text = str("\n".join(show))



    def buttonClicked(self,btn):
        matn = self.txt1.text
        kalame = matn.split()
        counter = Counter(kalame) 
        types = set(kalame)
        character = int(len(matn))
        spaces = int(matn.count(' '))

        stop_words = ['some', "hasn't", 'she', "hadn't", 'have', 'do', 'by', 'through', 'both', 't', 'haven', 'other', 'aren', 'again', 'these', 'yourselves', 'for', "should've", 'not', 's', 'being', 'all', 'doesn', 'on', 'them', 'an', 'so', "don't", 'ours', 'were', 'doing', 'down', 'i', 'off', 'don', 'above', 'what', 'than', "haven't", 'below', 'mustn', 'does', 'after', 'and', 'a', 'we', 'ourselves', 'while', 'yours', 'shan', 'nor', 'those', 'that', 'from', 'd', 'about', "won't", 'until', 'mightn', 'out', 'just', 'm', 'themselves', 'are', 'my', 'but', 'such', 'into', 'this', 'ain', 'or', 'more', 'll', 'should', 've', 'the', 'been', "shouldn't", 'at', 'whom', 'it', "didn't", 'over', 'then', 'further', 'before', 'myself', 'itself', 'with', "mightn't", 'against', 'which', "couldn't", 'didn', 'ma', 'needn', 'too', "wasn't", 'her', 'weren', 'will', 'wasn', 'himself', 'theirs', 'has', 'to', 'herself', 'there', 'own', 'if', 'same', 'shouldn', 'you', 'be', 're', 'your', 'did', "isn't", 'he', 'their', 'very', 'why', 'wouldn', "mustn't", 'because', 'here', 'having', 'who', 'hadn', 'was', "shan't", "you've", "it's", 'where', 'how', 'had', 'each', 'hers', "doesn't", 'most', 'once', 'isn', 'under', 'only', 'they', 'me', 'o', "weren't", "you'd", 'few', "needn't", 'between', 'hasn', "wouldn't", "she's", 'now', 'is', 'our', "you'll", 'him', 'its', "you're", 'in', "that'll", 'can', 'any', 'of', 'am', 'when', 'his', 'no', 'during', 'up', 'won', 'couldn', 'as', "aren't", 'yourself', 'y']
        stop_word = set(stop_words)
        filtered_sentence = []

        for i in kalame:
            if i in stop_word:
                filtered_sentence.append(i)
        keywords = []
        for i in kalame:
            if i not in stop_word:
                keywords.append(i)
        
        countkeywords = Counter(keywords)
        keywordsoccur = countkeywords.most_common(5)


        most_occur = counter.most_common(5) 


        
        self.lbl1.text = 'Characters : ' + str(character-spaces) + "\n Words :  " + str(len(kalame)) + '\n Stop Words : ' + str(len(filtered_sentence)) + '\n Sentences : ' + str(len(re.split('[\.\?!]', matn))) + '\n Types : ' + str(len(types)) + "\n Tokens :  " + str(len(kalame)) + '\n Lexical Densitiy : ' + '%' + str((float(len(types))) / (float(len(kalame)))*100)  + '\n Keywords : ' + str(keywordsoccur) + '\n Frequent : ' + str(most_occur)

# run app
if __name__ == "__main__":
    MyApp().run()
 # join all items in a list into 1 big string

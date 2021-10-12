#pip install googletrans

from googletrans import Translator, LANGUAGES

class Mytranslator:
    def__init__(self)
    self.lang = list(LANGUAGES.VALUES())
    def run( self,txt='Type text here',src'english',dest='hindi'):
            self.tarnslator= Translator()
            self.txt = txt
            self.src = srd
            self.dest = dest
            try:
                self.translated = self.translator.translate(self.txt,
                                                            src = self.src,
                                                            dest = self.dest)
            except:
                self.translated = self.translator.translate(self.txt)
                self.ttext = self.translated.text
                return self.ttext
    

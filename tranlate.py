from tkinter import *
from tkinter import ttk
from main import Mytranslator
import googletrans
app =Tk()
app.geometry('350x520')
app.title('Translater')
app.resizable(0,0)
app.config(bg='ghost white')

def get():
    s = srcLangs.get()
    d = destLangs.get()
    messaage = sourceText.get(1.0,END)
    translator = Mytranslator
    text = translator.run(txt=message,sec=s, dest=d)
    destText.delete(1.0,END)
    destText.insert(END,text)

appName = Label(app,text='Language Translator',font=('arial',20),
                 bg='darkblue',fg='white',height=2)
appName.pack(side=TOP,fill=BOTH,pady=0)
version =Label(app, text='beta',bg='darkblue',fg='white') .place(x=280,y=45)
frame = Frame(app).pack(side=BOTTOM)
sourceText = Text(frame, font=('arial',10),height=11,wrap=WORD)
sourceText.pack(side=TOP,padx=5,pady=5)

transBtn = Button(frame, text='Translate',font=('arial',10,'bold'),
                  fg='black',bg='white',activebackground='green',relief=GROOVE, command=get)
transBtn.pack(side=TOP,pady=15)
langs = Mytranslator().langs

secLangs = ttk.Combobox(frame,values=langs,width=10)
secLangs.place(x=30,y=280)
secLangs.set('English')

desLangs = ttk.Combobox(frame,values=langs,width=10)
desLangs.place(x=240,y=280)
desLangs.set('Hindi')

destText = Text(frame, font=('arial',10),height=11,wrap=WORD)
destText.pack(side=TOP,padx=5,pady=5)


app.mainloop()               
               
               

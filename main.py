from tkinter import *#wildcard cause its a lot of code
from tkinter import ttk
from googletrans import Translator, LANGUAGES
#Very tricky terminology- i had to install a special experimental version of googletrans(3.1.0a0) in order to run this code in tkinter
# as i kept getting nonetype attribute errors without it.
#https://projectgurukul.org/python-language-translator/ found it in the comments section of this project- where someone had an issue
# and needed a fix, and found that 3.1.0a0 was the fix.
root = Tk()
root.geometry('400x400')
root.resizable(False,False)
root.config(bg='#2d2d30')
root.title("Compact Translator GUI")
Label(root,bg='#252526',height=21,width=40).grid(row=1, column=0,columnspan=2,rowspan=4)
Label(root, text="Python Translator", font='Helvetica 40 bold',fg='#007acc',bg='#2d2d30').grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
Input_text = Text(root, font='Helvetica 15', height=11, wrap=WORD, padx=5, pady=5, width=38)
Input_text.grid(row=1, column=0, padx=20, pady=5)
language = list(LANGUAGES.values())#accessing languages list from googletrans
dest_lang = ttk.Combobox(root, values=language, width=22,background='#3e3e42',foreground='#007acc',font='Helvetica 20 bold')
dest_lang.grid(row=2, column=0, padx=20, pady=10)
dest_lang.set('Output Language')
def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(1.0, END), src='auto', dest=dest_lang.get())
    Input_text.delete(1.0, END)
    Input_text.insert(END, translated.text)
trans_btn = Button(root, width=20,height=2 ,cursor="exchange",text='Translate(CLICK)', font='helvetica 20 bold', padx=5,pady=3, command=Translate,bg='black',fg='#007acc')
#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html - found cool cursors here
trans_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()

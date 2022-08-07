from tkinter import *
from PyDictionary import PyDictionary
w=Tk()
w.geometry("400x400")
w.title("Dictionary")

def findmean():
    # word=entry.get()
    # dict=PyDictionary(word)
    # mean=dict.printMeanings()
    # wo=mean.get()
    l = Label(w, text=PyDictionary.meaning(entry.get()),wraplength=390)
    l.pack()


entry=Entry(w,font=("times",30,'bold'))
entry.pack()
B1=Button(w,text='Find Meaning',font=("Times",10,'bold'),command=findmean)
B1.pack()

w.mainloop()

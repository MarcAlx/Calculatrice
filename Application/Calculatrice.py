# -*- coding: utf-8 -*-
# Crée par Marc-Alexandre Blanchard
from tkinter import *

class Application(object):
    """ classe application """

    res = 0
    actualOp = '='

    def operation(self,s):
        global res,actualOp
        self.actualOp,self.res = s,self.screen.get(1.0,END)
        self.delW()

    def equal(self):
        if(self.actualOp=='+'):
            self.res = float(self.res)+float(self.screen.get(1.0,END))
        elif (self.actualOp=='-'):
            self.res = float(self.res)-float(self.screen.get(1.0,END))
        elif (self.actualOp=='*'):
            self.res = float(self.res)*float(self.screen.get(1.0,END))
        elif (self.actualOp=='/'):
            if(float(self.screen.get(1.0,END))!=0):
                self.res = float(self.res)/float(self.screen.get(1.0,END))
            else:
                self.res=''
        self.delW()
        if (self.actualOp!='='):
            self.printW(self.res)
        self.actualOp='='
        
    def printW(self,chaine):
        if(not '.' in self.screen.get(1.0,END) or chaine!='.'):
            self.screen.config(state=NORMAL)
            self.screen.insert(END,chaine)
            self.screen.config(state=DISABLED)
        
    def delW(self):
        self.screen.config(state=NORMAL)
        self.screen.delete(1.0, END)
        self.screen.config(state=DISABLED)
    
    def __init__(self):
            self._tk = Tk()
            self._tk.title("Calculatrice")
            self._tk.resizable(width=False, height=False)
            
            self.screen = Text(self._tk, height=1, width=12,background = 'blue',font = "Ar")
            self.screen.config(state=DISABLED)
            self.screen.pack(fill=X)

            
            self.conteneurBouton1 = Frame(self._tk)
            self.bouton1 = Button(self.conteneurBouton1,text='1', command=lambda n='1': self.printW(n))
            self.bouton1.pack(side = LEFT)
            self.bouton2 = Button(self.conteneurBouton1,text='2', command=lambda n='2': self.printW(n))
            self.bouton2.pack(side = LEFT)
            self.bouton3 = Button(self.conteneurBouton1,text='3', command=lambda n='3': self.printW(n))
            self.bouton3.pack(side = LEFT)
            self.boutonP = Button(self.conteneurBouton1,text='+', command=lambda s='+': self.operation(s))
            self.boutonP.pack(side = LEFT)
            self.conteneurBouton1.pack()

            self.conteneurBouton2 = Frame(self._tk)
            self.bouton4 = Button(self.conteneurBouton2,text='4', command=lambda n='4': self.printW(n))
            self.bouton4.pack(side = LEFT)
            self.bouton5 = Button(self.conteneurBouton2,text='5', command=lambda n='5': self.printW(n))
            self.bouton5.pack(side = LEFT)
            self.bouton6 = Button(self.conteneurBouton2,text='6', command=lambda n='6': self.printW(n))
            self.bouton6.pack(side = LEFT)
            self.boutonM = Button(self.conteneurBouton2,text='-', command=lambda s='-': self.operation(s))
            self.boutonM.pack(side = LEFT)
            self.conteneurBouton2.pack()

            self.conteneurBouton3 = Frame(self._tk)
            self.bouton7 = Button(self.conteneurBouton3,text='7', command=lambda n='7': self.printW(n))
            self.bouton7.pack(side = LEFT)
            self.bouton8 = Button(self.conteneurBouton3,text='8', command=lambda n='8': self.printW(n))
            self.bouton8.pack(side = LEFT)
            self.bouton9 = Button(self.conteneurBouton3,text='9', command=lambda n='9': self.printW(n))
            self.bouton9.pack(side = LEFT)
            self.boutonF = Button(self.conteneurBouton3,text='*', command=lambda s='*': self.operation(s))
            self.boutonF.pack(side = LEFT)
            self.conteneurBouton3.pack()

            self.conteneurBouton4 = Frame(self._tk)
            self.bouton0 = Button(self.conteneurBouton4,text='0', command=lambda n='0': self.printW(n))
            self.bouton0.pack(side = LEFT)
            self.boutonV = Button(self.conteneurBouton4,text=',', command=lambda p='.': self.printW(p))
            self.boutonV.pack(side = LEFT)
            self.boutonE = Button(self.conteneurBouton4,text='=', command=self.equal)
            self.boutonE.pack(side = LEFT)
            self.boutonD = Button(self.conteneurBouton4,text='/', command=lambda s='/': self.operation(s))
            self.boutonD.pack(side = LEFT)
            self.conteneurBouton4.pack()

    def mainloop(self):
        self._tk.mainloop()

if __name__ == '__main__':
    Application().mainloop()

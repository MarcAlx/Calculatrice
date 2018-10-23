# -*- coding: utf-8 -*-
# Crée par Marc-Alexandre Blanchard
from tkinter import *
val = ['1','2','3','+','4','5','6','-','7','8','9','*','0','.','=','/','=',0]
def operation(s):
    val[16],val[17] = s,screen.get(1.0,END);screen.config(state=NORMAL);screen.delete(1.0, END);screen.config(state=DISABLED) 
def equal():
    val[17] = float(val[17])+float(screen.get(1.0,END)) if(val[16]=='+') else val[17];val[17] = float(val[17])-float(screen.get(1.0,END)) if(val[16]=='-') else val[17];val[17] = float(val[17])*float(screen.get(1.0,END)) if(val[16]=='*') else val[17];val[17] = (float(val[17])/float(screen.get(1.0,END)) if(float(screen.get(1.0,END))!=0) else '') if (val[16]=='/') else val[17];screen.config(state=NORMAL);screen.delete(1.0, END);screen.config(state=DISABLED) 
    if (val[16]!='='):
        printW(val[17]) 
    val[16]='='   
def printW(chaine):
    if(not '.' in screen.get(1.0,END) or chaine!='.'):
        screen.config(state=NORMAL);screen.insert(END,chaine);screen.config(state=DISABLED)
Fenetre = Tk();Fenetre.title("Calculatrice");Fenetre.resizable(width=False, height=False);screen = Text(Fenetre, height=1, width=12,background = 'blue',font = "Ar",state=DISABLED);screen.grid(row=0, column=0,columnspan=4,sticky=W+E)
for i in range(0,4,1):
    for j in range(0,4,1):
        if(val[i*4+j]=='+' or val[i*4+j]=='-' or val[i*4+j]=='*' or val[i*4+j]=='/'):
            Button(Fenetre,text=val[i*4+j], command=lambda s=val[i*4+j]: operation(s)).grid(row=i+1, column=j)
        elif(val[i*4+j]=='='):
            Button(Fenetre,text=val[i*4+j], command=equal).grid(row=i+1, column=j)
        else:
            Button(Fenetre,text=val[i*4+j], command=lambda n=val[i*4+j]: printW(n)).grid(row=i+1, column=j)
Fenetre.mainloop()
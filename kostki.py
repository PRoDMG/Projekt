import tkinter
from tkinter import messagebox
from random import randint
tplyer = 0
tcomp = 0
player = 0
comp = 0
top = tkinter.Tk()
top.resizable(width = False, height =False)
top.geometry("200x100")
def Yes():
   global player
   global comp
   tplayer = randint(1,6)
   tcomp = randint(1,6)
   message =""
   if tplayer>tcomp:
      message = "Wygrales!"
      player+=1
   elif tplayer==tcomp:
      message = "Remis"
   else:
      message = "Przegrales"
      comp +=1
   messagebox.showinfo( "Wynik", "Gracz: "+str(player)+"     Komputer: "+str(comp)+"\nTwoj rzut "+str(tplayer)+"\n"+"Przeciwnik wyrzucil "+str(tcomp)+"\n"+message)
def No():
   messagebox.showinfo("Do zobaczenia")
   top.quit()
w = tkinter.Label(top,text = "Zagramy w kosci?\n")
B1 = tkinter.Button(top, text ="Tak", command = Yes,width = 10)
B2 = tkinter.Button(top, text = "Nie", command = No,width = 10)
w.grid(row = 0,column = 0)
B1.grid(row = 1, column = 0)
B2.grid(row = 1, column = 1)
top.mainloop()

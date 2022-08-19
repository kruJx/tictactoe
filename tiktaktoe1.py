import os
from tkinter import *
root = Tk()
root.title("TicTacToe")
root.geometry("400x300")

global list1
list1=[0,0,0,0,0,0,0,0,0]
global turn
turn=0
gameon=True

class btn:
    def test(self,x,y,j):
        def click():
            global gameon
            if gameon:
                global turn
                global list1
                if turn==0:
                    turn+=1
                    self.click=1
                    self.cl="X"
                    list1[j]=1
                elif turn==1:
                    turn=0
                    self.click=2
                    self.cl="O"
                    list1[j]=2
                self.config(text="{}".format(self.cl))
                if list1[0]==1 and list1[1]==1 and list1[2]==1 or list1[0]==1 and list1[4]==1 and list1[8]==1 or list1[3]==1 and list1[4]==1 and list1[5]==1 or list1[6]==1 and list1[7]==1 and list1[8]==1 or list1[0]==1 and list1[3]==1 and list1[6]==1 or list1[1]==1 and list1[4]==1 and list1[7]==1 or list1[2]==1 and list1[5]==1 and list1[8]==1 or list1[2]==1 and list1[4]==1 and list1[6]==1:
                    p = StringVar()
                    p.set("X's win")
                    winmes(p)
                    playagain()
                    gameon=False
                elif list1[0]==2 and list1[1]==2 and list1[2]==2 or list1[0]==2 and list1[4]==2 and list1[8]==2 or list1[3]==2 and list1[4]==2 and list1[5]==2 or list1[6]==2 and list1[7]==2 and list1[8]==2 or list1[0]==2 and list1[3]==2 and list1[6]==2 or list1[1]==2 and list1[4]==2 and list1[7]==2 or list1[2]==2 and list1[5]==2 and list1[8]==2 or list1[2]==2 and list1[4]==2 and list1[6]==2:
                    p = StringVar()
                    p.set("O's win")
                    winmes(p)
                    playagain()
                    gameon=False
                else:
                    try:
                        list1.index(0)
                    except:
                        gameon=False
                        p = StringVar()
                        p.set("Draw")
                        winmes(p)
                        playagain()
                self.config(state=DISABLED)
        self=Button(text=" ", background="#555", foreground="#ccc", padx=20, pady=8, font="Verdana 13", command=click)
        self.place(relx=x, rely=y)

btn1=btn()
btn2=btn()
btn3=btn()
btn4=btn()
btn5=btn()
btn6=btn()
btn7=btn()
btn8=btn()
btn9=btn()

def winmes(p):
    message=Message(root,textvariable=p)
    message.pack(side=BOTTOM)
        
def playbtns():
    btn1.test(0.10,0.05,0)
    btn2.test(0.43,0.05,1)
    btn3.test(0.76,0.05,2)
    btn4.test(0.10,0.35,3)
    btn5.test(0.43,0.35,4)
    btn6.test(0.76,0.35,5)
    btn7.test(0.10,0.65,6)
    btn8.test(0.43,0.65,7)
    btn9.test(0.76,0.65,8)

def playplay():
    play.place_forget()
    playbtns()
    global gameon
    gameon = True

def playagain():
    def plag():
        for widgets in root.winfo_children():
            widgets.place_forget()
            widgets.forget()
        play.place(relx=0.33, rely=0.33)
        global list1
        list1=[0,0,0,0,0,0,0,0,0]
    again=Button(text="Играть еще раз", command=plag)
    again.place(relx=0.05, rely=0.90)
                
play=Button(text="Играть", background="#555", foreground="#ccc", padx=20, pady=8, font="Verdana 24", command=playplay)
play.place(relx=0.33, rely=0.33)


root.mainloop()



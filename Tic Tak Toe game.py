from tkinter import *
import tkinter.messagebox as mb
a=[0]*8
b=[0]*8
counter=0
flag=False
def main2(window,e1,e2):
    window.destroy()
    root = Tk()
    #root.attributes('-fullscreen',True)
    root.geometry("850x600")
    root.title("TicTacToe")
    root.configure(bg="black")
    root.state('zoomed')
   # root.resizable(0,0)
    def command1(r,c,btn):
        global a
        global b
        global counter
        if counter%2==0:
            player=a
            btn.configure(text='X')
        else:
            player=b
            btn.configure(text='0')
        if r==c:
            player[6]+=1
        if r+c==2:
            player[7]+=1
        player[r]+=1
        player[c+3]+=1
        if max(a)==3:
            mb.showinfo("Winner","Player {} is winner".format(e1))
            flag=True
            root.destroy()
        elif max(b)==3:
            mb.showinfo("Winner","Player {} is winner".format(e2))
            flag=True
            root.destroy()
        if counter==8 and flag!=True:
            mb.showinfo("Draw","Match Draw")
            root.destroy()

        counter+=1
     
    f1 = Frame(root, width="830", height="580", bg="Sky blue").grid(row=0, column=0, rowspan=5, columnspan=5, padx=10,
                                                                        pady=10)
    Label(f1, text="{} V/S {}".format(e1,e2),font=("Times New Roman", 30, "bold italic"), bg="Sky blue").grid(row=0,column=1,columnspan=3)
                                                                                                              
                                                                                                                   
    f2 = Frame(root, width="565", height="515", bg="black",highlightthickness = 5).grid(row=1, column=1, rowspan=3, columnspan=3)

    b1 = Button(f2, text="", borderwidth=0,font=("arial",25,"bold"), command=lambda :command1(0,0,b1),activebackground='black')
    b1.grid(row=1, column=1, sticky="nsew", padx = 2, pady = 2)
    b2 = Button(f2, text="", borderwidth=0 ,font=("arial",25,"bold"),command=lambda :command1(0,1,b2),activebackground='black')
    b2.grid(row=1, column=2, sticky="nsew", padx = 2, pady = 2)
    b3 = Button(f2, text="", borderwidth=0,font=("arial",25,"bold"), command=lambda :command1(0,2,b3),activebackground='black')
    b3.grid(row=1, column=3, sticky="nsew", padx = 2, pady = 2)
    b4 = Button(f2, text="", borderwidth=0,font=("arial",25,"bold"), command=lambda :command1(1,0,b4),activebackground='black')
    b4.grid(row=2, column=1, sticky="nsew", padx = 2, pady = 2)
    b5 = Button(f2, text="", borderwidth=0,font=("arial",25,"bold"), command=lambda :command1(1,1,b5),activebackground='black')
    b5.grid(row=2, column=2, sticky="nsew", padx = 2, pady = 2)
    b6 = Button(f2, text="", borderwidth=0,font=("arial",25,"bold"), command=lambda :command1(1,2,b6),activebackground='black')
    b6.grid(row=2, column=3, sticky="nsew", padx = 2, pady = 2)
    b7 = Button(f2, text="", borderwidth=0,font=("arial",25,"bold"), command=lambda :command1(2,0,b7),activebackground='black')
    b7.grid(row=3, column=1, sticky="nsew", padx = 2, pady = 2)
    b8 = Button(f2, text="", borderwidth=0,font=("arial",25,"bold"), command=lambda :command1(2,1,b8),activebackground='black')
    b8.grid(row=3, column=2, sticky="nsew", padx = 2, pady = 2)
    b9 = Button(f2, text="", borderwidth=0,font=("arial",25,"bold"), command=lambda :command1(2,2,b9),activebackground='black')
    b9.grid(row=3, column=3, sticky="nsew", padx = 2, pady = 2)
    mainloop()

def main():
    root1 = Tk()
    root1.geometry("850x600")
    root1.title("TicTacToe")
    root1.state('zoomed')
    #root1.resizable(0,0)
    root1.configure(bg="black")
    f12 = Frame(root1, width="830", height="580", bg="Sky blue").grid(row=0, column=0, rowspan=5, columnspan=5, padx=10,                                                                    pady=10)
    Label(f12, text="Welcome To TicTacToe", font=("Times New Roman", 30, "bold italic"), bg="Sky blue").grid(row=0,                                                                                                               column=1,                                                                                                               columnspan=3)
    f22 = Frame(root1, width="515", height="515", bg="black",highlightthickness = 5).grid(row=1, column=1, rowspan=3, columnspan=5)
    Label(f22,text="Enter player 1",font=("Times New Roman",20, "bold italic"),fg='White',bg='Black').grid(row=2,column=2,sticky='nw',padx=70)
    Label(f22,text="Enter player 2",font=("Times New Roman", 20, "bold italic"),fg='white',bg='black').grid(row=3,column=2,sticky='nw',padx=70)
    e1=Entry(f22,bd=5,width=30)
    e1.grid(row=2,column=3,sticky='nw')
    e2=Entry(f22,bd=5,width=30)
    e2.grid(row=3,column=3,sticky='nw')
    btn0=Button(root1,text='Submit',command=lambda: main2(root1,e1.get(),e2.get()),width=20,height=3)
    btn0.grid(row=3,column=2,columnspan=3)
    root1.mainloop()

main()

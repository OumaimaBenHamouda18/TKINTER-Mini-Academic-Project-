from tkinter import *
from tkinter import messagebox
def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)
def somme(A,B):
    Resultat.place_forget()
    s=1
    for i in range(1,A+1):
        s+=B**i
    s=round(s,2)
    ResultLabel.config(text="S   =")
    ResultLabel.place(x=350,y=350)
    ResultValue.config(text=s)
    ResultValue.place(x=420,y=350)




def definir(fen,entrerN,entrerX):
    Resultat.place_forget()
    ResultLabel.place_forget()
    ResultValue.place_forget()
    N=entrerN.get()
    X=entrerX.get()
    msg1=1
    msg2=1
    try:
        N=int(entrerN.get())

    except ValueError:
        msg1=0
    try:
        X=float(entrerX.get())

    except ValueError:
        msg2=0
    if msg1==1 and msg2==1:
        if N>1:
            messagebox.showinfo("Good Job","Les données sont bien saisies !",parent=fen)
            Resultat.config(text="Résultat",command=lambda:somme(N,X))
            Resultat.place(x=380,y=280)
        else:
            messagebox.showerror("Error","Erreur:N doit etre > 1 !",parent=fen)
            entrerN.delete(0, END)
    if msg1==0 and msg2==0:
        entrerN.delete(0, END)
        entrerN.focus()
        entrerX.delete(0, END)
        messagebox.showerror("Error","Erreur:N doit etre un entier !\n X doit etre un réel !",parent=fen)

    if msg1==0 and msg2==1:
        entrerN.delete(0, END)
        entrerN.focus()
        messagebox.showerror("Error","Erreur:N doit etre un entier !",parent=fen)

    if msg1==1 and msg2==0:
        entrerX.delete(0, END)
        entrerX.focus()

        messagebox.showerror("Error","Erreur:X doit etre un réel !",parent=fen)
        
def ex1():
    def Reset():
        entrerN.focus()
        entrerN.delete(0,END)
        entrerX.delete(0,END)
        Resultat.place_forget()
        ResultValue.place_forget()
        ResultLabel.place_forget()
    fen = Toplevel()
    fen.title("Exercice8 : Somme 4")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    label_entier=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 11 bold ",
                    text="Entrer u entier N  :")
    label_entier.place(x=240,y=180)
    entrerN=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=10)
    entrerN.place(x=410,y=180)
    label_X=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 11 bold ",
                    text="Entrer un réel X  :")
    label_X.place(x=240,y=230)
    entrerX=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=10)
    entrerX.place(x=410,y=230)
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=120,bd=0,highlightthickness=0)
    stroke_text(420, 80, "Ce programme permet de calculer S = 1+x+x^2+x^3+...+ +x^N/N\navec N entier positif.",'white', 'green')
    canvas.place(x=20,y=10)
    info_icon=PhotoImage(file='icons\\info_icon.png')
    info_icon_label = Label(fen,
                       image = info_icon,
                       bd=0,
                       bg="black",
                       highlightthickness=0)
    info_icon_label.place(x=40,y=30)
    Definir=Button(fen,
                   fg="white",
                   font="verdana 10 bold italic",
                   text="Définir",
                   bg="#FF00CC",
                   command=lambda:definir(fen,entrerN,entrerX),
                   borderwidth=8,
                   width=8)
    Definir.place(x=380,y=280)
    
    Reset_btn =PhotoImage(file='icons\\reset2.png')
    Reset_label=Label(image=Reset_btn,bg="black")
    Reset=Button(fen,
                 bd=0,
                 activebackground="black",
                 bg="black",
                 highlightthickness = 0,  
                 image=Reset_btn,
                 command=Reset,
                 borderwidth=0 )
    Reset.place(x=480,y=285)
    global ResultLabel
    global ResultValue
    global Resultat

    Resultat=Button(fen,
                    fg="white",
                    font="verdana 10 bold italic",
                    text="Resultat",
                    bg="Blue",
                    borderwidth=8,
                    width=8)
    ResultLabel=Label(fen,text='S =',fg="#32C1F2",bg="black",font="verdana 14 bold  ")
    ResultValue=Label(fen,text='',fg="white",bg="black",font="verdana 14 bold italic")
    
    def quit():
        fen.destroy()
    img2 = PhotoImage(file="icons\\return_icon.png")
    exit_label=Label(image=img2,bg="black")
    Exit=Button(fen,
                 bd=0,
                 activebackground="black",
                 bg="black",
                 highlightthickness = 0,  
                 image=img2,
                 command=quit,
                 borderwidth=0 )
    Exit.place(x=790,y=430)
   
    fen.mainloop()

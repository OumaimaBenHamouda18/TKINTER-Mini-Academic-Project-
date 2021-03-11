from tkinter import *
from tkinter import messagebox
def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)
def Suite(A,B,C):
    Resultat.place_forget()
    res=0
    for i in range(2,A+1):
      res=C+((-1)**i)*B
      B=C
      C=res   
    
    ResultLabel.config(text="U"+str(A)+" =")
    ResultLabel.place(x=350,y=270)
    ResultValue.config(text=res)
    ResultValue.place(x=430,y=270)

def definir(fen,entrerT):
    try:
        T=int(entrerT.get())
        if T>0:
            Resultat.config(text="Résultat",command=lambda:Suite(T,2,3))
            Resultat.place(x=380,y=270)
        else:
            messagebox.showerror("Error","Erreur:N n'est pas\nun entier positif",parent=fen)
            entrerN.delete(0, END)
            entrerN.insert(0, "")
    except ValueError:
            messagebox.showerror("Error","Erreur:N n'est pas\nun entier ",parent=fen)
            entrerN.delete(0, END)
            entrerN.insert(0, "")     
def ex1():
    def Reset():
        entrerT.delete(0,END)
        Resultat.place_forget()
        ResultValue.place_forget()
        ResultLabel.place_forget()
    fen = Toplevel()
    fen.title("Exercice 9")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    label_entier=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 11 bold ",
                    text="Entrer le terme à calculer :")
    label_entier.place(x=150,y=200)
    entrerT=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=10)
    entrerT.place(x=380,y=200)
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=180,bd=0,highlightthickness=0)
    stroke_text(420, 80, "Ce programme permet de calculer un terme donné de la suite Sn\nSn = Sn−1 + (−1)n∗ Sn−2\nS0 = 2\nS1 = 3",'white', 'green')
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
                   command=lambda:definir(fen,entrerT),
                   borderwidth=3 )
    Definir.place(x=510,y=200)
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
    Reset.place(x=600,y=200)
    global ResultLabel
    global ResultValue
    global Resultat

    Resultat=Button(fen,
                    fg="white",
                    font="verdana 10 bold italic",
                    text="Resultat",
                    bg="Blue",
                    borderwidth=8 )
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

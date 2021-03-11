from tkinter import *
from tkinter import messagebox
def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)
def Distinct(A):
    Resultat.place_forget()
    message="est distinct"
    a=str(A)
    for i in range(0,len(a)):
      for j in range(i+1,len(a)):
        if a[i]==a[j]:
            message="n'est pas distinct"
            ResultLabel.config(text=str(A)+' '+message)
            ResultLabel.place(x=320,y=270)
            return 0
    ResultLabel.config(text=str(A)+' '+message)
    ResultLabel.place(x=320,y=270)


def definir(fen,entrerN):
    try:
        N=int(entrerN.get())
        if N>0:
            Resultat.config(text="Résultat",command=lambda:Distinct(N))
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
        entrerN.delete(0,END)
        Resultat.place_forget()
        ResultLabel.place_forget()
    fen = Toplevel()
    fen.title("Exercice 10")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    label_entier=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 11 bold ",
                    text="Entrer N:")
    label_entier.place(x=240,y=200)
    entrerN=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=10)
    entrerN.place(x=350,y=200)
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=180,bd=0,highlightthickness=0)
    stroke_text(420, 80, "Ce programme permet de vérifier si un entier N est distinct ou non.",'white', 'green')
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
                   command=lambda:definir(fen,entrerN),
                   borderwidth=3 )
    Definir.place(x=480,y=200)
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
    Reset.place(x=560,y=200)
    global ResultLabel
    global Resultat

    Resultat=Button(fen,
                    fg="white",
                    font="verdana 10 bold italic",
                    text="Resultat",
                    bg="Blue",
                    borderwidth=8 )
    ResultLabel=Label(fen,text='',fg="#32C1F2",bg="black",font="verdana 14 bold  ")
    
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

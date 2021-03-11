from tkinter import *
from tkinter import messagebox
def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)
def FACT(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f    
def Calcul_Cos (x):
    
    Resultat.place_forget()
    elm1 =1
    elm2 =elm1 -(x **2/2)
    signe=1
    i=2
    while abs (elm2 - elm1 ) >0.0001:
        i +=2
        f=FACT(i)
        elm1 = elm2
        elm2 = elm1 + signe *(x** i /f)
        signe *=( -1)
    elm2=round(elm2,3)
    ResultLabel.config(text="Cos ( "+str(x)+" ) = ")
    ResultLabel.place(x=290,y=300)
    ResultValue.config(text=elm2)
    ResultValue.place(x=430,y=300)



def definir(fen,entrerX):
    Resultat.place_forget()
    ResultLabel.place_forget()
    ResultValue.place_forget()
    try:
        X=float(entrerX.get())
        if (-1<= X  <=1):
            Resultat.config(text="Résultat",command=lambda:Calcul_Cos (X))
            Resultat.place(x=380,y=270)
        else:
            messagebox.showerror("Error","Erreur:X doit etre dans [-1,1] !",parent=fen)
            entrerX.delete(0, END)
            entrerX.insert(0, "")
    except ValueError:
            messagebox.showerror("Error","X doit etre un réel ",parent=fen)
            entrerX.delete(0, END)
            entrerX.insert(0, "") 
        
def ex1():
    def Reset():
        entrerX.delete(0,END)
        Resultat.place_forget()
        ResultValue.place_forget()
        ResultLabel.place_forget()
    fen = Toplevel()
    fen.title("Exercice 3")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    label_chaine=Label(fen,
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="arial 12 bold",
                    text="Entrer X : ")
    label_chaine.place(x=240,y=200)
    entrerX=Entry(fen,
              borderwidth=3,
              bg="white",
              fg="black",
              width=10,
              font="verdana 11 bold italic",
              textvariable=N)
    entrerX.place(x=185,y=160)
    entrerX.place(x=350,y=200)
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=180,bd=0,highlightthickness=0)
    stroke_text(430, 80, "Ce programme permet de determiner la valeur approchée du cos(x)\ncos(x)=1−x^2/2!+x^4/4!− x^6/6!+x^8/8!−...",'white', 'green')
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
                   command=lambda:definir(fen,entrerX),
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

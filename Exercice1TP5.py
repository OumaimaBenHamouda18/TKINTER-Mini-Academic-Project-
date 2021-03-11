from tkinter import *
from tkinter import messagebox
def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)
def Poids(ch):
    Resultat.place_forget()
    dictionnaire ={'A': 1, 'E': 5, 'I': 9, 'O': 15, 'U': 21, 'Y': 25}
    p= 0
    for i in range (0, len(ch)):
        if ch[i] in dictionnaire :
            p+= (i+1)*dictionnaire[ch[i]]
    ResultLabel.config(text=" Poids de la chaine "+'"'+ch+'"'+" = ")
    ResultLabel.place(x=200,y=300)
    ResultValue.config(text=p)
    ResultValue.place(x=570,y=300)




def definir(fen,entrerCH):
    Resultat.place_forget()
    ResultLabel.place_forget()
    ResultValue.place_forget()
    ch=entrerCH.get()
    if ch=='':
        entrerCH.delete(0, END)
        entrerCH.insert(0, "")
        messagebox.showerror("Error","La chaine ch ne doit pas etre vide !",parent=fen)
    elif ch.isalpha()==True and ch.isupper() ==True :
        Resultat.config(text="Résultat",command=lambda:Poids(ch))
        Resultat.place(x=380,y=270)
    else:
        entrerCH.delete(0, END)
        entrerCH.insert(0, "")
        messagebox.showerror("Error","La chaine ch doit etre formée uniquement\npar des lettres majuscules !",parent=fen)
 

        
def ex1():
    def Reset():
        entrerCH.delete(0,END)
        Resultat.place_forget()
        ResultValue.place_forget()
        ResultLabel.place_forget()
    fen = Toplevel()
    fen.title("Exercice 1")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    label_chaine=Label(fen,
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="arial 11 bold",
                    text="Entrer une chaine:")
    label_chaine.place(x=200,y=200)
    entrerCH=Entry(fen,
              borderwidth=3,
              bg="white",
              fg="black",
              width=10,
              font="verdana 11 bold italic",
              textvariable=N)
    entrerCH.place(x=350,y=200)
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=180,bd=0,highlightthickness=0)
    stroke_text(370, 80, "Ce programme permet de calculer le poids d'une chaine.",'white', 'green')
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
                   command=lambda:definir(fen,entrerCH),
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
    entrerCH.delete(0,END)

   
    fen.mainloop()

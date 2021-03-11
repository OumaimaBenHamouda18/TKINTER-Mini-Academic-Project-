from tkinter import *
from tkinter import messagebox
def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)
def maximum(x):
    ch1=str(x)
    ch2=""
    for i in range (len(ch1)):
        ch2=ch2+max(ch1)
        ch1=ch1.replace(max(ch1),"",1)  #une chaine est non modifiable
    x=int(ch2)
    return x


def minimum(x):
    ch1=str(x)
    ch2=""
    for i in range (len(ch1)):
        ch2=ch2+min(ch1)
        ch1=ch1.replace(min(ch1),"",1)  #une chaine est non modifiable
    x=int(ch2)
    return x

def Result(fen):
    L=list()
    L.append(N)
    ListeDeTermes=''
    i=0
    while True :
        ListeDeTermes+=str(L[i])+','
        y=maximum(L[i])-minimum(L[i])
        i=i+1
        if y!=L[i-1] :
            L.append(y) 
        if y==L[i-1] :
            break
    
    Resultat.place_forget()
    ListTerme.place(x=40,y=320)
    ListValue.config(text=ListeDeTermes[:-1])
    ListValue.place(x=320,y=320)
    NB.place(x=40,y=380)
    NBValue.config(text=len(L))
    NBValue.place(x=360,y=380)

    
 

        
def ex1():
    def Reset():
        entrerN.delete(0, END)
        Resultat.place_forget()
        ListTerme.place_forget()
        ListValue.place_forget()
        NB.place_forget()
        NBValue.place_forget()

        
    def definir():
        try:
            global N
            N=int(entrerN.get())
            if ( 1000<=N<=9999):
                Resultat.config(command=lambda:Result(fen))
                Resultat.place(x=380,y=300)
            else:
                entrerN.delete(0, END)
                entrerN.insert(0, "")
                messagebox.showerror("Error","N doit etre formé de 4 chiffre",parent=fen)
        except ValueError:
            messagebox.showerror("Error","N doit etre un entier",parent=fen)
            entrerN.delete(0, END)
            entrerN.insert(0, "")
    fen = Toplevel()
    fen.title("Exercice 5")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    label_entier=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 11 bold ",
                    text="Entrer U0:")
    label_entier.place(x=240,y=230)
    entrerN=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=10)
    entrerN.place(x=350,y=230)
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=180,bd=0,highlightthickness=0)
    stroke_text(440, 100, "Ce programme permet de saisir le premier terme U0,de calculer et \nd’afficher les termes d'une suite ainsi que leur nombre.\nUn = Max(Un−1)−Min(Un−1)\n   -Min(Un−1):le plus petit entier naturel qu’on peut former par les\n    chiffres du terme précédent.\n   -Max(Un−1):le plus grand entier naturel qu’on peut former par les\n    chiffres du terme précédent.",'white', 'green')
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
                   command=definir,
                   borderwidth=3 )
    Definir.place(x=480,y=230)
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
    Reset.place(x=560,y=230)
    global ListTerme
    global ListValue
    global NB
    global NBValue
    global Resultat

    Resultat=Button(fen,
                    fg="white",
                    font="verdana 10 bold italic",
                    text="Resultat",
                    bg="Blue",
                    borderwidth=8 )
    ListTerme=Label(fen,text='Les termes de la suite sont :',fg="#32C1F2",bg="black",font="verdana 13 bold  ")
    ListValue=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    NB=Label(fen,text='Nombre de termes de la suite  = ',fg="#32C1F2",bg="black",font="verdana 13 bold  ")
    NBValue=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    
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

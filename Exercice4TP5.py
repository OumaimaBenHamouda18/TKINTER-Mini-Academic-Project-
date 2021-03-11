from tkinter import *
from tkinter import messagebox
from random import *

def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)

  

def rang (U0,L):
    Resultat.place_forget()
    L.append(U0)
    L.append(',')
    rang=3
    while U0 !=4:
        if U0 %2==0:
            Un=U0 //2
            L.append(Un)
            L.append(',')

        else :
            Un =3* U0 +1
            L.append(Un)
            L.append(',')

    
        U0=Un
        rang +=1
    L.append(2)
    L.append(',')
    L.append(1)
    
    Resultat.place_forget()
    ListTerme.place(x=40,y=320)
    ListValue1.config(text=L[0:26])
    ListValue1.place(x=320,y=320)
    ListValue2.config(text=L[26:len(L)])
    ListValue2.place(x=40,y=340)
    NB.place(x=40,y=380)
    NBValue.config(text=rang)
    NBValue.place(x=130,y=380)

    
 

        
def ex1():
    def Reset():
        entrerN.delete(0, END)
        entrerN.insert(0, "Cliquer sur Définir")
        Resultat.place_forget()
        ListTerme.place_forget()
        ListValue1.place_forget()
        ListValue2.place_forget()
        NB.place_forget()
        NBValue.place_forget()

        
    def definir(fen,entrerU0):
        entrerN.bind("<Button-1>", clear)
        entrerRandom=str(randint(3,40))
        entrerN.insert(END,entrerRandom)
        L=[]
        Resultat.config(text="Résultat",command=lambda:rang(int(entrerN.get()),L))
        Resultat.place(x=380,y=300)
          
    fen = Toplevel()
    fen.title("Exercice 4")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    label_entier=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 11 bold ",
                    text="U0(Aléatoire):")
    label_entier.place(x=210,y=230)
    global entrerN
    entrerN=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 10  italic",
                  width=15)
    entrerN.place(x=350,y=232)
    entrerN.insert(0, "Cliquer sur Définir")
    
    def clear(event): 
        entrerN.delete(0, "end")
        return None
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=180,bd=0,highlightthickness=0)
    stroke_text(440, 80, "Ce programme permet de déterminer le rang à partir du quel une suite U\naboutit au cycle redondant 4,2 et 1",'white', 'green')
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
    Definir.place(x=490,y=230)
    Definir.bind("<Button-1>",clear)
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
    Reset.place(x=570,y=230)
    global ListTerme
    global ListValue1
    global ListValue2
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
    ListValue1=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    ListValue2=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    NB=Label(fen,text='Rang  = ',fg="#32C1F2",bg="black",font="verdana 13 bold  ")
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

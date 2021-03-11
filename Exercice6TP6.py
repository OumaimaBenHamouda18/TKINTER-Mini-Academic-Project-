from tkinter import *
from tkinter import messagebox
def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)
def decoupage(x):
    a=x
    a=str(a)
    L=[]
    while len(a)>0:
        ch=a[-3:]
        pos=a.find(ch)
        L.append(int(ch))
        a=a[:pos]
    return L
def calculV(L):
    signe=1
    v=0
    for i in range(len(L)-1,-1,-1):
        v+=L[i]*signe
        signe*=-1
    return v


def Result(fen,V):
    Liste=[]
    for i in L :
        Liste.append(i)
        Liste.append(',')
    Liste=Liste[:-1]
    Resultat.place_forget()
    ListLabel.place(x=40,y=320)
    ListValue1.config(text=Liste[0:31])
    ListValue1.place(x=340,y=320)
    ListValue2.config(text=Liste[31:72])
    ListValue2.place(x=40,y=350)
    if abs(V)%13==0:
        ResultLabel.config(text="|V|="+str(abs(V))+" est divisible par 13 , alors :\n\n N="+str(N)+" est divisible par 13")
        ResultLabel.place(x=40,y=370)

    else:
        ResultLabel.config(text="|V|="+str(abs(V))+" n'est pas divisible par 13 , alors :\n\n N="+str(N)+" n'est pas divisible par 13")
        ResultLabel.place(x=40,y=370)

    
 

        
def ex1():
    def Reset():
        entrerN.delete(0, END)
        Resultat.place_forget()
        ListValue1.place_forget()
        ListValue2.place_forget()
        ListLabel.place_forget()
        ResultLabel.place_forget()
        
    def definir():
        global cp
        global L
        cp=1
        L=[]
        try:
            global N
            N=int(entrerN.get())
            if N>0:
                L=decoupage(N)
                V=calculV(L)
                Resultat.config(command=lambda:Result(fen,V))
                Resultat.place(x=410,y=300)
                


                
            else:
                entrerN.delete(0, END)
                entrerN.insert(0, "")
                messagebox.showerror("Error","N doit etre un entier positif",parent=fen)
        except ValueError:
            messagebox.showerror("Error","N doit etre un entier",parent=fen)
            entrerN.delete(0, END)
            entrerN.insert(0, "")
    fen = Toplevel()
    fen.title("Exercice 6")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    label_entier=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 10 bold ",
                    text="Entrer un entier positif N:")
    label_entier.place(x=200,y=230)
    entrerN=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=17)
    entrerN.place(x=410,y=230)
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=180,bd=0,highlightthickness=0)
    stroke_text(450, 100, "Ce programme permet de déterminer si un nombre N formé d’un grand nombre\nde chiffres est divisible par 13 ou non.\nLe résultat est déterminée en suivant les étapes ci dessous:\n  -Separation de N par tranche de 3 chiffres en partant des unités\n  -Calcul de V qui est obtenue en insérant alternativement des - et des +\n   entre les tranches à partir du début du nombre en commencant par un -\n  - Le resultat est déterminée selon la valeur de V", 'white', 'green')
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
    Definir.place(x=640,y=230)
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
    Reset.place(x=720,y=230)
    global ListLabel
    global ListValue1
    global ListValue2
    global ListValue3
    global ResultLabel
    global ResultLabel2
    global ResultValue1
    global ResultValue2
    global Resultat
    global PasDeFact
    Resultat=Button(fen,
                    fg="white",
                    font="verdana 10 bold italic",
                    text="Resultat",
                    bg="Blue",
                    borderwidth=8 )
    ListLabel=Label(fen,text='Liste des tranches découpées :',fg="#32C1F2",bg="black",font="verdana 13 bold  ")
    ListValue1=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    ListValue2=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    ResultLabel=Label(fen,fg="#32C1F2",bg="black",font="verdana 13 bold ",anchor=W,justify=LEFT)
    
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

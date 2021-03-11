from tkinter import *
from tkinter import messagebox
def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)
def somme_chiffres(x):
        s=0
        while x:
                s=s+x % 10
                x=x//10
        return s

 

def somme_chiffres_facteurs(x):
        s=0
        i=2
        while x!=1:
                if x % i ==0:
                        x=x // i
                        s=s+somme_chiffres(i)
                else:
                        i=i+1
        return s


    

def Result(fen):
    Resultat.place_forget()
    ListeObtenue=[]
    for i in L:
        if somme_chiffres(i) == somme_chiffres_facteurs(i):
            ListeObtenue.append(i)
            ListeObtenue.append(',')

    if ListeObtenue==[]:
        ResultLabel.config(text='La liste L ne contient aucun entier Smith !',fg="red")
        ResultLabel.place(x=210,y=360)

    else:
        ListeObtenue=ListeObtenue[:-1]
        ResultLabel.config(text='Les entiers Smith de L sont : ',fg="#32C1F2")
        ResultLabel.place(x=40,y=360)
        ResultValue1.config(text=ListeObtenue[0:32])
        ResultValue1.place(x=320,y=360)
        ResultValue2.config(text=ListeObtenue[32:len(ListeObtenue)])
        ResultValue2.place(x=40,y=90)

def remplir(fen,N,elem,EelementInfo):
    global cp
    try:
        if len(L)!=N:
            E=int(elem.get())
            if E>0:
                if cp==N:
                    L.append(E)
                    messagebox.showinfo("Error","La liste est bien remplie!",parent=fen)
                    Resultat.config(command=lambda:Result(fen))
                    Resultat.place(x=380,y=340)
                else:
                    cp+=1
                    elem.delete(0, END)
                    L.append(E)
                    EelementInfo.config(text="Entrer l'élément "+str(cp)+':')  
            else:
                messagebox.showerror("Error","L'element de la liste doit etre un entier positif!",parent=fen)
                elem.delete(0, END)
    except ValueError:
        messagebox.showerror("Error","L'element de la liste doit etre un entier!",parent=fen)
        elem.delete(0, END)
        
def ex1():
    def Reset():
        entrerN.delete(0, END)
        Resultat.place_forget()
        entrerE.place_forget()
        Ajouter.place_forget()
        EelementInfo.place_forget()
        ResultLabel.place_forget()
        ResultValue1.place_forget()
        ResultValue2.place_forget()
        Resultat.place_forget()



        
    def definir():
        global cp
        global L
        cp=1
        L=[]
        L.clear()
        try:
            N=int(entrerN.get())
            if N<=50 and N>=2:
                global EelementInfo
                EelementInfo=Label(fen,text="Entrer l'élément "+str(cp)+':',bg="black",fg="white",font="verdana 11 bold ",)
                EelementInfo.place(x=240,y=270)
                global entrerE
                entrerE=Entry(fen,
                              width=10,
                              borderwidth=3,
                              bg="white",
                              fg="Black",
                              font="verdana 11 bold italic")
                entrerE.place(x=420,y=270)
                global Ajouter
                Ajouter=Button(fen,
                               fg="white",
                               font="verdana 10 bold italic",
                               text="Ajouter",
                               bg="#FF00CC",
                               command=lambda:remplir(fen,N,entrerE,EelementInfo),
                               borderwidth=3 )
                Ajouter.place(x=550,y=270)    
            else:
                entrerN.delete(0, END)
                messagebox.showerror("Error","La taille de la liste doit etre dans [2,50]",parent=fen)
        except ValueError:
            messagebox.showerror("Error","La taille de la liste doit etre un entier",parent=fen)
            entrerN.delete(0, END)
            entrerN.insert(0, "")
             
             
    fen = Toplevel()
    fen.title("Exercice 3")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    fen.iconbitmap('icons\\python_icon.ico')
    label_entier=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 11 bold ",
                    text="Entrer N:")
    label_entier.place(x=240,y=210)
    entrerN=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=10)
    entrerN.place(x=350,y=210)
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=180,bd=0,highlightthickness=0)
    canvas.pack()
    stroke_text(420, 100,"Ce programme permet de remplir une liste L par N entiers et déterminer \nles entiers Smith de L.\n  -Un nombre est dit smith s’il est un nombre dont la somme des chiffres\n   est égale à la somme de tous les chiffres de ses facteurs premiers.", 'white', 'green')

    canvas.place(x=40,y=10)
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
    Definir.place(x=480,y=210)
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
    Reset.place(x=560,y=210)
    global ResultLabel
    global ResultValue1
    global ResultValue2
    global Resultat
    Resultat=Button(fen,
                    fg="white",
                    font="verdana 10 bold italic",
                    text="Resultat",
                    bg="Blue",
                    borderwidth=8 )
    ResultLabel=Label(fen,text='',fg="#32C1F2",bg="black",font="verdana 12 bold italic")
    ResultValue1=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    ResultValue2=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")

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




from tkinter import *
from tkinter import messagebox
def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)
def premier(n):
    if n==1:
        return 0
    else:
        i=2
        while i<=n//2 :
            if n%i ==0 :
                return 0
            i=i+1
    return 1

def test(a):
    i=1
    while True:
        if a%i==0:
            a=a//i
        else:
            break
        i=i+1
    if a==1:
        return True
    else:
        return False
def Result(fen):
    Resultat.place_forget()
    ListeObtenue=[]
    ListeSaisie =[]
    for i in L:
        ListeSaisie.append(i)
        ListeSaisie.append(',')
        if premier(i)==1:
            if (test(i+1)==True)or (test(i-1)==True):
                ListeObtenue.append(i)
                ListeObtenue.append(',')
    ListeSaisie=ListeSaisie[:-1]
    ListeObtenue=ListeObtenue[:-1]            
    ListLabel.place(x=40,y=320)
    ListValue1.config(text=ListeSaisie[0:31])
    ListValue1.place(x=170,y=320)
    ListValue2.config(text=ListeSaisie[31:72])
    ListValue2.place(x=40,y=350)
    ListValue3.config(text=ListeSaisie[72:len(ListeSaisie)])
    ListValue3.place(x=40,y=370)
    ResultValue1.config(text=ListeObtenue[0:32])
    ResultValue2.config(text=ListeObtenue[32:len(ListeObtenue)])
          
    if N>25:
        if len(ListeObtenue)<1:
            PasDeFact.place(x=40,y=400)
        else:
            ResultLabel.place(x=40,y=400)
            ResultValue1.place(x=400,y=400)
            ResultValue2.place(x=40,y=430)
    else:
        if len(ListeObtenue)<1:
            PasDeFact.place(x=40,y=380)
        else:
            ResultLabel.place(x=40,y=380)
            ResultValue1.place(x=400,y=380)
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
                    Resultat.place(x=350,y=320)
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
        L.clear()
        EelementInfo.place_forget()
        entrerE.place_forget()       
        entrerN.delete(0, END)
        Ajouter.place_forget()
        Resultat.place_forget()
        ListValue1.place_forget()
        ListValue2.place_forget()
        ListValue3.place_forget()
        ListLabel.place_forget()
        ResultLabel.place_forget()
        ResultLabel2.place_forget()
        ResultValue1.place_forget()
        PasDeFact.place_forget()
        
    def definir():
        global cp
        global L
        cp=1
        L=[]
        try:
            global N
            N=int(entrerN.get())
            if N<=50 and N>=5:
                global EelementInfo
                EelementInfo=Label(fen,text="Entrer l'élément "+str(cp)+':',bg="black",fg="white",font="verdana 10 bold italic",)
                EelementInfo.place(x=200,y=270)
                global entrerE
                entrerE=Entry(fen,
                              width=6,
                              borderwidth=3,
                              bg="white",
                              fg="Black",
                              font="verdana 11 bold italic")
                entrerE.place(x=365,y=270)
                global Ajouter
                Ajouter=Button(fen,
                               fg="white",
                               font="verdana 10 bold italic",
                               text="Ajouter",
                               bg="#FF00CC",
                               command=lambda:remplir(fen,N,entrerE,EelementInfo),
                               borderwidth=3 )
                Ajouter.place(x=450,y=270)    
            else:
                entrerN.delete(0, END)
                entrerN.insert(0, "")
                messagebox.showerror("Error","La taille de la liste doit etre dans [5,50]",parent=fen)
        except ValueError:
            messagebox.showerror("Error","La taille de la liste doit etre un entier",parent=fen)
            entrerN.delete(0, END)
            entrerN.insert(0, "")
    fen = Toplevel()
    fen.title("Exercice 2")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    fen.iconbitmap('icons\\python_icon.ico')
    label_entier=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 10 bold italic",
                    text="Entrer un entier positif N:")
    label_entier.place(x=200,y=210)
    entrerN=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=6)
    entrerN.place(x=410,y=210)
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=180,bd=0,highlightthickness=0)
    canvas.pack()
    stroke_text(420, 100, "Ce programme permet de remplir une liste L par N entiers positifs et"+"\n"+"afficher tous les entiers factoriel de L ."+"\n"+"Un entier X est dit premier-factoriel s’il vérifie deux propriétés:"+"\n"+"- X est premier"+"\n"+"- X s’écrit sous la forme d’une factorielle incrémentée ou décrémenté\n  de 1 ( X=F ! - 1 ou X=F ! + 1)", 'white', 'green')

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
    Definir.place(x=495,y=210)
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
    Reset.place(x=575,y=210)
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
    ListLabel=Label(fen,text='Liste Saisie :',fg="#32C1F2",bg="black",font="verdana 13 bold  ")
    ListValue1=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    ListValue2=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    ListValue3=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    ResultLabel=Label(fen,text="Les entiers premier factoriel de la liste sont : ",fg="#32C1F2",bg="black",font="verdana 13 bold ")
    ResultLabel2=Label(fen,text='',fg="#52F232",bg="black",font="verdana 12 bold italic")
    ResultValue1=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    ResultValue2=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    ResultValue3=Label(fen,text='',fg="white",bg="black",font="verdana 12 bold italic")
    PasDeFact=Label(fen,text='La liste L ne contient aucun entier factoriel !',fg="red",bg="black",font="verdana 12 bold")

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

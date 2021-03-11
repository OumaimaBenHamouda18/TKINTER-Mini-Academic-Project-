from tkinter import *
from tkinter import messagebox
def stroke_text(x, y, text, textcolor, strokecolor):
    # make stroke text
    canvas.create_text(x, y, text=text, font=('courier', 13, 'bold'), fill=strokecolor)
    # make regular text
    canvas.create_text(x, y, text=text, font=('courier', 13), fill=textcolor)
def Result(fen,J,M,A,BS):
    Date_Aujourdhui=""
    Date_Lendemain=""
    Resultat.place_forget()
    Date_Aujourdhui=str(J)+'/'+str(M)+'/'+str(A)
    if M==12 and J==31:
        M=1
        J=1
        A+=1
    elif((M in [4,6,9,11])and (J==30))or ((M in [1,3,5,7,8,10,12])and (J==31))or((M==2 )and (BS==1) and (J==29))or ((M==2) and (BS==0 )and (J==28)):
        J=1
        M+=1        
    else:
        J+=1
    Date_Lendemain=str(J)+'/'+str(M)+'/'+str(A)
    Date1.config(text="Date d'aujourd'hui :")
    Date1.place(x=20,y=360)
    Date1Value.config(text=Date_Aujourdhui)
    Date1Value.place(x=250,y=360)
    Date2.config(text="Date du lendemain :")
    Date2.place(x=20,y=390)
    Date2Value.config(text=Date_Lendemain)
    Date2Value.place(x=250,y=390)
    
def definir(fen,entrerJ,entrerM,entrerA):
    
    Resultat.place_forget()
    msg1=1
    msg2=1
    msg3=1

    try:
        J=int(entrerJ.get())

    except ValueError:
        msg1=0
    try:
        M=int(entrerM.get())

    except ValueError:
        msg2=0
    try:
        A=int(entrerA.get())
    except ValueError:
        msg3=0  
    if msg1==0 and msg2==0 and msg3==0:
        entrerJ.delete(0, END)
        entrerJ.focus()
        entrerM.delete(0, END)
        entrerA.delete(0, END)
        messagebox.showerror("Error","Erreur:Les élément d'une date doivent etre des entiers !",parent=fen)
    elif msg1==0 and msg2==0 and msg3==1:
        entrerJ.delete(0, END)
        entrerJ.focus()
        entrerM.delete(0, END)
        messagebox.showerror("Error","Erreur:Le jour et le mois doivent etre des entiers !",parent=fen)
    elif msg1==0 and msg2==1 and msg3==0:
        entrerJ.delete(0, END)
        entrerJ.focus()
        entrerA.delete(0, END)
        messagebox.showerror("Error","Erreur:Le jour et l'année doivent etre des entiers !",parent=fen)
    elif msg1==1 and msg2==0 and msg3==0:
        entrerM.delete(0, END)
        entrerM.focus()
        entrerA.delete(0, END)
        messagebox.showerror("Error","Erreur:Le mois et l'année doivent etre des entiers !",parent=fen)
    elif msg1==0 and msg2==1 and msg3==1:
        entrerJ.delete(0, END)
        entrerJ.focus()
        messagebox.showerror("Error","Erreur:le jour doit etre un entier !",parent=fen)

    elif msg1==1 and msg2==0 and msg3==1:
        entrerM.delete(0, END)
        entrerM.focus()
        messagebox.showerror("Error","Erreur:le mois doit etre un entier !",parent=fen)
    elif msg1==1 and msg2==1 and msg3==0:
        entrerA.delete(0, END)
        entrerA.focus()
        messagebox.showerror("Error","Erreur:l'année doit etre un entier !",parent=fen)   
    elif msg1==1 and msg2==1 and msg3==1:
        LJ=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        LM=[1,2,3,4,5,6,7,8,9,10,11,12]
        if (J in LJ)  and (M in LM) and  A>=1990:
            ok=0
            if A%4 ==0:
                ok=1
            if M==2 and ok==1 and J>29:
                messagebox.showinfo("Error","Le jour n'est pas valide !\n il s'agit d'une année bisextile",parent=fen)         
                entrerJ.delete(0, END)
                entrerJ.focus()
            elif M==2 and ok==0 and J>28:
                messagebox.showinfo("Error","Le jour n'est pas valide !\n il ne s'agit pas d'une année bisextile",parent=fen)         
                entrerJ.delete(0, END)
                entrerJ.focus()
            else:
                BS=ok
                messagebox.showinfo("Good Job","Les données sont bien saisies !",parent=fen)
                Resultat.config(command=lambda:Result(fen,J,M,A,BS))
                Resultat.place(x=380,y=310)
        elif (J not in LJ )and ( M in LM ) and A>=1990:
            messagebox.showinfo("Error","Le jour n'est pas valide !\nLe jour doit etre dans [1,31]",parent=fen)       
            entrerJ.delete(0, END)
            entrerJ.focus()
        elif  (M not in LM) and J in LJ and(A>=1990):
            messagebox.showinfo("Error","Le mois n'est pas valide !\nLe mois doit etre dans [1,12]",parent=fen)         
            entrerM.delete(0, END)
            entrerM.focus()
        elif (not A>=1990) and (J in LJ )and( M in LM ) :
            messagebox.showinfo("Error","L'année n'est pas valide !\nLe mois doit etre > 1990",parent=fen)         
            entrerA.delete(0, END)
            entrerA.focus()

        elif (J not in LJ )and ( M not in LM ) and A>=1990:
            entrerJ.delete(0, END)
            entrerM.delete(0, END)
            entrerJ.focus()
            messagebox.showinfo("Error","Le mois et le jour ne sont pas valide !\nLe jour doit etre dans [1,31]\nLe mois doit etre dans [1,12]",parent=fen)         

        elif (J not in LJ )and ( M in LM ) and A<1990:
            entrerJ.delete(0, END)
            entrerA.delete(0, END)
            entrerJ.focus()
            messagebox.showinfo("Error","Le jour et l'année ne sont pas valide !\nLe jour doit etre dans [1,31]\nL'année doit etre >=1990 ",parent=fen)         

        elif (J in LJ )and ( M not in LM ) and A<1990:
            entrerM.delete(0, END)
            entrerA.delete(0, END)
            entrerM.focus()
            messagebox.showinfo("Error","Le mois et l'année ne sont pas valide !\nLe mois doit etre dans [1,12]\nL'année doit etre >=1990 ",parent=fen)         
        elif (J not  in LJ )and ( M not in LM ) and A<1990:
            messagebox.showinfo("Error","Les éléments de la date ne sont pas valide !\nL e jour doit etre dans [1,31]\nLe mois doit etre dans [1,12]\nL'année doit etre >=1990 ",parent=fen)         
            entrerJ.delete(0, END)
            entrerM.delete(0, END)
            entrerA.delete(0, END)
            entrerJ.focus()

            
            
            
    
def ex1():
    def Reset():
        entrerJ.focus()
        entrerJ.delete(0,END)
        entrerM.delete(0,END)
        entrerA.delete(0,END)
        Resultat.place_forget()
        Date1.place_forget()
        Date1Value.place_forget()
        Date2.place_forget()
        Date2Value.place_forget()
    fen = Toplevel()
    fen.title("Exercice 7")
    fen.geometry("852x480+250+90")
    fen.configure(background='black')
    label_entier=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 11 bold ",
                    text="Entrer le jour  :")
    label_entier.place(x=240,y=145)
    entrerJ=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=10)
    entrerJ.place(x=410,y=145)
    label_M=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 11 bold ",
                    text="Entrer le mois  :")
    label_M.place(x=240,y=195)
    entrerM=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=10)
    entrerM.place(x=410,y=195)
    label_A=Label(fen,
        
                    bg="black",
                    borderwidth=3,
                    fg="white",
                    font="verdana 11 bold ",
                    text="Entrer l'année  :")
    label_A.place(x=240,y=245)
    entrerA=Entry(fen,
                  borderwidth=3,
                  bg="white",
                  fg="Black",
                  font="verdana 11 bold italic",
                  width=10)
    entrerA.place(x=410,y=245)
    global canvas
    canvas = Canvas(fen, bg='black',width=840,height=120,bd=0,highlightthickness=0)
    stroke_text(420, 80, "Ce programme permet de déterminer la date du lendemain à partir\nd'une date saisie.",'white', 'green')
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
                   command=lambda:definir(fen,entrerJ,entrerM,entrerA),
                   borderwidth=8,
                   width=8)
    Definir.place(x=380,y=310)
    
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
    Reset.place(x=480,y=315)
    global Date1
    global Date1Value
    global Date2
    global Date2Value
    global Resultat


    Resultat=Button(fen,
                    fg="white",
                    font="verdana 10 bold italic",
                    text="Resultat",
                    bg="Blue",
                    borderwidth=8,
                    width=8)
    Date1=Label(fen,text='',fg="#32C1F2",bg="black",font="verdana 14 bold  ")
    Date1Value=Label(fen,text='',fg="white",bg="black",font="verdana 14 bold italic")
    Date2=Label(fen,text='',fg="#32C1F2",bg="black",font="verdana 14 bold  ")
    Date2Value=Label(fen,text='',fg="white",bg="black",font="verdana 14 bold italic")
    
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


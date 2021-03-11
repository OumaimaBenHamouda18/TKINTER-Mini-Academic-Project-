from tkinter import *
from tkinter import messagebox
import menu_principal,key

def clear_password(event):
    password.delete(0,END)
    password.config(show='*')
def definir(password):
    if password.get()==key.passwd:
            labelError.place_forget()
            login.destroy()
            menu_principal.menu()

    else:
        password.delete(0,END)
        labelError.config(text="Mot de passe incorrect !",fg="red",bg="black")
        labelError.place(x=80,y=250)
      
login = Tk()
login.title("Log In")
login.geometry("352x400+450+90")
login.configure(background='black')
background_image=PhotoImage(file='icons\\back5.png')
background_label = Label(login, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
password=Entry(login,
              show='',
              borderwidth=3,
              bg="black",
              fg="white",
              font="verdana 11  ",
              width=20)
password.place(x=80,y=220)
password.insert(0,"Password")
password.bind("<Button-1>",clear_password)
labelError=Label(login)
valider=Button(login,
               fg="white",
               text="Log In",
               bg="#FF00CC",
               font="verdana 11 bold ",
               command=lambda:definir(password),
               borderwidth=0 )
valider.place(x=150,y=300)   
global Resultat
lock=PhotoImage(file='icons\\user.png')
lock_label = Label(login, image=lock,bg="#060406")
lock_label.place(x=130,y=50)
login.mainloop()

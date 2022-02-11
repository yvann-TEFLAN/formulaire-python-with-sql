from cgitb import text
from curses.ascii import isalpha, isdigit
from email.errors import MessageError
from tkinter import*
import sqlite3
import bcrypt

from tkinter import messagebox
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
root = Tk() 
  
    
root.configure(background='light green') 


root.title("registration form") 


root.geometry("700x600")



def submit():
    conn = sqlite3.connect("Database.db")

    d= {
        "nom": nameE1.get(),
        "prenom": prenomE2.get(),
        "email":emailE3.get(),
        "mdp":mdpE4.get(),
        "confirmation":mdpconfirmE5.get()
      }
    if nameE1.get()=="" or prenomE2.get()=="" or emailE3.get()=="" or mdpE4.get()=="" or mdpconfirmE5.get()=="":
      messagebox.showerror("attention","tout les champs sont requis!")
    
    elif nameE1.get().isspace() or prenomE2.get().isspace() or  mdpE4.get().isspace() or  mdpconfirmE5.get().isspace():
      messagebox.showerror("attention","ERREUR espacement!")

    elif nameE1.get().isdigit() or prenomE2.get().isdigit():
       messagebox.showinfo("désolé","ces champs contiennent uniquement des lettres!")

    elif mdpE4.get() !=  mdpconfirmE5.get():
      messagebox.showinfo("ERREUR","mot de passe non identique")
    if (re.search(regex,emailE3.get())):
        messagebox.showinfo("erreur","email valide")

        c = conn.cursor()

        c.execute(""" CREATE TABLE IF NOT EXISTS user(
            nom text,
            prenom text,
            email text,
            mdp text,
            confirmation text

          )""")

        c.execute("INSERT INTO user VALUES(:nom, :prenom, :email, :mdp, :confirmation)",d)


        conn.commit()
        conn.close()

    else:
       messagebox.showerror("warning"," email non valide")
    nameE1.delete(0,END)
    prenomE2.delete(0,END)
    emailE3.delete(0,END)
    mdpE4.delete(0,END)
    mdpconfirmE5.delete(0,END)





heading = Label(root, text="Form", bg="light green") 
heading.grid(row=0, column=1,pady=10) 
    
name = Label(root, text="Nom", bg="light green") 
name.grid(row=1, column=0,pady=10) 

prenom = Label(root, text="prenom", bg="light green") 
prenom.grid(row=2, column=0,pady=10)


email = Label(root, text="Email", bg="light green")
email.grid(row=3, column=0,pady=10)  

mdp = Label(root,text="mdp", bg="light green") 
mdp.grid(row=4, column=0,pady=10) 

mdpconfirm = Label(root,text="confirmation", bg="light green") 
mdpconfirm.grid(row=5, column=0,pady=10) 



nameE1= Entry(root)
nameE1.grid(row=1, column=1, ipadx="100",pady=10) 


prenomE2 = Entry(root) 
prenomE2.grid(row=2, column=1, ipadx="100",pady=10) 


emailE3 = Entry(root) 
emailE3.grid(row=3, column=1, ipadx="100",pady=10) 


mdpE4 = Entry(root,show="*") 
mdpE4.grid(row=4,column=1, ipadx="100",pady=10) 


mdpconfirmE5 = Entry(root,show="*")
mdpconfirmE5.grid(row=5,column=1, ipadx="100",pady=10)  

inscription= Button(root,text="créer un compte",fg="black", command=submit)
inscription.grid(row=7, column=1,pady=40)



root.mainloop()




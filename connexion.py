from tkinter import*

#window

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')
def connexion():
  #username label and text entry box
  usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
  usernameEntry = Entry(tkWindow).grid(row=0, column=1)  

  #password label and password entry box
  passwordLabel = Label(tkWindow,text="mot de passe").grid(row=1, column=0)  
  passwordEntry = Entry(tkWindow, show='*').grid(row=1, column=1)  


  #login button
  loginButton = Button(tkWindow, text="Connexion").grid(row=4, column=0)  

  tkWindow.mainloop()
from cProfile import label
from cgitb import text
from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(False,False)
root.configure(bg="blue")

def please():
    frame1.place_forget()
    frame2.place(x=50,y=34)
frame1= Frame(root, highlightthickness=3, highlightbackground="black")
frame1.place(x=150,y=170)
btn=Button(frame1,text="inscription",command=please).pack()

frame2= Frame(root,highlightthickness=3, highlightbackground="black")
nom= Label(frame2,text="vilain")
nom.pack()
btn2=Button(frame2,text="connexion").pack()


root.mainloop()
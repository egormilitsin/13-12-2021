from tkinter import *


import addclick

tk = Tk()
tk.title('Clicker')
tk.geometry("800x600")
n = addclick.n
mul=addclick.mul
tk["bg"]="yellow"

def ady():
    addclick.addclick(label,btn1)
def cleary():
    Ivan.clearclicks(label,btn1)



btn1 = Button(text=f"Клик+{mul}", bg="yellow", fg="red",
              padx="70", pady="10", font="16", command=ady)
btn1.pack()

label = Label(tk, text=str(n) + '$', font=('Arial 200'),fg="red", bg="yellow")
label.pack()
btn2 = Button(text="Сброс", bg="yellow", fg="red",
              padx="20", pady="8", font="Arial 26", command=cleary)
btn2.pack()
mainloop()

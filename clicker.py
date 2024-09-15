import tkinter as tk 
from random import *
def randomness():
    button_click.place(x=randint(0,700), y=randint(0,500))
    window.after(800,randomness)
def click_on_button():
    global col
    col+=1
    counter["text"]=str(col)
window=tk.Tk()
window.title("Кликер")
window.geometry("800x600")
window.resizable(width=False, height=False)
window["bg"]="white"
col=0
counter=tk.Label(window,text='0',font=("Arial", 20, "bold"),bg="white",fg="black")
counter.pack()
button_click=tk.Button(window,text="кликни ", bg="yellow",fg="black",padx="20",pady="5",font=("Arial",12,"bold"),command=click_on_button)
button_click.place(x=randint(0,700), y=randint(0,500))
randomness()
window.mainloop()
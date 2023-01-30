from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from Trie import *

# Trie -------------------------------------------------------------------------
t = Trie()
# File -------------------------------------------------------------------------
global file
def choose_file():
    filepath = filedialog.askopenfilename(title='Open a text file')
    file = open(filepath) # Open file
    index = 1
    listbox.delete(0,END)
    for i in file.readlines(): # Inserting into the Trie
        t.insert(i)
        listbox.insert(index,i) # Inserting into the listbox
        index+=1
    file.close()
# ActionMethod ------------------------------------------------------------------
def ActionMethod(event):
    if entry.get() != "":
        var = t.AutoSuggestions(entry.get())
        if var == -1:
            listbox.delete(0,END)
            print("Trie is Empty...\n")
        elif var == 0:
            listbox.delete(0,END)
            print("No words found with this title...\n")
        else:
            listbox.delete(0,END)
            for index in range(len(var)):
                listbox.insert(index,var[index])
# Gui --------------------------------------------------------------------------
def gui():
    root=Tk() # Object of Tk liblary
    
    v = tk.StringVar()

    peyw = Label(root, text = "Please enter your word :").place(x=40,y=10)  # Label 
    
    global entry
    entry = tk.Entry(root , width=40)
    entry.pack(padx=40 , pady=40)
    entry.bind("<KeyRelease>" , ActionMethod) #Action listener

    global listbox
    listbox = Listbox(root , width= 40 ,height=10, activestyle="underline")
    listbox.pack(padx=40 , pady=10)
    
    Button(root,text="Choose File", command=choose_file, width=10).place(x=40,y=280) # Button Choose file

    root.geometry('330x330') # Size of root
    root.resizable(0,0)
    root.title("Data structure and Algorithm") # Title
    mainloop()
gui()
from tkinter import *
import app1

def definition():
    text1.delete('1.0',END)
    app1.dictionary(chosen_text.get())
    text1.insert(END, (app1.dictionary(chosen_text.get())))

window=Tk()

window.wm_title("Interactive Dictionary")

l1=Label(window, text="Welcome to the", font=("Courier",16, "bold"))
l1.grid(row=0,column=1)

l1=Label(window, text="Interactive Dictionary!", font=("Courier",16, "bold"))
l1.grid(row=0,column=2)

l1=Label(window, text="Enter word:", font=("Courier",12), anchor = "center")
l1.grid(row=3,column=0)

l1=Label(window, text="Definition", font=("Courier",12), anchor = "e")
l1.grid(row=4,column=0)

chosen_text=StringVar()
e4=Entry(window,textvariable=chosen_text)
e4.grid(row=3,column=1, columnspan=3)

b1=Button(window,text="Define", width=12,command=definition)
b1.grid(row=3,column=2)

sb1=Scrollbar(window)
sb1.grid(row=5,column=2)

#list1=Listbox(window,height=6,width=35)
#list1.grid(row=5,column=0,rowspan=10,columnspan=4)

text1=Text(window,height=6,width=40)
text1.grid(row=5,column=0,columnspan=6, rowspan=3)

text1.configure(yscrollcommand=sb1.set)
sb1.configure(command=text1.yview)

window.mainloop()

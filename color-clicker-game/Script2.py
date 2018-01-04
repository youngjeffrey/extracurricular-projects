import tkinter as tk
from tkinter import *
import random


root = tk.Tk()

e1=Label(root,text="Click", font=("Helvetica", 16, "bold"))
e1.grid(row=0,column=4)

e2=Label(root,text="Me", font=("Helvetica", 16, "bold"))
e2.grid(row=0,column=5)

e3=Label(root,text="Red", font=("Helvetica", 16, "bold"))
e3.grid(row=0,column=6)

score=0
#scoring=Label(root,text="Score: "+str(score), font=("Helvetica", 16))
#scoring.grid(row=5,column=10)

level=1

levels=Label(root)
levels.grid(row=4,column=10)
levels.configure(text="Level: 1")

scoring=Label(root)
scoring.grid(row=5,column=10)
scoring.configure(text="Score: 0")

for row in range(8):
    for col in range(8):
        button = tk.Button(root, bg='#%02x%02x%02x' % (255, 0, 0), width=6, height=3,
        command = lambda row1 = row, col1 = col: click(row1,col1))
        button.grid(row=row+1, column=col+1, sticky="nsew")

red=0
odd_one = tk.Button(root, bg='#%02x%02x%02x' % (255, 255, 255), width=6, height=3,
                    command=lambda row2=row, col2=col: click(row2, col2))
odd_one.grid(row=random.randint(1,row), column=random.randint(1,col), sticky="nsew")
grid_info2 = odd_one.grid_info()
row2 = grid_info2["row"]

def click(row, col):
    label.configure(text="%s , %s" % (row,col))

    if row == 7 and col == 7:
       lvl_inc(level)
       #score_inc(score)
       new_grid()

def lvl_inc(level):
    level=level+1
    levels.configure(text="Level: %s" % (level))

def score_inc(score):
    score=score+1
    score.configure(text="Score: %s" % (score))

r3 = 255

def new_grid():
    for row in range(8):
        for col in range(8):
            button = tk.Button(root, bg='#%02x%02x%02x' % (255, 0, 0), width=6, height=3,
                               command=lambda row1=row, col1=col: click(row1, col1))
            button.grid(row=row + 1, column=col + 1, sticky="nsew")

    def color_change(rn):
        return ("#%2.2x%2.2x%2.2x" % (255, rn-50, rn-50))

    global r3
    odd_one = tk.Button(root, width=6, height=3,
                        command=lambda row2=row, col2=col: click(row2, col2))
    odd_one.configure(bg = color_change(r3))
    odd_one.grid(row=random.randint(1, row), column=random.randint(1, col), sticky="nsew")
    grid_info2 = odd_one.grid_info()
    row2 = grid_info2["row"]


#def mouse(event):
    #global score
    #global level
    #global red
    #grid_info = event.widget.grid_info()
    #row1 = int(grid_info["row"])
    #print (event.x,event.y)

    #if row2==row1:
        #score=score+1
        #level=level+1
       # red=red+10
       # return True

label = tk.Label(root, text = "")
label.grid(row = 8, column = 0, columnspan=10, stick="nsew")


#root.bind("<Button-1>", mouse)
#print(root.bind("<Button-1>", mouse))


root.mainloop()

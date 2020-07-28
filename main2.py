from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("644x900")

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        scvalue.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=BOTH,padx=10,pady=10)

f=Frame(root,bg="grey")
b=Button(f,text="C",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6,)

b=Button(f,text=".",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="-",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)



f.pack(fill=X)

f=Frame(root,bg="grey")
b=Button(f,text="+",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="/",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="*",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)



f.pack()
f=Frame(root,bg="grey")
b=Button(f,text="0",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="00",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="=",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)




f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="9",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="8",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="7",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)



f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="5",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="4",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)



f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="3",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="2",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="1",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)



f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="9",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="8",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)

b=Button(f,text="7",padx=10,pady=10,height=1,width=7,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=6,pady=6)



f.pack()


root.mainloop()
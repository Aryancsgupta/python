from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
root = Tk()

root.geometry("644x980")
root.title("Calculator")
root.wm_iconbitmap("2.png")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvariable=scvalue, font= "lucida 40 bold")
screen.pack(fill =X, ipadx=8, pady = 10,padx= 10)

f = Frame(root,background="grey")

b = Button(f,text = "9",padx= 18,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "8",padx= 18,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "7",padx= 18,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

f.pack()


f = Frame(root,background="grey")

b = Button(f,text = "6",padx= 18,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "5",padx= 18,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "4",padx= 18,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

f.pack()


f = Frame(root,background="grey")

b = Button(f,text = "3",padx= 18,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "2",padx= 18,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "1",padx= 18,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root,background="grey")

b = Button(f,text = "0",padx= 20,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = ".",padx= 20,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "+",padx= 20,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root,background="grey")

b = Button(f,text = "-",padx= 23,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "*",padx= 23,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "/",padx= 23,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root,background="grey")

b = Button(f,text = "C",padx= 14,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "%",padx= 14,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text = "=",padx= 14,pady= 12,font = "licida 35 bold")
b.pack(side =LEFT,padx= 8,pady=2)
b.bind("<Button-1>",click)

f.pack()



root.mainloop()

import tkinter as tk
root = tk.Tk()
root.geometry("350x300+570+100")
def click(num):
    data = input_text.get()
    input_text.delete(0,tk.END)
    data = data + str(num)
    input_text.insert(0,data)
def clear():
    input_text.delete(0,tk.END)
def calculate():
    expression = input_text.get()
    result = eval(expression)
    input_text.delete(0,tk.END)
    input_text.insert(0,result)
input_text = tk.Entry(root,font=("Arial",20))
seven = tk.Button(root,text="7",font=("Arial",15),command=lambda :click(7))
eight = tk.Button(root,text="8",font=("Arial",15),command=lambda: click(8))
nine = tk.Button(root,text="9",font=("Arial",15), command=lambda :click(9))
plus = tk.Button(root,text="+",font=("Arial",15),command=lambda: click("+"))

four = tk.Button(root,text="4",font=("Arial",15),command=lambda: click(4))
five = tk.Button(root,text="5",font=("Arial",15), command=lambda: click(5))
six = tk.Button(root,text="6",font=("Arial",15), command=lambda: click(6))
minus = tk.Button(root,text="-",font=("Arial",15), command=lambda: click("-"))

three = tk.Button(root,text="3",font=("Arial",15),command=lambda: click(3))
two = tk.Button(root,text="2",font=("Arial",15),command=lambda: click(2))
one = tk.Button(root,text="1",font=("Arial",15), command=lambda: click(1))
multiply = tk.Button(root,text="*",font=("Arial",15),command=lambda: click("*"))

devide = tk.Button(root,text="/",font=("Arial",15),command= lambda: click("/"))
zero = tk.Button(root,text="0",font=("Arial",15),command=lambda: click(0))
clear = tk.Button(root,text="C",font=("Arial",15),command=clear)
equal = tk.Button(root,text="=",font=("Arial",15),command=calculate)

input_text.grid(row=0,column=0,columnspan=4)
seven.grid(row=1,column=0,ipadx=15,pady=5)
eight.grid(row=1,column=1,ipadx=15,pady=5)
nine.grid(row=1,column=2,ipadx=15,pady=5)
plus.grid(row=1,column=3,ipadx=15,pady=5)

four.grid(row=2,column=0,ipadx=15,pady=5)
five.grid(row=2,column=1,ipadx=15,pady=5)
six.grid(row=2,column=2,ipadx=15,pady=5)
minus.grid(row=2,column=3,ipadx=15,pady=5)

three.grid(row=3,column=0,ipadx=15,pady=5)
two.grid(row=3,column=1,ipadx=15,pady=5)
one.grid(row=3,column=2,ipadx=15,pady=5)
multiply.grid(row=3,column=3,ipadx=15,pady=5)

devide.grid(row=4,column=0,ipadx=15,pady=5)
zero.grid(row=4,column=1,ipadx=15,pady=5)
clear.grid(row=4,column=2,ipadx=15,pady=5)
equal.grid(row=4,column=3,ipadx=15,pady=5)

root.mainloop()
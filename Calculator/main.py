import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Calculator")



#func
def one() :
    nums.insert(END,1)

def two() :
    nums.insert(END,2)

def three() :
    nums.insert(END,3)

def four() :
    nums.insert(END,4)

def five() :
    nums.insert(END,5)

def six() :
    nums.insert(END,6)

def seven() :
    nums.insert(END,7)

def eight() :
    nums.insert(END,8)

def nine() :
    nums.insert(END,9)

def zero() :
    nums.insert(END,0)

def plus() :
    nums.insert(END,"+")

def minus() :
    nums.insert(END,"-")

def product() :
    nums.insert(END,"*")

def divide() :
    nums.insert(END,"/")

def dot() :
    nums.insert(END,".")

def answer() :
    x = eval(nums.get())
    nums.delete(0,END)
    nums.insert(0,x)

def dot_sym() :
    nums.insert(END,".")

def all_clear() :
    nums.delete(0,END)

def clear() :
    x = nums.get()
    nums.delete(len(x) -1 , END)


#inputs
nums = Entry()


#buuton
label1 = Button(text=1,width=3,command=one)
label2 = Button(text=2,width=3,command=two)
label3 = Button(text=3,width=3,command=three)
label4 = Button(text=4,width=3,command=four)
label5 = Button(text=5,width=3,command=five)
label6 = Button(text=6,width=3,command=six)
label7 = Button(text=7,width=3,command=seven)
label8 = Button(text=8,width=3,command=eight)
label9 = Button(text=9,width=3,command=nine)
label0 = Button(text=0,width=3,command=zero)
dot_sign = Button(text=".",width=3,command=dot_sym)
add_sym = Button(text="+",width=3,command=plus)
dif_sym = Button(text="-",width=3,command=minus)
mul_sym = Button(text="x",width=3,command=product)
div_sym = Button(text="/",width=3,command=divide)
ans_sign = Button(text="Ans",width=3,command=answer)
ac_button = Button(text="AC",command=all_clear)
clear_button = Button(text="C",command=clear)

#grid
label1.grid(row=1,column=0)
label2.grid(row=1,column=1)
label3.grid(row=1,column=2)
label4.grid(row=2,column=0)
label5.grid(row=2,column=1)
label6.grid(row=2,column=2)
label7.grid(row=3,column=0)
label8.grid(row=3,column=1)
label9.grid(row=3,column=2)
label0.grid(row=4,column=1)
dot_sign.grid(row=4,column=0)
add_sym.grid(row=1,column=3)
dif_sym.grid(row=2,column=3)
mul_sym.grid(row=3,column=3)
div_sym.grid(row=4,column=2)
ans_sign.grid(row=4,column=3)
ac_button.grid(row=2,column=4)
nums.grid(row=0,column=0,columnspan=5)
clear_button.grid(row=1,column=4)



window.mainloop()
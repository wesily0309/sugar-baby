def plus1():
    global num
    num+=1
    yrlabeltxt.set("目前計數為"+str(num)+"了");

def m1():
    global num
    num-=1
    yrlabeltxt.set("目前計數為"+str(num)+"了");




import tkinter as tk

yrwin=tk.Tk()

yrlabeltxt=tk.StringVar()
yrbtntxt=tk.StringVar()
yrbtntxt2=tk.StringVar()
num = 0
 
mylabel= tk.Label(yrwin,textvariable=yrlabeltxt)
yrlabeltxt.set("目前計數為0")
mylabel.pack()

mybtn=tk.Button(yrwin,textvariable=yrbtntxt,command=plus1)
yrbtntxt.set("+1")
mybtn.pack()

mybtn2=tk.Button(yrwin,textvariable=yrbtntxt2,command=m1)
yrbtntxt2.set("-1")
mybtn2.pack()

yrwin.mainloop()
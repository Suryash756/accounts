from tkinter import*
import random

root = Tk()
root.geometry("800x400")
root.title("account_app")
root.configure(background = "cyan")

months  = ("January","feburary","march","april","may","june","july","august","september","october","november","december")
profits = (10000,15000,20000,30000,40000,10000,23567,23500,30000,56000,57000,45000)
label_month = Label(root,text="months = "+str(months),bg="white",fg="black")
label_profit = Label(root,text="months = "+str(profits),bg="white",fg="black")
label_month.place(rely=0.2,relx=0.5,anchor=CENTER)
label_profit.place(rely=0.3,relx=0.5,anchor=CENTER)

pro_show = Label(root,bg="white",fg="black")

mon_show_min = Label(root,bg="white",fg="black")

def show() :
    max_profits = max(profits)
    max_profit_index = profits.index(max_profits)
    max_profit_month = months[max_profit_index]
    pro_show["text"] = "maximum profit is in the month of "+str(max_profit_month)+" and it is ="+str(max_profits)
    min_profits = min(profits)
    min_profit_index = profits.index(min_profits)
    min_profit_month = months[min_profit_index]
    mon_show_min["text"] ="minimum profit is in the month of "+str(min_profit_month)+" and it is ="+str(min_profits)

btn = Button(root,text="see the years profit and loss report",bg="yellow",fg="black",command=show)
btn.place(rely=0.5,relx=0.5,anchor=CENTER)

pro_show.place(rely=0.7,relx=0.5,anchor=CENTER)
mon_show_min.place(rely=0.9,relx=0.5,anchor=CENTER)
    
    
root.mainloop()
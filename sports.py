############# IMPORTING MODULES   ###################

from tkinter import *
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox



root=Tk()

root.title("SPORTS STORE MANAGEMENT")
# root.iconbitmap('c:/hnet.com-image.ico')
root.geometry("1200x600")

root.minsize(700,600)
root.configure(background="darkred")


#TITLE OF THE PROGRAM
titleLabel = Label(root, text=("SPORTS STORE MANAGEMENT SYSTEM"), pady=10, font=("Ink Free",38,"bold","italic"),
     justify=CENTER, bg="#d76d77",border=4.5,fg="darkred",relief = GROOVE)
titleLabel.place(relwidth=1, relheight=0.25)


develop_label=Label(root, text="developed by -Anmol Deshratna Saxena \n \t -Ayush Thakre  ", font=("Segoe Print", 14, "italic","bold"),
	pady=10, justify=LEFT, relief=GROOVE ,border=4.5 ,anchor=E, fg="darkblue",bg="#d76d77")

develop_label.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)


######  FUNCTIONS  ###########



def open1(frame):
    if frame == 'choice':
        
        choice.lift()

    if frame == 'items_sold':

        items_sold.lift()

    if frame == 'graphs':

        graphs.lift()

    if frame == 'stock':

        stock.lift()

    if frame == 'add_rec_ITEM':

        add_rec_ITEM.lift()

    if frame ==  'del_rec_ITEM':

        del_rec_ITEM.lift()

    if frame ==  'update_rec_ITEM':

        update_rec_ITEM.lift()

    if frame ==  'add_rec_STOCK':

        add_rec_STOCK.lift()

    if frame ==  'del_rec_STOCK':

        del_rec_STOCK.lift()

    if frame ==  'update_rec_STOCK':

       update_rec_STOCK.lift()

    if frame == 'display_rec_STOCK':

       display_rec_STOCK.lift()

    if frame == 'display_rec_ITEM':

       display_rec_ITEM.lift()

    if frame == 'pies':

       pies.lift()
       
    if frame == 'bars':

       bars.lift()

    if frame == 'lines':

       lines.lift()

    if frame == 'histos':

       histos.lift()



def back(parameter):
    if parameter == 'items sold':

        items_sold.lower()

    if parameter == 'stock rem':

        stock.lower()

    if parameter == 'add_rec_ITEM':

        add_rec_ITEM.lower()

    if parameter == 'del_rec_ITEM':

        del_rec_ITEM.lower()

    if parameter == 'update_rec_ITEM':

        update_rec_ITEM.lower()


    if parameter == 'add_rec_STOCK':

        add_rec_STOCK.lower()

    if parameter == 'del_rec_STOCK':

        del_rec_STOCK.lower()

    if parameter == 'update_rec_STOCK':

        update_rec_STOCK.lower()

    if parameter == 'display_rec_ITEM':

        display_rec_ITEM.lower()

    if parameter == 'display_rec_STOCK':

        display_rec_STOCK.lower()




def submit(execute):
    if execute == 'add':

        name1 = i_name_var.get()
        code1 = i_code_var.get()
        price1 = i_price_var.get()
        quantity1 = quantity_var.get()
        totalcost1 = total_cost_var.get()
        customername1 = customer_name_var.get()
        customerno1 = customer_no_var.get()
        company1 = company_var.get()

        cur.execute(f'insert into items_sold values("{name1}","{code1}","{price1}","{quantity1}","{totalcost1}","{customername1}","{customerno1}","{company1}")')
        myd.commit()

        add_rec_ITEM = messagebox.showinfo("^_^","RECORD SUCCESSFULLY ADDED")

    if execute == 'add1':
        name2 = i_name_var1.get()
        code2 = i_code_var1.get()
        price2 = i_price_var1.get()
        quantity2 = quantity_var1.get()
        company2 = company_var1.get()

        cur.execute(f'insert into stock values("{name2}","{code2}","{price2}","{quantity2}","{company2}")')
        myd.commit()

        add_rec_STOCK = messagebox.showinfo("^_^","RECORD SUCCESSFULLY ADDED")

        
    if execute == 'del':
        stockcode = stock_code_var.get()

        cur.execute(f'delete from items_sold where code1="{stockcode}"')
        myd.commit()

        del_record_ITEM = messagebox.askyesno("WARNING! !","The Record will be deleted !")

    if execute == "del1":
        stockcode1 = stock_code_var1.get()
        cur.execute(f'delete from stock where code2="{stockcode1}"')
        myd.commit()

    if execute == "update":   
        name3 = i_name_var2.get()
        code3 = i_code_var2.get()
        price3 = i_price_var2.get()
        quantity3 = quantity_var2.get()
        totalcost3= total_cost_var2.get()
        customername3 = customer_name_var2.get()
        customerno3 = customer_no_var2.get()
        company3 = company_var2.get()
        

        cur.execute(f'update items_sold set name1="{name3}",code1="{code3}",price1="{price3}",quantity1="{quantity3}",totalcost1="{totalcost3}",customername1="{customername3}",customerno1="{customerno3}",company="{company3}" where code1="{code3}"')
        myd.commit()
        
def display(display):

    if display == 'show':
    
        
        global show_rec_I
        
        cur.execute(f'select * from items_sold')
        dis=cur.fetchall()
        myd.commit()
        for i in range (len(dis)):
            show_rec_I.insert(i,dis[i])
            show_rec_I.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.05)

    if display == 'show1':
        
        global show_rec_S
        
        cur.execute(f'select * from stock')
        dis1=cur.fetchall()

        myd.commit()
        for i in range (len(dis1)):
            show_rec_S.insert(i,dis1[i])
            show_rec_S.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.05)


def clear(everything):

    if everything == 'item1':
        show_rec_I.delete(0,END)


def clear(everything1):

    if everything1 == 'stock':
        show_rec_S.delete(0,END)
    
    
def shut(hakai):
    if hakai == 'close':

        root.destroy()

    

    

##def update():
##    data = cur.fetchall()
##    df = pd.DataFrame(data)
##    cols=['i_code',......]
##
##    icode=i_code.get()
##    df.loc[df['i_code']==icode,cols] = [icode,iname,]


##EXECUTING main window #####
Home =Frame(root,bg='#a8e063')
Home.place(rely=0.25,relheight=0.65,relwidth=1)
Home.lift()



#main window defining
lg=Label(Home,text="           USERNAME :-",bg="#a8e063",fg="black",font=("Ariel Black",10))
lg.place(relx=.35,rely=.48)
lg2=Label(Home,text="           PASSWORD :-",bg="#a8e063",fg="black",font=("Ariel Black",10))
lg2.place(relx=.35,rely=.54)


image=Image.open("c:/dhoni.png")
image= image.resize((350,350),Image.LANCZOS)
my_img=ImageTk.PhotoImage(image)
lbl=Label(image=my_img,bg="#a8e063").place(relx=.65,rely=.3)


image1=Image.open("c:/football.png")
image1=image1.resize((350,350),Image.LANCZOS)
my_img1=ImageTk.PhotoImage(image1)
lbl_1=Label(image=my_img1,bg="#a8e063").place(relx=.05,rely=.3)



choice =Frame(root,bg='#f7bb97')
choice.place(relheight=1,relwidth=1)
choice.lower()
###############################################  LOGINNNN ###################################################

def check():
    global username, pass_word
    user_n = username.get()
    pass_w = pass_word.get()
    if user_n == "anmol"  and pass_w == "1234":
        
        open1('choice')

    else:
        messagebox.showerror("Wrong Password or Username","PLEASE TRY AGAIN LATER !!!!!!")
        root.destroy()
    
    

btn1=Button(Home,text="ENTER",fg="black",bg="green",bd=6,relief= RAISED,padx=40,pady=5,command=lambda: open1('choice')).place(relx=.48,rely=.64)
btn_exit= Button(Home,text="EXIT",fg="black",bg="red",bd=6,relief= RAISED,padx=45,pady=5,command=lambda: shut('close')).place(relx=.36,rely=.64)

username = StringVar(Home, value="root")
login_name=Entry(Home)
login_name.place(relx=.47,rely=.48)


password  = StringVar(Home, value="anmol#07")
pass_word=Entry(Home,show="*")
pass_word.place(relx=.47,rely=.54)

############################# 2nd window #######################################################
items_sold= Frame(root,bg="#00cdac")
items_sold.place(relheight=1,relwidth=1)
items_sold.lower()


btn2 = Button(choice,text="ITEMS SOLD",fg="darkblue",font =("Arial Black",12),padx=55,pady=15,bd=6,command=lambda: open1('items_sold')).place(relx=.26,rely=.44)


stock= Frame(root,bg="#004e92")
stock.place(relheight=1,relwidth=1)
stock.lower()



btn3 = Button(choice,text="STOCK REMAINING",fg="darkblue",font =("Arial Black",12),padx=50,pady=15,bd=6,command=lambda: open1('stock')).place(relx=.56,rely=.44)

graphs = Frame(root,bg="red")
graphs.place(relheight=1,relwidth=1)
graphs.lower()


btn_graphs = Button(choice,text="SHOW GRAPHS",fg="darkblue",font =("Arial Black",12),padx=55,pady=15,bd=6,command=lambda: open1('graphs')).place(relx=.4,rely=.59)

####################### 3rd window 'items' #####################################################


add_rec_ITEM= Frame(root,bg="#D76D77")
add_rec_ITEM.place(relheight=1,relwidth=1)
add_rec_ITEM.lower()


del_rec_ITEM= Frame(root,bg="#D76D77")
del_rec_ITEM.place(relheight=1,relwidth=1)
del_rec_ITEM.lower()


update_rec_ITEM= Frame(root,bg="#D76D77")
update_rec_ITEM.place(relheight=1,relwidth=1)
update_rec_ITEM.lower()


display_rec_ITEM= Frame(root,bg="#D76D77")
display_rec_ITEM.place(relheight=1,relwidth=1)
display_rec_ITEM.lower()




btn_add = Button (items_sold,text="ADD RECORD",padx=50,pady=20,bd=6,command=lambda: open1('add_rec_ITEM')).place(relx=.40,rely=.07)

btn_delete = Button (items_sold,text="DELETE RECORD",padx=50,pady=20,bd=6,command=lambda: open1('del_rec_ITEM')).place(relx=.40,rely=.27)

btn_update = Button (items_sold,text="UPDATE RECORD",padx=50,pady=20,bd=6,command=lambda: open1('update_rec_ITEM')).place(relx=.40,rely=.47)

btn_display = Button (items_sold,text="DISPLAY RECORD",padx=50,pady=20,bd=6,command=lambda: open1('display_rec_ITEM')).place(relx=.40,rely=.67)

btn_back1 = Button (items_sold,text="BACK",padx=50,pady=15,command=lambda: back('items sold')).place(relx=.02,rely=.9)


###############################sub windows items##################################################



## add record items

#buttons/entry fields

i_name_var = StringVar()
i_name_var.set('')


i_code_var = StringVar()
i_code_var.set('')

i_price_var = IntVar()
i_price_var.set('')

quantity_var = IntVar()
quantity_var.set('')

total_cost_var = IntVar()
total_cost_var.set('')

customer_name_var = StringVar()
customer_name_var.set('')

customer_no_var = IntVar()
customer_no_var.set('')

company_var = StringVar()
company_var.set('')



i_name= Entry(add_rec_ITEM,font=16,textvariable=i_name_var,border=3.5).place(relx= 0.2,rely=0.1,relwidth=.17,relheight=.07 )

i_code =  Entry(add_rec_ITEM,font=16,textvariable=i_code_var,border=3.5).place(relx= 0.2,rely=0.3,relwidth=.17,relheight=.07 )

i_price = Entry(add_rec_ITEM,font=16,textvariable=i_price_var,border=3.5).place(relx= 0.2,rely=0.5,relwidth=.17,relheight=.07 )

quantity = Entry(add_rec_ITEM,font=16,textvariable=quantity_var,border=3.5).place(relx= 0.2,rely=0.7,relwidth=.17,relheight=.07 )

total_cost= Entry(add_rec_ITEM,font=16,textvariable=total_cost_var,border=3.5).place(relx= 0.8,rely=0.1,relwidth=.17,relheight=.07 )

customer_name = Entry(add_rec_ITEM,font=16,textvariable=customer_name_var,border=3.5).place(relx= 0.8,rely=0.3,relwidth=.17,relheight=.07)

customer_no = Entry(add_rec_ITEM,font=16,textvariable=customer_no_var,border=3.5).place(relx= 0.8,rely=0.5,relwidth=.17,relheight=.07)

company= Entry(add_rec_ITEM,font=16,textvariable=company_var,border=3.5).place(relx= 0.8,rely=0.7,relwidth=.17,relheight=.07)

btn_back3 = Button (add_rec_ITEM,text="BACK",padx=50,pady=15,command=lambda: back('add_rec_ITEM')).place(relx=.02,rely=.9)

btn_clear1= Button(add_rec_ITEM,text="CLEAR",padx=50,pady=15,command=lambda: clear('item1')).place(relx=.3,rely=.9)

btn_submit1= Button(add_rec_ITEM,text="SUBMIT",padx=50,pady=15,command=lambda: submit('add')).place(relx=.55,rely=.9)


#labels
I_name =  Label(add_rec_ITEM, text="ITEM NAME:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.12)

I_code =  Label(add_rec_ITEM, text="ITEM CODE:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.32)

I_price =  Label(add_rec_ITEM, text="ITEM PRICE:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.52)

Quantity =  Label(add_rec_ITEM, text="QUANTITY:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.72)

Total_cost =  Label(add_rec_ITEM, text="TOTAL COST:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.12)

Customer_name =  Label(add_rec_ITEM, text="CUSTOMER NAME:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.32)

Customer_no =  Label(add_rec_ITEM, text="CUSTOMER NO.:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.52)

Company =  Label(add_rec_ITEM, text="COMPANY NAME:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.72)




##delete record items

#buttons/entry fields


stock_code_var = StringVar()
stock_code_var.set('')




i_name = Entry(del_rec_ITEM,font=16,state=DISABLED,border=3.5).place(relx= 0.2,rely=0.1,relwidth=.17,relheight=.07 )

i_code =  Entry(del_rec_ITEM,font=16,textvariable=stock_code_var,border=3.5).place(relx= 0.2,rely=0.3,relwidth=.17,relheight=.07 )

i_price = Entry(del_rec_ITEM,font=16,state=DISABLED,border=3.5).place(relx= 0.2,rely=0.5,relwidth=.17,relheight=.07 )

quantity = Entry(del_rec_ITEM,font=16,state=DISABLED,border=3.5).place(relx= 0.2,rely=0.7,relwidth=.17,relheight=.07 )

total_cost= Entry(del_rec_ITEM,font=16,state=DISABLED,border=3.5).place(relx= 0.8,rely=0.1,relwidth=.17,relheight=.07 )

customer_name = Entry(del_rec_ITEM,font=16,state=DISABLED,border=3.5).place(relx= 0.8,rely=0.3,relwidth=.17,relheight=.07)

customer_no = Entry(del_rec_ITEM,font=16,state=DISABLED,border=3.5).place(relx= 0.8,rely=0.5,relwidth=.17,relheight=.07)

company= Entry(del_rec_ITEM,font=16,state=DISABLED,border=3.5).place(relx= 0.8,rely=0.7,relwidth=.17,relheight=.07)

btn_back4= Button (del_rec_ITEM,text="BACK",padx=50,pady=15,command=lambda: back('del_rec_ITEM')).place(relx=.02,rely=.9)

btn_clear2= Button(del_rec_ITEM,text="CLEAR",padx=50,pady=15).place(relx=.3,rely=.9)

btn_submit2= Button(del_rec_ITEM,text="SUBMIT",padx=50,pady=15,command=lambda:submit('del')).place(relx=.55,rely=.9)

# LABELS

I_name =  Label(del_rec_ITEM, text="ITEM NAME:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.12)

I_code =  Label(del_rec_ITEM, text="ITEM CODE:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.32)

I_price =  Label(del_rec_ITEM, text="ITEM PRICE:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.52)

Quantity =  Label(del_rec_ITEM, text="QUANTITY:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.72)

Total_cost =  Label(del_rec_ITEM, text="TOTAL COST:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.12)

Customer_name =  Label(del_rec_ITEM, text="CUSTOMER NAME:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.32)

Customer_no =  Label(del_rec_ITEM, text="CUSTOMER NO.:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.52)

Company =  Label(del_rec_ITEM, text="COMPANY NAME:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.72)


###update record items
i_name_var2 = StringVar()
i_name_var2.set('')


i_code_var2 = StringVar()
i_code_var2.set('')

i_price_var2 = IntVar()
i_price_var2.set('')

quantity_var2 = IntVar()
quantity_var2.set('')

total_cost_var2 = IntVar()
total_cost_var2.set('')

customer_name_var2 = StringVar()
customer_name_var2.set('')

customer_no_var2= IntVar()
customer_no_var2.set('')

company_var2 = StringVar()
company_var2.set('')

#buttons/entry fields

i_name= Entry(update_rec_ITEM,font=16,border=3.5,textvariable=i_name_var2).place(relx= 0.2,rely=0.1,relwidth=.17,relheight=.07 )

i_code =  Entry(update_rec_ITEM,font=16,border=3.5,textvariable=i_code_var2).place(relx= 0.2,rely=0.3,relwidth=.17,relheight=.07 )

i_price = Entry(update_rec_ITEM,font=16,border=3.5,textvariable=i_price_var2).place(relx= 0.2,rely=0.5,relwidth=.17,relheight=.07 )

quantity = Entry(update_rec_ITEM,font=16,border=3.5,textvariable=quantity_var2).place(relx= 0.2,rely=0.7,relwidth=.17,relheight=.07 )

total_cost= Entry(update_rec_ITEM,font=16,border=3.5,textvariable=total_cost_var2).place(relx= 0.8,rely=0.1,relwidth=.17,relheight=.07 )

customer_name = Entry(update_rec_ITEM,font=16,border=3.5,textvariable=customer_name_var2).place(relx= 0.8,rely=0.3,relwidth=.17,relheight=.07)

customer_no = Entry(update_rec_ITEM,font=16,border=3.5,textvariable=customer_no_var2).place(relx= 0.8,rely=0.5,relwidth=.17,relheight=.07)

company= Entry(update_rec_ITEM,font=16,border=3.5,textvariable=company_var2).place(relx= 0.8,rely=0.7,relwidth=.17,relheight=.07)

btn_back5 = Button (update_rec_ITEM,text="BACK",padx=50,pady=15,command=lambda: back('update_rec_ITEM')).place(relx=.02,rely=.9)

btn_clear3= Button(update_rec_ITEM,text="CLEAR",padx=50,pady=15).place(relx=.3,rely=.9)

btn_submit3= Button(update_rec_ITEM,text="SUBMIT",padx=50,pady=15,command=lambda: submit('update')).place(relx=.55,rely=.9)

#labels
I_name =  Label(update_rec_ITEM, text="ITEM NAME:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.12)

I_code =  Label(update_rec_ITEM, text="ITEM CODE:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.32)

I_price =  Label(update_rec_ITEM, text="ITEM PRICE:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.52)

Quantity =  Label(update_rec_ITEM, text="QUANTITY:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.09,rely=0.72)

Total_cost =  Label(update_rec_ITEM, text="TOTAL COST:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.12)

Customer_name =  Label(update_rec_ITEM, text="CUSTOMER NAME:-",
                       font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.32)

Customer_no =  Label(update_rec_ITEM, text="CUSTOMER NO.:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.52)

Company =  Label(update_rec_ITEM, text="COMPANY NAME:-",font =("Ariel Black",14), bg = "#D76D77").place(relx=0.63,rely=0.72)


#display items


show_rec_I = Listbox(display_rec_ITEM,relief=GROOVE,border=4,font= ("Calibri",14))
show_rec_I.bind("<<ListboxSelect>>",display('display'))
show_rec_I.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.05)


btn_display_all_records1 = Button(display_rec_ITEM, text="DISPLAY ALL RECORDS",command=lambda: display('show'),pady=20,padx=30).place(relx=.2,rely=.88)

btn_back6 = Button (display_rec_ITEM,text="BACK",padx=50,pady=10,command=lambda: back('display_rec_ITEM')).place(relx=.02,rely=.9)

btn_clear_all_records2 = Button(display_rec_ITEM, text="CLEAR ALL RECORDS",command=lambda: clear('item1'),pady=20,padx=30).place(relx=.45,rely=.88)

##4TH  WINDOW 'stock'################################################


#DEFINING
add_rec_STOCK= Frame(root,bg="#78ffd6")
add_rec_STOCK.place(relheight=1,relwidth=1)
add_rec_STOCK.lower()

del_rec_STOCK= Frame(root,bg="#78ffd6")
del_rec_STOCK.place(relheight=1,relwidth=1)
del_rec_STOCK.lower()

update_rec_STOCK= Frame(root,bg="#78ffd6")
update_rec_STOCK.place(relheight=1,relwidth=1)
update_rec_STOCK.lower()

display_rec_STOCK= Frame(root,bg="#78ffd6")
display_rec_STOCK.place(relheight=1,relwidth=1)
display_rec_STOCK.lower()




btn_add = Button(stock,text="ADD RECORD",padx=50,pady=20,bd=6,command=lambda: open1('add_rec_STOCK')).place(relx=.40,rely=.07)

btn_delete = Button(stock,text="DELETE RECORD",padx=50,pady=20,bd=6,command=lambda: open1('del_rec_STOCK')).place(relx=.40,rely=.27)

btn_update = Button(stock,text="UPDATE RECORD",padx=50,pady=20,bd=6,command=lambda: open1('update_rec_STOCK')).place(relx=.40,rely=.47)

btn_display = Button(stock,text="DISPLAY RECORD",padx=50,pady=20,bd=6,command=lambda: open1('display_rec_STOCK')).place(relx=.40,rely=.67)

btn_back2 = Button (stock,text="BACK",padx=50,pady=15,command=lambda: back('stock rem')).place(relx=.02,rely=.9)


##################################### SUB WINDOW STOCK #############################################




#add record stock

#buttons/entry fields

i_name_var1 = StringVar()
i_name_var1.set('')


i_code_var1 = StringVar()
i_code_var1.set('')


i_price_var1 = IntVar()
i_price_var1.set('')


quantity_var1 = IntVar()
quantity_var1.set('')


company_var1 = StringVar()
company_var1.set('')


i_name= Entry(add_rec_STOCK,font=16,textvariable=i_name_var1,border=3.5).place(relx= 0.2,rely=0.1,relwidth=.17,relheight=.07 )

i_code =  Entry(add_rec_STOCK,font=16,textvariable=i_code_var1,border=3.5).place(relx= 0.8,rely=0.1,relwidth=.17,relheight=.07 )

i_price = Entry(add_rec_STOCK,font=16,textvariable=i_price_var1,border=3.5).place(relx= 0.2,rely=0.7,relwidth=.17,relheight=.07 )

quantity = Entry(add_rec_STOCK,font=16,textvariable=quantity_var1,border=3.5).place(relx= 0.8,rely=0.7,relwidth=.17,relheight=.07 )

company= Entry(add_rec_STOCK,font=16,textvariable=company_var1,border=3.5).place(relx= 0.5,rely=0.4,relwidth=.17,relheight=.07)

btn_back7 = Button(add_rec_STOCK,text="BACK",padx=50,pady=15,command=lambda: back('add_rec_STOCK')).place(relx=.02,rely=.9)

btn_submit4= Button(add_rec_STOCK,text="SUBMIT",padx=50,pady=15,command=lambda: submit('add1')).place(relx=.55,rely=.9)

btn_clear4= Button(add_rec_STOCK,text="CLEAR",padx=50,pady=15).place(relx=.3,rely=.9)

#labels

I_name =  Label(add_rec_STOCK, text="ITEM NAME:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.09,rely=0.12)

I_code =  Label(add_rec_STOCK, text="ITEM CODE:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.68,rely=0.12)

Quantity =  Label(add_rec_STOCK, text="QUANTITY:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.69,rely=0.72)

Company =  Label( add_rec_STOCK, text="COMPANY NAME:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.33,rely=0.413)

I_price =  Label(add_rec_STOCK, text="ITEM PRICE:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.09,rely=0.72)

#Delete record stock

stock_code_var1 = StringVar()
stock_code_var1.set('')


#buttons/entry fields


i_name= Entry(del_rec_STOCK,font=16,state=DISABLED,border=3.5).place(relx= 0.2,rely=0.1,relwidth=.17,relheight=.07 )

i_code =  Entry(del_rec_STOCK,font=16,textvariable= stock_code_var1,border=3.5).place(relx= 0.8,rely=0.1,relwidth=.17,relheight=.07 )

i_price = Entry(del_rec_STOCK,font=16,state=DISABLED,border=3.5).place(relx= 0.2,rely=0.7,relwidth=.17,relheight=.07 )

quantity = Entry(del_rec_STOCK,font=16,state=DISABLED,border=3.5).place(relx= 0.8,rely=0.7,relwidth=.17,relheight=.07 )

company= Entry(del_rec_STOCK,font=16,state=DISABLED).place(relx= 0.5,rely=0.4,relwidth=.17,relheight=.07)

btn_back8 = Button(del_rec_STOCK,text="BACK",padx=50,pady=15,command=lambda: back('del_rec_STOCK')).place(relx=.02,rely=.9)

btn_submit5= Button(del_rec_STOCK,text="SUBMIT",padx=50,pady=15,command=lambda: submit('del1')).place(relx=.55,rely=.9)

btn_clear5= Button(del_rec_STOCK,text="CLEAR",padx=50,pady=15).place(relx=.3,rely=.9)
#labels

I_name =  Label(del_rec_STOCK, text="ITEM NAME:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.09,rely=0.12)

I_code =  Label(del_rec_STOCK, text="ITEM CODE:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.68,rely=0.12)

Quantity =  Label(del_rec_STOCK, text="QUANTITY:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.69,rely=0.72)

Company =  Label(del_rec_STOCK, text="COMPANY NAME:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.33,rely=0.413)

I_price =  Label(del_rec_STOCK, text="ITEM PRICE:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.09,rely=0.72)


#Update record stock



#buttons/entry fields

i_name= Entry(update_rec_STOCK,font=16,border=3.5).place(relx= 0.2,rely=0.1,relwidth=.17,relheight=.07 )

i_code =  Entry(update_rec_STOCK,font=16,border=3.5).place(relx= 0.8,rely=0.1,relwidth=.17,relheight=.07 )

i_price = Entry(update_rec_STOCK,font=16,border=3.5).place(relx= 0.2,rely=0.7,relwidth=.17,relheight=.07 )

quantity = Entry(update_rec_STOCK,font=16,border=3.5).place(relx= 0.8,rely=0.7,relwidth=.17,relheight=.07 )

company= Entry(update_rec_STOCK,font=16,border=3.5).place(relx= 0.5,rely=0.4,relwidth=.17,relheight=.07)

btn_back9 = Button(update_rec_STOCK,text="BACK",padx=50,pady=15,command=lambda: back('update_rec_STOCK')).place(relx=.02,rely=.9)

btn_submit6= Button(update_rec_STOCK,text="SUBMIT",padx=50,pady=15,command=lambda: submit('update')).place(relx=.55,rely=.9)

btn_clear6= Button(update_rec_STOCK,text="CLEAR",padx=50,pady=15,command=lambda: clear('stock')).place(relx=.3,rely=.9)

#labels


I_name =  Label(update_rec_STOCK, text="ITEM NAME:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.09,rely=0.12)

I_code =  Label(update_rec_STOCK, text="ITEM CODE:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.68,rely=0.12)

Quantity =  Label(update_rec_STOCK, text="QUANTITY:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.69,rely=0.72)

Company =  Label( update_rec_STOCK, text="COMPANY NAME:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.33,rely=0.413)

I_price =  Label(update_rec_STOCK, text="ITEM PRICE:-",font =("Ariel Black",14), bg = "#78ffd6").place(relx=0.09,rely=0.72)

#display all records'

show_rec_S=Listbox(display_rec_STOCK,width=135,height=25,relief=GROOVE,border=4,font= "Calibri")
show_rec_S.bind("<<ListboxSelect>>",display('display'))
show_rec_S.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.05)


btn_display_all_records2 = Button(display_rec_STOCK, text="DISPLAY ALL RECORDS",command=lambda: display('show1'),pady=20,padx=30).place(relx=.2,rely=.88)
btn_back10 = Button (display_rec_STOCK,text="BACK",padx=50,pady=10,command=lambda: back('display_rec_STOCK')).place(relx=.02,rely=.9)
btn_clear_all_records2 = Button(display_rec_STOCK, text="CLEAR ALL RECORDS",command=lambda: clear('stock'),pady=20,padx=30).place(relx=.45,rely=.88)


###########################################    ALL GRAPHS     ##################################################################################

#WINDOW GRAPHS

pies=Frame(root,bg="#43C6AC")
pies.place(relheight=1,relwidth=1)
pies.lower()

btn_pie_G = Button(graphs,text="PIE GRAPHS",padx=24,pady=30,relief = RAISED,bd=7,command=lambda: open1('pies')).place(relx=.45,rely=.15)

lines=Frame(root,bg="#ffc3a0")
lines.place(relheight=1,relwidth=1)
lines.lower()

btn_line_G = Button(graphs,text="LINE GRAPHS",padx=20,pady=30,relief = RAISED,bd=7,command=lambda: open1('lines')).place(relx=.45,rely=.35)


bars=Frame(root,bg="#FFAFBD")
bars.place(relheight=1,relwidth=1)
bars.lower()

btn_bar_G = Button(graphs,text="BAR GRAPHS",padx=21,pady=30,relief = RAISED,bd=7,command=lambda: open1('bars')).place(relx=.45,rely=.55)


histos=Frame(root,bg="#2196f3")
histos.place(relheight=1,relwidth=1)
histos.lower()


btn_histo_G = Button(graphs,text="HISTOGRAM",padx=24,pady=30,relief = RAISED,bd=7,command=lambda: open1('histos')).place(relx=.45,rely=.75)

##PIE GRAPH###

btn1_PG = Button(pies,text="PIE 1",font=("Ink Free",18,"bold","italic"),command =lambda: MyPie1(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.22,rely=.1)

btn2_PG = Button(pies,text="PIE 2",font=("Ink Free",18,"bold","italic"),command =lambda: MyPie2(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.72,rely=.1)

btn3_PG = Button(pies,text="PIE 3",font=("Ink Free",18,"bold","italic"),command =lambda: MyPie3(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.12,rely=.7)

btn4_PG = Button(pies,text="PIE 4",font=("Ink Free",18,"bold","italic"),command =lambda: MyPie4(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.82,rely=.7)


##LINE GRAPH##

btn1_LG = Button(lines,text="LINE 1",font=("Ink Free",18,"bold","italic"),command =lambda: MyLine1(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.22,rely=.1)

btn2_LG = Button(lines,text="LINE 2",font=("Ink Free",18,"bold","italic"),command =lambda: MyLine2(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.72,rely=.1)

btn3_LG = Button(lines,text="LINE 3",font=("Ink Free",18,"bold","italic"),command =lambda: MyLine3(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.12,rely=.7)

btn4_LG = Button(lines,text="LINE 4",font=("Ink Free",18,"bold","italic"),command =lambda: MyLine4(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.82,rely=.7)


##BAR GRAPH##

btn1_BG = Button(bars,text="BAR 1",font=("Ink Free",18,"bold","italic"),command=lambda: MyBar1(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.22,rely=.1)

btn2_BG = Button(bars,text="BAR 2",font=("Ink Free",18,"bold","italic"),command=lambda: MyBar2(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.72,rely=.1)

btn3_BG = Button(bars,text="BAR 3",font=("Ink Free",18,"bold","italic"),command=lambda: MyBar3(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.12,rely=.7)

btn4_BG = Button(bars,text="BAR 4",font=("Ink Free",18,"bold","italic"),command=lambda: MyBar4(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.82,rely=.7)


##HISTOGRAM##

btn1_HG = Button(histos,text="HISTOGRAM 1",font=("Ink Free",18,"bold","italic"),command=lambda: MyHisto1(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.22,rely=.1)

btn2_HG = Button(histos,text="HISTOGRAM 2",font=("Ink Free",18,"bold","italic"),command=lambda: MyHisto2(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.72,rely=.1)

btn3_HG = Button(histos,text="HISTOGRAM 3",font=("Ink Free",18,"bold","italic"),command=lambda: MyHisto3(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.12,rely=.7)

btn4_HG = Button(histos,text="HISTOGRAM 4",font=("Ink Free",18,"bold","italic"),command=lambda: MyHisto4(),padx=45,pady=45,relief = RAISED,bd=9).place(relx=.75,rely=.7)


def MyLine1():
    x=[1990,1991,1992,1993]

    y=[1300,1240,1000,1800]

    plt.plot(x,y,color='blue')

    plt.scatter(x,y,marker='o')
    
    plt.xlabel('YEARS')

    plt.ylabel('GROSS TOTAL PRODUCTS SOLD')

    plt.title('PRODUCTS SOLD OVER YEARS')

    plt.show()
    

def MyLine2():
    x=[1994,1995,1996,1997]

    y=[1103,740,1586,1703]

    plt.plot(x,y,color='orange')

    plt.scatter(x,y,marker='o')

    plt.xlabel('YEARS')

    plt.ylabel('GROSS TOTAL PRODUCTS SOLD')

    plt.title('PRODUCTS SOLD OVER YEARS')

    plt.show()
    
def MyLine3():
    x=[1998,1999,2000,2001]

    y=[300,1440,1006,900]

    plt.plot(x,y,color='red')

    plt.scatter(x,y,marker='o')
     
    plt.xlabel('YEARS')

    plt.ylabel('GROSS TOTAL PRODUCTS SOLD')

    plt.title('PRODUCTS SOLD OVER YEARS')

    plt.show()
    
def MyLine4():
    x=[2002,2003,2004,2005]

    y=[1500,2102,1320,1111]

    plt.plot(x,y,color='magenta')

    plt.scatter(x,y,marker='o')

    plt.xlabel('YEARS')

    plt.ylabel('GROSS TOTAL PRODUCTS SOLD')

    plt.title('PRODUCTS SOLD OVER YEARS')

    plt.show()
    
def MyPie1():
    
    label1 = ['CRICKET BAT', 'FOOTBALL', 'JERSEYS', 'TENNIS RACKET', 'BADMINTON SET','HOCKEY STICKS', 'FOOTBALL STUDS','BOARD GAMES', 'BASKETBALL']

    # labels=list(label1)

    sizes = [550,600, 300, 200, 300, 50, 400, 100, 250]

    print(sizes)

    colors1 = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'pink', 'brown', 'violet']

    #SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)

    plt.title("PRODUCTS SOLD IN A MONTH MAY ")

    plt.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%',startangle=140)

    plt.axis('equal')

    a = plt.show()

    print(a)


def MyPie2():
    
    label1 = ['CRICKET BAT', 'FOOTBALL', 'JERSEYS', 'TENNIS RACKET', 'BADMINTON SET', 'HOCKEY STICKS', 'FOOTBALL STUDS','BOARD GAMES', 'BASKETBALL']

    # labels=list(label1)

    sizes = [250,200, 300, 100, 800, 50, 400, 100, 200]

    print(sizes)

    colors1 = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'pink', 'brown', 'violet']

    #SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)

    plt.title("PRODUCTS SOLD IN A MONTH MARCH")

    plt.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%',startangle=140)

    plt.axis('equal')

    a = plt.show()

    print(a)
   
def MyPie3():
    
    label1 = ['CRICKET BAT', 'FOOTBALL', 'JERSEYS', 'TENNIS RACKET', 'BADMINTON SET', 'HOCKEY STICKS', 'FOOTBALL STUDS','BOARD GAMES', 'BASKETBALL']

    # labels=list(label1)

    sizes = [950,600, 30, 250, 300, 450, 400, 700, 20]

    print(sizes)

    colors1 = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'pink', 'brown', 'violet']

    #SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)

    plt.title("PRODUCTS SOLD IN A MONTH APRIL")

    plt.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%',startangle=140)

    plt.axis('equal')

    a = plt.show()

    print(a)
   
def MyPie4():
    
    label1 = ['CRICKET BAT', 'FOOTBALL', 'JERSEYS', 'TENNIS RACKET', 'BADMINTON SET', 'HOCKEY STICKS', 'FOOTBALL STUDS','BOARD GAMES', 'BASKETBALL']

    # labels=list(label1)

    sizes = [550,60, 400, 250, 800, 150, 420, 100, 250]

    print(sizes)

    colors1 = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'pink', 'brown', 'violet']

    #SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)

    plt.title("PRODUCTS SOLD IN A MONTH OCTOBER")

    plt.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%',startangle=140)

    plt.axis('equal')

    a = plt.show()

    print(a)
    

##BAR GRAPH##
def MyBar1():
    
    
    objects = ('FOOTBALL', 'CRICKET BAT  ', 'BASKETBALL    ','BOARD GAMES','SPIKES')

    y_pos = np.arange(len(objects))
    
    types = (78, 65, 71 ,54 ,23)

    plt.bar(y_pos, types, align='center', color='red',edgecolor="blue")

    plt.xticks(y_pos, objects)

    plt.ylabel('CUSTOMER VISITED')

    plt.title('NUMBER OF CUSTOMER VISITED \n IN A MONTH')

    plt.show()

def MyBar2():
    
    
    objects1 = ('January','February','March','April','May')

    y_pos = np.arange(len(objects1))
    
    types = (56 , 44, 41 ,78 ,88)

    plt.bar(y_pos, types, align='center', color='red')

    plt.xticks(y_pos, objects1)

    plt.ylabel('CUSTOMER VISITED FOR FOOTBALL')

    plt.title('NUMBER OF CUSTOMER VISITED FOR FOOTBALL')

    plt.show()
def MyBar3():
    
    
    objects2 = ('MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER')

    y_pos = np.arange(len(objects2))
    
    types = (28, 45, 61 ,54 , 74 ,83)

    plt.bar(y_pos, types, align='center', color='red',edgecolor="blue")

    plt.xticks(y_pos, objects2)

    plt.ylabel('GIVEN FEEDBACK')

    plt.title('GOOD FEEDBACK GIVEN BY CUSTOMERS VISITED')

    plt.show()
def MyBar4():
    
    
    objects = ('FOOTBALL', 'CRICKET BAT  ', 'BASKETBALL    ','BOARD GAMES','SPIKES')

    y_pos = np.arange(len(objects))
    
    types = (20, 15, 11 , 6 ,21)

    plt.bar(y_pos, types, align='center', color='red',edgecolor="blue")

    plt.xticks(y_pos, objects)

    plt.ylabel('ITEMS REMAINING IN STOCK')

    plt.title('STOCK REMAINING')

    plt.show()


##HISTOS ########

def MyHisto1():
    print("DataFrame of Values histograms:\n")

    yearlysale = {'salesman':["Raj","Rita","Suraj","Rahul"],'sales':[1000,700,1100,800],'years':[1980,1990,2000,2010]}

    df = pd.DataFrame(yearlysale)
    print(df)

    empsales = [1981,1991,2001,2011]
    plt.hist(empsales,bins=[1980,1990,2000,2010,2020],weights=[1000,700,1100,800],facecolor='blue',edgecolor='red')
    plt.xlabel('years')
    plt.ylabel('sold items by an employee')
    plt.show()

def MyHisto2():
    print("DataFrame of Values histograms:\n")

    yearlysale = {'salesman':["Banerjee","Shukla","Siraj","Rahu"],'sales':[100,500,400,250],'years':[1980,1985,1990,1995]}

    df = pd.DataFrame(yearlysale)
    print(df)

    empsales = [1981,1986,1991,1996]
    plt.hist(empsales,bins=[1980,1985,1990,1995,2000],weights=[100,500,400,250],facecolor='blue',edgecolor='red')
    plt.xlabel('years')
    plt.ylabel('sold items by an employee')
    plt.show()

    
def MyHisto3():
    print("DataFrame of Values histograms:\n")

    yearlysale = {'salesman':["Taj","Ritani","Rohan","Bholu"],'sales':[700,300,100,550],'years':[2000,2005,2010,2015]}

    df = pd.DataFrame(yearlysale)
    print(df)

    empsales = [2001,2006,2011,2016]
    plt.hist(empsales,bins=[2000,2005,2010,2015,2020],weights=[700,300,100,550],facecolor='blue',edgecolor='red')
    plt.xlabel('years')
    plt.ylabel('sold items by an employee')
    plt.show()

def MyHisto4():
    print("DataFrame of Values histograms:\n")

    yearlysale = {'salesman':["Mohan","Rita","Dani","John"],'sales':[1000,700,1100,800],'years':[2020,2025,2030,2035]}

    df = pd.DataFrame(yearlysale)
    print(df)

    empsales = [2021,2026,2031,2036]
    plt.hist(empsales,bins=[2020,2025,2030,2035,2040],weights=[1000,700,1100,800],facecolor='blue',edgecolor='red')
    plt.xlabel('years')
    plt.ylabel('sold items by an employee')
    plt.show()





# DATABASE FUNCTIONS



myd= mysql.connector.connect(host="localhost",user="root",passwd="anmolis2405", database= "anmolIP")

cur=  myd.cursor()


root.mainloop()

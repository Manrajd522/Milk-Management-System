from tkinter import * 
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import csv

milk = Tk() 
milk.title("Milk Management System")
milk.geometry("1536x864")
title = Label(milk, text="Milk Management System",bd=2,relief="solid",font=("bold", 20),fg="white",bg='black')
title.pack(side=TOP,fill=X)

#====all variable used for seller============
user_var= StringVar()
name_var= StringVar()
date_var= StringVar()
quantity_var= StringVar()
fat_var= StringVar()
amount_var= StringVar()
add_seller_var= StringVar()
name_seller_var=StringVar()
r_name=StringVar()
rate_var=StringVar()
id_var= StringVar()

#=====all variable used for buyer==============
userb_var= StringVar()
nameb_var= StringVar()
dateb_var= StringVar()
quantityb_var= StringVar()
amountb_var= StringVar()
add_buyer_var= StringVar()
name_buyer_var=StringVar()
r_nameb=StringVar()
rateb_var=StringVar()
idb_var=StringVar()

##===============clear entry=======================
def clear():
    user_var.set("") 
    r_name.set("")
    quantity_var.set("") 
    fat_var.set("") 
    amount_var.set("") 
    userb_var.set("")  
    quantityb_var.set("")
    amountb_var.set("")
    id_var.set("")
    idb_var.set("")
    r_nameb.set("")
   
    

###==============Create database================
def database():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin")
        cur=db.cursor()
        ab="CREATE DATABASE IF NOT EXISTS mms"##(Milk Management System)
        cur.execute(ab)
        db.commit()
    except mysql.connector.errors.DatabaseError:  
        messagebox.showerror('Warning','Your server is not connected')
database()       
    
##====first frame/module =========================================================================================================

##=============set rate========================   
    
def rate():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        ab="CREATE TABLE IF NOT EXISTS rates(id INT AUTO_INCREMENT PRIMARY KEY, rate float)"
        cur.execute(ab)
        db.commit()
        
        ins=db.cursor()
        b="insert INTO rates(rate) SELECT * FROM (SELECT 6.8 AS rate) AS temp WHERE NOT EXISTS (SELECT id FROM rates WHERE id = 1)"
        ins.execute(b)
        db.commit()
        
        
        sel=db.cursor()
        tc="(SELECT rate FROM rates where id = 1)"
        sel.execute(tc)
        i = sel.fetchone()
        rate_var.set(i[0])
        
        db.commit()
    except mysql.connector.errors.DatabaseError:  
        messagebox.showerror('Warning','Your server is not connected')
        
rate()
        
def rate_update():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        ab="UPDATE rates SET rate = "+ rate_var.get() +""" WHERE id = 1"""
        cur.execute(ab)
        db.commit()
        messagebox.showinfo('success','Rate is update')
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected')  
           
#===========Insert seller data ==================
        
def seller_data(event):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        ab=("insert into  " + user_var.get() + """ (id,Date, Quantity, Fat, Amount) values 
            ( """+ id_var.get()+""",'"""+ date_var.get() +"""', '"""+ quantity_var.get() +"""', '"""+ fat_var.get() +"""',
             '"""+  amount_var.get() +"""')""")
        cur.execute(ab)
        db.commit()
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected')
    
    a= (id_var.get())
    b= (user_var.get())
    c= (r_name.get())
    r= (quantity_var.get())
    e= (fat_var.get())
    f= (amount_var.get())
    tree1.insert("",'end',
                values=(a,b,c,r,e,f))
    clear()
    userent.focus_set()
    
#================Delete=============

def delete():
    r = tree1.selection()[0] 
    tree1.delete(r)
    
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        tc=("DELETE FROM " + user_var.get() + """ where id ="""+ id_var.get() +"""""")
        cur.execute(tc)
        db.commit()
        db.close() 
        
        messagebox.showinfo('success','Record is Delete successfully')
    except mysql.connector.errors.DatabaseErrSor:
        messagebox.showerror('Warning','Your server is not connected')
    
    clear()
    

    
#==============insert data==========================
f1= Frame(milk,bd=2, relief='solid' , bg="#98AFC7") 
f1.place(x=10,y=50,width=900, height=250)

header = Label(f1, text="Sellers Data",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=0, width=900)

user = Label(f1, text="User ID:" , font=("bold", 15),fg="black", bg="#98AFC7").place(x=60,y=40)
userent= Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=user_var)
userent.place(x=60, y=90, width=100)

name = Label(f1, text="Name :",font=("bold", 15),fg="black", bg="#98AFC7").place(x=180,y=40)



id = Label(f1, text="Record id:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=60,y=140)
ident= Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=id_var)
ident.place(x=60, y=190, width=100)

date = Label(f1, text="Date:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=180,y=140)
date = DateEntry(f1,selectmode='day',textvariable=date_var).place(x=180,y=190)


quantity = Label(f1, text="Quantity:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=320,y=140)
quantityent= Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=quantity_var)
quantityent.place(x=320, y=190, width=100)


fat = Label(f1, text="Fat:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=460,y=140)
fatent= Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=fat_var)
fatent.place(x=460, y=190, width=100)
 

amount = Label(f1, text="Amount:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=600,y=140)
amountent= Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=amount_var)
amountent.place(x=600, y=190, width=100)


rat = Label(f1, text="Rate:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=460,y=40)
ratent= Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=rate_var)
ratent.place(x=460, y=90, width=100)

but1 = Button(f1, text ="Update Rate",command=rate_update).place(x=780, y=90, width=100)
but2 = Button(f1, text ="Clear",command=clear ).place(x=780, y=140, width=100)
but3 = Button(f1, text ="Delete",command=delete).place(x=780, y=190, width=100)

def go1(event):
    quantityent.focus_set()
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        man=db.cursor()
        tc="(SELECT default(Name) FROM "+ user_var.get() + """)"""
        man.execute(tc)
        i = man.fetchone()
        r_name.set(i[0])
        r=Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=r_name).place(x=180,y=90)
        
        ##======== selet recd from table====================================================
        
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        id=db.cursor()
        a="(select id from "+ user_var.get() + """ order by id desc limit 1)"""
        id.execute(a)
        i = id.fetchone()
        id_var.set(i[0])
        db.commit()
        
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected')
    a=int(ident.get()) 
    id_var.set("")   
    r=a+1
    ident.insert(0,r)


userent.focus()
userent.bind("<Return>",go1)
             

def go2(event):
             fatent.focus_set()

quantityent.bind("<Return>",go2)


def formula(event):
    try:
        a=float(quantityent.get())
        b=float(ratent.get())
        c=float(fatent.get())
        r=a*b*c
        e = float("{0:.2f}".format(r))
        amountent.insert(0,e)
        amountent.focus_set()
    except ValueError:
        messagebox.showerror('Warning','Please Enter All Values!!')     

fatent.bind('<Return>',formula)

amountent.bind('<Return>',seller_data)


###======================== second frame\modul========================== 

#=======get data from treeview to entry back using double click =========================================

def get_data(event):
    row=tree1.focus()
    contant=tree1.item(row)
    r=contant['values']
    id_var.set(r[0])
    user_var.set(r[1]) 
    r_name.set(r[2])
    quantity_var.set(r[3])
    fat_var.set(r[4])
    amount_var.set(r[5])
    
##=======================detail display==============

f2= Frame(milk,bd=2, relief='solid')
f2.place(x=10,y=310,width=900, height=280)

h2 = Label(f2, text="Todays Record",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=0, width=900)

scroll_y= Scrollbar(f2,orient=VERTICAL)

tree1= ttk.Treeview(f2,columns=(1,2,3,4,5,6),show ='headings',height=10,yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)

tree1.heading(1,text="Record id")
tree1.heading(2,text="User ID")
tree1.heading(3,text="Name")
tree1.heading(4,text="Quantity")
tree1.heading(5,text="Fat")
tree1.heading(6,text="Amount")

tree1.column(1,width=100, anchor= CENTER)
tree1.column(2,width=100, anchor= CENTER)
tree1.column(3,width=100, anchor= CENTER)
tree1.column(4,width=100, anchor= CENTER)
tree1.column(5,width=100, anchor= CENTER)
tree1.column(6,width=100, anchor= CENTER)

tree1.place(x=10, y=40, width= 870)
tree1.bind("<Double-1>",get_data)

  
###=================save data===========
def save_csv():
    
     with open("new.csv", "w", newline='') as myfile:
        csvwriter = csv.writer(myfile, dialect='excel')
        
        for row_id in tree1.get_children():
            row = tree1.item(row_id)['values']
            csvwriter.writerow(row)
but1 = Button(f2, text ="save",command=save_csv).place(x=750, y=250, width=100)

    
##===========Third frame\module=====================================================================

##===========create new seller==================================
def create_seller():
    
    try:  
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        try:
            ab="CREATE TABLE " + add_seller_var.get() + """
                 (id INT PRIMARY KEY,Date VARCHAR(10),Name CHAR(22) DEFAULT ' """+ name_seller_var.get() +""" ',
                 Quantity varchar(10),Fat varchar(5),Amount varchar(10))"""
            cur.execute(ab)
            messagebox.showinfo('success','New seller is add successfully')
        except:
             messagebox.showerror('Warning','User is already exists')
        
        ins=db.cursor()
        b="Insert into  "+ add_seller_var.get() +""" (id,Name) values( 0,'"""+ name_seller_var.get() +"""')"""
        ins.execute(b)
        db.commit()
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected')
    add_seller_var.set("")
    name_seller_var.set("")   
        

fs= Frame(milk,bd=2, relief='solid' , bg="#98AFC7")
fs.place(x=10,y=600,width=450, height=150)

h3 = Label(fs, text="Add New User",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=0, width=450)

cs = Label(fs, text="User ID:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=10,y=40)
csent= Entry(fs,relief=RIDGE,font=("bold", 15),textvariable=add_seller_var)
csent.place(x=90, y=40, width=100)

ns = Label(fs, text="Name:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=220,y=40)
nsent= Entry(fs,relief=RIDGE,font=("bold", 15),textvariable=name_seller_var)
nsent.place(x=290, y=40, width=150)

buts = Button(fs, text ="ADD SELLER",font=("bold", 10),command=create_seller ).place(x=10, y=90, width=100)

def gons():
    nbent.focus_set()
    
csent.bind('<Return>',gons)

#======== create New buyer=================================
def create_buyer():
    a=(add_buyer_var.get())
    b=(name_buyer_var.get())
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        try:
            ab="CREATE TABLE " + a + """(id INT PRIMARY KEY,Date VARCHAR(10), 
                             Name CHAR(22) DEFAULT ' """+ b +""" ',Quantity varchar(10),
                             Amount varchar(10))"""
            cur.execute(ab)
            
            messagebox.showinfo('success','New buyer is add successfully')
        except:
             messagebox.showerror('Warning','User is already exists')
             
        ins=db.cursor()
        b="Insert into  "+ a +""" (id,Name) values( 0,'"""+ b +"""')"""
        ins.execute(b)
        db.commit()
        add_buyer_var.set("")
        name_buyer_var.set("")
        
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected')
    

fb= Frame(milk,bd=2, relief='solid' , bg="#98AFC7")
fb.place(x=460,y=600,width=450, height=150)

hb = Label(fb, text="ADD BUYER",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=0, width=450)

cb = Label(fb, text="User ID:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=10,y=40)
cbent= Entry(fb,relief=RIDGE,font=("bold", 15),textvariable=add_buyer_var)
cbent.place(x=90, y=40, width=100)

nb = Label(fb, text="Name:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=220,y=40)
nbent= Entry(fb,relief=RIDGE,font=("bold", 15),textvariable=name_buyer_var)
nbent.place(x=290, y=40, width=150)

butb = Button(fb, text ="ADD BUYER",font=("bold", 10),command=create_buyer).place(x=10, y=90, width=100)

#==bind

def gonb():
    nbent.focus_set()
    
cbent.bind('<Return>',gonb)
    

##=============== forth frame\module===========================================================================

#==============set rate for buyer====================================
def rateb():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        ab="CREATE TABLE IF NOT EXISTS rateb(id INT AUTO_INCREMENT PRIMARY KEY, rate float)"
        cur.execute(ab)
        db.commit()
        
        ins=db.cursor()
        b="insert INTO rateb(rate) SELECT * FROM (SELECT 50 AS rate) AS temp WHERE NOT EXISTS (SELECT id FROM rateb WHERE id = 1)"
        ins.execute(b)
        db.commit()
        
        
        sel=db.cursor()
        tc="(SELECT rate FROM rateb where id = 1)"
        sel.execute(tc)
        i = sel.fetchone()
        rateb_var.set(i[0])
        db.commit()
    except mysql.connector.errors.DatabaseError:  
        messagebox.showerror('Warning','Your server is not connected')

rateb()
        
def rateb_update():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        ab="UPDATE rateb SET rate = "+ rateb_var.get() +""" WHERE id = 1"""
        cur.execute(ab)
        db.commit()
        messagebox.showinfo('success','Rate is update')
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected') 

####===============insert buyer data===================================================
def buyer_data(event):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        ab=("insert into  " + userb_var.get() + """ (id,Date, Quantity, Amount) values 
            ( """+idb_var.get()+""",'"""+ dateb_var.get() +"""', '"""+ quantityb_var.get() +"""','"""+  amountb_var.get() +"""')""")
        cur.execute(ab)
        db.commit()
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected')
    
    a=(idb_var.get())
    b= (userb_var.get())
    c= (r_nameb.get())
    
    r= (quantityb_var.get())
    f= (amountb_var.get())
    tree1.insert("",'end',
                values=(a,b,c,r,"",f))
    clear()
    


f4 = Frame(milk, bd=2, relief='solid',bg="#98AFC7")
f4.place(x=920,y=50,width=600,height=230)

h5 = Label(f4, text="BUYER DATA",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=0, width=600)



userb = Label(f4, text="User ID:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=20,y=40)
userbent= Entry(f4,relief=RIDGE,font=("bold", 15),textvariable=userb_var)
userbent.place(x=20, y=90, width=100)

name = Label(f4, text="Name :",font=("bold", 15),fg="black", bg="#98AFC7").place(x=140,y=40)

idb = Label(f4, text="Record Id:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=20,y=140)
idbent= Entry(f4,relief=RIDGE,font=("bold", 15),textvariable=idb_var)
idbent.place(x=20, y=190, width=100)

dateb = Label(f4, text="Date:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=140,y=140)
datebent = DateEntry(f4,selectmode='day',textvariable=dateb_var).place(x=140,y=190)


quantityb = Label(f4, text="Quantity:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=260,y=140)
quantitybent= Entry(f4,relief=RIDGE,font=("bold", 15),textvariable=quantityb_var)
quantitybent.place(x=260, y=190, width=100)


amountb = Label(f4, text="Amount:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=380,y=140)
amountbent= Entry(f4,relief=RIDGE,font=("bold", 15),textvariable=amountb_var)
amountbent.place(x=380, y=190, width=100)

ratb = Label(f4, text="Rate:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=380,y=40)
ratbent= Entry(f4,relief=RIDGE,font=("bold", 15),textvariable=rateb_var)
ratbent.place(x=380, y=90, width=100)

but1 = Button(f4, text ="Update Rate",command=rateb_update).place(x=490, y=40, width=100)

def go3(event):
    quantitybent.focus_set()
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        man=db.cursor()
        tc="(SELECT default(Name) FROM "+ userb_var.get() + """)"""
        man.execute(tc)
        i = man.fetchone()
        r_nameb.set(i[0])
        r=Entry(f4,relief=RIDGE,font=("bold", 15),textvariable=r_nameb).place(x=140,y=90)
        
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        id=db.cursor()
        a="(select id from "+ userb_var.get() + """ order by id desc limit 1)"""
        id.execute(a)
        i = id.fetchone()
        idb_var.set(i[0])
        db.commit()
        
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected')
    a=int(idbent.get()) 
    idb_var.set("")   
    r=a+1
    idbent.insert(0,r)
    
userbent.bind("<Return>",go3)


def b_formula(event):
    try:
        a=float(quantitybent.get())
        b=float(ratbent.get())
        r=a*b
        e = float("{0:.2f}".format(r))
        amountbent.insert(0,e)
        amountbent.focus_set()
    except ValueError:
        messagebox.showerror('Warning','Please Enter All Values!!')     

quantitybent.bind('<Return>',b_formula)

amountbent.bind('<Return>',buyer_data)


##===========fifth frame/module=============================================================

##===========  show selected record to user  =================================

searchent_var = StringVar()
to_var=StringVar()
from_var=StringVar()
s_name=StringVar()

#============ it shows seller record and total of record from selected dates===================
def record():
    
    tree2= ttk.Treeview(f5,columns=(0,1,2,3,4),show ='headings',height=10,yscrollcommand=scroll_y.set)
    
    tree2.heading(0,text="Record id")
    tree2.heading(1,text="Date")
    tree2.heading(2,text="Quantity")
    tree2.heading(3,text="Fat")
    tree2.heading(4,text="Amount")

    tree2.column(0,width=100, anchor= CENTER)
    tree2.column(1,width=100, anchor= CENTER)
    tree2.column(2,width=100, anchor= CENTER)
    tree2.column(3,width=100, anchor= CENTER)
    tree2.column(4,width=100, anchor= CENTER)

    tree2.place(x=10, y=130, width= 560,)
    
    tree3= ttk.Treeview(f5,columns=(1,2,3,4),show ='headings',height=1)
    tree3.heading(1,text="Total")
    tree3.heading(2,text="Quantity")
    tree3.heading(3,text="Fat")
    tree3.heading(4,text="Amount")
    tree3.column(1,width=100, anchor= CENTER)
    tree3.column(2,width=100, anchor= CENTER)
    tree3.column(3,width=100, anchor= CENTER)
    tree3.column(4,width=100, anchor= CENTER)

    tree3.place(x=10, y=400, width= 560,)
    
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        try:
            ab="(SELECT id,Date,Quantity,Fat,Amount FROM "+searchent_var.get()+ """ WHERE  date between '"""+ from_var.get() +"""' and '"""+ to_var.get() +"""')"""
            cur.execute(ab)
        except mysql.connector.errors.ProgrammingError:
            messagebox.showerror('Warning','Please Click Right Button')
        rows = cur.fetchall()
        for row in rows:
                tree2.insert("",END, values=row)
        db.commit()
        
            
            #================ total of record ================

            
        man=db.cursor()
        tc="(SELECT count(Date),sum(Quantity),avg(Fat),sum(Amount) FROM "+searchent_var.get()+ """ WHERE  date between '"""+ from_var.get() +"""' and '"""+ to_var.get() +"""')"""
        man.execute(tc)
        i = man.fetchall()
        for a in i:
                tree3.insert("",END, values=a)
        db.commit()
        
         
      
        man=db.cursor()
        tc="(SELECT default(Name) FROM "+ searchent_var.get() + """)"""
        man.execute(tc)
        i = man.fetchone()
        s_name.set(i[0])
        
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected')

                                
#============ it shows buyer record and total of record from selected dates===================

def b_record():
    
    tree2= ttk.Treeview(f5,columns=(1,2,3),show ='headings',height=10,yscrollcommand=scroll_y.set)
    
    tree2.heading(0,text="Record id")
    tree2.heading(1,text="Date")
    tree2.heading(2,text="Quantity")
    tree2.heading(3,text="Amount")

    tree2.column(0,width=100, anchor= CENTER)
    tree2.column(1,width=100, anchor= CENTER)
    tree2.column(2,width=100, anchor= CENTER)
    tree2.column(3,width=100, anchor= CENTER)

    tree2.place(x=10, y=130, width= 560,)

    tree3= ttk.Treeview(f5,columns=(0,1,2,3),show ='headings',height=1)
    tree3.heading(1,text="Total")
    tree3.heading(2,text="Quantity")
    tree3.heading(3,text="Amount")
    tree3.column(1,width=100, anchor= CENTER)
    tree3.column(2,width=100, anchor= CENTER)
    tree3.column(3,width=100, anchor= CENTER)

    tree3.place(x=10, y=400, width= 560,)
    
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        try:
            ab="(SELECT id,Date,Quantity,Amount FROM "+searchent_var.get()+ """ WHERE  date between '"""+ from_var.get() +"""' and '"""+ to_var.get() +"""')"""
            cur.execute(ab)
        except mysql.connector.errors.ProgrammingError:
            messagebox.showerror('Warning','Please Click Right Button')
        rows = cur.fetchall()
        for row in rows:
            tree2.insert("",END, values=row)
        

        #=========total of record ===================================
        man=db.cursor()
        tc="(SELECT count(Date),sum(Quantity),sum(Amount) FROM "+searchent_var.get()+ """ WHERE  date between '"""+ from_var.get() +"""' and '"""+ to_var.get() +"""')"""
        man.execute(tc)
        i = man.fetchall()
        for a in i:
            tree3.insert("",END, values=a)
        
        man=db.cursor()
        tc="(SELECT default(Name) FROM "+ searchent_var.get() + """)"""
        man.execute(tc)
        i = man.fetchone()
        s_name.set(i[0])
        
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected')
  
    
f5= Frame(milk,bd=2, relief='solid') 
f5.place(x=920,y=290,width=600, height=460)

h4 = Label(f5, text="Passbook",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=0, width=600)

scroll_y= Scrollbar(f5,orient=VERTICAL)
scroll_y.pack(side=RIGHT,fill=Y)

fr= Frame(f5,bd=2, relief='solid',bg="#98AFC7") 
fr.place(x=0,y=30,width=580, height=90)

search = Label(fr, text="User ID:",font=("bold", 13),fg="black",bg="#98AFC7").place(x=3,y=5)
searchent= Entry(fr,relief=RIDGE,font=("bold", 13),textvariable=searchent_var).place(x=70, y=5, width=100)

sname=Entry(fr,relief=RIDGE,font=("bold", 15),textvariable=s_name).place(x=10,y=40,width=150)               
             
form = Label(fr, text="From:",font=("bold", 13),fg="black",bg="#98AFC7").place(x=190,y=5)
form = DateEntry(fr,selectmode='day',textvariable=from_var).place(x=238,y=5)

to = Label(fr, text="TO:",font=("bold", 13),fg="black",bg="#98AFC7").place(x=350,y=5)
to = DateEntry(fr,selectmode='day',textvariable=to_var).place(x=380,y=5)

but4 = Button(fr, text ="Seller",font=("bold", 10),command=record).place(x=180, y=40, width=100)
but5 = Button(fr, text ="Buyer",font=("bold", 10),command=b_record).place(x=300, y=40, width=100)

h5 = Label(f5, text="Total",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=360, width=580)

title1 = Label(milk, text="MANRAJ SINGH(12100168)",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black')
title1.place(x=1150,y=755, width=400)

milk.mainloop()
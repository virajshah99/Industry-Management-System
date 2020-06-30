from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter.ttk import *
import tkinter.ttk as ttk
conn = sqlite3.connect('product.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS data(name TEXT,stage INTEGER,quantity INTEGER,price INTEGER)""")
c.execute("""CREATE TABLE IF NOT EXISTS staff(username TEXT,pass TEXT)""")

STAFF_INSERT_DATA="INSERT INTO staff values(?,?)"
STAFF_SELECT_USER="SELECT * FROM staff WHERE username=?"
STAFF_SELECT_DATA="SELECT * FROM staff WHERE username=? and pass=?"


#GUI'S----------------------------------------------------------------------------------------------------------------
root=Tk()
root.title("Production Management")
width = 800
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)			
#---------------------------------------------------------------------------------------------
def Exit():
	MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
	if MsgBox == 'yes':
		root.destroy()
#---------------------------------------------------------------------------------------------

def admin_login_form():
	def alogin():	
		username=t5.get()
		password=t6.get()
		if (username == "abc"):
			if ((username == "abc") and (password == "abc")):
				messagebox.showinfo("LOGGED IN!","SUCCESSFUL LOGIN")
				alogin_wd.destroy
				admin_work()
			else:
				messagebox.showwarning("UNSUCCESFUL","INCORRECT PASSWORD")
		else:
			messagebox.showwarning("UNSUCCESFUL","USER NOT FOUND")
	def back():
		alogin_wd.destroy()
		root.deiconify()
	global alogin_wd
	alogin_wd=Toplevel()
	root.withdraw()
	alogin_wd.geometry("280x130")
	alogin_wd.resizable(0, 0)
	alogin_wd.title("ADMIN LOGIN FORM")
	l5=Label(alogin_wd,text="Username")
	l6=Label(alogin_wd,text="Password")
	t5=Entry(alogin_wd)
	t6=Entry(alogin_wd,show='*')
	b5=Button(alogin_wd,text="Login",command=alogin)
	b15=Button(alogin_wd,text="Back",command=back)
	l5.grid(row=1,column=2)
	l6.grid(row=2,column=2)
	t5.grid(row=1,column=4)
	t6.grid(row=2,column=4)
	b5.grid(row=3,column=3)
	b15.grid(row=4,column=3)
#---------------------------------------------------------------------------------------------
def admin_work():
	def Logout_a():
		MsgBox = messagebox.askquestion ('Logout','Are you sure you want to logout',icon = 'warning')
		if MsgBox == 'yes':
			alogin_w.destroy()
			root.deiconify()
	global alogin_w
	alogin_w=Toplevel()
	alogin_wd.withdraw()
	alogin_w.geometry("700x500")
	alogin_w.title("ADMIN WORK")
	c.execute("SELECT * FROM `data`")
	fetch = c.fetchall()
	height=len(fetch)
	width=4
	ln=Label(alogin_w,text="Name      ")
	ls=Label(alogin_w,text="Stage    ")
	lq=Label(alogin_w,text="Quantity")
	lp=Label(alogin_w,text="Price")
	ln.grid(row=1,column=5)
	ls.grid(row=1,column=6)
	lq.grid(row=1,column=7)
	lp.grid(row=1,column=8)
	for i in range(height):
		for  j in  range(width):
			b=Entry(alogin_w)
			b.insert(END,fetch[i][j])
			b.grid(row=i+2,column=j+5)
	b6= Button(alogin_w,text="Add Product",command=Add_Product)
	b8= Button(alogin_w,text="Delete Product",command=Delete_Product)
	b12=Button(alogin_w,text="Logout",command=Logout_a)
	b6.grid(row=1,column=1)
	b8.grid(row=3,column=1)
	b12.grid(row=6,column=1)

#---------------------------------------------------------------------------------------------
def Delete_Product():
	def delete_it():
		nn=combo.get()
		if(nn[0]=='{'):
			nn = nn[1:-1]
		c.execute("""DELETE FROM data WHERE name=?""",(nn,))
		conn.commit()
		c.close
		messagebox.showinfo("Data Deleted!","Data Deleted!")
		admin_delete.destroy()
		admin_work()
	def leave():
		admin_delete.destroy()
		admin_work()
	admin_delete=Toplevel()
	alogin_w.withdraw()
	admin_delete.title("ADMIN WORK\DELETE PRODUCT")
	l13=Label(admin_delete,text="Enter name of item to be deleted")
	c.execute("""SELECT name FROM data""")
	fetch=c.fetchall()
	combo = Combobox(admin_delete)
	combo['values']=fetch
	combo.current(0) #set the selected item
	combo.grid(row=1,column=4,)
	b10=Button(admin_delete,text="Submit",command=delete_it)
	b11=Button(admin_delete,text="Exit",command=leave)
	l13.grid(row=1,column=1)
	b10.grid(row=2,column=1)
	b11.grid(row=2,column=2)
#---------------------------------------------------------------------------------------------
def Add_Product():
	def add_it():
		name=t7.get()
		stage=t8.get()
		quantity=t9.get()
		price=t10.get()
		c.execute("""INSERT INTO data VALUES(?,?,?,?)""",(name,stage,quantity,price))
		conn.commit()
		messagebox.showinfo("New Data Saved!","New Data Saved!")
		admin_add.withdraw()
		admin_work()
	def leave():
		admin_add.destroy()
		admin_work()
	global admin_add
	admin_add=Toplevel()
	alogin_w.withdraw()
	admin_add.title("ADMIN WORK\ADD PRODUCT")
	l13=Label(admin_add,text="Name")
	l14=Label(admin_add,text="Stage")
	l15=Label(admin_add,text="Quantity")
	l16=Label(admin_add,text="Price")		
	t7=Entry(admin_add)
	t8=Entry(admin_add)
	t9=Entry(admin_add)
	t10=Entry(admin_add)
	b7=Button(admin_add,text="Submit",command=add_it)
	b9=Button(admin_add,text="Exit",command=leave)
	l13.grid(row=1,column=2)
	l14.grid(row=2,column=2)
	l15.grid(row=3,column=2)
	l16.grid(row=4,column=2)
	t7.grid(row=1,column=4)
	t8.grid(row=2,column=4)
	t9.grid(row=3,column=4)
	t10.grid(row=4,column=4)
	b7.grid(row=6,column=3)
	b9.grid(row=7,column=3)
#---------------------------------------------------------------------------------------------
def staff_login_form():
	def slogin():	
		username=t1.get()
		password=t2.get()
		c.execute(STAFF_SELECT_USER,(username,))
		if (len(c.fetchall())):
			c.execute(STAFF_SELECT_DATA,(username,password))
			if (len(c.fetchall())):
				messagebox.showinfo("LOGGED IN!","SUCCESSFUL LOGIN")
				slogin_wd.destroy
				staff_work()
			else:
				messagebox.showwarning("UNSUCCESFUL","INCORRECT PASSWORD")
		else:
			messagebox.showwarning("UNSUCCESFUL","USER NOT FOUND")
	def back():
		slogin_wd.destroy()
		root.deiconify()
	global slogin_wd
	slogin_wd=Toplevel()
	root.withdraw()
	slogin_wd.geometry("280x150")
	slogin_wd.resizable(0, 0)
	slogin_wd.title("STAFF LOGIN FORM")
	l1=Label(slogin_wd,text="Username")
	l2=Label(slogin_wd,text="Password")
	t1=Entry(slogin_wd)
	t2=Entry(slogin_wd,show='*')
	b1=Button(slogin_wd,text="Login",command=slogin)
	b2=Button(slogin_wd,text="New User",command=staff_register_form)
	b16=Button(slogin_wd,text="Back",command=back)
	l1.grid(row=1,column=2)
	l2.grid(row=2,column=2)
	t1.grid(row=1,column=4)
	t2.grid(row=2,column=4)
	b1.grid(row=3,column=3)
	b2.grid(row=4,column=3)
	b16.grid(row=5,column=3)
#---------------------------------------------------------------------------------------------
def staff_register_form():
	def submit():
		username=t3.get()
		password=t4.get()
		c.execute(STAFF_SELECT_USER,(username,))
		if(len(c.fetchall())):
			messagebox.showerror("user exists","please choose another")
		else:
			c.execute(STAFF_INSERT_DATA,(username,password))
			conn.commit
			messagebox.showinfo("NEW USER SAVED","REGISTRATION SUCCESSFUL")
			staff_reg.withdraw()
			slogin_wd.deiconify()
	def back():
		staff_reg.destroy()
		staff_login_form()
	global staff_reg
	staff_reg=Toplevel()
	slogin_wd.withdraw()
	staff_reg.geometry("500x500")
	#staffconfigure(background="white")
	staff_reg.title("STAFF REGISTER FORM")
	l3=Label(staff_reg,text="Username:")
	l4=Label(staff_reg,text="Password")
	t3=Entry(staff_reg)
	t4=Entry(staff_reg,show='*')
	b3= Button(staff_reg,text="Submit",command=submit)
	bback=Button(staff_reg,text="Back",command=back)
	l3.grid(row=1,column=2)
	l4.grid(row=2,column=2)
	t3.grid(row=1,column=4)
	t4.grid(row=2,column=4)
	b3.grid(row=3,column=3)
	bback.grid(row=4,column=3)
#--------------------------------------------------------------------------------------------

def staff_work():
	def Logout_s():
		MsgBox = messagebox.askquestion ('Logout','Are you sure you want to logout',icon = 'warning')
		if MsgBox == 'yes':
			staff_w.destroy()
			root.deiconify()
	global staff_w
	slogin_wd.withdraw()
	staff_w=Toplevel()
	staff_w.geometry("700x500")
	c.execute("SELECT * FROM `data`")
	fetch = c.fetchall()
	height=len(fetch)
	width=3
	staff_w.title("STAFF WORK")
	b14=Button(staff_w,text="Update Stage",command=update_stage)
	b13=Button(staff_w,text="Logout",command=Logout_s)
	b13.grid(row=3,column=1)
	b14.grid(row=1,column=1)
	ln=Label(staff_w,text="Name")
	ls=Label(staff_w,text="Stage")
	lq=Label(staff_w,text="Quantity")
	ln.grid(row=1,column=5)
	ls.grid(row=1,column=6)
	lq.grid(row=1,column=7)
	for i in range(height):
		for  j in  range(width):
			if j!=4 :
				b=Entry(staff_w)
				b.insert(END,fetch[i][j])
				b.grid(row=i+2,column=j+5)
#--------------------------------------------------------------------------------------------
def update_stage():
	def submit():
		nn=combo.get()
		if(nn[0]=='{'):
			nn = nn[1:-1]
		c.execute("""SELECT * FROM data WHERE name = ?""",(nn,))
		s=c.fetchall()
		a = s[0][1]
		a=a+1
		c.execute("""UPDATE data SET stage = ? WHERE name = ?""", (a,nn))
		conn.commit()
		update_s.destroy()
		staff_work()
	def back():
		update_s.destroy()
		staff_work()
	global update_s
	staff_w.withdraw()
	update_s=Toplevel()
	update_s.title(r"STAFF WORK\UPDATE STAGE")
	update_s.geometry("300x200")
	lname=Label(update_s,text="Name")
	c.execute("""SELECT name FROM data""")
	fetch=c.fetchall()
	combo = Combobox(update_s)
	combo['values']=fetch
	combo.current(0) #set the selected item
	combo.grid(row=2, column=4)
	bname=Button(update_s,text="Submit",command=submit)
	bback=Button(update_s,text="Back",command=back)
	lname.grid(row=2,column=2)
	bname.grid(row=3,column=3)
	bback.grid(row=4,column=3)
#--------------------------------------------------------------------------------------------
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Admin login", command=admin_login_form)
filemenu.add_command(label="Staff login", command=staff_login_form)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="OPTIONS", menu=filemenu)
root.config(menu=menubar)

Title = Frame(root)
Title.pack(pady=10)

lbl_display = Label(Title, text="Production Management", font=('Cambria', 45))
lbl_display.pack()
#lbl = Label(Title, justify=LEFT, padx=10).pack()

root.mainloop()
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
from PIL import ImageTk, Image


def f1():
	root.withdraw()
	aw.deiconify()

def f2():
	aw.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	con=None
	try:
		con=connect("kc.db")
		cursor=con.cursor()
		sql="select * from student order by rno"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info+"rno:"+str(d[0])+"  name:"+str(d[1])+"\n"
		vw_st_data.insert(INSERT,info)

	except Exception as e:
		showerror("issue",e)


	finally:

		if con is not None:
			con.close()


def f4():
	vw.withdraw()
	root.deicoify()

def f5():
	con=None
	try:
		con=connect("kc.db")	
		cursor=con.cursor()
		sql="insert into student values('%d','%s')"		
		rno=int(aw_ent_rno.get())	
		name=aw_ent_name.get()
		cursor.execute(sql%(rno,name))
		con.commit()
		showinfo("Success","record created")

	except Exception as e:
		con.rollback()
		showerror("issue",e)
	

	finally:

		if con is not None:
			con.close()
		aw_ent_rno.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_rno.focus()

root=Tk()
root.title("S.M.S")
root.geometry("1000x600+50+50")
f=("Simsun",30,"bold")





btn_add=Button(root,text="Add Student",font=f,command=f1)
btn_view=Button(root,text="View Student",font=f,command=f3)
btn_add.pack(pady=30)
btn_view.pack(pady=30)



aw=Toplevel(root)
aw.geometry("1000x600+50+50")
aw_lab_rno=Label(aw,text="Enter roll no",font=f)
aw_ent_rno=Entry(aw,font=f,bd=2)

aw_lab_name=Label(aw,text="Enter name",font=f)
aw_ent_name=Entry(aw,font=f)

aw_btn_save=Button(aw,text="Save",font=f,command=f5)
aw_btn_back=Button(aw,text="Back",font=f,command=f2)

aw_lab_rno.pack(pady=10)
aw_ent_rno.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lab_rno.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
def f7(event):
	f5()
aw_btn_save.bind('<Return>',f7)	
aw.withdraw()


vw=Toplevel(root)
vw.geometry("1000x600+50+50")
vw.title("View")
vw_st_data=ScrolledText(vw,width=20,height=10,font=f)
vw_btn_back=Button(vw,text="Back",font=f,command=f4)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)

vw.withdraw()


def f6():
	answer=askyeso(title='confirmation',message="Are you sure you want to exits ?")
	if answer:
		root.destroy()
root.protocol("WN_DELETE_WINDOW",f6)
root.mainloop()
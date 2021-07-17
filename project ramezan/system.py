from tkinter import *	
from tkinter import messagebox
import systemdata

root=Tk()
root.geometry("450x700")
root.config(bg='skyblue')
root.title("JOB  MANAGEMENT SYSTEM")



def exit():
	exit=messagebox.askyesno("hesabe khodam","Are you sure?")
	if exit>0:
		root.destroy()
		return
	
def adddata():
		systemdata.adddata(endate.get(),enkarfarma.get(),ennkar.get(),entedad.get(),enzaman.get(),envexit.get(),entarikh.get(),endaryafti.get())
		list.delete(0,END)
		list.insert(END,(endate.get(),enkarfarma.get(),ennkar.get(),entedad.get(),enzaman.get(),envexit.get(),entarikh.get(),endaryafti.get()))
		
	
	

	
def viewdata():
	list.delete(0,END)
	for row in systemdata.viewdata():
		list.insert(END,row)
	
	
def selectitem(event):
	global selecteditem
	index=list.curselection()[0]
	selecteditem=list.get(index)
	endate.delete(0,END)
	endate.insert(END,selecteditem[1])
	enkarfarma.delete(0,END)
	enkarfarma.insert(END,selecteditem[2])
	ennkar.delete(0,END)
	ennkar.insert(END,selecteditem[3])
	entedad.delete(0,END)
	entedad.insert(END,selecteditem[4])
	enzaman.delete(0,END)
	enzaman.insert(END,selecteditem[5])
	envexit.delete(0,END)
	envexit.insert(END,selecteditem[6])
	entarikh.delete(0,END)
	entarikh.insert(END,selecteditem[7])
	endaryafti.delete(0,END)
	endaryafti.insert(END,selecteditem[8])
		

def deldata():
		e=messagebox.askyesno('ACCOUNTING SYSTEM','ARE YOU SURE YOU WANT TO DELETE THIS CLIENT?\nALL DATA FOR THIS CLIENT WILL BE GONE!!')
		if e>0:
			systemdata.deldata(selecteditem[0])
			endate.delete(0,END)
			enkarfarma.delete(0,END)
			ennkar.delete(0,END)
			entedad.delete(0,END)
			enzaman.delete(0,END)
			envexit.delete(0,END)
			entarikh.delete(0,END)
			endaryafti.delete(0,END)
		else:
			return
		viewdata()
	

def update():
		systemdata.update(selecteditem[0],endate.get(),enkarfarma.get(),ennkar.get(),entedad.get(),enzaman.get(),envexit.get(),entarikh.get(),endaryafti.get())
		viewdata()
		messagebox.showinfo('client management system',f'The client updated\n{endate.get()}\n{enkarfarma.get().upper()}\n{ennkar.get().upper()}\n{entedad.get()}\n{enzaman.get()}\n{envexit.get()}\n{entarikh.get().upper()}\n{endaryafti.get()}')
	
	
	
	
def search():	
		list.delete(0,END)
		for row in systemdata.search(endate.get(),enkarfarma.get(),ennkar.get(),entedad.get(),enzaman.get(),envexit.get(),entarikh.get(),endaryafti.get()):
			list.insert(END,row)



def clear():
	endate.delete(0,END)
	enkarfarma.delete(0,END)
	ennkar.delete(0,END)
	entedad.delete(0,END)
	enzaman.delete(0,END)
	envexit.delete(0,END)
	entarikh.delete(0,END)
	endaryafti.delete(0,END)
	list.delete(0,END)



	
mainframe=Frame(root,bd=5,bg='skyblue',width=450,height=700,relief=RIDGE)
mainframe.pack()
ftitle=Frame(mainframe,bd=5,bg="skyblue",width=445,height=50,relief=RIDGE)
ftitle.pack()
lbltitle=Label(ftitle,text="JOB  MANAGEMENT SYSTEM",bg='skyblue',font='times 15 bold italic', padx=33)
lbltitle.pack()


finfo=Frame(mainframe,bd=5,bg='skyblue',width=445,height=300,relief=RIDGE)
finfo.pack()
lbldate=Label(finfo,text='Date',bg='skyblue',font="times 10 bold italic")
lbldate.grid(row=0,column=0)
endate=Entry(finfo,font="times 10 bold",width=13)
endate.grid(row=0,column=1)

lblkarfarma=Label(finfo,text='karfarma',bg='skyblue',font="times 10 bold italic")
lblkarfarma.grid(row=0,column=2)
enkarfarma=Entry(finfo,font="times 10 bold",width=15)
enkarfarma.grid(row=0,column=3)

lblnkar=Label(finfo,text='nkar',bg='skyblue',font="times 10 bold italic")
lblnkar.grid(row=1,column=0)
ennkar=Entry(finfo,font="times 10 bold",width=13)
ennkar.grid(row=1,column=1)

lbltedad=Label(finfo,text='tedad',bg='skyblue',font="times 10 bold italic")
lbltedad.grid(row=1,column=2)
entedad=Entry(finfo,font="times 10 bold",width=15)
entedad.grid(row=1,column=3)

lblzaman=Label(finfo,text='zaman',bg='skyblue',font="times 10 bold italic")
lblzaman.grid(row=2,column=0)
enzaman=Entry(finfo,font="times 10 bold",width=13)
enzaman.grid(row=2,column=1)

lblvexit=Label(finfo,text='vexit',bg='skyblue',font="times 10 bold italic")
lblvexit.grid(row=2,column=2)
envexit=Entry(finfo,font="times 10 bold",width=15)
envexit.grid(row=2,column=3)
#==========::::::==============
fdaryafti=Frame(mainframe,bd=5,bg='skyblue',width=445,height=50,relief=RIDGE)
fdaryafti.pack()

lbltarikh=Label(fdaryafti,text='tarikh',bg='skyblue',font="times 10 bold italic")
lbltarikh.grid(row=0,column=0)
entarikh=Entry(fdaryafti,font="times 10 bold",width=13)
entarikh.grid(row=0,column=1)
entarikh.insert(END,0)

lbldaryafti=Label(fdaryafti,text='daryafti',bg='skyblue',font="times 10 bold italic")
lbldaryafti.grid(row=0,column=2)
endaryafti=Entry(fdaryafti,font="times 10 bold",width=15)
endaryafti.grid(row=0,column=3)
endaryafti.insert(END,0)

#===============::::=============
fbutton=Frame(mainframe,bd=5,bg='skyblue',width=445,height=50,relief=RIDGE)
fbutton.pack()
btnadd=Button(fbutton,text="add",width=2,command=adddata)
btnadd.grid(row=0,column=0)

btnadd=Button(fbutton,text="edit",width=2)
btnadd.grid(row=0,column=1)

btnadd=Button(fbutton,text="delete",width=2,command=deldata)
btnadd.grid(row=0,column=2)

btnadd=Button(fbutton,text="update",width=3,command=update)
btnadd.grid(row=0,column=3)

btnadd=Button(fbutton,text="search",width=3,command=search)
btnadd.grid(row=0,column=4)

btnadd=Button(fbutton,text="view",width=3,command=viewdata)
btnadd.grid(row=0,column=5)

btnadd=Button(fbutton,text="clr",width=3,command=clear)
btnadd.grid(row=0,column=6)

btnadd=Button(fbutton,text="exit",width=2,command=exit)
btnadd.grid(row=0,column=7)

flist=Frame(mainframe,bd=5,bg='skyblue',width=445,height=500,relief=RIDGE)
flist.pack()
scroll=Scrollbar(flist)
scroll.pack(side=RIGHT,fill=Y)
scrollx=Scrollbar(flist,orient=HORIZONTAL)
scrollx.pack(side=BOTTOM,fill=X)
list=Listbox(flist,width=440,height=400,bg="gray",yscrollcommand=scroll.set,xscrollcommand=scrollx.set,font="times 15 bold italic")
list.pack(side=LEFT,fill=BOTH)
scroll.config(command=list.yview)
scrollx.config(command=list.xview)
list.bind('<<ListboxSelect>>',selectitem)

root.mainloop()
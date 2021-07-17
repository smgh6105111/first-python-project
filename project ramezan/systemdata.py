import sqlite3


def dataentry():
	con=sqlite3.connect("job.db")
	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS job(id INTEGER PRIMARY KEY,date text,karfarma text, nkar text,tedad text,zaman text,vexit text,tarikh text,daryafti text)")
	con.commit()
	con.close()
	
def adddata(date,karfarma,nkar,tedad,zaman,vexit,tarikh,daryafti):
		con=sqlite3.connect("job.db")
		cur=con.cursor()
		cur.execute("INSERT INTO job VALUES(NULL,?,?,?,?,?,?,?,?)",(date,karfarma,nkar,tedad,zaman,vexit,tarikh,daryafti))
		con.commit()
		con.close()
	
def viewdata():
	con=sqlite3.connect("job.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM job")
	rows=cur.fetchall()
	con.close()
	return rows	
	
	

	
def deldata(id):
	con=sqlite3.connect("job.db")
	cur=con.cursor()
	cur.execute("DELETE FROM job WHERE id=?",(id,))
	con.commit()
	con.close()	
	

def update(id,date="",karfarma="",nkar="",tedad="",zaman="",vexit="",tarikh="",daryafti=""):
	con=sqlite3.connect("job.db")
	cur=con.cursor()
	cur.execute("UPDATE job SET date=?,karfarma=?,nkar=?,tedad=?,zaman=?,vexit=?,tarikh=?,daryafti=?  WHERE id=?",(date,karfarma,nkar,tedad,zaman,vexit,tarikh,daryafti,id))
	con.commit()
	con.close()
	

def search(date="",karfarma="",nkar="",tedad="",zaman="",vexit="",tarikh="",daryafti=""):
	con=sqlite3.connect("job.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM job WHERE date=? or karfarma=? or nkar=? or tedad=? or zaman=? or vexit=? or tarikh=? or daryafti=?",(date,karfarma,nkar,tedad,zaman,vexit,tarikh,daryafti))
	rows=cur.fetchall()
	con.close()
	return rows	

dataentry()

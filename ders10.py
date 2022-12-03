import sqlite3
from tkinter import *


connection=sqlite3.connect("library.db")
cursor=connection.cursor()

def creatTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf (name TEXT,author TEXT,publisher TEXT,pageNumber INT)")
    connection.commit()
def importData():
    cursor.execute("insert into bookshelf Values ('Safahat','Mehmet Akif ERSOY','ANKA',644)")
    connection.commit()
def importData2(name, author, publisher, pageNumber):
    cursor.execute("insert into bookshelf Values(?,?,?,?)",(name,author, publisher, pageNumber))
    connection.commit()
def importData3():
    name=input("kitap ismi giriniz ")
    author=input("yazar ismi giriniz ")
    publisher=input("yayın evi ismi giriniz ")
    pageNumber=input("sayfa sayisi ismi giriniz ")
    cursor.execute("insert into bookshelf Values(?,?,?,?)",(name,author, publisher, pageNumber))
    connection.commit()
def getData():
    cursor.execute("select * from bookshelf")
    liste=cursor.fetchall()
    #print(liste)
    print("Mevcut kütüphanedeki kitap bilgileri")
    for i in liste:
        print(i)       
def getFilterData():
    cursor.execute("select name,author from bookshelf")
    liste=cursor.fetchall()
    print("Mevcut kütüphanedeki kitap bilgileri")
    for i in liste:
        print(i)
def getFilterData2(publisher):
    cursor.execute("select * from bookshelf where publisher=?",(publisher,))
    liste=cursor.fetchall()
    print("Mevcut kütüphanedeki kitap bilgileri")
    for i in liste:
        print(i)
def getFilterData3(author):
    cursor.execute("select publisher,pageNumber from bookshelf where author=?",(author,))
    liste=cursor.fetchall()
    print("Mevcut kütüphanedeki kitap bilgileri")
    for i in liste:
        print("BU KİTABİN YAYİN EVİ:",i[0]," SAYFA SAYİSİ:",i[1])
def updateData(oldPub,newPub):
    cursor.execute("UPDATE bookshelf set publisher=? where publisher=?",(newPub,oldPub))
    connection.commit()
def deleteData(author):
    cursor.execute("insert into bookshelf Values(?,?,?,?)",(name,author, publisher, pageNumber))
    connection.commit()
def click():
    name=myEntry.get()
    author=myEntry1.get()
    publisher=myEntry2.get()
    pageNumber=int(myEntry3.get())
    importData2(name, author, publisher, pageNumber)

root=Tk()
root.geometry("800x300")
root.title("demo1")
myEntry=Entry(root,text="Name ",font=("ARIAL",25))
myEntry.grid(row=0,column=1)
myEntry1=Entry(root,text="Author",font=("ARIAL",25))
myEntry1.grid(row=1,column=1)
myEntry2=Entry(root,text="Page Number ",font=("ARIAL",25))
myEntry2.grid(row=2,column=1)
myEntry3=Entry(root,text="Publisher ",font=("ARIAL",25))
myEntry3.grid(row=3,column=1)
myButton=Button(root,text="Click",font=("ARIAL",25),command=click)
myButton.grid(row=4,column=1)
myLabel=Label(root,text="Name")
myLabel.grid(row=0,column=0)
myLabel1=Label(root,text="author")
myLabel1.grid(row=1,column=0)
myLabel2=Label(root,text="publisher")
myLabel2.grid(row=2,column=0)
myLabel3=Label(root,text="pageNumber")
myLabel3.grid(row=3,column=0)



root.mainloop()   

connection.close()
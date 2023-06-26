import pickle
import os
def writefile_list():
    fw=open("book.dat","wb")
    n=int(input("how many records"))
    l=[0 for i in range(n)]
    for i in range(n):
        l=[]
        bid=int(input("enter the book id"))
        bnm=input("enter book name")
        bprice=float(input("accept price"))
        l.extend([bid,bnm,bprice])
        pickle.dump(l,fw)
    fw.close()
def readfile_list():
    with open("book.dat","rb")as f:
        while True:
            try:
                r=pickle.load(f)
                c=input("wait")
                print(r)
            except EOFError:
                break
def countrecord():
    count=0
    with open("book.dat","rb")as f:
        while True:
            try:
                r=pickle.load(f)
                count=count+1
                print(r)
            except EOFError:
                break
    print("no.of records",count)
def deleterecord():
    id=int(input("enter the book id to be deleted"))
    fr=open("temp.dat","wb")
    with open("book.dat","rb")as f:
        while True:
            count=0
            try:
                r=pickle.load(f)
                for a in r:
                    if a==id:
                        count=count+1
                if count==0:
                    pickle.dump(r,fr)
            except EOFError:
                break
    os.remove("book.dat")
    os.rename("temp.dat","book.dat")
def searchrecord():
    bnm=input("enter the book id to be searched")
    count=0
    with open("book.dat","rb")as f:
        while True:
            try:
                r=pickle.load(f)
                for a in r:
                    if a==bnm:
                        count=count+1
                        print(r)
                    if count==1:
                        break
            except EOFError:
                 break
    if count==0:
        print("not present in the file")
    else:
        print("yes",bnm,"present in the file")
def updaterecord():
    no=int(input("enter which book id's details to be updated"))
    count=0
    with open("book.dat","rb+")as f:
        while True:
            try:
                p=f.tell()
                print(p)
                r=pickle.load(f)
                for a in r:
                    if a==no:
                        nm=input("enter book name")
                        price=float(input("enter price"))
                        r[1]=nm
                        r[2]=price
                        f.seek(p)
                        pickle.dump(r,f)
            except EOFError:
                break
def sortrecord():
    l1=[]
    with open("book.dat","rb+")as f:
        while True:
            dic=[]
            try:
                dic=pickle.load(f)
                print(dic)
                l1.append(dic)
            except EOFError:
                break
    print(l1)
    for i in range(0,len(l1)):
        for j in range(0,len(l1)-i-1):
            if l1[j][2]<l1[j+1][2]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
    print("hello")
    print(l1)
    with open("cloth.dat","rb+")as f:
        for k in l1:
            pickle.dump(k,f)
reply="y"
while reply=='Y' or reply=="y":
    print("Bookshop Management System")
    print("1.write binaryfile")
    print("2.read binaryfile")
    print("3.count record")
    print("4.delete record")
    print("5.search record")
    print("6.update record")
    print("7.sort record")
    ch=int(input("enter the choice"))
    if ch==1:
        writefile_list()
    elif ch==2:
        readfile_list()
    elif ch==3:
        countrecord()
    elif ch==4:
        deleterecord()
    elif ch==5:
        searchrecord()
    elif ch==6:
        updaterecord()
    elif ch==7:
        sortrecord()
    reply=input("wish to continue y-for yes n for no")
                
    

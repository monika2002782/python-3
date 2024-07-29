


'''
#1.

for i in range(1,11):
    print(i)

#2.
i=1
while i<=16:
    print(i,"*",2,"=",i*2)
    i=i+1
#3.
for x in range(42):
    if(x==40):
        break
    print(x)
    

#4.
name="karma is boomerang"
print(name.split("r"))

#5.

name=input("enter your name:")
cls=int(input("enter your class:"))
tam=int(input("enter your tam mark:"))
eng=int(input("enter your eng mark:"))
maths=int(input("enter your maths mark:"))
sci=int(input("enter your sci mark:"))
social=int(input("enter your social mark:"))
total=tam+eng+maths+sci+social
if total<=35:
    print("pass")
elif total==0:
    print("your are not eligible for HSLC")
else:
    print("your are eligible for HSLC")

name=int(input("enter your number:"))
if name<30:
    print("positive number")
elif name==100:
    print("equal number")
elif name>10:
    print("another number")
else:
    print("negative number")
        
 
name=input("enter your name:")
place=input("enter your place:")
age=int(input("enter your age:"))
course=input("enter your course:")
if age>30:
    print("computer student")
elif age==30:
    print("maths student")
else:
    print("unknown student")
    

name=("a great opportunity  to  get a  treasure")
print(name[::-1])

for i in range(10):
    print(i)
    
name="alphabets letter must be print only uppercase"
print(name[-40:-6])

def add(a,b):
    return a+b
res=add(4,5)
print(res)
'''
'''

from tkinter import *
from tkinter import ttk,font,messagebox
from PIL import ImageTk,Image
import os


def customerloginpage(data,win):
    win.destroy()
    win=Tk()
    win.attributes('-fullscreen',True)
    win.geometry("500x500")
    f=Frame(win,width=1500,height=50,bg="blue")
    f.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f1=Label(win,text="HDFC Bank",font=label_font,bg="blue",fg="white")
    f1.place(relx=0.40,rely=0.5)
    f1.pack()
    frame1=Frame(win,width=400,height=470,bg="pink")
    frame1.place(relx=0.35,rely=0.25)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Label(win,text="CustomerLogin Page",bg="green",fg="white",font=label_font)
    b.place(relx=0.41,rely=0.16)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Name  "+data[0],font=label_font)
    l1.place(relx=0.37,rely=0.31)
    l2=Label(win,text="Aadhar No  "+data[1],font=label_font)
    l2.place(relx=0.37,rely=0.41)
    l3=Label(win,text="Pan No  "+data[2],font=label_font)
    l3.place(relx=0.37,rely=0.51)
    l4=Label(win,text="Contact  "+data[3],font=label_font)
    l4.place(relx=0.37,rely=0.61)
    l5=Label(win,text="Email ID  "+data[4],font=label_font)
    l5.place(relx=0.37,rely=0.71)
    l6=Label(win,text="Address  "+data[5],font=label_font)
    l6.place(relx=0.37,rely=0.81)
    print(data)


    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="@Copyrights 2024",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.36,rely=0.95)
    win.mainloop()


def  customerlogin1(a,b,win):

    if os.path.exists('bankpro.txt'):
        with open('bankpro.txt','r') as file:
            lines=file.readlines()
            for x in lines:  
                x1=x.split("\t")            
                username1=x1[0]
                password1=x1[3]
                if(username1==a and password1==b):
                    customerloginpage(x1,win)
                
def customerlog(win):
    win.destroy()
    win=Tk()
    win.geometry("500x500")
    win.attributes('-fullscreen',True)
    f=Frame(win,width=1500,height=50,bg="blue")
    f.pack()
    frame1=Frame(win,width=400,height=250,bg="pink")
    frame1.place(relx=0.35,rely=0.35)
    
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f1=Label(win,text="HDFC Bank",font=label_font,bg="blue",fg="white")
    f1.place(relx=0.40,rely=0.5)
    f1.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b2=Label(win,text="Customer Login",bg="green",fg="white",font=label_font)
    b2.place(relx=0.43,rely=0.23)

    label_font=font.Font(win,weight="bold",family="Times New Roman",size=15)
    l=Label(win,text="Customer ID",font=label_font).place(relx=0.37,rely=0.41)
    l=Label(win,text="Password",font=label_font).place(relx=0.37,rely=0.51)
    e1=Entry(win)
    e1.place(relx=0.49,rely=0.41,width=150,height=30)
    e2=Entry(win)
    e2.place(relx=0.49,rely=0.51,width=150,height=30)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Login",bg="green",font=label_font,command=lambda:customerlogin1(e1.get(),e2.get(),win))
    b.place(relx=0.49,rely=0.60)
    
    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="@Copyrights 2024",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.38,rely=0.90)
    win.mainloop()

def custreg(win):
    win.destroy()
    win=Tk()
    win.attributes('-fullscreen',True)
    win.geometry("500x500")
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    frame1=Frame(win,width=400,height=530,bg="pink")
    frame1.place(relx=0.35,rely=0.20)
    f=Frame(win,width=1500,height=500,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="HDFC Bank",font=label_font,bg="blue",fg="white")
    f.place(relx=0.40,rely=0.5)
    f.pack()

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Label(win,text="Customer Registration",bg="green",fg="white",font=label_font)
    b.place(relx=0.40,rely=0.14)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Name",font=label_font).place(relx=0.38,rely=0.23)
    l2=Label(win,text="Aadhar No",font=label_font).place(relx=0.38,rely=0.33)
    l3=Label(win,text="Pan No",font=label_font).place(relx=0.38,rely=0.43)
    l4=Label(win,text="Contact",font=label_font).place(relx=0.38,rely=0.53)
    l5=Label(win,text="Email ID",font=label_font).place(relx=0.38,rely=0.63)
    l6=Label(win,text="Address",font=label_font).place(relx=0.38,rely=0.73)
    e1=Entry(win)
    e1.place(relx=0.50,rely=0.24,width=150,height=30)
    e2=Entry(win)
    e2.place(relx=0.50,rely=0.34,width=150,height=30)
    e3=Entry(win)
    e3.place(relx=0.50,rely=0.44,width=150,height=30)
    e4=Entry(win)
    e4.place(relx=0.50,rely=0.54,width=150,height=30)
    e5=Entry(win)
    e5.place(relx=0.50,rely=0.64,width=150,height=30)
    e6=Entry(win)
    e6.place(relx=0.50,rely=0.74,width=150,height=30)
    
    def file(a,b,c,d,win):
        f=open('bankpro.txt','a')
        f.write('\n')
        f.write(e1.get())
        f.write('\t')
        f.write(str(e2.get()))
        f.write('\t')
        f.write(str(e3.get()))
        f.write('\t')
        f.write(str(e4.get()))
        f.write('\t')
        f.write(e5.get())
        f.write('\t')
        f.write(str(e6.get()))
        f.write('\t')

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Register",bg="green",fg="white",font=label_font,command=lambda:file(e1.get(),e2.get(),e3.get(),e4.get(),win))
    b.place(relx=0.50,rely=0.80)
    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="@Copyrights 2024",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.40,rely=0.93)
    win.mainloop()

def adminpage(win):
    win=Tk()
    win.attributes('-fullscreen',True)
    win.geometry("500x500")
    f=Frame(win,width=1500,height=50,bg="blue")
    f.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f1=Label(win,text="HDFC Bank",font=label_font,bg="blue",fg="white")
    f1.place(relx=0.40,rely=0.3)
    f1.pack()
    frame1=Frame(win,width=400,height=480,bg="pink")
    frame1.place(relx=0.35,rely=0.25)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Label(win,text="Admin Page",bg="green",fg="white",font=label_font)
    b.place(relx=0.45,rely=0.18)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Name",font=label_font).place(relx=0.38,rely=0.26)
    l2=Label(win,text="Aadhar No",font=label_font).place(relx=0.38,rely=0.36)
    l3=Label(win,text="Pan No",font=label_font).place(relx=0.38,rely=0.46)
    l4=Label(win,text="Contact",font=label_font).place(relx=0.38,rely=0.56)
    l5=Label(win,text="Email ID",font=label_font).place(relx=0.38,rely=0.66)
    l6=Label(win,text="Address",font=label_font).place(relx=0.38,rely=0.76)
    e1=Entry(win)
    e1.place(relx=0.50,rely=0.27,width=150,height=30)
    e2=Entry(win)
    e2.place(relx=0.50,rely=0.37,width=150,height=30)
    e3=Entry(win)
    e3.place(relx=0.50,rely=0.47,width=150,height=30)
    e4=Entry(win)
    e4.place(relx=0.50,rely=0.57,width=150,height=30)
    e5=Entry(win)
    e5.place(relx=0.50,rely=0.67,width=150,height=30)
    e6=Entry(win)
    e6.place(relx=0.50,rely=0.77,width=150,height=30)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Login",bg="green",font=label_font,command=lambda:file(e1.get(),e2.get(),e3.get(),e4.get(),win))
    b.place(relx=0.50,rely=0.83,width=150,height=30)
    def file(a,b,c,d,win):
        f=open('bankpro.txt','a')
        f.write('\n')
        f.write(e1.get())
        f.write('\t')
        f.write(str(e2.get()))
        f.write('\t')
        f.write(str(e3.get()))
        f.write('\t')
        f.write(str(e4.get()))
        f.write('\t')
        f.write(e5.get())
        f.write('\t')
        f.write(str(e6.get()))
        f.write('\t')


    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="@Copyrights 2024",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.40,rely=0.93)
    win.mainloop()



def adminlogin(a,b,win):
    win.destroy()
    if(a=="admin" and b=="admin"):
        adminpage(win)
    else:
        print("invalid username or password")

def adminlog(win):
    win.destroy()
    win=Tk()
    win.attributes('-fullscreen',True)
    win.geometry("500x500")
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    
    frame1=Frame(win,width=400,height=250,bg="pink")
    frame1.place(relx=0.35,rely=0.35)

    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="HDFC Bank",font=label_font,bg="blue",fg="white")
    f.place(relx=0.40,rely=0.5)
    f.pack()

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Label(win,text="Admin Login",bg="green",fg="white",font=label_font)
    b.place(relx=0.44,rely=0.22)
  
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="UserName",bg="pink",font=label_font).place(relx=0.36,rely=0.40)
    l2=Label(win,text="Password",bg="pink",font=label_font).place(relx=0.36,rely=0.50)
   
    e1=Entry(win)
    e1.place(relx=0.52,rely=0.40,width=150,height=30)
    e2=Entry(win)
    e2.place(relx=0.52,rely=0.50,width=150,height=30)
    
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Login",bg="green",font=label_font,command=lambda:adminlogin(e1.get(),e2.get(),win))
    b.place(relx=0.52,rely=0.58)
    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="@Copyrights 2024",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.38,rely=0.90)
    win.mainloop()

def home():
    win=Tk()
    win.geometry("500x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    f=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="HDFC Bank",font=label_font,bg="blue",fg="white")
    f.place(relx=0.30,rely=0.1)
    f.pack()
    f1=Frame(win,width=1000,height=50)
    f1.pack()
    f1.place(relx=0.39,rely=0.2)
    img=ImageTk.PhotoImage(Image.open("bank2.jpg"))
    l=Label(f1,image=img)
    l.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    s="""A bank is a financial institution that accepts deposits from the public and creates a demand deposit 
     while simultaneously making loans. 
     A bank is a financial institution that is licensed to accept checking and savings deposits and make loans. 
     Lending activities can be directly performed by the bank or indirectly through capital markets."""
    l1=Label(win,text=s,font=label_font)
    l1.place(relx=0.01,rely=0.45)
    b=Button(win,text="Customer Registration",bg="green",fg="white",font=label_font,command=lambda:custreg(win))
    b.place(relx=0.15,rely=0.70)
    b1=Button(win,text="Admin Login",bg="green",fg="white",font=label_font,command=lambda:adminlog(win))
    b1.place(relx=0.44,rely=0.70)
    b2=Button(win,text="Customer Login",bg="green",fg="white",font=label_font,command=lambda:customerlog(win))
    b2.place(relx=0.65,rely=0.70)
    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="@Copyrights 2024",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.40,rely=0.93)
    win.mainloop()
home()
'''












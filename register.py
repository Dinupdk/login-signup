from tkinter import *
from tkinter import messagebox
import mysql.connector

def user_enter(e):
    user.delete(0,END)
def user_leave(e):
    if user.get()=='':
        user.insert(0,'UserID')
def password_enter(e):
    code.delete(0,END)
    code.config(show='*')
    eyebutton.config(image=closeeye)
def password_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
button_mode=True
def hide():
    global button_mode
    if button_mode:
        eyebutton.config(image=openeye,activebackground='#375174')
        code.config(show='')
        button_mode=False
    else:
        eyebutton.config(image=closeeye,activebackground='#375174')
        code.config(show='*')
        button_mode=True
def login():
    root.destroy()
    import login

dbhost='localhost'
dbuser='root'
dbpassword='pdk789'
dbdatabase='studentregistration'
def register():
    username=str(user.get())
    password=str(code.get())
    admincode=adminaccess.get()
    print(username,password,admincode)

    if admincode=='123':
        if (username=='' or username=='UserID') or (password=='' or password=='Password'):
            messagebox.showerror('error','type username and password')
        else:
            try:
                mydb=mysql.connector.connect(host=dbhost,user=dbuser,password=dbpassword)
                mycursor=mydb.cursor()
                print('connected with mysql123')
            except:
                messagebox.showerror('ERROR','fail to connect with database!!!!!!!')
            try:
                
                command='create database studentregistration'
                mycursor.execute(command)
                command='use studentregistration'
                mycursor.execute(command)
                command='create table login (user int auto_increment key not null ,username Varchar(100),password Varchar(100))'
                mycursor.execute(command)
            except:
                mycursor.execute('use studentregistration')
                mydb=mysql.connector.connect(host=dbhost,user=dbuser,password=dbpassword,database=dbdatabase)
                mycursor=mydb.cursor()
                command='insert into login (username,password) values(%s,%s)'
                mycursor.execute(command,(username,password))
                mydb.commit()
                mydb.close()
                messagebox.showinfo('info','sucessfully registered ')            
    else:
        messagebox.showerror('Admincode error','give correct admincode to add new user !!!!!!')







background='#06283D'
framebg='#EDEDED'
framefg='#06283D'
root=Tk()
root.title('New User Registration')
root.geometry('1250x700')
root.config(bg=background)
root.resizable(False,False)

image_icon=PhotoImage(file='icon.png')
root.iconphoto(False,image_icon)
frame=Frame(root,bg='red')
frame.pack(fill=Y)
backgroundimage=PhotoImage(file='register.png')
Label(frame,image=backgroundimage).pack()
adminaccess=Entry(frame,width=15,fg='#000',bd=0,bg='#e8ecf7',font=('arial 20 bold'),show="*")
adminaccess.focus()
adminaccess.place(x=550,y=275)

user = Entry(root,width=18,fg='black',bg='#375174',bd=0,font=('arial 20 bold'))
user.place(x=500,y=380)
user.insert(0,'UserID')
user.bind('<FocusIn>',user_enter)
user.bind("<FocusOut>",user_leave)

code = Entry(root,width=18,fg='#fff',bg='#375174',bd=0,font=('arial 20 bold'))
code.place(x=500,y=470)
code.insert(0,'Password')
code.bind('<FocusIn>',password_enter)
code.bind("<FocusOut>",password_leave)

openeye=PhotoImage(file='openeye.png')
closeeye=PhotoImage(file='close eye.png')
eyebutton=Button(root,image=openeye,bg='#375174',activebackground='#375174',bd=0,command=hide)
eyebutton.place(x=780,y=470)

regis=Button(root,text='ADD NEW USER ',bg='#455e88',width=13,height=1,fg='black',font=('arial 16 bold'),activebackground='#375174',
             cursor='hand2',bd=0,command=register)
regis.place(x=530,y=600)
backbuttonimage=PhotoImage(file='backbutton.png')
back=Button(root,image=backbuttonimage,border=0,width=0,height=0,activebackground='lightpink',command=login)
back.place(x=20,y=15)
root.mainloop()

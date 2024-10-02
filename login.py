
def trial():
    pass
def loginuser():
    username= user.get()
    password= code.get()
    #print(username,password)
    if( username=='' or username=='UserID') or (password=='' or password=='Password'):
        messagebox.showerror('Entry error','Type username and password')
    else:
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',password='pdk789'
                                         ,database='studentregistration')
            mycursor=mydb.cursor()
            #print('connected to database')
        except:
            messagebox.showerror('connection','Database is not connected')
            return
        command='use studentregistration'
        mycursor.execute(command)
        command='select * from login where username=%s and password= %s'
        mycursor.execute(command,(username,password))
        myresult=mycursor.fetchone()
        if myresult== None:
            messagebox.showinfo('invalid','invalid username and password!!!')
            trial()
        else:
            messagebox.showinfo('Login ','Sucessfully Login!!!')
            root.destroy()
            import notepad


def user_enter(e):
    user.delete(0,END)
def user_leave(e):
    if user.get()=='':
        user.insert(0,'UserID')
def password_enter(e):
    code.delete(0,END)
def password_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
def register():
    root.destroy()
    import register

from tkinter import *
from tkinter import messagebox
import mysql.connector
bgg='#06283D'
root=Tk()
root.title('login system')
root.resizable(False,False)
root.geometry('1250x700')
img=PhotoImage(file='icon.png')
root.iconphoto(False,img)
frame=Frame(root,bg='red')
frame.pack(fill=Y)
backgroundimage=PhotoImage(file='register.png')
Label(frame,image=backgroundimage).pack()

user=Entry(frame,width=18,fg='#fff',bd=0,bg='#375174',font=('arial 20 bold'))
user.place(x=500,y=380)
user.bind("<FocusIn>",user_enter)
user.bind('<FocusOut>',user_leave)
user.insert(0,'UserID')

code=Entry(frame,width=18,fg='#fff',bd=0,bg='#375174',font=('arial 20 bold'))
code.place(x=500,y=470)
code.bind("<FocusIn>",password_enter)
code.bind('<FocusOut>',password_leave)
code.insert(0,'Password')

button_mode=True
def hide():
    global button_mode
    if button_mode:
        eyebutton.config(image=closeeye,activebackground='white')
        code.config(show='*')
        button_mode=False
    else:
        eyebutton.config(image=openeye,activebackground='white')
        code.config(show='')
        button_mode=True

openeye=PhotoImage(file='openeye.png')
closeeye=PhotoImage(file='close eye.png')
eyebutton=Button(root,image=openeye,bg='#375174',bd=0,command=hide)
eyebutton.place(x=780,y=470)

loginbutton=Button(root,text='LOGIN',bg='#1f5675',fg='white',width=10,height=1
                   ,font=('arial 16 bold'),command=loginuser,cursor='hand2',bd=0)
loginbutton.place(x=570,y=600)
label=Label(root,text='Dont have an account',fg='#fff',bg='#00264d',
            font=('Microsoft YaHei UI Light ',9))
label.place(x=500,y=550)
reg=Button(root,width=10,text='Add new User',bd=0,bg='#00264d',fg='#57a1f8',command=register
           ,cursor = 'hand2')
reg.place(x=650,y=550)
root.mainloop()

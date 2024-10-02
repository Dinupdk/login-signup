from tkinter import *
from tkinter import filedialog
root=Tk()
def sf():
    of=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if of is None:
        return
    text=str(entry.get(1.0,END))
    of.write(text)
    of.close()
def of ():
    file=filedialog.askopenfile(mode='r',filetype=[('Text file',".txt")])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)


root.title('NotePad')
root.geometry('600x600')
root.config(bg='dodgerblue')
b1=Button(text='Save file',bg='light green',bd=0,activebackground='dodgerblue2',font=('Microsoft Yehai UI Light',10,'bold'),width=20,command=sf)
b1.place(x=100,y=5)
b2=Button(text='Open file',bg='light green',bd=0,activebackground='dodgerblue2',font=('Microsoft Yehai UI Light',10,'bold'),width=20,command=of)
b2.place(x=300,y=5)
entry=Text(root,height=33,width=72,wrap=WORD)

entry.place(x=10,y=60)
root.mainloop()
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class register:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Register')

        # Background
        self.bg = ImageTk.PhotoImage(file=r'img5.jpg')
        bg_lbl = Label(self.root,image = self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # Left Image
        self.bg1 = ImageTk.PhotoImage(file=r'user.jpg')
        left_lbl = Label(self.root,image = self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        # Register Frame
        frame = Frame(self.root,bg='white')
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl = Label(frame,text="REGISTER HERE",font=('times new roman',15,'bold'),fg="green",bg="white")
        register_lbl.place(x=20,y=20)

        # Row1
        fname = Label(frame,text='First Name',font=('arial',13,'bold'),fg='black',bg='white')
        fname.place(x=50,y=100)

        fname_entry = ttk.Entry(frame,width=22,font=('arial',13,'bold'))
        fname_entry.place(x=50,y=130,width=250)

        l_name = Label(frame,text='Last Name',font=('arial',11,'bold'),fg='black',bg='white')
        l_name.place(x=370,y=100)

        self.txt_lname = ttk.Entry(frame,width=22,font=('arial',14,'bold'))
        self.txt_lname.place(x=370,y=130,width=250)

        # Row2
        fname = Label(frame,text='First Name',font=('arial',13,'bold'),fg='black',bg='white')
        fname.place(x=50,y=100)

        fname_entry = ttk.Entry(frame,width=22,font=('arial',13,'bold'))
        fname_entry.place(x=50,y=130,width=250)

        l_name = Label(frame,text='Last Name',font=('arial',11,'bold'),fg='black',bg='white')
        l_name.place(x=370,y=100)

        self.txt_lname = ttk.Entry(frame,width=22,font=('arial',14,'bold'))
        self.txt_lname.place(x=370,y=130,width=250)




if __name__=="__main__":
    root = Tk()
    obj = register(root)
    root.mainloop()
        
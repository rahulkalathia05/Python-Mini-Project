from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
import mysql.connector
from tkinter import messagebox
from employee import employee
from register import register

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r'bgimg.jpg')
        lbl_bg = Label(self.root,image = self.bg)
        lbl_bg.place(x=0,y=0,width=1530,height=790)

        frame = Frame(self.root,bg='white')
        frame.place(x=610,y=170,width=340,height=450)

        img1 = Image.open(r"loginicon.jpg")
        img1 = img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image = self.photoimage1, bg="white",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str = Label(frame,text='Get Started',font=('times new roman',20,'bold'),bg='white',fg='black')
        get_str.place(x=95,y=100)

        #label
        username = Label(frame,text='Email',font=('times new roman',15,'bold'),bg='white',fg='black')
        username.place(x=70,y=155)

        self.txtuser = ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.txtuser.place(x=40,y=180,width=270)

        password = Label(frame,text='Password',font=('times new roman',15,'bold'),bg='white',fg='black')
        password.place(x=70,y=225)

        self.txtpass = ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.txtpass.place(x=40,y=250,width=270)

        # Icon Imgaes
        img2 = Image.open(r"emailicon.png")
        img2 = img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image = self.photoimage2, bg="white",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3 = Image.open(r"lockicon.png")
        img3 = img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image = self.photoimage3, bg="white",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)

        # Button
        loginbtn = Button(frame,text='Login',command=self.login,font=('times new roman',15,'bold'),width=13,bg='red',fg='black',activeforeground="black",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn = Button(frame,text='New User Register',command=self.register_window,borderwidth=0,font=('times new roman',12,'bold'),width=13,bg='white',fg='black',activeforeground="black",activebackground="white")
        registerbtn.place(x=20,y=350,width=160)

        forgetbtn = Button(frame,text='Forget Password',command=self.forgot_password_window,borderwidth=0,font=('times new roman',12,'bold'),width=13,bg='white',fg='black',activeforeground="black",activebackground="white")
        forgetbtn.place(x=10,y=380,width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="R@#ul051102",database="employee_management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app = employee(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # Reset Password
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="R@#ul051102",database="employee_management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)
                self.root2.destroy()


        
    
     # Forgot Window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the User Email to reset the password")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="R@#ul051102",database="employee_management")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row==None:
                messagebox.showerror("My Error","Please enter the valid username email")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                self.root2.configure(bg="white")

                l = Label(self.root2,text="Forget Password",font=('times new roman',20,'bold'),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2,text='Select Security Questions',font=('times new roman',15,'bold'),fg='black',bg='white')
                security_Q.place(x=50,y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,font=('times new roman',15,'bold'),width=17,state='readonly')
                self.combo_security_Q['values']=('Select','Your Birth Place','Your Girlfriend Name','Your Pet Name')
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50,y=110,width=250)

                security_A = Label(self.root2,text='Security Answer',font=('times new roman',15,'bold'),fg='black',bg='white')
                security_A.place(x=50,y=150)

                self.txt_security = ttk.Entry(self.root2,width=22,font=('times new roman',14,'bold'))
                self.txt_security.place(x=50,y=180,width=250)

                new_password = Label(self.root2,text='New Password',font=('times new roman',15,'bold'),fg='black',bg='white')
                new_password.place(x=50,y=220)

                self.txt_newpass = ttk.Entry(self.root2,width=22,font=('times new roman',14,'bold'))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn = Button(self.root2,text="Reset",command=self.reset_pass,font=('times new roman',15,'bold'),fg="white",bg="green")
                btn.place(x=130,y=290)


if __name__ == "__main__":
    main()


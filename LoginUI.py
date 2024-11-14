import tkinter as tk
from tkinter import ttk
import sqlite3 
from UI import Homepage
# from Signup_UI import Signup
from db_function import select_query

N=tk.N
E=tk.E
W=tk.W
S=tk.S

class Login(tk.Frame):
     
    def __init__(selfref, parent, controller):
        
        tk.Frame.__init__(selfref, parent)
        logincheck=selfref.login_check
        selfref.controller=controller
        self = ttk.Frame(selfref, padding="3 3 3 3")
        self.grid(column=10, row=10, sticky=(tk.N, tk.W, tk.E, tk.S))
        #self.title("Login")
        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)

        user = tk.StringVar()
        selfref.user_entry = ttk.Entry(self, width=7, textvariable=user)
        selfref.user_entry.grid(column=0, row=1, sticky=(tk.W, tk.E))

        username = tk.StringVar()
        ttk.Label(self, textvariable=username).grid(column=1, row=1, sticky=(tk.W, tk.E))

        passw = tk.StringVar()
        selfref.pass_entry = ttk.Entry(self, width=7, textvariable=passw, show="*")
        selfref.pass_entry.grid(column=0, row=2, sticky=(tk.W, tk.E))

        password = tk.StringVar()
        ttk.Label(self, textvariable=password).grid(column=1, row=2, sticky=(tk.W, tk.E))

        ttk.Label(self, text="Username").grid(column=1, row=1, sticky=tk.W)
        ttk.Label(self, text="Password").grid(column=1, row=2, sticky=tk.W)


        Login_Button= ttk.Button(self, text= "Login", command=logincheck)
        Login_Button.grid(column= 1, row=5, sticky=(tk.N))

        #error message label

        selfref.message= tk.StringVar()
        ttk.Label(self, textvariable=selfref.message).grid(column=1, row=7, sticky=(tk.E))
        
  
        # button to show frame 2 with text
        # layout2
        Signup_button=ttk.Button(self, text = "Don't Have an account? Please Sign Up",
            command = lambda : controller.show_frame(Signup))
        Signup_button.grid(row= 9, column= 1, padx = 10, pady = 10)

    def login_check(self):
        print(self.user_entry.get())
        print(self.pass_entry.get())
        r=select_query("Register_Teachers", self.user_entry.get(), self.pass_entry.get() )
        # cursor.execute('select * from Register_Teachers where Name_Teacher="'+self.user_entry.get()+'" 
        # and Password_Teacher="'+self.pass_entry.get()+'"')
        
        print(r)
        if r:
            print(type(r))
            with open("cookie","w") as f:
                f.write(str(r[2]))
            self.controller.show_frame(Homepage)
            
        else:
            self.message.set("Authentication Failed")               # puts message in label hence no textvariable was created 
            print("FAILED")



class Signup(tk.Frame):
    def __init__(selfref, parent, controller):
        selfref.controller= controller
        tk.Frame.__init__(selfref, parent)
        self=ttk.Frame(selfref, padding="10 10 10 10")
        self.grid(column=10, row=10, sticky=(N, W, E, S))
        register=selfref.add_register

        #Teacher id

        teach_id=tk.StringVar()
        selfref.teacherid_entry=ttk.Entry(self, width=7)
        selfref.teacherid_entry.grid(column=0, row=1, sticky=(W, E))

        #username
        username1=tk.StringVar()
        selfref.username_entry=ttk.Entry(self, width=7, textvariable=username1)
        selfref.username_entry.grid(column=0, row=2, sticky=(W, E))

        username2=tk.StringVar()
        ttk.Label(self, textvariable=username2).grid(column=1, row=2, sticky=(W, E))

        #password 
        password1=tk.StringVar()
        selfref.pass_entry=ttk.Entry(self, width=7, textvariable=password1)
        selfref.pass_entry.grid(column=0, row=3, sticky=(W, E))

        password2=tk.StringVar()
        ttk.Label(self, textvariable=password2).grid(column=1, row=3, sticky=(W, E))

        #password confirm
        password3=tk.StringVar()
        selfref.passw_entry=ttk.Entry(self, width=7, textvariable=password3)
        selfref.passw_entry.grid(column=0, row=4, sticky=(W, E))

        password4=tk.StringVar()
        ttk.Label(self, textvariable=password4).grid(column=1, row=4, sticky=(W, E))

        #Labels for pasword and username

        ttk.Label(self, text="Teacher-ID").grid(column=1, row=1, sticky=W)
        ttk.Label(self, text="Username").grid(column=1, row=2, sticky=W)
        ttk.Label(self, text="Password").grid(column=1, row=3, sticky=W)
        ttk.Label(self, text="Confirm-Password").grid(column=1, row=4, sticky=W)

        #register button 

        register_button=ttk.Button(self, text= "Register", command=register)
        register_button.grid(column= 1, row=5, sticky=(E))

        #authentication fail msg:

        selfref.message1= tk.StringVar()
        ttk.Label(self, textvariable=selfref.message1).grid(column=2, row=1, sticky=(W))

        selfref.message2= tk.StringVar()
        ttk.Label(self, textvariable=selfref.message2).grid(column=2, row=4, sticky=(W))

    def add_register(self):
        u=self.username_entry.get()
        p=self.pass_entry.get()
        # t=int(self.teacherid_entry.get())
        valid=False
        # if type(t)==int:
        #     valid=True
        # else:
        #     valid=False
        #     self.message1.set("Please make sure the teacher id is an integer")

        try: 
            t= int(self.teacherid_entry.get()) 
        except: 
            #put error message code here
            self.message1.set("Please make sure the teacher id is an integer")
        if p == self.passw_entry.get():
            valid=True
        else:
            valid=False
            self.message2.set("Please Make sure the passwords are same in both fields")
        if valid:
            var = f"'{u}', '{p}', {t}"
            connection=sqlite3.connect("Documentation.db")
            cursor=connection.cursor()
            query='insert into Register_Teachers values ('+var+')'
            print(query)
            cursor.execute(query)    
            connection.commit()
            connection.close()
            self.controller.show_frame(Login)
        
 


# import tkinter as tk
# from tkinter import ttk
# import sqlite3 
# connection=sqlite3.connect("Documentation.db")
# cursor=connection.cursor()

# N=tk.N
# W=tk.W
# S=tk.S
# E=tk.E

# class Signup(tk.Frame):
#     def __init__(selfref, parent, controller):
#         selfref.controller= controller
#         tk.Frame.__init__(selfref, parent)
#         self=ttk.Frame(selfref, padding="10 10 10 10")
#         self.grid(column=10, row=10, sticky=(N, W, E, S))
#         register=selfref.add_register


#         #Teacher id

#         teach_id=tk.StringVar()
#         selfref.teacherid_entry=ttk.Entry(self, width=7)
#         selfref.teacherid_entry.grid(column=0, row=1, sticky=(W, E))

#         #username
#         username1=tk.StringVar()
#         selfref.username_entry=ttk.Entry(self, width=7, textvariable=username1)
#         selfref.username_entry.grid(column=0, row=2, sticky=(W, E))

#         username2=tk.StringVar()
#         ttk.Label(self, textvariable=username2).grid(column=1, row=2, sticky=(W, E))

#         #password 
#         password1=tk.StringVar()
#         selfref.pass_entry=ttk.Entry(self, width=7, textvariable=password1)
#         selfref.pass_entry.grid(column=0, row=3, sticky=(W, E))

#         password2=tk.StringVar()
#         ttk.Label(self, textvariable=password2).grid(column=1, row=3, sticky=(W, E))

#         #password confirm
#         password3=tk.StringVar()
#         selfref.passw_entry=ttk.Entry(self, width=7, textvariable=password3)
#         selfref.passw_entry.grid(column=0, row=4, sticky=(W, E))

#         password4=tk.StringVar()
#         ttk.Label(self, textvariable=password4).grid(column=1, row=4, sticky=(W, E))

#         #Labels for pasword and username

#         ttk.Label(self, text="Teacher-ID").grid(column=1, row=1, sticky=W)
#         ttk.Label(self, text="Username").grid(column=1, row=2, sticky=W)
#         ttk.Label(self, text="Password").grid(column=1, row=3, sticky=W)
#         ttk.Label(self, text="Confirm-Password").grid(column=1, row=4, sticky=W)

#         #register button 

#         register_button=ttk.Button(self, text= "Register", command=register)
#         register_button.grid(column= 1, row=5, sticky=(E))

#         #authentication fail msg:

#         selfref.message1= tk.StringVar()
#         ttk.Label(self, textvariable=selfref.message1).grid(column=2, row=1, sticky=(W))

#         selfref.message2= tk.StringVar()
#         ttk.Label(self, textvariable=selfref.message2).grid(column=2, row=4, sticky=(W))

#     def add_register(self):
#         u=self.username_entry.get()
#         p=self.pass_entry.get()
#         t=int(self.teacherid_entry.get())
#         valid=False
#         # if type(t)==int:
#         #     valid=True
#         # else:
#         #     valid=False
#         #     self.message1.set("Please make sure the teacher id is an integer")

#         try: 
#             t= int(self.teacherid_entry.get()) 
#         except: 
#             #put error message code here
#             self.message1.set("Please make sure the teacher id is an integer")
#         if p == self.passw_entry.get():
#             valid=True
#         else:
#             valid=False
#             self.message2.set("Please Make sure the passwords are same in both fields")
#         if valid:
#             var = f"'{u}', '{p}', {t}"
#             query='insert into Register_Teachers values ('+var+')'
#             print(query)
#             cursor.execute(query)    
#             connection.commit()
#         connection.close()



        

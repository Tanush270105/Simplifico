import time
import tkinter as tk
from tkinter import ttk
import tkinter
from tkcalendar import DateEntry
import sqlite3

N=tk.N
E=tk.E
W=tk.W
S=tk.S

class Events(tk.Frame):
    def __init__(selfref, parent, controller):
        tk.Frame.__init__(selfref, parent)
        selfref.controller=controller
        self = ttk.Frame(selfref, padding="3 3 3 3")
        self.grid(column=10, row=10, sticky=(tk.N, tk.W, tk.E, tk.S))
        header_label=ttk.Label(selfref, text="This is a list of school events for you")
        header_label.grid(column=0, row=0, sticky=(W))

        selfref.event_list=selfref.fetch_events()
        print(selfref.event_list)
        total_rows = len(selfref.event_list)
        if total_rows:
            total_columns = len(selfref.event_list[0])
            selfref.absent_list=[]
            for i in range(total_rows+1):
                for j in range(total_columns):
                    if i == 0:
                        selfref.header1=ttk.Label(self, text="Date", background='white',font=('Arial',14,'bold'))
                        selfref.header1.grid(column=0, row=0, sticky=(W,E))
                        selfref.header2=ttk.Label(self, text="Time", background='white',font=('Arial',14,'bold'))
                        selfref.header2.grid(column=1, row=0, sticky=(W,E))
                        selfref.header2=ttk.Label(self, text="Description", background='white',font=('Arial',14,'bold'))
                        selfref.header2.grid(column=2, row=0, sticky=(W,E))
                    else:
                        selfref.e = ttk.Entry(self, width=20, background='white',
                                    font=('Arial',14))
                    
                        selfref.e.grid(row=i, column=j, sticky=(N,E))
                        selfref.e.insert(tk.END, selfref.event_list[i-1][j])
                        # if j == total_columns - 1:
                        #     selfref.absent_list.append(tk.IntVar())
                        #     selfref.checkbox=ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=selfref.absent_list[i-1])
                        #     selfref.checkbox.grid(row= i, column=j+1)
        else:
            selfref.noRecord=ttk.Label(self, text="There are no records created", background='white',font=('Arial',14,'bold'))
            selfref.noRecord.grid(column=0, row=0, sticky=(W,E))
            
        Add_Button= ttk.Button(self, text= "Add Event", command=selfref.create_events)
        Add_Button.grid(sticky=(S))

        Add_Button= ttk.Button(self, text= "Refresh", command=selfref.refresh)
        Add_Button.grid(sticky=(S))
    
    def refresh(self):
        self.destroy
        self.__init__

    def fetch_events(self):
        connection=sqlite3.connect("Documentation.db")
        cursor=connection.cursor()
        cursor.execute("""select Date, Time, Description from Events;""")
        eventDetails=cursor.fetchall()
        print(eventDetails)
        connection.close()
        return eventDetails

    def create_events(self):
        win = tk.Toplevel()
        win.wm_title("Event Creation")

        date_label= ttk.Label(win, text="Date:")
        date_label.grid(column=0, row=0, sticky=(W))

        date_entry= DateEntry(win)
        date_entry.grid(column= 1, row=0, sticky=(E))

        #creation of Time label and entry box

        time_label= ttk.Label(win, text="Time:")
        time_label.grid(column=0, row=1, sticky=(W))

        time_entry= ttk.Entry(win)
        time_entry.grid(column=1, row=1, sticky=(E))

        # e-mail address label and box

        mail_label=ttk.Label(win, text="Notification E-mails")
        mail_label.grid(column=0, row=2, sticky=(W))

        mail_entry=ttk.Entry(win)
        mail_entry.grid(column=1, row=2, sticky=(E))

        #Description label and box

        desc_label=ttk.Label(win, text="Description")
        desc_label.grid(column=0, row=3, sticky=(W))

        desc_entry=tk.Text(win)
        desc_entry.grid(column=1, row=3, sticky=(E))

        def save():
            print(desc_entry.get("1.0",'end-1c'))
            query = """ insert into Events (Date,Time,Description,Email) values ("{}","{}","{}","{}")""".format(date_entry.get_date(),time_entry.get(),desc_entry.get("1.0",'end-1c'),mail_entry.get())
            connection=sqlite3.connect("Documentation.db")
            cursor=connection.cursor()
            cursor.execute(query)
            connection.commit()
            connection.close()
            win.destroy()
            


        b = ttk.Button(win, text="Save", command=save)
        b.grid(row=4, column=1,sticky=(W,E))


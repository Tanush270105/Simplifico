import tkinter as tk
from tkinter import ttk, filedialog, Listbox

import datetime
import shutil
import os



N=tk.N
E=tk.E
W=tk.W
S=tk.S

class Homepage(tk.Frame):
    def __init__(selfref, parent, controller):
        tk.Frame.__init__(selfref, parent)

        #root.title("Home Page")
        self=ttk.Frame(selfref, padding= "5 5 5 5")
        # self.grid(column=30, row=30, sticky=(N, W, E, S))
        # self.grid()
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=8)
        #buttons for the UI
        mystudents_button=ttk.Button(selfref, text="My students", command= lambda: controller.show_frame(myStudents))
        mystudents_button.grid(column=0, row=0, sticky=(W,E))

        addstudents_button=ttk.Button(selfref, text="Add New students to list", command= lambda: controller.show_frame(SaveStudents))
        addstudents_button.grid(column=0, row=1, sticky=(W,E))

        documents_button=ttk.Button(selfref, text="My Documents", command= lambda: controller.show_frame(Documents))
        documents_button.grid(column=0, row=2, sticky=(W, E))

        class_button=ttk.Button(selfref, text="My Classroom", command= lambda: controller.show_frame(Attend))
        class_button.grid(column=0, row=3, sticky=(W, E))

        event_button=ttk.Button(selfref, text="Upcoming Events", command= lambda: controller.show_frame(Events))
        event_button.grid(column=0, row=4, sticky=(W, E))

        quit_button=ttk.Button(selfref, text="Quit", command=self.quit)
        quit_button.grid(column=0, row=5, sticky=(W))

        #Labels for the UI 

        ttk.Label(selfref, text="You can look at the details of all the students from this button.").grid(column=1, row=0, sticky=(W,E))

        ttk.Label(selfref, text="Any missing or new students can be added to the database from this button").grid(column=1, row=1, sticky=(W,E))
        
        ttk.Label(selfref, text="Documentations of any type be it Past Papers, L.O.R.s, saved, and managed here.").grid(column=1, row=2, sticky=(W, E))

        ttk.Label(selfref, text="The attendance for your classroom can be handled from here").grid(column=1, row=3, sticky=(W,E))

        ttk.Label(selfref, text="Any events such as competetitions can be added here and you will get an instant reminder regarding them.").grid(column=
         1, row=4, sticky=(W,E))


from tkcalendar import DateEntry
import sqlite3


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
            selfref.mail_list=[]
            for i in range(total_rows+1):
                for j in range(total_columns):
                    if i == 0:
                        selfref.header1=ttk.Label(self, text="Date", background='white',font=('Arial',14,'bold'))
                        selfref.header1.grid(column=0, row=0, sticky=(W,E))
                        selfref.header2=ttk.Label(self, text="Time", background='white',font=('Arial',14,'bold'))
                        selfref.header2.grid(column=1, row=0, sticky=(W,E))
                        selfref.header2=ttk.Label(self, text="Description", background='white',font=('Arial',14,'bold'))
                        selfref.header2.grid(column=2, row=0, sticky=(W,E))
                        selfref.header2=ttk.Label(self, text="Email", background='white',font=('Arial',14,'bold'))
                        selfref.header2.grid(column=3, row=0, sticky=(W,E))
                    else:
                        selfref.e = ttk.Entry(self, width=20, background='white',
                                    font=('Arial',14))
                    
                        selfref.e.grid(row=i, column=j, sticky=(N,E))
                        selfref.e.insert(tk.END, selfref.event_list[i-1][j])
                        if j == total_columns - 1:
                            selfref.mail_list.append(tk.IntVar())
                            selfref.checkbox=ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=selfref.mail_list[i-1])
                            selfref.checkbox.grid(row= i, column=j+1)
        else:
            selfref.noRecord=ttk.Label(self, text="There are no records created", background='white',font=('Arial',14,'bold'))
            selfref.noRecord.grid(column=0, row=0, sticky=(W,E))
        
        Mail_Button= ttk.Button(self, text= "Send Mail", command=selfref.send_mail)
        Mail_Button.grid(column=3,row=40,sticky=(E))

        Add_Button= ttk.Button(self, text= "Add Event", command=selfref.create_events)
        Add_Button.grid(column=2,row=40,sticky=(E))

        Back_Button= ttk.Button(self, text= "Back Home", command=lambda: controller.show_frame(Homepage))
        Back_Button.grid(column=0,row=40,sticky=(W))
    
    def send_mail(self):
        import mail
        for i in range(len(self.mail_list)):
            if self.mail_list[i].get():
                message = "This is a reminder for "+self.event_list[i][2]+" to be held on "+self.event_list[i][0]+" "+self.event_list[i][1]
                mail_id = self.event_list[i][3]
                mail.send_mail_notification(message,mail_id)

    def fetch_events(self):
        connection=sqlite3.connect("Documentation.db")
        cursor=connection.cursor()
        cursor.execute("""select Date, Time, Description,Email from Events;""")
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
            query = """ insert into Events (Date,Time,Description,Email) values ("{}","{}","{}","{}")""".format(date_entry.get_date(), time_entry.get(),desc_entry.get("1.0",'end-1c'),mail_entry.get())
            connection=sqlite3.connect("Documentation.db")
            cursor=connection.cursor()
            cursor.execute(query)
            connection.commit()
            connection.close()
            win.destroy()
            

        b = ttk.Button(win, text="Save", command=save)
        b.grid(row=4, column=1,sticky=(W,E))


class Attend(tk.Frame):
    
    def __init__(selfref, parent, controller):

        tk.Frame.__init__(selfref, parent)
        selfref.controller=controller
        self = ttk.Frame(selfref, padding="3 3 3 3")
        self.grid(column=10, row=10, sticky=(tk.N, tk.W, tk.E, tk.S))

        # into_label=ttk.Label(selfref, text="Select Class")
        # into_label.grid(column=0, row= 0, sticky=(N))
        
        # connection=sqlite3.connect("Documentation.db")
        # cursor=connection.cursor()
        # class_query=""" select Class_Name, Section from Class """
        # cursor.execute(class_query)
        # class_details = cursor.fetchall()

        # options = []
        # for detail in class_details:
        #     options.append(str(detail[0])+" "+detail[1])
        # selfref.standard = tk.StringVar(self)
        # selfref.standard= tk.OptionMenu(self, selfref.standard, *options)
        # selfref.standard.grid(column=1,row=0)

        selfref.student_list=selfref.fetch_students()
        print(selfref.student_list)
        total_rows = len(selfref.student_list)
        total_columns = len(selfref.student_list[0])
        selfref.absent_list=[]
        for i in range(total_rows+1):
            for j in range(total_columns):
                if i == 0:
                    selfref.header1=ttk.Label(self, text="Admission_id", background='white',font=('Arial',14,'bold'))
                    selfref.header1.grid(column=0, row=0, sticky=(W,E))
                    selfref.header2=ttk.Label(self, text="Student Name", background='white',font=('Arial',14,'bold'))
                    selfref.header2.grid(column=1, row=0, sticky=(W,E))
                    selfref.header2=ttk.Label(self, text="Student Email", background='white',font=('Arial',14,'bold'))
                    selfref.header2.grid(column=2, row=0, sticky=(W,E))
                    selfref.header2=ttk.Label(self, text="Class", background='white',font=('Arial',14,'bold'))
                    selfref.header2.grid(column=3, row=0, sticky=(W,E))
                    selfref.header2=ttk.Label(self, text="Section", background='white',font=('Arial',14,'bold'))
                    selfref.header2.grid(column=4, row=0, sticky=(W,E))
                else:
                    selfref.e = ttk.Entry(self, width=20, background='white',
                                font=('Arial',14))
                 
                    selfref.e.grid(row=i, column=j, sticky=(N,E))
                    selfref.e.insert(tk.END, selfref.student_list[i-1][j])
                    if j == total_columns - 1:
                        selfref.absent_list.append(tk.IntVar())
                        selfref.checkbox=ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=selfref.absent_list[i-1])
                        selfref.checkbox.grid(row= i, column=j+1)
        
        Add_Button= ttk.Button(self, text= "Save Attendance", command=selfref.save_attend)
        Add_Button.grid(column=5,row=40,sticky=(S))
        Add_Button= ttk.Button(self, text= "Back Home", command=lambda: controller.show_frame(Homepage))
        Add_Button.grid(column=0,row=40,sticky=(S))
        Add_Button= ttk.Button(self, text= "Export Attendance", command=selfref.get_attendance)
        Add_Button.grid(column=1,row=40,sticky=(S))
    
    def save_attend(self):
        for i in range(len(self.absent_list)):
            print(self.absent_list[i].get())
            print(self.student_list[i])
            connection=sqlite3.connect("Documentation.db")
            cursor=connection.cursor()
            query = """ insert into Attendance (Student_ID,Class_ID,Date,Absent) values ({},{},"{}",{}); """.format(self.student_list[i][0],self.student_list[i][5],datetime.date.today(),self.absent_list[i].get())
            print(query)
            cursor.execute(query)
            connection.commit()
            connection.close()
        return "Attendence Saved"
        
    def fetch_students(self):
        connection=sqlite3.connect("Documentation.db")
        cursor=connection.cursor()
        cursor.execute("""select Student.Admission_id, Student.Name, Student.Email, Class.Class_Name, Class.Section,
        Student.Class_id from Student join Class on Student.Class_id=Class.id;""")
        studentDetails=cursor.fetchall()
        print(studentDetails)
        connection.close()
        return studentDetails

    def get_attendance(self):
        win = tk.Toplevel()
        win.wm_title("Export as Excel")

        date_label= ttk.Label(win, text="Date for attendance:")
        date_label.grid(column=0, row=0, sticky=(W))

        date_entry= DateEntry(win)
        date_entry.grid(column= 1, row=0, sticky=(E))

        def export():
            attendance_date=date_entry.get_date()
            query = """select Student_ID, (select Class_Name from Class where id=Class_ID),(select Section from Class where id=Class_ID) ,
            Absent from Attendance where Date="{}" """.format(attendance_date)
            connection=sqlite3.connect("Documentation.db")
            cursor=connection.cursor()
            cursor.execute(query)
            attendance = cursor.fetchall()
            print("Attendance",attendance)
            connection.close()

            import xlwt
            from xlwt import Workbook
            
            # Workbook is created
            wb = Workbook()
            
            # add_sheet is used to create sheet.
            sheet1 = wb.add_sheet(str(attendance_date))
            
            sheet1.write(0, 0, 'Student')
            sheet1.write(0, 1, 'Class')
            sheet1.write(0, 2, 'Section')
            sheet1.write(0, 3, 'Attendance')
            for value in range(len(attendance)):
                sheet1.write(value+1, 0, attendance[value][0])
                sheet1.write(value+1, 1, attendance[value][1])
                sheet1.write(value+1, 2, attendance[value][2])
                if attendance[value][3]:
                    sheet1.write(value+1, 3, 'Absent')
                else:
                    sheet1.write(value+1, 3,'Present')
            
            wb.save(str(attendance_date)+'attendance.xls')
            win.destroy()
            

        b = ttk.Button(win, text="Export", command=export)
        b.grid(row=4, column=1,sticky=(W,E))

# my students functionality 

class myStudents(tk.Frame):
    def __init__(selfref, parent, controller):

        tk.Frame.__init__(selfref, parent)
        selfref.controller=controller
        self = ttk.Frame(selfref, padding="3 3 3 3")
        self.grid(column=10, row=10, sticky=(tk.N, tk.W, tk.E, tk.S))

        into_label=ttk.Label(selfref, text="The List of students you teach are available below:")
        into_label.grid(column=0, row= 0, sticky=(N))
        selfref.disp_students(controller)
    def disp_students(selfref, controller):   
        s=selfref.fetch_students()
        print(s)
        total_rows = len(s)
        total_columns = len(s[0])
        
        for i in range(total_rows+1):
            for j in range(total_columns):
                if i == 0:
                    selfref.header1=ttk.Label(selfref, text="Admission_id", background='white',font=('Arial',14,'bold'))
                    selfref.header1.grid(column=0, row=1, sticky=(W,E))
                    selfref.header2=ttk.Label(selfref, text="Student Name", background='white',font=('Arial',14,'bold'))
                    selfref.header2.grid(column=1, row=1, sticky=(W,E))
                    selfref.header2=ttk.Label(selfref, text="Student Email", background='white',font=('Arial',14,'bold'))
                    selfref.header2.grid(column=2, row=1, sticky=(W,E))
                    selfref.header2=ttk.Label(selfref, text="Class", background='white',font=('Arial',14,'bold'))
                    selfref.header2.grid(column=3, row=1, sticky=(W,E))
                    selfref.header2=ttk.Label(selfref, text="Section", background='white',font=('Arial',14,'bold'))
                    selfref.header2.grid(column=4, row=1, sticky=(W,E))
                else:
                    selfref.e = ttk.Entry(selfref, width=20, background='white',
                                font=('Arial',14))
                    
                    selfref.e.grid(row=i+1, column=j, sticky=(W,E))
                    selfref.e.insert(tk.END, s[i-1][j])

        Add_Button= ttk.Button(selfref, text= "Back Home", command=lambda: back_home(controller))
        Add_Button.grid(column=0,row=40,sticky=(W))

        def back_home(controller):
            controller.show_frame(Homepage)
            myStudents.destroy(selfref)

    def fetch_students(self):
        connection=sqlite3.connect("Documentation.db")
        cursor=connection.cursor()
        cursor.execute("""select Student.Admission_id, Student.Name, Student.Email, Class.Class_Name, Class.Section from Student join 
        Class on Student.Class_id=Class.id""")
        studentDetails=cursor.fetchall()
        print(studentDetails)
        connection.close()
        return studentDetails
    
    def fetch_classes(self):
        connection=sqlite3.connect("Documentation.db")
        cursor=connection.cursor()
        classDetails=["Select Class"]
        cursor.execute("""select id,Class_Name,Section from Class""")
        for detail in cursor.fetchall():
            classDetails.append(detail)
        print(classDetails)
        connection.close()
        return classDetails


class SaveStudents(tk.Frame):
    def __init__(selfref, parent, controller):
        #creation of window and conifguring columns in the window
        #root.title("Saving Student Details")
        addstudent=selfref.add_student
        tk.Frame.__init__(selfref, parent)
        selfref.controller=controller
        self = ttk.Frame(selfref, padding="3 3 3 3")
        self.grid(column=10, row=10, sticky=(tk.N, tk.W, tk.E, tk.S))
        # root.columnconfigure(0, 1)
        # root.columnconfigure(0, 3)

        #creation of username label and entry box

        username_label= ttk.Label(selfref, text="Username:")
        username_label.grid(column=0, row=0, sticky=(W))

        selfref.username_entry= ttk.Entry(selfref)
        selfref.username_entry.grid(column= 1, row=0, sticky=(E))

        #creation of StudentID label and entry box

        ID_label= ttk.Label(selfref, text="Admission ID:")
        ID_label.grid(column=0, row=1, sticky=(W))

        selfref.ID_entry= ttk.Entry(selfref)
        selfref.ID_entry.grid(column=1, row=1, sticky=(E))

        #creation of Class label and entry box

        class_label= ttk.Label(selfref, text="Class:")
        class_label.grid(column=0, row=2, sticky=(W))

        selfref.class_entry= ttk.Entry(selfref)
        selfref.class_entry.grid(column=1, row=2, sticky=(E))

        #creation of Section Label and entry box

        section_label= ttk.Label(selfref, text="Section")
        section_label.grid(column=0, row=3, sticky=(W))

        selfref.section_entry= ttk.Entry(selfref)
        selfref.section_entry.grid(column=1, row=3, sticky=(E))

        #e-mail address label and box

        mail_label=ttk.Label(selfref, text="E-mail address")
        mail_label.grid(column=0, row=4, sticky=(W))

        selfref.mail_entry=ttk.Entry(selfref)
        selfref.mail_entry.grid(column=1, row=4, sticky=(E))

        #add button 

        Add_Button= ttk.Button(selfref, text= "Add student to list", command=addstudent)
        Add_Button.grid(column= 1, row=5, sticky=(E))

        exit1=ttk.Button(selfref, text="Back to homepage", command= lambda: back_button(controller))
        exit1.grid(column=1, row=6, sticky= (W, E))

        def back_button(controller):
            controller.show_frame(Homepage)
            myStudents.disp_students(controller)

    def add_student(self):
        try:
            connection=sqlite3.connect("Documentation.db")
            cursor=connection.cursor()
            c=self.class_entry.get()
            sec=self.section_entry.get()
            print(c,sec)
            slct_qry="""select * from Class where Class_Name={} and Section="{}" """.format(c,sec)
            cursor.execute(slct_qry)
            cls = cursor.fetchone()
            if not cls:
                query="""insert into Class (Class_Name,Section) values ({},"{}")""".format(c,sec)
                print(query)
                cursor.execute(query)
                cursor.execute("select max(id) from Class")
                cls = cursor.fetchone()
            i=self.ID_entry.get()
            u=self.username_entry.get()
            m=self.mail_entry.get()
            query1="""insert into Student values ({},"{}","{}",{})""".format(i,u,m,cls[0])
            print(query1)
            cursor.execute(query1)
            connection.commit()
            connection.close()
        except:
            print("error")
        else:
            self.open_popup()

    def open_popup(self):
        top= tk.Toplevel()
        top.title("Successful")
        tk.Label(top, text= "New student registered!", font=('Mistral 18 bold')).grid(row=1,column=2)

FILE_PATH='/Users/tanushzutshi/Desktop/'

class Documents(tk.Frame):
     
    def __init__(selfref, parent, controller):
        
        tk.Frame.__init__(selfref, parent)
        selfref.controller=controller
        self = ttk.Frame(selfref, padding="3 3 3 3")
        self.grid(column=10, row=10, sticky=(tk.N, tk.W, tk.E, tk.S))
        #self.title("Login")
        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)

        selfref.filename = tk.StringVar()
        selfref.filename_entry = ttk.Entry(self, width=7, textvariable=selfref.filename)
        selfref.filename_entry.grid(column=0, row=1, sticky=(tk.W, tk.E))

        ttk.Label(self, text="Uploaded file").grid(column=1, row=1, sticky=tk.W)
        docupload=ttk.Button(self, text="Upload from computer", command=selfref.upload)
        docupload.grid(column= 0, row=0, sticky=(tk.N))

        classname=tk.StringVar()
        selfref.class_entry= ttk.Entry(self, width=7, textvariable=classname)
        selfref.class_entry.grid(column=0, row=3, sticky=(W, E))

        ttk.Label(self, text="Enter Class").grid(column=1, row=3, sticky=(W))

        section=tk.StringVar()
        selfref.section_entry=ttk.Entry(self, width=7, textvariable=section)
        selfref.section_entry.grid(column=0, row=4, sticky=(W, E))

        ttk.Label(self, text="Section").grid(column=1, row=4, sticky=(W))

        subjects = [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Computer Science",
            "Language",
            "Others"
        ]
        selfref.subj = tk.StringVar(self)
        selfref.subj.set(subjects[0])
        selfref.subj=tk.OptionMenu(self, selfref.subj, *subjects)
        selfref.subj.grid(column=0, row=5, sticky=(W, E))
        ttk.Label(self, text="Select Subject").grid(column=1, row=5, sticky=(W)) 


        options = [
            "Marksheet",
            "LOR",
            "Attendance",
            "Past Papers",
            "Worksheets and assessments"
        ]
        selfref.doc_type = tk.StringVar(self)
        selfref.doc_type.set(options[0])
        selfref.doctype=tk.OptionMenu(self, selfref.doc_type, *options)
        # selfref.doctype_entry=ttk.Entry(self, width=7, textvariable=doctype)
        selfref.doctype.grid(column=0, row=6, sticky=(W, E))

        ttk.Label(self, text="Kindly Specify the type of document (Ex:Marksheet, L.O.R., etc)").grid(column=1, row=6, sticky=(W)) 

        selfref.boolvar = tk.IntVar()
        selfref.boolvar_entry=ttk.Checkbutton(self, width=7, variable=selfref.boolvar)
        selfref.boolvar_entry.grid(column=0, row=7, sticky=(W, E))

        ttk.Label(self, text="Is it a public file?").grid(column=1, row=7, sticky=(W))


        docsave=ttk.Button(self, text="Upload File", command=selfref.store_file)
        docsave.grid(column= 0, row=8, sticky=(N))

        view_Button= ttk.Button(self, text= "View existing documents", command= lambda: controller.show_frame(Viewdoc))
        view_Button.grid(column= 1, row=8, sticky=(N,E))


        exit=ttk.Button(self, text="Back to homepage", command= lambda: controller.show_frame(Homepage))
        exit.grid(column=2, row=8, sticky=(W, E))

    def upload(self):
        f=filedialog.askopenfilename()
        self.filename.set(f)

    def store_file(self):
        try:
            path=self.filename_entry.get()
            c=self.class_entry.get()
            s=self.section_entry.get()
            d=self.doc_type.get()
            file = path.split("/")[-1]
            print(file)
            t=(c, s, d)
            relative_path=""
            for i in t:
                if i:
                    relative_path +=  i+"/"
            target = FILE_PATH + relative_path
            print(path,target+file)
            shutil.copy(path,target)
            date_object=datetime.date.today()
            date=str(date_object.year)+"-"+ str(date_object.month) +"-"+ str(date_object.day)
            print(file,type(file))
            connection=sqlite3.connect("Documentation.db")
            cursor=connection.cursor()
            cursor.execute('select max(file_id) from Documents')
            fileId=cursor.fetchone()
            connection.commit()
            connection.close()
            print("This is file id:::::",fileId)
            if fileId[0] is None:
                fileId = "0"
            else:
                fileId = fileId[0]
            public = self.boolvar_entry.state()
            print("This is check val", public)
            if public:
                public = True
            else:
                public = False
            print(public)
            with open("cookie","r") as f:
                logged_in_user = f.read()
            values='"'+file+ '",'+logged_in_user+',"'+ target+ '","'+d+'","'+ file.split('.')[-1]+ '","'+str(public)+'","'+ date + '",'+str(int(fileId)+1)
            print("This is the value for sting")
            print(values)

            from db_function import insert_query

            insert_query("Documents", values)
            return relative_path+file

            #function here to add info to db.
        except OSError as e:
            print(e)
            self.create_path(target)
            self.store_file()
        # except Exception as e:
        #     print(e)        
    def create_path(self, path=FILE_PATH):
        os.makedirs(path,exist_ok=True)
        print(path," created")

class Viewdoc(tk.Frame):
    def __init__(selfref, parent, controller):
        tk.Frame.__init__(selfref, parent)
        self= ttk.Frame(selfref, padding="3 3 3 3")
        self.grid(column=10, row=10, sticky=(tk.N, tk.W, tk.E, tk.S))
        # ttk.Label(self, text="This is a label"). grid(column=0, row =10)

        selfref.files = selfref.get_file_list()
        total_rows = len(selfref.files)
        # total_columns = len(selfref.files[0])

        # Define a label for the list.  
        ttk.Label(self, text = " File List").grid(column=0, row=2, sticky=(W, E))
        # for i in range(total_rows):
        #     for j in range(total_columns):
                 
        #         self.e = ttk.Entry(self, width=20, foreground='blue',
        #                        font=('Arial',16,'bold'))
                 
        #         self.e.grid(row=i, column=j)
        #         self.e.insert(tk.END, selfref.files[i][j])

        selfref.listbox = Listbox(self, 
                #   height = 10, 
                #   width = 15, 
                  bg = "dark blue",
                  activestyle = 'dotbox', 
                #   font = "Helvetica",
                  fg = "white")
        
        # insert elements by their
        # index and names.
        i = 0
        for file in selfref.files:
            i+=1
            selfref.listbox.insert(i,file[0])        
        selfref.listbox.grid( column=0, row=4, sticky=(W, E))   
        selfref.listbox.bind('<<ListboxSelect>>', selfref.item_selected)

        view_Button= ttk.Button(self, text= "Upload documents", command= lambda: controller.show_frame(Documents))
        view_Button.grid(column= 1, row=5, sticky=(N,E))


        exit=ttk.Button(self, text="Back to homepage", command= lambda: controller.show_frame(Homepage))
        exit.grid(column=2, row=5, sticky=(W, E))

    def item_selected(self,event):
        selected_indices = self.listbox.curselection()
        index = selected_indices[0]
        file_path = self.files[index][2]+self.files[index][0]
        self.open_file(file_path)
    
    def open_file(self,filepath):
        import subprocess, os, platform
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(filepath)
        else:                                   # linux variants
            subprocess.call(('xdg-open', filepath))

    def get_file_list(self):
        connection=sqlite3.connect("Documentation.db")
        cursor=connection.cursor()
        with open("cookie","r") as f:
            logged_in_user = f.read()
        cursor.execute('select file_name,creator,file_path,file_type,file_id from Documents where access="True" or creator='+logged_in_user)
        files=cursor.fetchall()
        connection.close()
        return files



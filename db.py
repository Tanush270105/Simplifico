import sqlite3
connection=sqlite3.connect("Documentation.db") 
cursor=connection.cursor()

# registration for teachers table 

# cursor.execute("""create table Register_Teachers 
# (Name_Teacher varchar(50),
# Password_Teacher varchar(25),
# teacher_id integer primary key);""")
# cursor.execute('insert into Register_Teachers values ("Sir","Password",1)')
# connection.commit()

#documents table

# cursor.execute("""create table Documents
# (file_name varchar(50),
# creator varchar(50),
# file_path varchar(50),
# file_type varchar(50),
# extension varchar(50),
# access varchar(50),
# date_created varchar(50),
# file_id varchar(1000) primary key);""")
# connection.commit()
# connection.close()

# cursor.execute("""create table Documents_Type
# (file_type varchar(50),
# type_id varchar(5) primary key);""")
# connection.commit()

#class table
# cursor.execute("""create table Class 
# (id integer,
# Class_Name integer,
# Section varchar(5));""")
#cursor.execute('insert into Class values (1,12,"B")')
# connection.commit()

#student table
# cursor.execute("""create table Student
# (Admission_id integer primary key,
# Name varchar(30),
# Email varchar(50),
# Class_id integer);""")
# cursor.execute('insert into Student values (1, "ABCD", "abc@gmail.com",1)')
# connection.commit()

#files table
# cursor.execute("""create table Files
# (Subject Name varchar(15),
# File Name varchar(30),
# Format varhcar(7),
# Category varchar(25));""")
# cursor.execute('insert into Files values ("Physics", "ClassTest", "pdf", "Formative assessment")')
# connection.commit()


#Subject Name

# cursor=connection.cursor()
# cursor.execute("""create table Subjects
# (Subject_ID integer primary key,
# Subject_Name varhcar(15));""")
# cursor.execute('insert into Subjects values (123, "Chemistry")')
# k=cursor.execute('select Subject_Name from Subjects where Subject_ID=123')
# print(k.fetchall())
# connection.commit()
# connection.close()
#make all tables required

#Attendence
# cursor=connection.cursor()
# cursor.execute("""create table Attendance
# (Attendance_ID integer primary key AUTOINCREMENT NOT NULL,
# Student_ID integer,
# Class_ID varhcar(15),
# Date text,
# Absent integer)
# ;""")
# connection.commit()
# connection.close()

#Events
# cursor=connection.cursor()
# cursor.execute("""create table Events
# (Event_ID integer primary key AUTOINCREMENT NOT NULL,
# Date text,
# Time text,
# Description varchar(100),
# Email varchar(200))
# ;""")
# connection.commit()
# connection.close()


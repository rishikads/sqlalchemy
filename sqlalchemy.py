from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean
import re
engine = create_engine('sqlite:///Student.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('USN', String(10), primary_key = True), 
   Column('student_name', String(50)), 
   Column('gender', String(1)),
   Column('entry_type', String(10)),
   Column('YOA', Integer),
   Column('migrated', Boolean),
   Column('Details_of_transfer', String(100)),
   Column('admission_in_separate_division', Boolean),
   Column('Details_of_admission_in_seperate_division', String(100)),
   Column('YOP', Integer),
   Column('degree_type', String(2)),
   Column('pu_marks', Integer),
   Column('entrance_marks', Integer)
)

meta.create_all(engine)
conn = engine.connect()

def create():
    N=int(input("Enter the number of student's details to be entered: "))
    for i in range(N):
        USN=str(input("Enter the USN of the student: "))
        student_name=str(input("Enter the name of the student: "))
        gender=str(input("Enter the gender of the student: " ))
        if not re.match("^[m,f]*$", gender):
            print("Error! Only letters m and f allowed!")
        entry_type=str(input("Enter the entry type (normal/lateral) of the student: "))
        YOA=int(input("Enter the year of admission of the student: "))
        migrated=(input("Has the student migrated to other programs / Institutions - Yes / No: "))
        if migrated=="Yes":
           migrated== 1
           Details_of_transfer= str(input("Enter the details of transfer of the student: "))
        else:
            migrated== 0
            Details_of_transfer= None
        admission_in_separate_division=(input("Does the student have admission in a seperate division - Yes (With details) / No: "))
        if admission_in_separate_division=="Yes":
           admission_in_separate_division==True
           Details_of_admission_in_seperate_division= str(input("Enter the details of admission in seperate division of the student: "))
        else:
            admission_in_separate_division==False
            Details_of_admission_in_seperate_division= None
        YOP=int(input("Year of Passing: "))
        degree_type=str(input("Student enrolled for UG / PG?: "))
        pu_marks=int(input("12th marks in PCM subjects: "))
        entrance_marks=int(input("Entrance Exam ranks/marks: "))
        ins = students.insert().values(USN= USN, student_name = student_name, gender = gender, entry_type= entry_type, YOA= YOA, migrated= migrated, Details_of_transfer= Details_of_transfer, admission_in_separate_division= admission_in_separate_division, Details_of_admission_in_seperate_division= Details_of_admission_in_seperate_division, YOP= YOP, degree_type= degree_type, pu_marks= pu_marks, entrance_marks= entrance_marks)
        result = conn.execute(ins)

def read():
   s = students.select()
   result = conn.execute(s)

   for row in result:
      print (row)

def update():
    id=int(input("Enter the USN of the student: "))
    new=str(input("Enter the new name of the student: "))
    stmt=students.update().where(students.c.USN==id).values(student_name=new)
    conn.execute(stmt)
    s = students.select()
    conn.execute(s).fetchall()
        
def delete():
    x=input("Enter the id of the student whose record has to deleted: ")
    stmt = students.delete().where(students.c.id == x)
    conn.execute(stmt)
    s = students.select()
    conn.execute(s).fetchall()
        
operation_dict = {1: create, 2: read, 3: update, 4: delete}

while(True):
    operation = int(input("""To perform the following operations: 
          Press 1 to enter new values:
          Press 2 to view the table: 
          Press 3 to update the records: 
          Press 4 to delete a record: """))
    performing = operation_dict[operation]()

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine("mysql://root:07102002@localhost/Student",echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer(10), primary_key = True), 
   Column('name', String(50)), 
   Column('sem', int(1)),
   Column('Degree', String(2)),
   Column('Branch', String(4)),
   Column('gpa', int(2))
)

meta.create_all(engine)
conn = engine.connect()

def create():
    N=int(input("Enter the number of student's details to be entered: "))
    for i in range(N):
        Id=int(input("Enter the id of the student: "))
        Name=str(input("Enter the name of the student: "))
        Sem=int(input("Enter the sem of the student: " ))
        Degree=str(input("Enter the graduation of the student: "))
        Branch=str(input("Enter the branch of the student: "))
        GPA=float(input("Enter the SGPA of the student: "))
        ins = students.insert()
        ins = students.insert().values(id= Id, name = Name, sem = Sem, degree= Degree, branch= Branch, gpa= GPA )
        result = conn.execute(ins)

def read():
   s = students.select()
   result = conn.execute(s)

   for row in result:
      print (row)

def update():
    old=int(input("Enter the original id of the student: "))
    new=str(input("Enter the new name of the student: "))
    stmt=students.update().where(students.c.id==old).values(id=new)
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

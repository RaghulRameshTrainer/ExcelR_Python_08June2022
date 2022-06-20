import sqlite3
dbh=sqlite3.connect('excelR.db')
c=dbh.cursor()

def create_table():
    c.execute("CREATE TABLE employee(empid REAL, ename REAL, tech REAL)")
def load_data():
    id=int(input("Enter your Empid:"))
    name=input("Enter your name:")
    skill=input("Enter your technology:")
    c.execute("INSERT INTO employee VALUES(?,?,?)",(id,name,skill))
def update_data():
    c.execute("UPDATE employee SET tech='Web Technology' WHERE tech='Java'")
def delete_data():
    c.execute("DELETE FROM employee WHERE tech='AIML'")
def read_data():
    c.execute("SELECT * FROM employee")
    #print(c.fetchone())
    #print(c.fetchmany(5))
    for row in c.fetchall():
        print(row[1].upper() + " ===> "+ row[2].upper())

#create_table()
# for x in range(5):
#     load_data()
#update_data()
#delete_data()
read_data()
# dbh.commit()
# c.close()
# dbh.close()
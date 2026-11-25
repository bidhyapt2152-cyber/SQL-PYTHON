# Q1. Create a database school_db with a table Student(student_id AUTO_INCREMENT, name, marks, department).
# Write a class School_db with methods create, read, retrieve, update, delete, and a menu-driven main program.

import mysql.connector

class School_db:
    def __init__(self):

        try:


            self.con=mysql.connector.connect(
                host="localhost",user="root",
                password="Bidhya",database="school_db"
            )
        except Exception:
            print("Connection Failed")
            self.con=None


    #create
    def create(self,name,marks,department):
        if self.con is None:
            return
        try:


            cursor=self.con.cursor()
            query="INSERT INTO Student(name,marks,department) VALUES(%s,%s,%s)"

            data=(name,marks,department)

            cursor.execute(query,data)

            self.con.commit()
            print("Student Record Created Successfully!")

        except Exception:
            print("Failed to create Student record")

        finally:
            cursor.close()




    #read all
    def read(self):
        if self.con is None:
            return
        try:


            cursor = self.con.cursor()
            query="SELECT student_id,name,marks,department FROM Student"

            cursor.execute(query)

            records=cursor.fetchall()

            if records:
                for row in records:

                    print(row)
            else:print("No Records Founded")

        except Exception:
            print("Failed to Read Student Records")

        finally:
            cursor.close()



    #retrieve
    def retrieve(self,student_id):
        if self.con is None:
            return
        try:


            cursor = self.con.cursor()
            query="SELECT student_id,name,marks,department FROM Student WHERE student_id=%s"

            cursor.execute(query,(student_id,))

            record=cursor.fetchone()

            if record:
                print(record)
            else:
                print("No Record Found")
        except Exception:
            print("Failed to Retrieve student Data")

        finally:
            cursor.close()






    #update
    def update(self,student_id,name,marks,department):
        if self.con is None:
            return
        try:


            cursor = self.con.cursor()
            query="UPDATE Student SET name=%s,marks=%s,department=%s WHERE student_id=%s"
            data=(name,marks,department,student_id)
            cursor.execute(query,data)

            self.con.commit()

            if cursor.rowcount>0:
                print("Student Record with ID",student_id," is updated successfully")
            else:
                print("Student Record with ID", student_id, " is NOT Updated")
        except Exception:
            print("Failed To Update Student Record")
        finally:
            cursor.close()

    #delete
    def delete(self,student_id):
        if self.con is None:
            return
        try:
            cursor = self.con.cursor()
            query="DELETE FROM Student WHERE student_id=%s"

            cursor.execute(query,student_id)

            self.con.commit()

            if cursor.rowcount>0:
                print("Student Record Deleted Sucessfully")

            else:
                print("Student Record not Founded")
        except Exception:
            print("Failed Delete Student Record")
        finally:
            cursor.close()




#menu driven
b=School_db()

while True:
    print("\n")
    print("School Management System")
    print("_________________________")

    print("1.create a Student Record")
    print("2.Read all Student Records")
    print("3.Retrieve a Student Record")
    print("4.Update a student Record")
    print("5.Delete a Student Record")
    print("6.Exit")

    ch=int(input("Enter the Choice :"))

    if ch ==1:
        name=input("Enter Student Name :")
        marks=int(input("Enter Mark :"))
        department=input("Enter Department :")

        b.create(name,marks,department)

    elif ch==2:

        b.read()

    elif ch==3:
        student_id=int(input("Enter the Student ID :"))

        b.retrieve(student_id)

    elif ch==4:
        student_id=int(input("Enter the Student ID :"))
        name = input("Enter Student Name :")
        marks = int(input("Enter Mark :"))
        department = input("Enter Department :")

        b.update(student_id,name,marks,department)

    elif ch==5:
        student_id=int(input("Enter the Student ID :"))


        b.delete(student_id)

    elif ch==6:
        break
    else:
        print("Invalid Choice")







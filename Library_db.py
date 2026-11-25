import mysql.connector

class Library_db:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(
                host="localhost",user="root",
                password="Bidhya",database="library_db"

            )
        except Exception:
            print("Connection Failed")
            self.con=None

    #create
    def create(self,title,author,pages,price,language):
        if self.con is None:
            return

        try:
            cursor=self.con.cursor()
            query="INSERT INTO Book(title,author,pages,price,language) VALUES(%s,%s,%s,%s,%s)"
            data=(title,author,pages,price,language)

            cursor.execute(query,data)

            self.con.commit()

            print("Book saved")

        except Exception:
            print("Failed to save")

        finally:
            cursor.close()




    #read all
    def read(self):
        if self.con is None:
            return
        try:
            cursor=self.con.cursor()
            query="SELECT book_id,title,author,pages,price,language FROM Book"

            cursor.execute(query)

            records=cursor.fetchall()

            if records:
                for rows in records:
                    print(rows)
            else:
                print("No book records")
        except Exception:
            print("Failed to read books")
        finally:
            cursor.close()


    #retrive

    def retrieve(self,book_id):
        if self.con is None:
            return

        try:
            cursor=self.con.cursor()
            query="SELECT book_id,title,author,pages,price,language FROM Book WHERE book_id=%s"

            cursor.execute(query,(book_id,))

            record=cursor.fetchone()

            if record:
                print(record)
            else:
                print("No record found")
        except Exception:
            print("Failed to retrieve book")
        finally:
            cursor.close()


    #update
    def update(self,book_id,title,author,pages,price,language):
        if self.con is None:
            return
        try:
            cursor=self.con.cursor()
            query="UPDATE Book SET title=%s,author=%s,pages=%s,price=%s,language=%s WHERE book_id=%s"
            data=(title,author,pages,price,language,book_id)


            cursor.execute(query,data)

            self.con.commit()

            if cursor.rowcount>0:
                print("Book Updated")
            else:
                print("Not updated")

        except Exception:
            print("Failed to update book record")
        finally:
            cursor.close()


    def delete(self,book_id):
        if self.con is None:
            return
        try:
            cursor=self.con.cursor()
            query="DELETE FROM Book WHERE book_id=%s"

            cursor.execute(query,(book_id,))

            self.con.commit()

            if cursor.rowcount>0:
                print("Book record deleted")
            else:
                print("Book record not found")

        except Exception:
            print("Failed Deletion")

        finally:
            cursor.close()



b=Library_db()

while True:
    print("\n")
    print("Library Management System")
    print("__________________________")

    print("1.Create Book Record")
    print("2.Read all Book Records")
    print("3.Retrieve a Book Record")
    print("4.Update a Book Record")
    print("5.Delete a Record")
    print("6.Exit")

    ch=int(input("Enter the choice :"))

    if ch==1:
        title=input("Enter the Title :")
        author=input("Enter the Author :")
        pages=int(input("Enter the number of pages :"))
        price=float(input("Enter the price :"))
        language=input("Enter the Language :")

        b.create(title,author,pages,price,language)

    elif ch==2:
        b.read()

    elif ch==3:
        book_id=int(input("Enter the book ID :"))

        b.retrieve(book_id)

    elif ch==4:
        book_id=int(input("Enter the book ID :"))
        title = input("Enter the Title :")
        author = input("Enter the Author :")
        pages = int(input("Enter the number of pages :"))
        price = float(input("Enter the  price :"))
        language = input("Enter the Language :")


        b.update(book_id,title,author,pages,price,language)

    elif ch==5:
        book_id=int(input("Enter the book ID :"))
        b.delete(book_id)

    elif ch==6:
        break
    else:
        print("Invalid choice")






















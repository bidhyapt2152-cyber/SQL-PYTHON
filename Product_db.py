# Q3. Create a table Product(product_id AUTO_INCREMENT, name, price, quantity). Write a class
#     Shop_db with full CRUD and a menu.
import mysql.connector
class Product_db:
        def __init__(self):
            try:
                self.con=mysql.connector.connect(
                    host="localhost",user="root",
                    password="Bidhya",database="shop_db"
                )

            except Exception:
                print("Connection Failed")

                self.con=None

        #create
        def create(self,name,price,quantity):
            if self.con is None:
                return
            try:
                cursor=self.con.cursor()
                query="INSERT INTO Product(name,price,quantity) VALUES(%s,%s,%s)"
                data=name,price,quantity

                cursor.execute(query,data)

                self.con.commit()
                print("Connection Success!")
            except Exception:
                print("Connection Failed")
            finally:
                cursor.close()



        #read all
        def read(self):
            if self.con is None:
                return
            try:
                cursor=self.con.cursor()
                query="SELECT product_id,name,price,quantity FROM Product"
                cursor.execute(query)

                results=cursor.fetchall()
                if results:
                    for rows in results:
                        print(rows)
                else:
                    print("No Records Found")
            except Exception:
                print("Failed to read all records")
            finally:
                cursor.close()



        #retrieve
        def retrieve(self,product_id):
            if self.con is None:
                return
            try:
                cursor=self.con.cursor()
                query="SELECT product_id,name,price,quantity FROM Product WHERE product_id=%s"
                cursor.execute(query,(product_id,))

                result=cursor.fetchone()

                if result:
                    print(result)
                else:
                    print("No Records Found")

            except  Exception:
                print("Failed to retrieve Record")
            finally:
                cursor.close()



        #update
        def update(self,product_id,name,price,quantity):
            if self.con is None:
                return
            try:
                cursor=self.con.cursor()
                query="UPDATE INTO Product SET name=%s,price=%s,quantity=%s WHERE product_id=%s"

                cursor.execute(query,(product_id,))

                self.con.commit()

                if cursor.rowcount>0:
                    print("Product record with ID",product_id," is updated")
                else:
                    print("Product record with ID", product_id, " is not updated")
            except Exception:
                print("Failed to Update record")
            finally:
                cursor.close()


#delete
        def delete(self,product_id):
            if self.con is None:
                return
            try:
                cursor=self.con.cursor()
                query="DELETE FROM Product WHERE product_id=%s"

                cursor.execute(query,(product_id,))
                self.con.commit()

                if cursor.rowcount>0:
                    print("Product record with ID",product_id," is deleted")
                else:
                    print("Product record with ID", product_id, " is not deleted")
            except Exception:
                print("Failed to Delete record")
            finally:
                cursor.close()


#menu driven
b=Product_db()

while True:
    print("\n")
    print("Shop Management System")
    print("_________________________")
    print("1.Create Product Record")
    print("2.Show All records")
    print("3.Retrive A Record")
    print("4.Update A Record")
    print("5.Delete A Record")
    print("6.Exit")

    ch=int(input("Enter the Choice :"))

    if ch==1:
        name=input("Enter Product Name :")
        price=int(input("Enter the Price :"))
        quantity=int(input("Enter the Quantity :"))

        b.create(name,price,quantity)


    elif ch==2:

        b.read()


    elif ch==3:
        product_id=int(input("Enter the ID :"))

        b.retrieve(product_id)


    elif ch==4:
        product_id=int(input("Enter the ID :"))
        name = input("Enter Product Name :")
        price = int(input("Enter the Price :"))
        quantity = int(input("Enter the Quantity :"))



        b.update(product_id,name,price,quantity)


    elif ch==5:
        product_id=int(input("Enter the ID :"))


        b.delete(product_id)


    elif ch==6:
        break
    else:
        print("Invalid choice")

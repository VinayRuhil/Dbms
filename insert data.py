import mysql.connector as c

con = c.connect(
    host="localhost",
    user="root",
    password="vinayruhil@174",
    database="example",
)

## Insert Data ##

def insert_data(con):
  Fname = input("Enter Fmame: ")
  Ssn = int(input("Enter Ssn: "))
  Address = input("Enter Address: ")
  Salary = int(input("Enter Salary: "))
  val = (Fname,Ssn,Address,Salary)
  cursor = con.cursor()
  sql = "INSERT INTO employee (Fname,Ssn,Address,Salary) VALUES (%s,%s,%s,%s)"
  cursor.execute(sql, val)
  con.commit()
  print("{} data Inserted".format(cursor.rowcount))

insert_data(con)


## Show Data ##

def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM employee"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("There is not any data")
  else:
    for data in results:
      print(data)
      
show_data(db)

## Update Data ##

def update_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("Choose id employee: ")
  name = input("New Name: ")
  address = input("New Address: ")

  sql = "UPDATE employee SET name=%s, address=%s WHERE customer_id=%s"
  val = (name, address, customer_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data successfully changed".format(cursor.rowcount))

## Delete Data ##

def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("Choose id customer> ")
  sql = "DELETE FROM customers WHERE customer_id=%s"
  val = (customer_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data successfully deleted".format(cursor.rowcount))


## Search Data ##

def search_data(db):
  cursor = db.cursor()
  keyword = input("Keyword: ")
  sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("There is not any data")
  else:
    for data in results:
      print(data)

from tkinter import EXCEPTION
import mariadb
conn = mariadb.connect(
  user="root",
  password="Kprv@0600",
  host="localhost",
  port=3306,
  database="python_employee"
  )
cur = conn.cursor()
conn.autocommit = True
try:
  cur.execute("create table myemployees2 (name VARCHAR(30), MOBILE INTEGER, age INTEGER,Salary INTEGER, City VARCHAR(40), Department VARCHAR(30) )");
except Exception as y:
  print(y)
cur.execute("INSERT INTO myemployees2 (name, MOBILE, age, Salary, City, Department) VALUES ('rishi',98,23,100000,'mysore','IDS'), ('rose',01,24,100002,'blore','DH'), ('sam',155,22,898111,'mys','MD')");

cur.execute("SELECT name, MOBILE, age, Salary, City, Department FROM myemployees2")

for (name,MOBILE,age,Salary,City,Department) in cur:
  print("Name:",{name}, "Contact:",{MOBILE}, "Age:",{age}, "SALARY:",{Salary}, "CITY:",{City}, "DEPARTMENT:",{Department})


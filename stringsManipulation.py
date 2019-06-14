import datetime
import mysql.connector

cnx = mysql.connector.connect(user='anshu', database='college', password='anshu123')
cursor = cnx.cursor()
print("Please enter student details. \nName: ")
s_name = input()
print("\nAge:.")
age = int(input())
print("\nCourse:")
course = input()
print("\nContact:")
contact = int(input())
print("\nAddress:")
address = input()
query = ("INSERT INTO stu" "(s_name, age, course, contact, address) " "VALUES (%s, %s, %s, %s, %s)")
data_student = (s_name, age, course, contact, address)
cursor.execute(query, data_student) 
cnx.commit()
cursor.close()
cnx.close()

#https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
#https://pynative.com/install-mysql-connector-python/
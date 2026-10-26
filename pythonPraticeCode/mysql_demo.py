import mysql.connector as db
from mysql.connector import Error

def main():
	connection = None
	cursor = None
	try:
		connection = db.connect(host="localhost",user="python_user",password="Python@1234",database="python_db",port=3306)
		if connection.is_connected():
			print("connected to Mysql successfully!")
		cursor = connection.cursor()
		insert_query = """ INSERT INTO user (sno,name) values (%s,%s)"""
		user_data = ("1001","mani")
		cursor.execute(insert_query, user_data)
		connection.commit()
		select_query =""" select sno,name FROM user where sno = %s"""
		cursor.execute(select_query,(1001,))
		record = cursor.fetchall()
		if record:
			print("\nfetched record from Mysql : ")
			print("SNo : ",record[0])
			print("Name : ",record[1])
	except Error as e:
		print("MySql error : ",e)
		if connection and connection.is_connected():
			connection.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if connection and connection.is_connected():
			connection.close()
			print("\n MySql connection closed.")
 
if __name__ == "__main__":
	main()

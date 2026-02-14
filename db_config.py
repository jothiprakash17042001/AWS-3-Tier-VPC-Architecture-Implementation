import mysql.connector

def get_db_connection():
    try:
        # Connect to RDS server without specifying database initially
        conn = mysql.connector.connect(
            host="database-01.c4x08mokks33.us-east-1.rds.amazonaws.com", # your AWS RDS endpoint paste same place 
            user="admin", # your admin name in RDS
            password="kalaprakash" Your Password in AWS RDS
        )
        cursor = conn.cursor()

        # Create database and table if they are missing
        cursor.execute("CREATE DATABASE IF NOT EXISTS reservation")
        cursor.execute("USE reservation")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                booking_date VARCHAR(50),
                booking_time VARCHAR(50)
            )
        """)
        return conn
    except mysql.connector.Error as err:
        print(f"Connection Error: {err}")
        return None

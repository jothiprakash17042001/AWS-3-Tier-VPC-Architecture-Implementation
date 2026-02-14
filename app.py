from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Updated Configuration - Cleaned from your screenshot error
DB_CONFIG = {
    'host': 'database-01.c4x08mokks33.us-east-1.rds.amazonaws.com', # ENDPOINT ONLY
    'user': 'admin',
    'password': 'kalaprakash', # Use the password you set in RDS
    'database': 'reservation',
    'cursorclass': pymysql.cursors.DictCursor
}

@app.route('/api/reserve', methods=['POST'])
def reserve():
    connection = None
    try:
        data = request.get_json()

        # Establish connection
        connection = pymysql.connect(**DB_CONFIG)

        with connection.cursor() as cursor:
            sql = "INSERT INTO bookings (name, email, booking_date, booking_time) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (data['name'], data['email'], data['date'], data['time']))

        connection.commit()
        return jsonify({"message": "Reservation saved successfully!"}), 200

    except Exception as e:
        print(f"Database Error: {e}")
        return jsonify({"error": f"Database Connection Failed: {str(e)}"}), 500

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    # 0.0.0.0 is required for AWS Networking
    app.run(host='0.0.0.0', port=5000)

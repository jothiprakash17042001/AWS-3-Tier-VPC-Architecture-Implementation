from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import os

app = Flask(__name__)
CORS(app)

DB_CONFIG = {
    'host': 'database-01.c4x08mokks33.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'shanmugam',
    'database': 'reservation',
    'cursorclass': pymysql.cursors.DictCursor
}

@app.route('/api/reserve', methods=['POST'])
def reserve():
    connection = None
    try:
        data = request.get_json()

        # Validate Required Fields
        required_fields = ['name', 'age', 'address', 'email', 'date', 'time']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"{field} is required"}), 400

        connection = pymysql.connect(**DB_CONFIG)



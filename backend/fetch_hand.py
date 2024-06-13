from server import get_db_connection
from convert_history import parse_hand_history
import psycopg2
from flask import Flask

fh_app = Flask(__name__)

# This function should not introduce changes to the database. No commits are made.
@fh_app.route('/fetch_hand', methods=['GET'])
def fetch_hand(hand_id: int, username: str, conn: psycopg2.connect) -> str:
    cursor = conn.cursor()
    with open ('backend/sql/fetch_hand_query_template.sql') as fetch_hand_query_template:
        cursor.execute(fetch_hand_query_template.read())
        cursor.execute(f'EXECUTE hand_data({hand_id}, \'{username}\')') # TODO: remove security vulnerability.
        output: str = cursor.fetchall()

    cursor.close()

    return output

fh_app.run()
print(fetch_hand(2524, 'CashMatteo', get_db_connection())) # For testing purposes.


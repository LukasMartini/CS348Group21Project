from server import get_db_connection
from convert_history import parse_hand_history
import psycopg2

# This function should not introduce changes to the database. No commits are made.
def fetch_hand(hand_id: int, username: str, conn: psycopg2.connect) -> str:
    cursor = conn.cursor()
    with open ('backend/sql/fetch_hand_query_template.sql') as fetch_hand_query_template:
        cursor.execute(fetch_hand_query_template.read())
        cursor.execute(f'EXECUTE hand_data({hand_id}, \'{username}\')') # TODO: remove security vulnerability.
        output: str = cursor.fetchall()

    cursor.close()

    return output

print(fetch_hand(1, 'Ted', get_db_connection()))


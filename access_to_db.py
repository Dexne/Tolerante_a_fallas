import sqlite3


def fetch_user_by_id(user_id):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user_data = cursor.fetchone()
        conn.close()
        return user_data
    except sqlite3.Error as e:
        print("Error en la consulta a la base de datos:", e)
        return None

user_id = 1
user_info = fetch_user_by_id(user_id)
if user_info:
    print("Información del usuario:", user_info)

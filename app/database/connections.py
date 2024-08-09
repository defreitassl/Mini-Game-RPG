import mysql.connector


def create_conn():
    """Create a database connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',       
            database='RPG',         
            user='root',            
            password='admin' 
        )
        if connection.is_connected():
            print("\n Database RPG connection successful! \n")
            return connection
    except Exception as e:
        print(f"Error: {e}")
        return None
    

def close_conn(connection, cursor, commit=True):
    try:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            if commit:
                connection.commit()
            connection.close()
    except Exception as e:
        print(f"Error closing connection or cursor: {e}")

    
conn = create_conn()
cursor = conn.cursor()

    

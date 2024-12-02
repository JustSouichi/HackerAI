import sqlite3

def analyze_logins(database_file):
    conn = sqlite3.connect(database_file)  # Connect to the SQLite database
    cursor = conn.cursor()

    # Query to find logins outside normal hours
    cursor.execute("""
        SELECT user_id, timestamp, ip_address 
        FROM logins
        WHERE strftime('%H', timestamp) NOT BETWEEN '08' AND '22'
    """)
    results = cursor.fetchall()

    if results:
        print("Suspicious logins detected:")
        for row in results:
            print(f"User {row[0]} logged in at {row[1]} from IP {row[2]}")
    else:
        print("No suspicious activity detected.")

    conn.close()

# Run the analysis
if __name__ == "__main__":
    analyze_logins("data/example.db")  # Use the database file, not the SQL script

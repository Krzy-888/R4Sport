import sqlite3
print(sqlite3.sqlite_version)
conn = sqlite3.connect('data/Users.sqlite')
curr = conn.cursor()
curr.execute("CREATE TABLE users(login text, password text)")
curr.execute("""
    INSERT INTO users VALUES
        ('TestAdmin@test.com', 'Pass1234!')
""")
conn.commit()
conn.close()
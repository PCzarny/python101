import sqlite3

connection = sqlite3.connect("test.db")
# connection = sqlite3.connect(':memory') # to store data in memory

# To enable using column names not only indexes
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS projects;")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY ASC,
        title varchar(250) NOT NULL
    )""")

cursor.executescript("""
    DROP TABLE IF EXISTS tasks;
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY ASC,
        title varchar(250) NOT NULL,
        description varchar(250) DEFAULT '',
        project_id INTEGER NOT NULL,
        FOREIGN KEY(project_id) REFERENCES projects(id)
    );""")

cursor.execute("INSERT INTO projects VALUES(NULL, ?);", ("Home",))

cursor.execute('SELECT id FROM projects WHERE title = ?', ('Home',))
project_id = cursor.fetchone()[0]

tasks = (
    (None, 'Shopping', '', project_id),
    (None, 'Washing dishes', '', project_id),
    (None, 'Cleaning', '', project_id)
)

cursor.executemany('INSERT INTO tasks VALUES(?,?,?,?)', tasks)
connection.commit()

def get_all_tasks () :
    cursor.execute(
        """
        SELECT * FROM tasks;
        """)
    tasks = cursor.fetchall()
    for task in tasks:
        print(task['title'])

get_all_tasks()

cursor.execute('UPDATE tasks SET title=? WHERE title=?', ('Go shopping', 'Shopping'))
print()
cursor.execute('DELETE FROM tasks WHERE title=?', ('Cleaning',))

get_all_tasks()

connection.close()
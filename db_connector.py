import sqlite3 #pip install pysqlite3

sql_file_name = "entries.sql"
db_name = "entries.db"
db_conn = None
db_cursor = None

def create_connection():
    db_conn = sqlite3.connect(db_name)

    db_cursor = db_conn.cursor()

    with open(sql_file_name, "r") as file:
        sql_content = file.read()
    
    db_cursor.executescript(sql_content)

    db_conn.commit()


def validate_input(input_str):
    valid = True
    if(input_str is None):
        valid = False
    else:
        injection_str = ['INSERT', 'DELETE', 'DROP', '=', 'OR', 'CREATE', 'JOIN', '--', 'WHERE', '*', '>', '<', 'ADD']
        for entry in injection_str:
            if(entry in input_str.upper()):
                valid = False
    return valid

def search_by_courseID(faculty_code, course_num):
    query_result = None

    if(db_cursor is not None and validate_input(faculty_code) and validate_input(course_num)):
        query = "SELECT * FROM Entry WHERE uofm_course_details LIKE '%" + faculty_code + "%' AND  uofm_course_details LIKE '%" + course_num + "%';"
        db_cursor.execute(query)
        query_result = db_cursor.fetchall()
    
    return query_result

def close_connection():
    if(db_conn is not None):
        db_conn.close()







    











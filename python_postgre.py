import psycopg2

hostname = 'localhost'
database = 'python-postgre'
username = 'postgres'
pwd = 'enter password here'
port_id = 5432
conn = None
cur = None


try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)
    
    cur = conn.cursor()
   # cur.execute('DROP TABLE IF EXISTS EMPLOYEE')
    create_script = ''' Create Table if not exists EMPLOYEE(

    id  int Primary key,
    name    varchar(40) not NULL,
    salary  int,
    department_id   varchar(20))'''

    cur.execute(create_script)

    '''insert_script = 'INSERT if not exists INTO  EMPLOYEE(id, name, salary, department_id) values (%s, %s, %s, %s)'
    insert_values =[(5, 'John', 20000, 'D2'), (6, 'Xavier', 18000, 'D4')]
    for record in insert_values:
        cur.execute(insert_script, record)
    conn.commit()
    '''

    delete_script = "delete from employee where department_id = 'D4'"
    cur.execute(delete_script)


    cur.execute('select * from employee order by id asc')
    for record in cur.fetchall():
        print(record)
    

    '''update_script = 'update employee set salary = salary + (salary * 0.5)'
    cur.execute(update_script)
    
    '''

    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()




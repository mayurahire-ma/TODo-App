import mysql.connector
conn_obj=mysql.connector.connect(host='localhost',
                        user='root',
                        password='Mayur1710',
                        database='mydata')
if conn_obj:
    print("Connection Established")
else:
    print("Please try again")
    
#Cursor Object
cur_object=conn_obj.cursor()
def create_table():
    cur_object.execute("create table if not exists tasksatable(task Text,task_status text,tast_due_date Date)") 
conn_obj.commit()

def add_data(task,task_status,tast_due_date):
    cur_object.execute('INSERT INTO tasksatable(task,task_status,tast_due_date)VALUES(%s,%s,%s)',(task,task_status,tast_due_date))
conn_obj.commit()

def view_all_data():
    cur_object.execute('select * from tasksatable')
    data = cur_object.fetchall()
    return data

def view_unique_task():
    cur_object.execute('SELECT DISTINCT task FROM tasksatable')
    data = cur_object.fetchall()
    return data

def get_task(task):
    cur_object.execute('select * from tasksatable WHERE task = "{}"'.format(task))
    data = cur_object.fetchall()
    return data 

def edit_task_data(new_task,new_task_status,new_tast_due_date,task,task_status,tast_due_date):
    cur_object.execute("UPDATE tasksatable SET task = %s,task_status= %s, tast_due_date= %s WHERE task = %s and task_status=%s and tast_due_date=%s",(new_task,new_task_status,new_tast_due_date,task,task_status,tast_due_date))
    conn_obj.commit()
    data = cur_object.fetchall()
    return data 

def delete_data(task):
    cur_object.execute('DELETE FROM tasksatable WHERE task="{}"'.format(task))
    conn_obj.commit()

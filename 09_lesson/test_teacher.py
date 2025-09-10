from sqlalchemy import create_engine, inspect, text
import psycopg2
#from TeacherTable import TeacherTable
#from TeacherApi import TeacherApi

db_connection_string = "postgresql://_____________________" # вставить строку подключения
db = create_engine(db_connection_string)


#получение информации о таблицах
def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[4] == 'teacher'


#Добавить преподавателя: insert
def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("INSERT INTO teacher(\"teacher_id\", \"email\", \"group_id\") VALUES (:teacher_id, :email, :group_id)")
    connection.execute(sql,
                       {"teacher_id": 1000000, 
                        "email": "skypro@mail.ru",
                        "group_id": 876})
   
    transaction.commit()
    connection.close()


# Обновить информацию о преподавателе: update
def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE teacher SET group_id = :group_id WHERE email = :email")
    connection.execute(sql, {"group_id": 543, "email": "skypro@mail.ru"})

    
    transaction.commit()
    connection.close()

# Удалить преподавателя
def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM teacher WHERE email = :email")
    connection.execute(sql, {"email": "skypro@mail.ru"})
    rows = connection.execute(sql,{"email": "skypro@mail.ru"})
    assert rows.rowcount == 0
    
    transaction.commit()
    connection.close()
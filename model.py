import mysql.connector
class Model:
    def connect(self):
        return mysql.connector.connect (host="localhost", user="root", password="", database="crudpython" )

    def read(self):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("SELECT * FROM backend")
        return cur.fetchall()

    def create(self, student_id, student_name, student_class, student_gender, favorite_course, reason):
        con = Model.connect(self)
        cur = con.cursor()
        sql = ("INSERT INTO backend (student_id, student_name, student_class, student_gender, favorite_course, reason) VALUES (%s,%s,%s,%s,%s,%s)")
        data = (student_id, student_name, student_class, student_gender, favorite_course, reason)
        cur.execute(sql,data)
        con.commit()
        return True

    def readById(self, id):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("SELECT * FROM backend WHERE student_id = %s", (id,))
        return cur.fetchall()

    def update(self, student_id, student_name, student_class, student_gender, favorite_course, reason, id):
        con = Model.connect(self)
        cur = con.cursor()
        sql = ("UPDATE backend SET student_id = %s, student_name = %s, student_class = %s, student_gender = %s, favorite_course = %s, reason = %s WHERE student_id = %s")
        data = (student_id, student_name, student_class, student_gender, favorite_course, reason, id,)
        cur.execute(sql,data)
        con.commit()
        return True

    def delete(self, id):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("DELETE FROM backend WHERE student_id = %s", (id,))
        con.commit()
        return True
from flask import Flask,request,jsonify
import psycopg2

app = Flask(__name__)

## DATABASE details ##

db_name = "ravnxhin"
db_user = "ravnxhin"
db_pass = "Bvni2U-fQ0XLFRqlsieWB-yiFHhGwgR3"
db_host = "john.db.elephantsql.com"
db_port = "5432"

## Connnecting DATABASE ##

connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)

print("database connected")

### Creating tables ###

# curr = connection.cursor()
# req = """CREATE TABLE task (ID INT PRIMARY KEY NOT NULL,
#                             TITLE TEXT NOT NULL,
#                             DESCRIPTION TEXT NOT NULL,
#                             DONE BOOLEAN NOT NULL)"""
# curr.execute(req)
# connection.commit()
# print("table created")



@app.route('/todo/api/v1.0/tasks',methods=['GET'])
def get_alltasks():
    dic = []
    # connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
    curr = connection.cursor()
    req = "SELECT * FROM task"
    curr.execute(req)
    data = curr.fetchall()
    connection.commit()
    connection.close()
    for i in range(len(data)):
            dic.append({'id':data[i][0],'title':data[i][1],'description':data[i][2],'done':bool(data[i][3])})
    return jsonify(dic)



@app.route('/todo/api/v1.0/tasks/<id>', methods=['GET'])
def getting_singleTask(id):
    connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
    curr = connection.cursor()
    req = "SELECT * FROM task WHERE id = " + str(id)
    curr.execute(req)
    data = curr.fetchall()
    connection.commit()
    connection.close()
    for i in range(len(data)):
        dic = {'id':data[i][0],'title':data[i][1],'description':data[i][2],'done':bool(data[i][3])}
    return jsonify(dic)    




@app.route('/todo/api/v1.0/tasks',methods=['POST'])
def addTasks():
    data = request.get_json()
    connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
    curr = connection.cursor()
    req = "SELECT id FROM task"
    curr.execute(req)
    find_id = curr.fetchall()
    if (data != None) and ('id' in data):
        if (len(find_id) != 0):
            for i in find_id:
                if (i[0] == data['id']):
                    return "id already taken"
        req1 = "INSERT INTO task(ID, TITLE, DESCRIPTION, DONE) VALUES(" + str(data['id']) + ",'" + str(data['title'])+ "','" +str(data['description']) + "'," + str(data['done']) + ")"
        curr.execute(req1)
        connection.commit()
        connection.close()
        return 'task added'
    return "id error"



@app.route('/todo/api/v1.0/tasks/<id>',methods=['PUT'])
def update_Task(id):
    data = request.get_json()
    connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
    curr = connection.cursor()
    req = "SELECT id FROM task"
    curr.execute(req)
    find_id = curr.fetchall()
    if (len(find_id) != 0):
        if (data != None):
            for i in find_id:
                if (str(i[0]) == str(id)):
                    req1 = "UPDATE task SET "
                    for i in data:
                        if (str(i) == 'title'):
                            req1 += "title='" + data['title'] + "',"
                        if (str(i) =='description'):
                            req1 += "description='" + data['description'] + "',"
                        if (str(i) =='done'):
                            req1 += "done=" + str(data['done']) + ","
                    req1 = req1[:len(req1)-1]
                    req1 += " WHERE id = " + str(id)
                    curr.execute(req1)
                    connection.commit()
                    connection.close()
                    return "task updated"
    return "id not found"
                    



@app.route('/todo/api/v1.0/tasks/<id>', methods=['DELETE'])
def delete_Task(id):
    connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
    curr = connection.cursor()
    req = "SELECT id FROM task"
    curr.execute(req)
    find_id = curr.fetchall()
    for i in find_id:
        if (str(i[0]) == str(id)):    
            req = "DELETE FROM task WHERE id = " + str(id)
            curr.execute(req)
            connection.commit()
            connection.close()
            return "task deleted"
    return "id not found"





if __name__ == "__main__":
    app.run(debug=True)





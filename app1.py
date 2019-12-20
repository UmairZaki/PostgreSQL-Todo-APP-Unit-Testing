from flask import Flask,request,jsonify
import psycopg2

app = Flask(__name__)

## DATABASE details ##

db_name = "vhpimhhs"
db_user = "vhpimhhs"
db_pass = "k3CiOaI6T3Z4ijDKanhunq2doaYFJTXl"
db_host = "rajje.db.elephantsql.com"
db_port = "5432"

## Connnecting DATABASE ##

connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)

print("database connected")

### Creating tables ###

# curr = connection.cursor()
# tab = """CREATE TABLE newtable (ID INT PRIMARY KEY NOT NULL,
#                             TITLE TEXT NOT NULL,
#                             DESCRIPTION TEXT NOT NULL,
#                             DONE BOOLEAN NOT NULL)"""
# curr.execute(tab)
# connection.commit()
# print("table created")



@app.route('/getTask', methods=['GET'])
def getTask():
    task = []
    # connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
    curr = connection.cursor()
    req = "SELECT * FROM newtable"
    curr.execute(req)
    data = curr.fetchall()
    connection.commit()
    connection.close()
    for i in range(len(data)):
            task.append({'id':data[i][0],'title':data[i][1],'description':data[i][2],'done':bool(data[i][3])})
    return jsonify(task)



@app.route('/getSingleTask/<id>', methods=['GET'])
def getSingleTask(id):
    connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
    curr = connection.cursor()
    req = "SELECT * FROM newtable WHERE id = " + str(id)
    curr.execute(req)
    data = curr.fetchall()
    connection.commit()
    connection.close()
    for i in range(len(data)):
        task = {'id':data[i][0],'title':data[i][1],'description':data[i][2],'done':bool(data[i][3])}
    return jsonify(task)    




@app.route('/createTask', methods=['POST'])
def createTask():
    task = request.json
    connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
    curr = connection.cursor()
    req = "SELECT id FROM newtable"
    curr.execute(req)
    match = curr.fetchall()
    if (task != None) and ('id' in task):
        if (len(match) != 0):
            for i in match:
                if (i[0] == task['id']):
                    return "id already taken"
        req1 = "INSERT INTO newtable(ID, TITLE, DESCRIPTION, DONE) VALUES(" + str(task['id']) + ",'" + str(task['title'])+ "','" +str(task['description']) + "'," + str(task['done']) + ")"
        curr.execute(req1)
        connection.commit()
        connection.close()
        return 'task added'
    return "id error"



@app.route('/updateTask', methods=['PUT'])
def updateTask():
    task = request.json
    connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
    curr = connection.cursor()
    req = "SELECT id FROM newtable"
    curr.execute(req)
    match = curr.fetchall()
    if (len(match) != 0):
        if (task != None):
            for i in match:
                if (str(i[0]) == str(id)):
                    req1 = "UPDATE task SET "
                    for i in task:
                        if (str(i) == 'title'):
                            req1 += "title='" + task['title'] + "',"
                        if (str(i) =='description'):
                            req1 += "description='" + task['description'] + "',"
                        if (str(i) =='done'):
                            req1 += "done=" + str(task['done']) + ","
                    req1 = req1[:len(req1)-1]
                    req1 += " WHERE id = " + str(id)
                    curr.execute(req1)
                    connection.commit()
                    connection.close()
                    return "task updated"
    return "id not found"
                    



@app.route('/deleteTask/<id>', methods=['DELETE'])
def deleteTask(id):
    connection = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
    curr = connection.cursor()
    req = "SELECT id FROM newtable"
    curr.execute(req)
    match = curr.fetchall()
    for i in match:
        if (str(i[0]) == str(id)):    
            req = "DELETE FROM newtable WHERE id = " + str(id)
            curr.execute(req)
            connection.commit()
            connection.close()
            return "task deleted"
    return "id not found"





if __name__ == "__main__":
    app.run(debug=True)





#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort

#add module for auth 
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
#Create auth object
auth = HTTPBasicAuth()


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    },
    {
        'id': 3,
        'title': u'Stock market',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]




'''
Simple Hello world program 
'''
@app.route('/')
def index():
    return "Hello, World!"

'''
Auth Function for authorized access
'''
@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None


'''
Unauthorized access function
'''
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

'''
Route for login popup. if login username correct then show tasks
'''
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})

'''
End Auth function
'''


'''
Retrive all task in json form
'''
# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})


'''
Create new task 
''' 
# @app.route('/todo/api/v1.0/tasks', methods=['POST'])
# def create_task():
#     if not request.json or not 'title' in request.json:
#         abort(400)
#     task = {
#         'id':  tasks[-1]['id'] + 1,
#         'title': request.json['title'],
#         'description': request.json.get('description', ""),
#         'done': False
#     }
#     tasks.append(task)
#     return jsonify({'task': task}), 201


'''
Update task 
'''
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     if not request.json:
#         abort(400)
#     if 'title' in request.json and type(request.json['title']) != unicode:
#         abort(400)
#     if 'description' in request.json and type(request.json['description']) is not unicode:
#         abort(400)
#     if 'done' in request.json and type(request.json['done']) is not bool:
#         abort(400)
#     task[0]['title'] = request.json.get('title', task[0]['title'])
#     task[0]['description'] = request.json.get('description', task[0]['description'])
#     task[0]['done'] = request.json.get('done', task[0]['done'])
#     return jsonify({'task': task[0]})


'''
Delete task
'''
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
# def delete_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     tasks.remove(task[0])
#     return jsonify({'result': True})


'''
Improved delete task function. after deleted task.tasks will show json format
'''
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     return jsonify({'task': task[0]})

# Make public task 
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

'''
Create a task using method 
'''
# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': [make_public_task(task) for task in tasks]})


# Error Handling
'''
404 Error Handling
''' 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404) 


 
'''
Abort task
'''
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     return jsonify({'task': task[0]})


if __name__ == '__main__':
    app.run(debug=True)

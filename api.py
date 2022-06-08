from flask import Flask, request
from flask_restx import Api, Resource, reqparse, fields, abort

app = Flask(__name__)
api = Api(app)

model = api.model('Model', {
    'task': fields.String,
    'uri': fields.Url('todo_ep')
})

# multiple URLs
# api.add_resource(HelloWorld, '/hello', '/world')
#
# # or
#
# @api.route('/hello', '/world')

# parser = reqparse.RequestParser()
# parser.add_argument('rate', type=int, help='Rate to charge for this resource')
# args = parser.parse_args()


# @api.route('/hello', '/world')
# class HelloWorld(Resource):
#     def get(self):
#         return {'Hello': 'World'}, 201, {'Etag': 'some-opaque-string'}


# @api.route('/todo/<int:todo_id>', endpoint='todo_ep')
# class HelloWorld(Resource):
#     def get(self, todo_id):
#         return {todo_id: 'World'}, 201, {'Etag': 'some-opaque-string'}


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

parser = reqparse.RequestParser()
parser.add_argument('task')


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


model = api.model('Model', {
    'task': fields.String,
    'uri': fields.Url('todo_ep'),
    'status': fields.String,
    'check': fields.Boolean
})


class TodoDao:
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'


@api.route('/todo/<int:todo_id>', endpoint='todo_ep')
class Todo(Resource):
    @api.marshal_with(model)
    def get(self, **kwargs):
        return TodoDao(todo_id=1, task='Remember the milk')

    # def get(self, todo_id):
    #     abort_if_todo_doesnt_exist(todo_id)
    #     return TODOS[todo_id]
    #
    # def delete(self, todo_id):
    #     abort_if_todo_doesnt_exist(todo_id)
    #     del TODOS[todo_id]
    #     return '', 204
    #
    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201


# @api.route('/<string:todo_id>')
# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}
#
#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}


if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from .models import create_todo, get_todos, get_todo_by_id, update_todo, delete_todo, get_total_todos_count

bp = Blueprint('todo', __name__)

# Create a new todo
@bp.route('/todos', methods=['POST'])
@jwt_required()
def add_todo():
    user_id = get_jwt_identity()
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title:
        return jsonify({'error': 'Title is required.'}), 400

    # Create the todo item and get its ID
    todo_id = create_todo(user_id, title, description)

    # Retrieve the created todo item using the ID
    todo = get_todo_by_id(user_id, todo_id)

    return jsonify({
            'id': todo['id'],
            'title': todo['title'],
            'description': todo['description']
    }), 201

# Get all todos with optional pagination
@bp.route('/todos', methods=['GET'])
@jwt_required()
def get_all_todos():
    user_id = get_jwt_identity()
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    # Fetch the total count of todos for the user
    total_count = get_total_todos_count(user_id)

    # Fetch the paginated todos
    todos = get_todos(user_id, page, limit)

    return jsonify({
        'data': [dict(todo) for todo in todos],
        'page': page,
        'limit': limit,
        'total': total_count
    }), 200

# Get a specific todo by ID
@bp.route('/todos/<int:todo_id>', methods=['GET'])
@jwt_required()
def get_todo(todo_id):
    user_id = get_jwt_identity()
    todo = get_todo_by_id(user_id, todo_id)

    if todo is None:
        return jsonify({'error': 'Todo not found.'}), 404

    return jsonify(dict(todo)), 200

# Update a specific todo by ID
@bp.route('/todos/<int:todo_id>', methods=['PUT'])
@jwt_required()
def update_todo_route(todo_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed')

    if title is None and description is None and completed is None:
        return jsonify({'error': 'At least one of title, description, or completed is required to update.'}), 400

    existing_todo = get_todo_by_id(user_id, todo_id)
    if existing_todo is None:
        return jsonify({'error': 'Todo not found.'}), 404

    update_todo(
        user_id,
        todo_id,
        title or existing_todo['title'],
        description or existing_todo['description'],
        completed if completed is not None else existing_todo['completed']
    )
    return jsonify({'message': 'Todo updated successfully.'}), 200

# Delete a specific todo by ID
@bp.route('/todos/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete_todo_route(todo_id):
    user_id = get_jwt_identity()
    delete_todo(user_id, todo_id)
    return jsonify({'message': 'Todo deleted successfully.'}), 204
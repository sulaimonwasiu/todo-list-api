import bcrypt
from flask import jsonify
from flask_jwt_extended import create_access_token
from flask import Blueprint, g, request
from todo.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    db = get_db()
    error = None

    if not email:
        error = 'Email is required.'
    elif not password:
        error = 'Password is required.'

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    if error is None:
        try:
            db.execute(
                "INSERT INTO user (email, password) VALUES (?, ?)",
                (email, hashed_password),
            )
            db.commit()
            return jsonify({'message': 'User registered successfully'}), 201
        
        except db.IntegrityError:
            return jsonify({'message': f'User with email {email} is already registered.'}), 400
    return jsonify({'message': error})

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    db = get_db()

    user = db.execute(
        'SELECT * FROM user WHERE email = ?', (email,)
    ).fetchone()

    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        access_token = create_access_token(identity=user['id'])
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid email or password"}), 401
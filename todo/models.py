from .db import get_db

def create_todo(user_id, title, description):
    db = get_db()
    cursor = db.execute(
        'INSERT INTO todo (title, description, completed, user_id) VALUES (?, ?, ?, ?)', 
        (title, description, False, user_id)
    )
    db.commit()
    return cursor.lastrowid  # Return the ID of the newly created todo

def get_todos(user_id, page, limit):
    db = get_db()
    query = 'SELECT * FROM todo WHERE user_id = ? ORDER BY id LIMIT ? OFFSET ?'
    return db.execute(query, (user_id, limit, (page - 1) * limit)).fetchall()

def get_total_todos_count(user_id):
    db = get_db()
    return db.execute('SELECT COUNT(*) FROM todo WHERE user_id = ?', (user_id,)).fetchone()[0]

def get_todo_by_id(user_id, todo_id):
    db = get_db()
    return db.execute('SELECT * FROM todo WHERE id = ? AND user_id = ?', (todo_id, user_id)).fetchone()

def update_todo(user_id, todo_id, title, description, completed):
    db = get_db()
    db.execute('UPDATE todo SET title = ?, description = ?, completed = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ? AND user_id = ?',
               (title, description, completed, todo_id, user_id))
    db.commit()

def delete_todo(user_id, todo_id):
    db = get_db()
    db.execute('DELETE FROM todo WHERE id = ? AND user_id = ?', (todo_id, user_id))
    db.commit()
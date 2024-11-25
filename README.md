# Todo List API

This is a simple Todo List API built using Flask and SQLite. The API allows users to manage their to-do items with features to create, read, update, and delete tasks. User authentication is handled using JWT.

## Features

- User authentication
- Create, retrieve, update, and delete to-do items
- Pagination for retrieving to-do items
- SQLite database for data storage

## Technologies Used

- Flask
- SQLite
- Flask-JWT-Extended
- Click for command line interface

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/todo-list-api.git
   cd todo-list-api
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   python -m flask --app blog init-db
   ```

5. Set the environment variable for the Flask app:

   ```bash
   export FLASK_APP=blog  # On Windows use `set FLASK_APP=blog`
   ```

### Configuration

You can configure the database URI in your Flask application’s configuration. By default, it uses an SQLite database.

Example configuration in `config.py`:

```python
DATABASE = 'todo.db'
```

## API Endpoints

### Authentication

#### Register User

- **Endpoint**: `/auth/register`
- **Method**: `POST`
- **Body**: 
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```

#### Login User

- **Endpoint**: `/auth/login`
- **Method**: `POST`
- **Body**:
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
      "access_token": "your_jwt_token"
  }
  ```

### Todo Items

#### Create Todo Item

- **Endpoint**: `/todos`
- **Method**: `POST`
- **Headers**: 
  - `Authorization: Bearer <access_token>`
- **Body**:
  ```json
  {
      "title": "Buy groceries",
      "description": "Buy milk, eggs, bread"
  }
  ```
- **Response**:
  ```json
  {
      "message": "Todo created successfully.",
      "todo": {
          "id": 1,
          "title": "Buy groceries",
          "description": "Buy milk, eggs, bread",
          "completed": false,
          "created_at": "2024-01-01T00:00:00",
          "updated_at": "2024-01-01T00:00:00"
      }
  }
  ```

#### Get All Todo Items

- **Endpoint**: `/todos`
- **Method**: `GET`
- **Headers**: 
  - `Authorization: Bearer <access_token>`
- **Query Parameters**: 
  - `page` (optional)
  - `limit` (optional)
- **Response**:
  ```json
  {
      "data": [
          {
              "id": 1,
              "title": "Buy groceries",
              "description": "Buy milk, eggs, bread"
          }
      ],
      "page": 1,
      "limit": 10,
      "total": 1
  }
  ```

#### Get Specific Todo Item

- **Endpoint**: `/todos/<int:todo_id>`
- **Method**: `GET`
- **Headers**: 
  - `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  {
      "id": 1,
      "title": "Buy groceries",
      "description": "Buy milk, eggs, bread",
      "completed": false,
      "created_at": "2024-01-01T00:00:00",
      "updated_at": "2024-01-01T00:00:00"
  }
  ```

#### Update Todo Item

- **Endpoint**: `/todos/<int:todo_id>`
- **Method**: `PUT`
- **Headers**: 
  - `Authorization: Bearer <access_token>`
- **Body**:
  ```json
  {
      "title": "Buy groceries",
      "description": "Buy milk and bread",
      "completed": true
  }
  ```
- **Response**:
  ```json
  {
      "message": "Todo updated successfully."
  }
  ```

#### Delete Todo Item

- **Endpoint**: `/todos/<int:todo_id>`
- **Method**: `DELETE`
- **Headers**: 
  - `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  {
      "message": "Todo deleted successfully."
  }
  ```

## Testing the API

You can use tools like Postman or cURL to test the API endpoints. Ensure you have a valid JWT token for authenticated endpoints.

## Project Link
[Project URL](https://roadmap.sh/projects/todo-list-api)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you want to contribute to this project.


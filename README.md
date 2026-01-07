# Todo Web Application

![Banner](https://github.com/user-attachments/assets/42c59f03-67b2-4451-be07-8f531fac6ccb)


A clean and simple Todo web application built with Django that allows users to manage daily tasks efficiently with authentication, priorities and deadlines in an efficent way.

## Features

- User authentication (Signup, Login, Logout)
- Create, update, and delete todos
- Priority levels (Low, Medium, High)
- Strike-through completed tasks automatically
- Due date support
- Clean and modern UI with responsive design

## Tech Stack

- Frontend: HTML, Tailwind CSS
- Backend: Django
- Database: SQLite
- Authentication: Django built-in authentication system

## Installation and Setup

Follow these steps to run the project locally.

#### 1. Clone the repository
```
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

#### 2. Create and activate virtual environment
```
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

#### 3. Install dependencies
```
pip install django
```

#### 4. Run migrations
```
cd todo_web_app
python manage.py makemigrations
python manage.py migrate
```

#### 5. Run Tailwind CSS build
```
npx tailwindcss -i ./todo_web_app/static/src/input.css -o ./todo_web_app/static/src/output.css --watch
```

#### 6. Start the development server
```
python manage.py runserver
```

#### 7. Visit the app at:
```
http://127.0.0.1:8000/todos/
```

## Author  

**Abdul Manan Maqsood**  
- [GitHub](https://github.com/hello-abdul-manan)  
- [LinkedIn](https://www.linkedin.com/in/helloabdulmanan/)

## License  

This project is open source and available for learning and personal use.

---

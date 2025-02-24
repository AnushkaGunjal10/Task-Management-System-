# Task Management System

## 📌 Overview
This **Task Management System** is a web-based application built using **Streamlit** and **MySQL**. It allows users to add, update, view, and search tasks efficiently. The system stores tasks in a MySQL database, ensuring data persistence.

## 🚀 Features
- **Add Task**: Create a new task with a unique ID, description, due date, and priority.
- **Update Task**: Modify task status and due date.
- **View Tasks**: Display all tasks in a tabular format.
- **Search Tasks**: Find tasks based on description or status.
- **Persistent Storage**: Uses MySQL database for task management.

## 🛠️ Technologies Used
- **Python**
- **Streamlit** (for the web interface)
- **MySQL** (for data storage)
- **Pandas** (for data handling)

## 📂 Installation & Setup

### 1️⃣ Install Dependencies
Ensure you have **Python** installed, then install the required libraries:
```sh
pip install streamlit mysql-connector-python pandas
```

### 2️⃣ Set Up MySQL Database
Create a MySQL database named **task_manager** and a table **tasks**:
```sql
CREATE DATABASE task_manager;
USE task_manager;

CREATE TABLE tasks (
    id VARCHAR(255) PRIMARY KEY,
    description TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending',
    due_date DATE NOT NULL,
    priority VARCHAR(10) NOT NULL
);
```

### 3️⃣ Configure Database Connection
Modify the database connection details in `TASK.PY`:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="task_manager"
)
```
Replace `yourpassword` with your actual MySQL root password.

### 4️⃣ Run the Application
Execute the following command in the project directory:
```sh
streamlit run TASK.PY
```

## 📸 Screenshots
🔹 **Task Management UI** (Add, Update, View, Search tasks)

![Task Manager Screenshot](#)

## 📝 Usage
1. **Add a Task**: Enter Task ID, description, due date, and priority, then click **Add Task**.
2. **Update a Task**: Enter Task ID, update the status or due date, then click **Update Task**.
3. **View Tasks**: See all tasks displayed in a table format.
4. **Search Tasks**: Enter a keyword to find specific tasks.

## 🔗 Future Enhancements
- ✅ User authentication
- ✅ Task notifications & reminders
- ✅ Advanced filtering options

## 💡 Credits
Developed by **Anushka Gunjal** 🎉


import streamlit as st
from datetime import datetime, date
import pandas as pd
import mysql.connector
import atexit

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Welcome@2020",
    database="task_manager"
)
cursor = conn.cursor()

class TaskManager:
    def add_task(self, task_id, description, due_date, priority):
        try:
            cursor.execute("INSERT INTO tasks (id, description, due_date, priority) VALUES (%s, %s, %s, %s)",
                           (task_id, description, due_date, priority))
            conn.commit()
            st.success(f"✅ Task '{description}' added with ID {task_id}, Due Date: {due_date}, Priority: {priority}.")
        except Exception as e:
            st.error(f"❌ Error adding task: {e}")

    def update_task(self, task_id, status=None, due_date=None):
        try:
            if status:
                cursor.execute("UPDATE tasks SET status = %s WHERE id = %s", (status, task_id))
            if due_date:
                cursor.execute("UPDATE tasks SET due_date = %s WHERE id = %s", (due_date, task_id))
            conn.commit()
            st.success(f"🔄 Task ID {task_id} updated successfully.")
        except Exception as e:
            st.error(f"❌ Error updating task: {e}")

    def view_tasks(self):
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        if not tasks:
            st.warning("No tasks available.")
            return
        df = pd.DataFrame(tasks, columns=["Task ID", "Description", "Status", "Due Date", "Priority"])
        st.dataframe(df, use_container_width=True)

    def search_task(self, keyword):
        cursor.execute("SELECT * FROM tasks WHERE description LIKE %s OR status LIKE %s", (f"%{keyword}%", f"%{keyword}%"))
        tasks = cursor.fetchall()
        if tasks:
            df = pd.DataFrame(tasks, columns=["Task ID", "Description", "Status", "Due Date", "Priority"])
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("🚫 No matching tasks found.")

# Streamlit UI
st.set_page_config(page_title="Task Manager", page_icon="✅", layout="wide")

st.title("📝 Task Manager with Streamlit")

manager = TaskManager()

tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Task", "🔄 Update Task", "📋 View Tasks", "🔍 Search Task"])

with tab1:
    st.subheader("➕ Add a New Task")
    task_id = st.text_input("Enter Task ID")
    description = st.text_input("Enter Task Description")
    due_date = st.date_input("Enter Due Date", min_value=date.today())
    priority = st.selectbox("Select Priority", ["High", "Medium", "Low"])
    if st.button("Add Task"):
        if task_id and description:
            manager.add_task(task_id, description, due_date.strftime("%Y-%m-%d"), priority)
        else:
            st.warning("⚠️ Please enter Task ID and Description.")

with tab2:
    st.subheader("🔄 Update Task Status or Due Date")
    task_id_update = st.text_input("Enter Task ID to Update")
    status = st.selectbox("Select New Status", ["", "Pending", "In Progress", "Completed"])
    due_date_update = st.date_input("Update Due Date", min_value=date.today())
    if st.button("Update Task"):
        if task_id_update:
            manager.update_task(task_id_update, status if status else None, due_date_update.strftime("%Y-%m-%d"))
        else:
            st.warning("⚠️ Please enter a valid Task ID.")

with tab3:
    st.subheader("📋 View All Tasks")
    manager.view_tasks()

with tab4:
    st.subheader("🔍 Search Task by Description or Status")
    keyword = st.text_input("Enter Description or Status")
    if st.button("Search"):
        manager.search_task(keyword)

# Ensure MySQL connection closes when the script stops
def close_connection():
    if conn.is_connected():
        cursor.close()
        conn.close()

atexit.register(close_connection)

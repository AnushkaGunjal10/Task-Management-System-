CREATE DATABASE task_manager;
USE task_manager;

CREATE TABLE IF NOT EXISTS tasks (
    id VARCHAR(50) PRIMARY KEY,
    description TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    due_date DATE NOT NULL,
    priority VARCHAR(10) NOT NULL
);
select *from tasks;
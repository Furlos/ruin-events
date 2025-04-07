document.addEventListener('DOMContentLoaded', () => {
    const menuBtn = document.querySelector('.menu-btn');
    const sideMenu = document.querySelector('.side-menu');
    const closeBtn = document.querySelector('.close-btn');
    const todoForm = document.getElementById('todo-form');
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');

    // Toggle side menu
    menuBtn.addEventListener('click', () => {
        sideMenu.classList.add('open');
    });

    closeBtn.addEventListener('click', () => {
        sideMenu.classList.remove('open');
    });

    // Load saved tasks from local storage
    const savedTasks = JSON.parse(localStorage.getItem('tasks')) || [];
    savedTasks.forEach(task => addTaskToDOM(task));

    // Add task
    todoForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const taskText = todoInput.value.trim();
        if (taskText !== '') {
            addTaskToDOM(taskText);
            saveTask(taskText);
            todoInput.value = '';
        }
    });

    // Remove task
    todoList.addEventListener('click', (event) => {
        if (event.target.tagName === 'BUTTON') {
            const taskItem = event.target.parentElement;
            const taskText = taskItem.firstChild.textContent;
            removeTask(taskText);
            taskItem.remove();
        }
    });

    function addTaskToDOM(taskText) {
        const li = document.createElement('li');
        li.textContent = taskText;
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        li.appendChild(removeButton);
        todoList.appendChild(li);
    }

    function saveTask(taskText) {
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks.push(taskText);
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    function removeTask(taskText) {
        let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks = tasks.filter(task => task !== taskText);
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }
});
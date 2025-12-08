const API = '/api/tasks';

async function loadTasks() {
    const res = await fetch(API);
    const tasks = await res.json();
    const ul = document.getElementById('taskList');
    ul.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.className = task.done ? 'done' : '';
        li.innerHTML = `
            <span>
                <input type="checkbox" ${task.done ? 'checked' : ''} onchange="toggleDone(${task.id}, this.checked)">
                ${task.title}
            </span>
            <button class="delete-btn" onclick="deleteTask(${task.id})">حذف</button>
        `;
        ul.appendChild(li);
    });
}

async function addTask() {
    const title = document.getElementById('titleInput').value.trim();
    if (!title) return alert('عنوان رو بنویس!');
    
    await fetch(API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title })
    });
    document.getElementById('titleInput').value = '';
    loadTasks();
}

async function toggleDone(id, done) {
    await fetch(`${API}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ done })
    });
}

async function deleteTask(id) {
    if (!confirm('مطمئنی می‌خوای حذف کنی؟')) return;
    await fetch(`${API}/${id}`, { method: 'DELETE' });
    loadTasks();
}

// وقتی صفحه لود شد
document.addEventListener('DOMContentLoaded', loadTasks);
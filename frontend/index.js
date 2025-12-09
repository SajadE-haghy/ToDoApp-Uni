const API = '/api/tasks';

async function loadTasks() {
    const res = await fetch('/api/tasks');
    const tasks = await res.json();
    const ul = document.getElementById('taskList');
    ul.innerHTML = '';

    tasks.forEach(task => {
        const isPending = task.status === 'pending';
        const li = document.createElement('li');
        li.className = task.status === 'done' ? 'done' : task.status === 'canceled' ? 'canceled' : '';

        li.innerHTML = `
            <div class="task-main">
                ${isPending ? `<input type="text" value="${task.title}" onchange="updateTitle(${task.id}, this.value)">` : `<strong>${task.title}</strong>`}
                ${task.description ? `<p class="desc">${task.description}</p>` : ''}
                <small>ساخته شده: ${new Date(task.created_at).toLocaleString('fa-IR')}</small>
                ${task.status === 'done' ? `<small class="done">انجام شد: ${new Date(task.completed_at).toLocaleString('fa-IR')}</small>` : ''}
                ${task.status === 'canceled' ? `<small class="canceled">کنسل شد: ${new Date(task.updated_at).toLocaleString('fa-IR')}</small>` : ''}
            </div>
            <div class="actions">
                ${isPending ? `
                    <button onclick="setStatus(${task.id}, 'done')">انجام شد</button>
                    <button onclick="setStatus(${task.id}, 'canceled')">کنسل</button>
                ` : ''}
                <button class="delete-btn" onclick="deleteTask(${task.id})">حذف</button>
            </div>
        `;
        ul.appendChild(li);
    });
}

async function updateTitle(id, newTitle) {
    if (!newTitle.trim()) return;
    await fetch(`/api/tasks/${id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title: newTitle})
    });
}

async function addTask() {
    const title = document.getElementById('titleInput').value.trim();
    const desc = document.getElementById('descInput').value.trim();
    if (!title) return alert('عنوان رو بنویس!');
    
    await fetch(API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description: desc })
    });
    document.getElementById('titleInput').value = '';
    document.getElementById('descInput').value = '';
    loadTasks();
}

async function setStatus(id, status) {
    await fetch(`/api/tasks/${id}/status`, {   
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status })
    });
    loadTasks();
}

async function deleteTask(id) {
    if (!confirm('مطمئنی؟')) return;
    await fetch(`${API}/${id}`, { method: 'DELETE' });
    loadTasks();
}

document.addEventListener('DOMContentLoaded', loadTasks);
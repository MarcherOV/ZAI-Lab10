/* script.js */
let currentMode = 'form';
let availableFields = [];
let workspaceItems = [];

document.addEventListener('DOMContentLoaded', () => {
    fetchFields();
    loadFileList();
    setMode('form');
});

// Отримання полів з Django API
async function fetchFields() {
    try {
        const response = await fetch('/api/get-fields/');
        const json = await response.json();
        if (json.status === 'success') {
            availableFields = json.data;
            renderFieldButtons();
        }
    } catch (error) {
        console.error('Error fetching fields:', error);
    }
}

function renderFieldButtons() {
    const container = document.getElementById('fields-container');
    if (!container) return;
    container.innerHTML = '';
    availableFields.forEach(field => {
        const btn = document.createElement('button');
        btn.className = 'field-btn';
        btn.innerText = field;
        btn.onclick = () => addFieldToWorkspace(field);
        container.appendChild(btn);
    });
}

function setMode(mode) {
    currentMode = mode;
    const label = document.getElementById('current-mode-label');
    if (label) label.innerText = 'Tryb: ' + (mode === 'form' ? 'Formularz' : 'Szablon');
    
    const btnForm = document.getElementById('btn-form');
    const btnTemplate = document.getElementById('btn-template');
    if (btnForm) btnForm.classList.toggle('active-mode', mode === 'form');
    if (btnTemplate) btnTemplate.classList.toggle('active-mode', mode === 'template');
    
    clearWorkspace();
}

function addFieldToWorkspace(fieldName) {
    if (currentMode === 'form') {
        const exists = workspaceItems.some(item => item.name === fieldName);
        if (exists) {
            showMessage('Błąd: W trybie formularza pole można dodać tylko raz!', 'red');
            return;
        }
    }

    const item = {
        id: Date.now() + Math.random(),
        name: fieldName,
        value: '' 
    };
    workspaceItems.push(item);
    renderWorkspace();
}

function renderWorkspace() {
    const ws = document.getElementById('workspace');
    if (!ws) return;
    ws.innerHTML = '';
    
    if (workspaceItems.length === 0) {
        ws.innerHTML = '<p class="placeholder">Obszar roboczy pusty</p>';
        return;
    }

    workspaceItems.forEach((item, index) => {
        const div = document.createElement('div');
        div.className = 'workspace-item';
        
        let contentHtml = `<span>${index + 1}. <strong>${item.name}</strong></span>`;
        if (currentMode === 'template') {
            contentHtml += `<input type="text" placeholder="Wartość testowa..." onchange="updateValue(${item.id}, this.value)" value="${item.value || ''}">`;
        } else {
            contentHtml += `<input type="text" disabled placeholder="Input field">`;
        }

        const delBtn = document.createElement('button');
        delBtn.innerText = 'X';
        delBtn.className = 'btn-remove';
        delBtn.onclick = () => removeField(item.id);

        div.innerHTML = contentHtml;
        div.appendChild(delBtn);
        ws.appendChild(div);
    });
}

function removeField(id) {
    workspaceItems = workspaceItems.filter(i => i.id !== id);
    renderWorkspace();
}

function updateValue(id, val) {
    const item = workspaceItems.find(i => i.id === id);
    if(item) item.value = val;
}

function clearWorkspace() {
    workspaceItems = [];
    renderWorkspace();
    showMessage('', 'black');
}

// Збереження через Django API з використанням CSRF-токена
async function saveDocument() {
    if (workspaceItems.length === 0) {
        showMessage('Błąd: Pusty dokument', 'red');
        return;
    }

    const saveModeElem = document.querySelector('input[name="saveDest"]:checked');
    const saveMode = saveModeElem ? saveModeElem.value : 'file';

    const payload = {
        type: currentMode,
        createdAt: new Date().toISOString(),
        saveMode: saveMode,
        fields: workspaceItems
    };

    try {
        const response = await fetch('/api/save/', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'X-CSRFToken': typeof csrftoken !== 'undefined' ? csrftoken : '' 
            },
            body: JSON.stringify(payload)
        });
        const result = await response.json();
        
        if (result.status === 'success') {
            showMessage(result.message, 'green');
            loadFileList();
        } else {
            showMessage(result.message, 'red');
        }
    } catch (e) {
        console.error(e);
        showMessage('Błąd komunikacji', 'red');
    }
}

async function loadFileList() {
    const saveModeElem = document.querySelector('input[name="saveDest"]:checked');
    const mode = saveModeElem ? saveModeElem.value : 'file';
    
    try {
        // Оновлено шлях для Django
        const res = await fetch(`/api/list/?mode=${mode}`);
        const json = await res.json();
        const list = document.getElementById('file-list');
        if (!list) return;
        list.innerHTML = '';
        
        if(json.data) {
            json.data.forEach(item => {
                const li = document.createElement('li');
                li.style.cursor = 'pointer';
                li.style.textDecoration = 'underline';
                li.innerText = item;
                li.onclick = () => loadDocument(item); 
                list.appendChild(li);
            });
        }
    } catch (e) {
        console.error(e);
    }
}

async function loadDocument(targetName) {
    try {
        const res = await fetch(`/api/load/?target=${encodeURIComponent(targetName)}`);
        const data = await res.json();
        
        if (data.status === 'error') {
            showMessage(data.message, 'red');
            return;
        }

        setMode(data.type);
        workspaceItems = data.fields;
        renderWorkspace();
        showMessage(`Załadowano: ${targetName}`, 'blue');
    } catch (e) {
        showMessage('Błąd ładowania', 'red');
    }
}

function showMessage(msg, color) {
    const p = document.getElementById('message-panel');
    if (p) {
        p.innerText = msg;
        p.style.color = color;
    }
}
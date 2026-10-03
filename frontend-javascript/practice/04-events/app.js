// Isolated lesson: adding data and reporting success; dynamic task rendering comes next.
let tasks = [];
let nextId = 1;
function normalizeTitle(value) { return String(value).trim().replace(/\s+/g, ' '); }
function addTask(list, title, category, id) {
  const clean = normalizeTitle(title);
  if (!clean) return { list, error: 'Enter a task name.' };
  return { list: [...list, { id, title: clean, category, done: false }], error: null };
}
const form = document.querySelector('#task-form');
const titleInput = document.querySelector('#task-title');
const categoryInput = document.querySelector('#task-category');
const status = document.querySelector('#form-status');
form.addEventListener('submit', event => {
  event.preventDefault();
  const result = addTask(tasks, titleInput.value, categoryInput.value, nextId);
  if (result.error) { status.textContent = result.error; titleInput.focus(); return; }
  tasks = result.list;
  nextId += 1;
  status.textContent = `Added ${tasks[tasks.length - 1].title}; stored ${tasks.length}`;
  console.log(JSON.stringify(tasks));
  titleInput.value = '';
  titleInput.focus();
});

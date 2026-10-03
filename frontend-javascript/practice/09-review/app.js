// Isolated lesson: seeded records, safe rendering, completion and focus.
let tasks = [
  { id: 1, title: 'Bring notebook', category: 'Practice', done: false },
  { id: 2, title: '<b>Pack water</b>', category: 'Review', done: false }
];
const list = document.querySelector('#task-list');
const count = document.querySelector('#task-count');
const filter = document.querySelector('#task-filter');
const empty = document.querySelector('#empty-state');
function render(focusId = null) {
  const shown = tasks.filter(task => filter.value === 'all' || (filter.value === 'done' ? task.done : !task.done));
  list.replaceChildren();
  for (const task of shown) {
    const row = document.createElement('li'); row.className = 'task';
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox'; checkbox.checked = task.done; checkbox.id = `task-${task.id}`;
    const label = document.createElement('label'); label.htmlFor = checkbox.id;
    label.textContent = task.title; label.style.margin = '0';
    checkbox.addEventListener('change', () => { task.done = checkbox.checked; render(task.id); });
    row.append(checkbox, label); list.append(row);
  }
  let remaining = 0;
  for (const task of tasks) if (!task.done) remaining += 1;
  count.textContent = `${remaining} ${remaining === 1 ? 'task' : 'tasks'} remaining`;
  empty.textContent = tasks.length === 0 ? 'No tasks yet. Add one to begin.' : 'No tasks match this filter.';
  empty.hidden = shown.length > 0;
  if (focusId !== null) (document.getElementById(`task-${focusId}`) || filter).focus();
}
document.querySelector('#task-form').addEventListener('submit', event => event.preventDefault());
filter.addEventListener('change', () => render());
render();
